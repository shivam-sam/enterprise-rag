from bs4 import BeautifulSoup
import logfire


def parse_html(file_path: str) -> str:
    """
    Parses an HTML file and returns its text content.
    Cleans scripts, styles, and other non-text elements from the HTML for RAG.

    Args:
        file_path (str): The path to the HTML file.
    """
    with logfire.span("📄 HTML Parsing", file_path=file_path):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                html_content = file.read()
            soup = BeautifulSoup(html_content, "html.parser")

            # 1. Remove script, style, meta, and noscript elements
            for script in soup(["script", "style", "meta", "noscript"]):
                script.decompose()  # Remove scripts and styles, meta, noscript

            # 2. Get text and clean it
            text = soup.get_text(separator="\n", strip=True)

            # 3. Clean the text (whitespaces, collapse newlines, etc.)
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text_clean = "\n".join(chunk for chunk in chunks if chunk)

            return text_clean
        except Exception as e:
            logfire.error(f"❌ Error parsing HTML file {file_path}: {e}")
            return ""

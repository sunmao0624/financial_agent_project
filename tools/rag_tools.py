import pdfplumber
from langchain.tools import tool
import os


@tool("search_pdf_knowledge")
def search_pdf_knowledge(question: str) -> str:
    """
    检索 PDF 知识库
    """

    folder = "knowledge/pdf_reports"

    all_text = ""

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            path = os.path.join(folder, file)

            with pdfplumber.open(path) as pdf:

                for page in pdf.pages:
                    text = page.extract_text()

                    if text:
                        all_text += text[:500]

    return all_text[:2000]
# python
import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    # Download HTML content from url
    response = requests.get(url, timeout=10)
    # Force response encoding to UTF-8 to correctly decode Chinese characters
    response.encoding = "utf-8"
    response.raise_for_status()
    return response.text

def convert_table_to_markdown(table):
    header = []
    rows = []

    thead = table.find("thead")
    if thead:
        header_row = thead.find("tr")
        header = [cell.get_text(strip=True) for cell in header_row.find_all(["th", "td"])]
    else:
        first_row = table.find("tr")
        if first_row:
            header_cells = first_row.find_all("th")
            if header_cells:
                header = [cell.get_text(strip=True) for cell in header_cells]

    tbody = table.find("tbody")
    if tbody:
        tr_elements = tbody.find_all("tr")
    else:
        tr_elements = table.find_all("tr")
        if header:
            tr_elements = tr_elements[1:]

    for tr in tr_elements:
        cells = [cell.get_text(strip=True) for cell in tr.find_all(["td", "th"])]
        if cells:
            rows.append(cells)

    markdown = ""
    if header:
        markdown += "| " + " | ".join(header) + " |\n"
        markdown += "| " + " | ".join(["---"] * len(header)) + " |\n"
    for row in rows:
        markdown += "| " + " | ".join(row) + " |\n"

    return markdown

def main():
    url = "https://www.coderjia.cn/archives/dba3f94c-a021-468a-8ac6-e840f85867ea"
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")

    if not table:
        print("No table found in the HTML.")
        return

    markdown_content = convert_table_to_markdown(table)

    with open(r"mirrors.md", "w", encoding="utf-8") as file:
        file.write(markdown_content)

    print("Markdown table has been saved to mirrors.md")

if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup

def get_website_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
def get_predicting_table(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    table = soup.find("table")
    return table


if __name__ == "__main__":
    url = "https://www.fantasyfootballpundit.com/fpl-points-predictor/"
    html_text = get_website_html(url)
    
    if html_text:
        table = get_predicting_table(html_text)
        if table:
            print(table.prettify())
        else:
            print("Predicting table not found.")
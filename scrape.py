from requests_html import HTMLSession
from bs4 import BeautifulSoup

def main():
    URL = "https://us.tamrieltradecentre.com/pc/Trade/Detail/562431659"
 
    session = HTMLSession()
 
    resp = session.get(URL)
 
    # Vou assumir que te faltava isto
    resp.html.render(sleep=2)

    soup = BeautifulSoup(resp.html.html, "lxml")
 
    span_tags = soup.find_all("span", {"class": "gold-amount bold"})
 
    prices = [tag.text for tag in span_tags]
    print(prices)

if __name__ == "__main__":
    main()
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("sina2.html"))
a = soup.find_all("a")
for item in a:
    if len(item.contents) > 0 :
        print item.contents[0].encode("utf-8")
    if "href" in item.attrs:
        print item["href"].encode("utf-8")

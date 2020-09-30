import selenium
from selenium import webdriver as wb
import lidl
from lidl import check_price_lidl
from lidl import webD

items = ["birra", "beer", "ceci", "amaro", "vino", "succo", "spumante", "uova"]

if __name__ == '__main__':

    print()
    print("----------LIDL----------\n")

    for i in items:
        check_price_lidl(i)

    webD.close()
    print()

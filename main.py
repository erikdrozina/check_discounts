import selenium
from selenium import webdriver as wb
import lidl
from lidl import check_price_lidl
from lidl import webD

# list of wanted items
items = ["birra", "ceci", "succo", "uova"]


# check items on lidl site
def lidl():
    print()
    print("----------LIDL----------\n")

    for i in items:
        check_price_lidl(i)

    webD.close()
    print()


# main
if __name__ == '__main__':

    lidl()

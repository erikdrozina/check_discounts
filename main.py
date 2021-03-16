import lidl
from lidl import check_price_lidl
from lidl import webD as webD_lidl

import penny
from penny import check_price_penny
from penny import webD as webD_penny

# list of wanted items
items = ["birra", "ceci", "grappa", "vino", "cioccolato", "gocciole"]


# check items on lidl and penny sites
def lidl():
    print()
    print("----------LIDL----------\n")

    for i in items:
        check_price_lidl(i)

    webD_lidl.close()
    print()


def penny():
    print()
    print("----------PENNY----------\n")

    for i in items:
        check_price_penny(i)

    webD_penny.close()
    print()


# main
if __name__ == '__main__':

    lidl()
    penny()

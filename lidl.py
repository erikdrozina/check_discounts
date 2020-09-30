import selenium
from selenium import webdriver as wb

# initial setup
page_url = "https://www.lidl.it/it/c/offerte-settimanali/c10/w1"
webD = wb.Firefox()
webD.get(page_url)

# click on the "accept cookies" button
button = webD.find_element_by_xpath("/html/body/dialog/div/div[1]/button")
button.click()


def check_price_lidl(strin):

    # creating list for products and prices
    products = webD.find_elements_by_class_name("product__title")
    prices = webD.find_elements_by_class_name("pricebox__price")

    # check the wanted products
    for i in range(len(products)):
        if strin in products[i].text.lower():
            print(products[i].text.lower()+": " + prices[i].text + "€")
        else:
            pass

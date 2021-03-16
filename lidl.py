import selenium
from selenium import webdriver as wb
from time import sleep
from selenium.webdriver.firefox.options import Options


# initial setup
options = Options()
options.headless = True
page_url = "https://www.lidl.it/it/offerte-settimanali"
webD = wb.Firefox(options=options)
webD.get(page_url)
print()
print("Headless Firefox Initialized at Lidl site")

# click on the "accept cookies" button
sleep(2)
button = webD.find_element_by_xpath("/html/body/dialog/div/div[1]/button")
button.click()
sleep(2)


def check_price_lidl(strin):

    # creating list for products and prices
    products = webD.find_elements_by_class_name("product__title")
    prices = webD.find_elements_by_class_name("pricebox__price")

    # check the wanted products
    for i in range(len(products)):
        if strin in products[i].text.lower():
            print(products[i].text.lower()+": " + prices[i].text + " €")
        else:
            pass

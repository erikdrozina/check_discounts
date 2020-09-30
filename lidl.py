import selenium
from selenium import webdriver as wb


page_url = "https://www.lidl.it/it/c/offerte-settimanali/c10/w1"
webD = wb.Firefox()
webD.get(page_url)
button = webD.find_element_by_xpath("/html/body/dialog/div/div[1]/button")
button.click()


def check_price_lidl(strin):

    n = webD.find_elements_by_class_name("product__title")
    prices = webD.find_elements_by_class_name("pricebox__price")

    for i in range(len(n)):
        if strin in n[i].text.lower():
            print(n[i].text.lower()+": " + prices[i].text + "€")
        else:
            pass

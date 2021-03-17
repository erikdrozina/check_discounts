import selenium
from selenium import webdriver as wb
from time import sleep
from selenium.webdriver.chrome.options import Options


# initial setup
options = Options()
#options.headless = True
page_url = "https://www.pennymarket.it/categorie/all"
webD = wb.Chrome(options=options)
webD.get(page_url)
print()
print("Headless Chrome Initialized at Penny site\n")

# click on the "accept cookies" button
sleep(2)
button = webD.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
button.click()
sleep(2)


def check_price_penny(strin):

    prices = []
    products = []

    # creating raw lists for products and prices
    products_raw = webD.find_elements_by_tag_name("h1")
    prices_raw = webD.find_elements_by_tag_name("s")

    # creating final lists
    for i in range(len(prices_raw)):
        if("€" in prices_raw[i].text):
            prices.append(prices_raw[i])

    for i in range(len(products_raw)):
        if products_raw[i].text != "":
            products.append(products_raw[i])

    # check the wanted products
    for i in range(len(products)):
        if strin in products[i].text.lower():
            print(products[i].text.lower() + ": " +
                  prices[i].text.lower())
        else:
            pass

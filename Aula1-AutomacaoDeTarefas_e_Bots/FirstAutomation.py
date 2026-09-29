import pyautogui
import time

# Create and set variables
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
user_email = "mail.sample@provider.com"
user_password = "samplePass"

# Set parameters for pyautogui
pyautogui.PAUSE = 0.2

# Open Safari Browser
pyautogui.hotkey("command", "space")
pyautogui.write("safari")
pyautogui.press("enter")
time.sleep(3)

# Open the sistem
pyautogui.write(site)
pyautogui.press("enter")
time.sleep(3)

# Login
pyautogui.click(x=641, y=380)
pyautogui.write(user_email)
pyautogui.press("tab")
pyautogui.write(user_password)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Start registration of products

# Config Pandas
import pandas as pd

table = pd.read_csv("products.csv")

for row in table.index:
    # Select and fills in the Product Code field
    pyautogui.click(x=735, y=253)
    productCode = table.loc[row, "codigo"]
    pyautogui.write(productCode)

    # Select and fills in the Product Brand field
    pyautogui.press("tab")
    productBrand = table.loc[row, "marca"]
    pyautogui.write(productBrand)

    # Select and fills in the Product Tipe field
    pyautogui.press("tab")
    productType = table.loc[row, "tipo"]
    pyautogui.write(productType)

    # Select and fills in the Product Category field
    pyautogui.press("tab")
    productCategory = str(table.loc[row, "categoria"])
    pyautogui.write(productCategory)

    # Select and fills in the Product Unit Price field
    pyautogui.press("tab")
    productUnitPrice = str(table.loc[row, "preco_unitario"])
    pyautogui.write(productUnitPrice)

    # Select and fills in the Product Cost field
    pyautogui.press("tab")
    productCost = str(table.loc[row, "custo"])
    pyautogui.write(productCost)

    # Select and fills in the Observations field
    pyautogui.press("tab")
    productObservations = str(table.loc[row, "obs"])
    if productObservations != "nan":
        pyautogui.write(productObservations)

    # Select and press submit button
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Return to the top of the page
    pyautogui.scroll(3000)



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

# Select and fills in the Product Code field
pyautogui.click(x=735, y=253)
pyautogui.write("cod produto")

# Select and fills in the Product Brand field
pyautogui.press("tab")
pyautogui.write("marca produto")

# Select and fills in the Product Tipe field
pyautogui.press("tab")
pyautogui.write("tipo produto")

# Select and fills in the Product Category field
pyautogui.press("tab")
pyautogui.write("categoria produto")

# Select and fills in the Product Unit Price field
pyautogui.press("tab")
pyautogui.write("preco unitario")

# Select and fills in the Product Cost field
pyautogui.press("tab")
pyautogui.write("custo produto")

# Select and fills in the Observations field
pyautogui.press("tab")
pyautogui.write("observacoes")

# Select and press submit button
pyautogui.press("tab")
pyautogui.press("enter")

# Return to the top of the page
pyautogui.scroll(3000)



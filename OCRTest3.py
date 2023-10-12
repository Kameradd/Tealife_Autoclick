import pyautogui
import pytesseract
import time
from PIL import Image
from fuzzywuzzy import fuzz
import autoit

# Define the initial capture area and scroll amount
left, top, width, height = 1000, 430, 400, 400
scroll_pixels = 100

# Dictionary mapping menu items to button coordinates
menu_button_mapping_upper = {
    "Americano": (262, 500),
    "Milk Tea": (442, 500),
    "Malty Smoothie": (622, 500),
    "Rose Puer Tea": (802, 500),
    "Hazelnut Coco": (262, 660),
    "Bang Fresh Milk": (442, 660),
    "Mango Smoothie": (622, 660),
    "Nishio Latte": (802, 660),
}

menu_button_mapping_lower = {
    "Red Bean": (262, 500),
    "Strawberry Pudding": (442, 500),
    "Superior Coco": (622, 500),
    "Popcorn Chicken": (802, 500),
    "Softea Cone": (262, 660),
    "Bubble Softea": (442, 660),
    "Malty Horlicks": (622, 660),
    "Spicy Popcorn": (802, 660),
}

def scroll_up():
    scrollbar_x, scrollbar_y = 947, 600  # Adjust these coordinates to your scrollbar
    autoit.mouse_click("left", scrollbar_x, scrollbar_y)
    autoit.mouse_down("left")
    autoit.mouse_move(scrollbar_x, scrollbar_y - scroll_pixels, speed=10)
    autoit.mouse_up("left")
    return

# Function to scroll down
def scroll_down():
    scrollbar_x, scrollbar_y = 947, 500  # Adjust these coordinates to your scrollbar
    autoit.mouse_click("left", scrollbar_x, scrollbar_y)
    autoit.mouse_down("left")
    autoit.mouse_move(scrollbar_x,  scrollbar_y + scroll_pixels, speed=10)
    autoit.mouse_up("left")
    return

# Function to capture a portion of the screen
def capture_screen(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

# Function to find matching items in a given menu
def find_matching_items_in_menu(text, menu_mapping):
    matches = []
    for item, (x, y) in menu_mapping.items():
        similarity = fuzz.partial_ratio(item.lower(), text.lower())
        if similarity >= 60:
            matches.append((item, x, y))
    return matches

# Continuously capture, scroll, and search for menu items
while True:
    
    screenshot = capture_screen(left, top, width, height)
    text = pytesseract.image_to_string(screenshot)

    # Check for matching menu items in both upper and lower menus
    matching_items_upper = find_matching_items_in_menu(text, menu_button_mapping_upper)
    matching_items_lower = find_matching_items_in_menu(text, menu_button_mapping_lower)

    if matching_items_upper:
        scroll_up()
        screenshot = capture_screen(left, top, width, height)
        text = pytesseract.image_to_string(screenshot)
        matching_items_upper = find_matching_items_in_menu(text, menu_button_mapping_upper)
        print("Matching items found in upper menu:")
        for item, x, y in matching_items_upper:
            print(item)
            autoit.mouse_click("left", x, y)
            print(f"Button for {item} clicked.")
        # Scroll up
        scroll_down()
        time.sleep(1)
    if matching_items_lower:
        matching_items_lower = find_matching_items_in_menu(text, menu_button_mapping_lower)
        print("Matching items found in lower menu:")
        for item, x, y in matching_items_lower:
            print(item)
            autoit.mouse_click("left", x, y)
            print(f"Button for {item} clicked.")
        # Scroll down
        matching_items_upper = []  # Clear matching items
        matching_items_lower = []  # Clear matching items
        scroll_up()
        time.sleep(1)
        autoit.mouse_click("left",1650, 780)

    else:
        print("No matching items found in the current OCR result. Scrolling again...")
        # Depending on your application's behavior, you may need to add a break condition here to avoid an infinite loop.

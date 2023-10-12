import pyautogui
import pytesseract
from fuzzywuzzy import fuzz
import autoit
import keyboard  # New library for listening to a key press
import time

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
    time.sleep(1/4)
    autoit.mouse_down("left")
    autoit.mouse_move(scrollbar_x, scrollbar_y - scroll_pixels, speed=10)
    autoit.mouse_up("left")
    return

def scroll_down():
    scrollbar_x, scrollbar_y = 947, 500  # Adjust these coordinates to your scrollbar
    autoit.mouse_click("left", scrollbar_x, scrollbar_y)
    time.sleep(1/4)
    autoit.mouse_down("left")
    autoit.mouse_move(scrollbar_x, scrollbar_y + scroll_pixels, speed=10)
    autoit.mouse_up("left")
    return

def capture_screen(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

def find_matching_items_in_menu(text, menu_mapping):
    matches = []
    for item, (x, y) in menu_mapping.items():
        similarity = fuzz.partial_ratio(item.lower(), text.lower())
        if similarity >= 80:
            matches.append((item, x, y))
    return matches

# Listen for a key press to initiate a single run
while True:
    keyboard.wait("e")
    time.sleep(2)

    screenshot = capture_screen(left, top, width, height)
    text = pytesseract.image_to_string(screenshot)

    matching_items_upper = find_matching_items_in_menu(text, menu_button_mapping_upper)
    matching_items_lower = find_matching_items_in_menu(text, menu_button_mapping_lower)
    scroll_up()
    if matching_items_upper:
        print("Matching items found in upper menu:")
        for item, x, y in matching_items_upper:
            print(item)
            autoit.mouse_click("left", x, y)
            print(f"Button for {item} clicked.")
        scroll_down()
    if matching_items_lower:
        print("Matching items found in lower menu:")
        for item, x, y in matching_items_lower:
            print(item)
            autoit.mouse_click("left", x, y)
            print(f"Button for {item} clicked.")
        autoit.mouse_click("left", 1650, 780)

# Scroll after processing the menu
    matching_items_upper = []  # Clear matching items
    matching_items_lower = []  # Clear matching items
    scroll_up()

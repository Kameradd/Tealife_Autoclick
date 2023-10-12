import pyautogui
import pytesseract
import time
from PIL import Image
from fuzzywuzzy import fuzz
import autoit

# Capture a portion of the screen
left, top, width, height = 1000, 430, 400, 400  # Adjust these coordinates as needed
scroll_pixels = 200
menu = ["Bang Fresh Milk", "Superior Coco", "Popcorn Chicken", "Softea Cone",
        "Red Bean", "Milk Tea", "Americano", "Mango Smoothie", "Hazelnut Coco", "Nishio Latte"
        , "Rose Puer Tea", "Malty Smoothie"]
def scroll_up():
    pyautogui.moveTo(949, 600)
    pyautogui.dragTo(0, 500, button='left')
    return 0
def scroll_down():
    pyautogui.moveTo(949, 500)
    pyautogui.dragTo(0, 600, button='left')
    return 0
def capture_screen(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot
def find_matching_items(text, menu):
    matches = []
    for item in menu:
        # Use fuzzy string matching to allow for slight variations in text
        similarity = fuzz.partial_ratio(item.lower(), text.lower())
        if similarity >= 80:  # You can adjust the threshold as needed
            matches.append(item)
    return matches
menu_button_mapping_upper = {
    "Americano": (262, 500),
    "Milk Tea": (442, 500),
    "Malty Smoothie": (622, 500),
    "Rose Puer Tea":(802, 500),
    "Hazelnut Coco": (262, 660),
    "Bang Fresh Milk": (442, 660),
    "Mango Smoothie": (622, 660),
    "Nishio Latte": (802, 660),
}
menu_button_mapping_lower {
    "Red Bean": (262, 500),
    "Strawberry Pudding": (442, 500),
    "Superior Coco": (622, 500),
    "Popcorn Chicken": (802, 500),
    "Softea Cone": (262, 660),
    "Bubble Softea": (442, 660),
    "Malty Horlicks": (622, 660),
    "Spicy Popcorn": (802, 660),
}
screenshot = capture_screen(left, top, width, height)
text = pytesseract.image_to_string(screenshot)
matching_items = find_matching_items(text, menu_button_mapping.keys())
# If matching items are found, click the corresponding buttons
if matching_items:
    print("Matching items found in OCR result:")
    for item in matching_items:
        print(item)
        if item in menu_button_mapping:
            button_x, button_y = menu_button_mapping[item]
            autoit.mouse_click("left", button_x, button_y)
            print(f"Button for {item} clicked.")
else:
    print("No matching items found in the initial OCR result.")

# Optionally, you can continue scrolling and searching for menu items
while True:
    time.sleep(1)  # Optional: Add a delay to ensure the screen updates
    screenshot = capture_screen(left, top, width, height)
    text = pytesseract.image_to_string(screenshot)
    matching_items = find_matching_items(text, menu_button_mapping.keys())
    if matching_items:
        print("Matching items found in OCR result:")
        for item in matching_items:
            print(item)
            if item in menu_button_mapping:
                button_x, button_y = menu_button_mapping[item]
                autoit.mouse_click("left", button_x, button_y)
                print(f"Button for {item} clicked.")
        autoit.mouse_click("left",1650, 780)
            
    else:
        print("No matching items found in the current OCR result. Scrolling again...")
        


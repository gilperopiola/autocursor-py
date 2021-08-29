import pyautogui
import time
import random

size = pyautogui.size()
width = size[0]
height = size[1]

random_nuance_min = 0.0025
random_nuance_max = 0.479
random_nuance = random.uniform(random_nuance_min, random_nuance_max)

# move to following and click and go to middle of screen
pyautogui.moveTo(1085, 255, duration = 1 + random_nuance)
random_nuance = random.uniform(random_nuance_min, random_nuance_max)

time.sleep(0.1 + random_nuance / 2)
random_nuance = random.uniform(random_nuance_min, random_nuance_max)

pyautogui.click(1085, 255)
time.sleep(0.6 + random_nuance / 2)
random_nuance = random.uniform(random_nuance_min, random_nuance_max)

pyautogui.moveTo(width/2, height/2, duration = 0.5 + random_nuance)
random_nuance = random.uniform(random_nuance_min, random_nuance_max)

time.sleep(0.15 + random_nuance / 2)

# start scrolling
total_pages_to_fetch = 10 # 10 = 150 accounts~, 100 = 1500~ 
scrolls_per_fetch = 12 + random.randint(0, 3)
scroll_force = -40 + random.randint(-3, 3)

for i in range(total_pages_to_fetch):
  for i in range(scrolls_per_fetch):
    pyautogui.scroll(scroll_force)
    random_nuance = random.uniform(random_nuance_min, random_nuance_max)
    time.sleep(0.03 + random_nuance / 2) 
  time.sleep(1.5 + random_nuance)


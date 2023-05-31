import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import time

# 找到 Albion Online 的窗口
albion_window = gw.getWindowsWithTitle('Albion Online')[0]

# 将 Albion Online 窗口置顶
albion_window.activate()
time.sleep(1)
# 获取 Albion Online 窗口的位置
x, y, width, height = albion_window.left, albion_window.top, albion_window.width, albion_window.height

print(f"Screenshot size: {x},{y},{width},{height}")
# 截取 Albion Online 窗口的屏幕截图
screenshot = pyautogui.screenshot(region=(x, y, width, height))
screenshot.save('img1.png')
print(f"Screenshot width: {screenshot.width}, height: {screenshot.height}")
print(f"Albion Online window width: {width}, height: {height}")
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


pyautogui.press('n')
time.sleep(1)

screenshot = pyautogui.screenshot(region=(x, y, width, height))

screenshot.save('img2.png')
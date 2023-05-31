import cv2
import numpy as np
import pyautogui

# 步骤1：按下 'n' 键获取屏幕截图
pyautogui.press('n')
pyautogui.sleep(1)  # 等待一会儿，让截图被成功获取

# 步骤2：捕获屏幕截图
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# 步骤3：在屏幕截图中找到农田和人物
farm_template = cv2.imread('farm.png', cv2.IMREAD_UNCHANGED)
character_template = cv2.imread('character.png', cv2.IMREAD_UNCHANGED)

res_farm = cv2.matchTemplate(screenshot, farm_template, cv2.TM_CCOEFF_NORMED)
res_character = cv2.matchTemplate(screenshot, character_template, cv2.TM_CCOEFF_NORMED)

_, _, _, max_loc_farm = cv2.minMaxLoc(res_farm)
_, _, _, max_loc_character = cv2.minMaxLoc(res_character)

# 步骤4：计算人物和每个农田之间的距离
distances = np.sqrt((max_loc_farm[0]-max_loc_character[0])**2 + (max_loc_farm[1]-max_loc_character[1])**2)

# 步骤5：找到最近的农田
closest_farm_index = np.argmin(distances)
closest_farm_location = max_loc_farm[closest_farm_index]

# 步骤6：使用 WASD 键将人物移动到最近的农田
if closest_farm_location[0] > max_loc_character[0]:  # 如果农田在右边
    pyautogui.keyDown('d')
    pyautogui.sleep(1)  # 调整等待时间以移动正确的距离
    pyautogui.keyUp('d')
elif closest_farm_location[0] < max_loc_character[0]:  # 如果农田在左边
    pyautogui.keyDown('a')
    pyautogui.sleep(1)  # 调整等待时间以移动正确的距离
    pyautogui.keyUp('a')

if closest_farm_location[1] > max_loc_character[1]:  # 如果农田在下方
    pyautogui.keyDown('s')
    pyautogui.sleep(1)  # 调整等待时间以移动正确的距离
    pyautogui.keyUp('s')
elif closest_farm_location[1] < max_loc_character[1]:  # 如果农田在上方
    pyautogui.keyDown('w')
    pyautogui.sleep(1)  # 调整等待时间以移动正确的距离
    pyautogui.keyUp('w')


import pyautogui
x = int(input("Tell me how many circles around the screen you want?(1 circle is 12seconds): "))
pyautogui.moveTo(100,100)
distance_x = 2300
distance_y = 1200


for i in range(0,x):
    pyautogui.move(0,distance_y,duration=3)
    pyautogui.move(distance_x,0,duration=3)
    pyautogui.move(0,-distance_y,duration=3)
    pyautogui.move(-distance_x,0,duration=3)

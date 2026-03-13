import serial
import time
import pyautogui

# Change COM port if needed
ArduinoSerial = serial.Serial('COM18', 9600)

time.sleep(2)

while True:

    incoming = str(ArduinoSerial.readline())
    print(incoming)

    if 'Play/Pause' in incoming:
        pyautogui.press('space')

    if 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')

    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right')

    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'up')

    if 'Vdown' in incoming:
        pyautogui.hotkey('ctrl', 'down')

    incoming = ""
import time, pyautogui

if __name__ == "__main__":
    song = open("motherland.txt", 'r', encoding="utf-8")
    time.sleep(5)
    for word in song:
        pyautogui.typewrite(word)
        pyautogui.hotkey("shiftleft", "enter")
        time.sleep(2)
    pyautogui.press("enter")
    song.close()

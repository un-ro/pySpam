import time, pyautogui

def translate(key):
    """Returns qwerty key or the given key itself if no mapping found"""
    return "".join(map(lambda x: tr.get(x, x), key))


qwerty = """qwertyuiop[]asdfghjkl;'zxcvbnm,.?/QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>"""
ycuken = """йцукенгшщзхъфывапролджэячсмитьбю,.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"""
# join as keys and values
tr = dict(zip(ycuken, qwerty))

if __name__ == "__main__":
    song = open("motherland.txt", 'r', encoding="utf-8")
    time.sleep(5)
    for word in song:
        pyautogui.typewrite(translate(word))
        pyautogui.press("enter")
        time.sleep(2)
    song.close()

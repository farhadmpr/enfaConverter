import keyboard
import pyperclip

en = "qwertyuiop[]\\asdfghjkl;'zxcvbnm,.?"
fa = "ضصثقفغعهخحجچپشسیبلاتنمکگظطزرذدئو.؟"

def Handle():
    print('key pressed')
    keyboard.send('ctrl+c')
    text = pyperclip.paste()
    pyperclip.copy(Conver(text))
    keyboard.send('ctrl+v')

def GetLang(text):
    if text[0] in en or text[-1] in en:
        return "en"
    elif text[0].lower() in en or text[-1].lower() in en:
        return "en"
    elif text[0] in fa or text[-1] in fa:
        return "fa"
    else:
        return None

def Conver(text):
    lang=GetLang(text)
    res=""
    if(lang=="en"):
        text=text.lower()
        for c in text:
            if(c in en):
                res+=fa[en.index(c)]
            else:
                res+=c
        return res
    elif(lang=="fa"):
        for c in text:
            if(c in fa):
                res+=en[fa.index(c)]
            else:
                res+=c
        return res
    else:
        return text

keyboard.add_hotkey('ctrl+.', Handle)
keyboard.wait()

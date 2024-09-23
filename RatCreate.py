import os
from datetime import datetime
import time 

end = '\033[0m'
blue = '\033[94m'
green = '\033[92m'
white = '\033[97m'
yellow = '\033[93m'
debug_symbol = '\033[92m[</>]'

Version = "0.0.2"

def Main_menu():
    print(f"{white}RatCreate Version: {yellow}{Version}{end}")

def create_script():
    filename = input("Bitte den Namen des neuen Scripts eingeben (ohne .py): ") + ".py"

    if os.path.exists(filename):
        print(f"{white}Die Datei {yellow}'{filename}' {white}existiert bereits.{end}")
        time.sleep(4)
        return
    
    script_content = '''
from datetime import datetime
import time

end = '\\033[0m'
blue = '\\033[94m'
green = '\\033[92m'
white = '\\033[97m'
yellow = '\\033[93m'
debug_symbol = '\\033[92m[</>]'

def sleep(settime):
    time.sleep(settime)

def Abstand():
    print(" ")

def space(Value):
    global space
    if Value == 1:
        Abstand()
    elif Value == 2:
        Abstand()
        Abstand()
        Abstand()
    elif Value == 3:
        Abstand()
        Abstand()
        Abstand()

def format_value(text):
    try:
        value = float(text)
        return f"{yellow}{text}{white}"
    except ValueError:
        if text in ["True", "False", "true", "false"]:
            return f"{yellow}{text}{white}"
        return text

def debug(text):
    formatted_text = " ".join([format_value(word) for word in text.split()])

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"{blue}{current_time}{end} {debug_symbol} {white}{formatted_text}{end}")

#----------------------
    
        

# Script hier :D



#----------------------

if __name__ == "__main__":
    debug("Datei wurde erfolgreich erstellt mit Wert 42 und Status True")
'''


    with open(filename, 'w') as f:
        f.write(script_content)

    print(f"{white}Das Script {yellow}'{filename}' {white}wurde erfolgreich erstellt.{end}")
    time.sleep(4)

if __name__ == "__main__":
    Main_menu()
    create_script()
# By Mausi Schmausi

import os
from datetime import datetime

def create_script():
    filename = input("Bitte den Namen des neuen Scripts eingeben (ohne .py): ") + ".py"
    

    if os.path.exists(filename):
        print(f"Die Datei '{filename}' existiert bereits.")
        return
    
    script_content = '''import datetime

end = '\\033[0m'
blue = '\\033[94m'
green = '\\033[92m'
white = '\\033[97m'
yellow = '\\033[93m'
debug_symbol = '\\033[92m[</>]\\033[0m'

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

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"{blue}{current_time}{end} {debug_symbol} {white}{formatted_text}{end}")

if __name__ == "__main__":
    debug("Datei wurde erfolgreich erstellt mit Wert 42 und Status True und false.")
'''

    with open(filename, 'w') as f:
        f.write(script_content)

    print(f"Das Script '{filename}' wurde erfolgreich erstellt.")

if __name__ == "__main__":
    create_script()
#By Mausi Schmausi
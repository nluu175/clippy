import pyperclip
import time


def printClipboardItem(copy):
    print(copy)
    print("---")


def main():
    previous = ""

    clipboardFile = open(".\clipboard.txt", "a")
    try:
        while True:
            if pyperclip.paste() != previous and pyperclip.paste() != "":
                previous = pyperclip.paste()
                clipboardFile.write(pyperclip.paste())
                clipboardFile.write("\n---\n")
                printClipboardItem(pyperclip.paste())
            time.sleep(0.1)

    except KeyboardInterrupt:
        clipboardFile.close()


if __name__ == "__main__":
    main()

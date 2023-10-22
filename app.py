import msvcrt as m

from clicknium import clicknium as cc
from clicknium import locator


def wait():
    m.getch()

def main():
    site = "https://gamerant.com/search/?q="
    game = input("Find Codes for:")
    string = site + game.replace(" ", "+")
    tab = cc.chrome.open(string, is_maximize=False, is_wait_complete=False)

    elem = tab.find_element(locator.gamerant.link)
    elem.click()
    cc.wait_appear(locator.gamerant.codes)
    codes = tab.find_elements(locator.gamerant.codes)
    print("Found: " + str(len(codes)) + " code(s).")
    if len(codes) > 0:
        with open(game + ".txt", "w", encoding="utf-8") as f:
            for code in codes:
                text = f"'{code.get_text()}',"
                f.write(text + "\n")
        print("Success!\nPress any key to exit.")
    tab.close()
    wait()

if __name__ == "__main__":
    main()

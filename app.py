import os
from tqdm import tqdm
from gemini import Generator


def find_between(s, start, end):
    result = False
    try:
        result = s.split(start)[1].split(end)[0]
    except IndexError:
        result = False
    finally:
        return result
    

def main(game_name):

    codes = []
    g = Generator()
    result = g.prompt(game_name)

    for line in result.splitlines():
        if find_between(line, "**", "**"):
            code = find_between(line, "**", "**").strip(":-").__add__("\n").split(" ")[0]
            codes.append(code)

    if len(codes) > 0:
        if os.path.exists(f'{game_name}.txt'):
            with open(f'{game_name}.txt', 'r') as r:
                for code in codes:
                    if code in r.read():
                        codes.remove(code)

        with open(f'{game_name}.txt', 'a') as f:
            for code in codes:
                f.write(code)
    return codes


if __name__ == "__main__":
    game_name = input("Enter a game name:")
    count = 0
    for i in tqdm (range(5), desc="Searching Codes: ",
                   ascii=False, ncols=75):
        count += len(main(game_name))
    print("Complete.")
    print(f'{count} codes were saved to {os.curdir + game_name}.txt')
    input('Press Any Key To Exit')

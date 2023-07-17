import sys
from pyfiglet import Figlet

def get_font(args):
    if len(args) == 0:
        return None
    if len(args) != 2 or args[0] not in ['-f', '--font']:
        sys.exit("Invalid usage")
    return args[1]

def main():
    font = get_font(sys.argv[1:])
    figlet = Figlet(font=font) if font else Figlet()
    text = input("Input: ")
    rendered_text = figlet.renderText(text)
    print(rendered_text)

if __name__ == "__main__":
    main()

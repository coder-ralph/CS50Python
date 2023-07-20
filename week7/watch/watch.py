import re

def main():
    print((parse(input("HTML: "))))


def parse(s):
    # <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
    # <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    # https://youtu.be/xvFZjo5PgG0
    match = re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
    if match:
        link = "https://youtu.be/" + match.group(1)
        return link
    else:
        return None


if __name__ == "__main__":
    main()
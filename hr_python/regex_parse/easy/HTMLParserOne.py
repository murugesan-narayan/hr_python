from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for n, v in attrs:
            print('->', n, '>', v)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for n, v in attrs:
            print('->', n, '>', v)


if __name__ == '__main__':
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    for i in range(int(input())):
        parser.feed(input())

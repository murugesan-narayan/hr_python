from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for n, v in attrs:
            print('->', n, '>', v)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for n, v in attrs:
            print('->', n, '>', v)


if __name__ == '__main__':
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    html = ''
    for i in range(int(input())):
        html += input().rstrip() + '\n'
    parser.feed(html)

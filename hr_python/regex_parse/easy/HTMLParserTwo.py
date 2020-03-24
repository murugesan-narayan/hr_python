from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        if '\n' not in data:
            print('>>> Data', data, sep='\n')

    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment", data, sep='\n')
        else:
            print(">>> Single-line Comment", data, sep='\n')


if __name__ == '__main__':
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    html = ''
    for i in range(int(input())):
        html += input().rstrip()+'\n'
    parser.feed(html)

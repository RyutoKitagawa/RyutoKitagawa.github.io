import os
from bs4 import BeautifulSoup, Tag

strip_comment = lambda comment: comment.string.strip()[1:]
strip_file = lambda file_name: file_name.split('.')[0]

def read_template(template):
    with open('template/' + template[1:] + '.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    return soup

templates = set(['#' + strip_file(i) for i in os.listdir('template')])
print(templates)

def rebuild_page(page):
    with open(page, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    # soup find all div with id in templates
    for template in templates:
        div = soup.find('div', {'id': template})
        if div:
            div.insert_after(read_template(template))
            div.decompose()
    soup = soup.prettify()
    with open('../' + page, 'w') as f:
        f.write(soup)

rebuild_page('index.html')
rebuild_page('resume.html')
rebuild_page('blog.html')

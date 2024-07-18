import os
import markdown
import yaml
from bs4 import BeautifulSoup, Tag

strip_comment = lambda comment: comment.string.strip()[1:]
strip_file = lambda file_name: file_name.split('.')[0]

def read_template(template):
    with open('template/' + template[1:] + '.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    return soup

templates = set(['#' + strip_file(i) for i in os.listdir('template')])

def rebuild_page(page, dir='../'):
    with open(page, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    for template in templates:
        div = soup.find('div', {'id': template})
        if div:
            div.insert_after(read_template(template))
            div.decompose()

    div = soup.find('div', {'id': '#blog-cards'})
    if div:
        for f in os.listdir('blogs'):
            if f.endswith('-card.html'):
                with open('blogs/' + f, 'r') as f:
                    div.insert_after(BeautifulSoup(f, 'html.parser'))
        div.decompose()

    soup = soup.prettify()
    with open(dir + page, 'w') as f:
        f.write(soup)

def create_blog_card(name, yamldata):
    path = 'build/' + name
    soup = read_template('#blog-card')
    soup.find('a', {'id': '#link'})['href'] = path + '.html'
    soup.find('img', {'id': '#photo'})['src'] = yamldata['photo']
    soup.find('p', {'id': '#meta'}).append(yamldata['meta'])
    soup.find('time', {'id': '#date'}).append(yamldata['date'])
    soup.find('h3', {'id': '#title'}).append(yamldata['title'])
    soup.find('p', {'id': '#summary'}).append(yamldata['summary'])

    with open(f'{name}-card.html', 'w') as f:
        f.write(soup.prettify())

def create_blog_page(name, yamldata, md):
    md = BeautifulSoup(markdown.markdown(md), 'html.parser')
    with open('template/blog-page.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    soup.find('h2', {'id': '#title'}).append(yamldata['title'])
    soup.find('section', {'id': '#content'}).append(md)
    with open(f'{name}.html', 'w') as f:
        f.write(soup.prettify())

def parse_blog(md_file):
    with open(md_file, 'r') as f:
        data = f.read().split('---')
        yamldata, md = data[1].strip(), data[2].strip()
    yamldata = yaml.load(yamldata, yaml.BaseLoader)
    name = md_file.split('.')[0]
    create_blog_card(name, yamldata)
    create_blog_page(name, yamldata, md)

for i in os.listdir('blogs'):
    if i.endswith('.md'):
        parse_blog('blogs/' + i)
        rebuild_page(f'blogs/{i[:-3]}.html', './')
rebuild_page('index.html')
rebuild_page('resume.html')
rebuild_page('blog.html')

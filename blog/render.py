import os
from unidecode import unidecode
from database import conn
from pathlib import Path

# 1 Get the data from the database
cursor = conn.cursor()
fields = ('id', 'title', 'content', 'author')
results = cursor.execute('SELECT * FROM post;')
posts =[dict(zip(fields, post)) for post in results]

# 2 Creating the site directory
site_dir = Path('blog/site')
site_dir.mkdir(exist_ok=True)

# 3 Creating a function to generate the url with slug
def get_post_url(post):
    slug = post["title"].lower().replace(' ', '-')
    slug = unidecode(slug)
    return f'{slug}.html'

# 4 Rendering the index page
index_template = Path('blog/list.template.html').read_text()
index_page = site_dir / Path('index.html')
post_list = [
    f"<li><a href='{get_post_url(post)}'>{post['title']}</a></li>"
    for post in posts
]

index_page.write_text(index_template.format(post_list="\n".join(post_list)))

# 5 Rendering the post pages
for post in posts:
    post_template = Path('blog/post.template.html').read_text()
    post_page = site_dir / Path(get_post_url(post))
    post_page.write_text(post_template.format(post=post))

print('Site generated successfully!')
conn.close()

cmd = 'python -m http.server --directory blog/site 8000'
os.system(cmd)
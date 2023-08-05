# 1 Connect to the database
from sqlite3 import connect
conn = connect('blog/blog.db')
cursor = conn.cursor()

# 2 Create a table
conn.execute('''\
CREATE TABLE if not exists post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title varchar(100) NOT NULL UNIQUE,
    content varchar(1000) NOT NULL UNIQUE,
    author TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')

# 3 create few rows of data

posts = [
    {
        'title': 'First Post é', 
        'content': 'First post content', 
        'author': 'João'
     },
    {
        'title': 'Second Post', 
        'content': 'Second post content', 
        'author': 'Maria'
     },
     {'title': 'Third Post',
      'content': 'Third post content',
      'author': 'José'
        }
]

4 # Insert data into the table
count = cursor.execute('SELECT COUNT(*) FROM post').fetchone()[0]
if count == 0:
    cursor.executemany(
        """\
            INSERT INTO post (title, content, author) 
            VALUES (:title, :content, :author)
        """
    , posts)
    conn.commit()

5 # Check if the data was inserted
posts = cursor.execute('SELECT * FROM post').fetchall()
assert len(posts) == 3
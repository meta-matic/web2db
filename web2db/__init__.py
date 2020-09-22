import requests
import time
import pandas as pd
import sqlite3
from tqdm import trange


def dump(
        sqlite3_file_path,
        urls,
        urls_file_csv=None,
        urls_column_name='url',
        sleep_seconds=1):
    # DB connection
    conn = sqlite3.connect(sqlite3_file_path)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS WebPages
        (url text, fulltext text);
    ''')
    conn.commit()

    # Resume idx
    d = conn.execute('''
        SELECT COUNT(url) FROM WebPages;
    ''')
    idx_resume = next(d)[0]

    # Init requests session object
    s = requests.Session()

    if urls_file_csv:
        # Load URLs from CSV
        urls = pd.read_csv(urls_file_csv)[urls_column_name]

    # For each URL
    for idx in trange(len(urls), initial=idx_resume):
        # Fetch full text
        url = urls[idx]
        response = s.get(url)
        full_text = response.text
        # Persist WikiLink full text to DB
        conn.execute('''
            INSERT INTO WebPages VALUES
            (?, ?);
        ''', (url, full_text))
        conn.commit()
        # Don't be evil!
        time.sleep(sleep_seconds)


def to_df(sqlite3_file_path):
    conn = sqlite3.connect(sqlite3_file_path)
    return pd.read_sql_query('''SELECT * FROM WebPages;''', conn)


if __name__ == '__main__':
    # Dump
    sqlite3_file_path = 'tech_news_data.db'
    urls = [
        'https://www.reddit.com/',
        'https://news.ycombinator.com/',
        'https://techcrunch.com/',
        'https://www.producthunt.com/',
        'https://www.techradar.com/in'
    ]
    dump(sqlite3_file_path, urls, sleep_seconds=5)

    # Validate
    df = to_df(sqlite3_file_path)
    print(df.shape)
    print(df)

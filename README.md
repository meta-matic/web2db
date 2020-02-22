# web2db


Fetches the full text of input URLs and persists them to sqlite3 DB file.  
Fetching is resumable and comes with a progressbar.  


### Install:  
```pip install web2db```


### Quickstart:  

```python
import web2db  
web2db.dump('data.db', urls=[
    'https://www.google.com',
    'https://www.yahoo.com',
    'https://www.msn.com'
])
```

Query the DB file:
```python
conn = sqlite3.connect(sqlite3_file_path)
df = pd.read_sql_query('''SELECT * FROM WebPages;''', conn)
print(df)
...
```



### Features:
- Resumable webpage fetching
- Saves to local SQLITE3 DB
- tqdm progress bar

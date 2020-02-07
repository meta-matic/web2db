# web2db


### Quickstart:  

```python
import web2db  
web2db.dump('data.db', urls=[
    'https://www.google.com',
    'https://www.yahoo.com',
    'https://www.msn.com'
])
```


### Features:
- Resumable webpage fetching
- Saves to local SQLITE3 DB
- tqdm progress bar

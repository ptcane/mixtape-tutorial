<div class="content-links">
<a target="_blank" href="../replit-database-slides.html" class="btn btn-outline-secondary">Slideshow</a>
</div>
# The repl.it database

## Database commands

There's a simple **key:value store** associated with every repl. To work with it in Python, we first **import** the `db` module from `replit`:

    from replit import db

Then, we can:

- **Set** values: `db['my_key'] = my_value`  
- **Get** values: `my_variable = db['my_key']`  
- **Delete** entries: `del db['my_key']`  
- **List** the keys: `list(db.keys())`
- **Clear** the database: `db.clear()`

### repl.it code snippet

Fork the [repl](https://repl.it/@datadesigns/mixtape-replit-database) and **copy your `access_token` into `main.py`** (you'll need to create a new one if it's more than an hour old).



<iframe height="800px" width="100%" src="https://repl.it/@datadesigns/mixtape-replit-database?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



## Code walkthrough

```python
from auth import access_token
```
- we've imported `access_token` from `auth.py` (in which we copied our own token), and can now use `access_token` in our subequent code

```python
from replit import db
```

- we've imported the `db` module from `replit` so we can use its methods to work with the database

```python
from tracks import get_track_data, track_summary
```

- we've imported some functions from `tracks.py` which we'll use later


```python
db.clear()
```

- the `.clear()` method will remove all content (keys and values) from the database
    - remove or comment out this line if you want to re-run `main.py` without doing so...
    
```python    
track_id = '2H7PHVdQ3mXqEHXcvclTB0' #'7azo4rpSUh8nXgtonC6Pkq'
track_data = get_track_data(access_token, track_id)
```

- we assign a value to `track_id` (the commented out one is an alternative for you to try), and then call the `get_track_data()` function, using `access_token` and `track_id` as **arguments**, assigning the result to `track_data`



### `get_track_data()` function

Take a look at `tracks.py`; you'll see the **function definitions** for the two functions we imported from there into `main.py`.  

- `get_track_data()` will attempt to collect the track data from the Spotify API as we have seen previously, using the `access_token` and `track_id` supplied to it  

    - if successful, `track_data` in `main.py` will hold the returned data  
    - if not, an error will be printed and the `track_data` value will be `None`

### Writing to the database

```python
if track_data:
    db[track_id] = track_data
```

- if the `track_data` value is '**truthy**' (by this we mean not empty, zero, `False` or `None`), the following line will be executed, and `track_data` will be written to the database, as the value associated with the key of `track_id`
- if `get_track_data()` returned `None`, `track_data` would therefore be `None`, and the line underneath the `if` statement will be skipped

### Reading from the database

```python
print(list(db.keys()))

print(track_summary(db[track_id]))
```

- we used the `.keys()` method to fetch a list of the database **keys**; the object returned by this method is an **iterable**, on which we need to use the Python built-in `list()` function to get the keys themselves

- we called the `track_summary()` function, using the value from the database associated with the key equal to `track_id`, i.e. the data previously fetched from the API and stored there  

    - this function would throw an error if the key isn't in the database  
    - we `print()` the value returned by `track_summary()` function


### `track_summary()` function

We can see what `track_summary()` will do by looking at the code in `tracks.py`:

```python
summary = {
        'track_name': track_data['name'],
        'artist_name': track_data['artists'][0]['name'],
        'album_name': track_data['album']['name'],
        'image_url': track_data['album']['images'][0]['url'],
    }
```

- the function extracts specific **features** nested in `track_data` (which contained everything in the response sent by the Spotify API to our request for the given track), and returns a dictionary  

We could have extracted these features *before* writing to the database and then only storing this smaller dataset - but by storing *all* of the data from the API response, we could change which features we want to use later on, without having to make another request to the API.

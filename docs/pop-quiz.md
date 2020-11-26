# POP QUIZ

*It's quiz time, music (and / or coding) lovers!*

If you're a first-timer, please take a look at the [Exercise Guide](/resources) to see how we rock 'n' roll.

[Autograder repl](https://seeder-autograder.datadesigns.repl.co)  
[Pop Quiz repl](https://repl.it/@datadesigns/seeder-pop-quiz)

## Part 1

The early questions in relate only to the track with the `id` given below.


```python
track_id = '4u7EnebtmKWzUH433cf5Qv'
```

**How long is this track, to the nearest minute?**

- the duration is recorded in the data in millisecond
- your answer should be an integer, assigned to `duration_mins`
- be sure to round *up* if closer to the integer above

**Which artist(s) created the track?**

- your answer should be a string, assigned to `artist`
- if there's more than one, join them together into a single string separated by `', '`

**What's the `id` of the first (or only) artist who made the track?**

- your answer should be a string, assigned to `artist_id`

**How many genres are listed for this artist?**

- You'll need to collect data using the `artist_id`
- Your answer should be an integer, assigned to `number_genres`

## Part 2

In Part 2 we're going to be working with multiple tracks - so it'll pay to write functions or use iteration to gather the answers. We'll be working with the following `tracks_list`:


```python
tracks_list = ['7h1GPeQupf9g614yiSeRDv','3OYh9wHWqWD6bpmO3WQNlM',
'2HQWTyTz7VRJ8g0wbXcf7A','2mKsPUojh602HvSeNt04CB',
'2QgWuCtBpNIpl5trmKCxRf','0OQcEcs36ckWOB1nywhmBV', 
'1ymbXk2MMRS68Hdy5wSE9n','7xdLNxZCtY68x5MAOBEmBq']
```

**Which artists were involved in making these tracks?**

- create a list of all of the different artists involved
- ensure there are no duplicate entries in the list
- order the list alphabetically
- assign the list to `artists_list`

Note that you'll need the `id` for these artists for the subsquent question.

**Which genres are associated with any of the artists in `artists_set`?**

- create another list which contains all of the different genres
- ensure that there are no duplicates
- order the list alphabetically
- assign the list to `artists_genres`


```python

```

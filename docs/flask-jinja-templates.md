<div class="content-links">
<a target="_blank" href="../flask-jinja-templates-slides.html" class="btn btn-outline-secondary">Slideshow</a>
</div>
# Flask Web Apps

## Flask web framework

`flask` is a Python package which can help you to:

- quickly create dynamic web applications
- add functionality with many extensions available
- scale up in complexity when required

It is a **lightweight web application framework** which is popular, flexible, and easy to get started with.

### 'Hello, World' example

Take a look at [this repl](https://repl.it/@datadesigns/mixtape-flask-hello-world) to see how we can serve a web page with Flask:


```python
%%html
<iframe height="600px" width="100%" src="https://repl.it/@datadesigns/mixtape-flask-hello-world?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
```


<iframe height="600px" width="100%" src="https://repl.it/@datadesigns/mixtape-flask-hello-world?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>




```python
from flask import Flask
app = Flask(__name__)
```

- we imported the `Flask` class definition, and assigned an instance of it to `app`

Things we don't need to worry about for now, but:

- `__name__`is a special Python variable which determines where Flask should look for files such as templates
- `__main__` will be the value of `__name__` if this file is itself being run directly rather than by another file






```python
@app.route('/')
```
- this is a  **decorator**, which acts as a '**wrapper**' around the subsequent function
- in short this tells Flask to use the function to determine what will be shown at the 'root URL', i.e. mysite.com**`/`**

```python
def index():
    return 'Hello, World'
```

- our function returns some text, which is shown on the web page
- it could be called anything, but usually `index` is used for the root URL


```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

- `__name__` will equal `__main__` because we are running the file directly (unimportant for now)
- the `.run()` method of `app` will serve the page at the given `host` (required for replit)
- `debug=True` means we can see changes in the page without running the code again

*Try changing the 'Hello, World' text and refreshing the page.*

## Jinja templates

`jinja` is a Python package which is used for **templating**. We can use it to:

- create reusable structures for web pages (such as the header and footer)
- combine blocks of content into a single document or web page
- conditionally include elements or specific data based on user inputs

The **syntax** used in Jinja templates is **similar to Python**.

### Jinja syntax example

This code snippet is taken from the example we'll see later, showing a part of the template where rows in a template are created based on data in a list of dictionaries:

```html
    {% for activity in activities %}
    <tr>
      <th scope="row">{{ loop.index }}</th>
      <td>{{ activity['activity'] }}</td>
      <td>{{ activity['price'] }}</td>
    </tr>
    {% endfor %}

```

- we can see **statements** within `{% ... %}` tags (here designating a `for` loop)
- we can see **expressions** within `{{ ... }}` tags (here looking up values in a dictionary)

## Flask & Jinja templates

Rather than our page function to simply return text, we can use the `flask.render_template()` function to:

- return a jinja template instead to be displayed (which itself may incorporate other templates)
- pass Python data structures to be used by that template (such as lists and dictionaries)

This is a powerful combination which is central to making our web pages **dynamic**.


### Code walkthrough - Flask

Here's a Flask example which uses Jinja templating, including the code we've just seen:  

[fork the repl](https://repl.it/@datadesigns/mixtape-flask-jinja#main.py)


<iframe height="900px" width="100%" src="https://repl.it/@datadesigns/mixtape-flask-jinja?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



```python
site_name = 'Bucket List'
activities = []

for i in range(5):
    resp = requests.get('https://www.boredapi.com/api/activity?type=recreational')
    activities.append(resp.json())
```

- we've set `site_name` to a string, which we'll use in our web page
- we've used `requests.get()` as seen previously to collect data from an API
 - in this case, the [Bored API](www.boredapi.com), which doesn't require credentials
- `activities` now has a list of dictionaries containing data for our page

```python
@app.route('/')
def index():

    return render_template('index.html', site_name=site_name, activities=activities)
```

- we've called the `render_template()` function, giving our template file as the first argument, followed by two **keyword arguments** containing our data to be used by the template  
- the variable names used in the Python logic are typically (but don't have to be) the same as those used in the Jinja templates

### Code walkthrough - Jinja templates

Take a look at `base.html`:

```html
<title>{{ site_name }}</title>
```

```html
<body>    
    {% block content %}
    {% endblock %}
</body>
```

- the value passed for `site_name` will be used as the `title` (shown in the browser tab)
- any templates which **extend** this template can insert a **block** labelled `content` in the given location
_

The rest of `base.html` is simply a '**boilerplate**' or 'blank canvas' for using the **Bootstrap** CSS framework:

- the **viewport** metadata ensures the page will be **responsive**
- the Bootstrap CSS is imported from a **CDN** (Content Delivery Network)

### Blocks and extensions

Take a look at `index.html`:

```html
{% extends "base.html" %}
{% block content %}
...
{% endblock %}
```

- the `{% extends ... %}` statement tells Jinja to use `base.html` as a starting point for this template  
... placing what's between the `{% block ... %}` and `{% endblock ...%}` tags in the position with the same label (here `content`)

- there could be several such blocks within `base.html` and `index.html`, using different labels 


### Loops and dictionaries

```html
  {% for activity in activities %}
    <tr>
      <th scope="row">{{ loop.index }}</th>
      <td>{{ activity['activity'] }}</td>
      <td>{{ activity['price'] }}</td>
    </tr>
   {% endfor %}
```

- as we saw earlier, `{% for...%}` and `{% endfor... %}` designate loops to be completed for each item in a list
- we can use the same syntax as Python for getting values from dictionaries: `dictionary['key']`
- `loop.index` returns the current iteration count; note that this isn't zero-indexed, and the first value in the table is `1`
    - zero-indexed values can be obtained using `loop.index0`

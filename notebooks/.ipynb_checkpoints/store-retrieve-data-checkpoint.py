# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# # Getting data with `requests`

# %% slideshow={"slide_type": "skip"} tags=["remove"]
import requests
from requests.auth import HTTPBasicAuth
import os

# %load_ext dotenv
# %dotenv

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
print(client_id)

# %% tags=["remove"]

response = requests.post('https://accounts.spotify.com/api/token', {    
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
})
print(response.status_code)
access_token = response.json()['access_token']

print(access_token)

# %% tags=["remove-input"] language="html"
# <iframe height="800px" width="100%" src="https://repl.it/@datadesigns/mixtape-store-retrieve-data?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Code walkthrough
#
# Let's go through `main.py` and see what happened...
#
# ### Authorization headers

# %% slideshow={"slide_type": "-"}
import requests

#replace this with your current client_credentials access_token:
access_token = 'BQDNokgFn6wBLEpB1NPe-dhG4g29OWnLCPrRZGZvZ-ZlRHGPsi51els1Thy5lARaGkHVikTu4D9gB9XUeus' 

headers = {'Authorization': f'Bearer {access_token}'}

# %% [markdown]
# - we imported `requests` and assigned our token to `access_token`
# - we created a `headers` dictionary, with this `parameter:value` pair:  
#     `Authorization: Bearer [access_token]`
#     
# *Notice that we had to do some work to get the value in the format the API requires (with `Bearer ` before the `access_token`); this is mentioned in the [API documentation](https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow) but wasn't clear to me before Google came to the rescue.*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### URL components

# %% slideshow={"slide_type": "-"}
base_url = 'https://api.spotify.com/v1'
endpoint = '/tracks/'
identifier = '7azo4rpSUh8nXgtonC6Pkq'
full_url = f'{base_url}{endpoint}{identifier}'

# %% [markdown]
# - the URL is in component parts and combined using an f-string; this will allow us to make further requests to different endpoints more easily
#
# - the value assigned to `identifier` is an `album_id`; these can be found at the end of the URL of any album page on the [Spotify Web Player](https://open.spotify.com/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Response data

# %% slideshow={"slide_type": "-"}
response = requests.get(full_url, headers=headers)
data = response.json()

print(list(data.keys()), '\n\n', data['name'])

# %% [markdown]
# - we used the `.json()` method on the `Response` object to convert the JSON data into equivalent Python data stuctures
# - we took a look at the `list` of `.keys()` in the resulting dictionary
# - we fished out the value for the `name` key from the dictionary

# %% [markdown] slideshow={"slide_type": "slide"}
# ## JSON structure

# %% [markdown]
# We learned previously how JSON is made up of the following structures:  
#
# - **JSON objects**, which get converted to **Python dictionaries**
# - **JSON arrays**, which get converted to **Python lists**
#
# JSON datasets are often heavily **nested**; by this it's meant that we can expect to encounter instances of these data structures *within* others.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Example of JSON structure

# %% slideshow={"slide_type": "-"}
data['artists']

# %%
data['artists'][0]['name']

# %% [markdown]
# - the value associated with the `data` key is itself a list of dictionaries (in this case there is only one element in the list, but the structure means that several artists could be accomodated) 

# %% slideshow={"slide_type": "slide"}
print(data['artists'][0]['external_urls']['spotify'])

# %% [markdown] slideshow={"slide_type": "-"}
# - to extract the Spotify URL we are getting a value from a dictionary, which is itself a value in another dictionary, which is itself an element in a list, which is itself a value in another dictionary. Phew! 
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### The repl.it console
#
# After running the `repl` you forked earlier, you can access the `data` dictionary via the console:
#
# ![thriller](images/thriller-console.png)

# %% [markdown]
# - after running `main.py`, the `data` dictionary (and anything else imported or created) is in memory
# - as a Python `repl`, the Python **interpreter** is already running, and we can enter Python commands

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
# # Introduction to web APIs

# %% [markdown] slideshow={"slide_type": "slide"}
# ## What's an API?
#
# **API** stands for **Application Programming Interface**
#
# ... and here's a definition:
#
# > A set of functions and procedures allowing the creation of applications that access the features or data of an operating system, application, or other service.
#
# *Source: Oxford Languages via [Google](https://www.google.com/search?q=api+definition)*

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Web APIs
#
# Web APIs are used to exchange data via the internet, and typically have the following characteristics:
#
# - resources are accessed via URLs with the structure:  
#     `{base_url}{endpoint}`
#
# - support data transfer using standard HTTP methods:  
#     `GET`, `POST`, `PUT`, and `DELETE` 
#     
# - data is transferred in the following formats:  
#     `JSON`(most common and what we'll focus on), `XML` or `YAML`
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### API URLs: Example
#
# `https://api.spotify.com/v1` is the **base URL** for the main Spotify API, onto which numerous **endpoints** can be added, such as:
#
# `/browse/categories`  
# `/artists/albums`  
# `/tracks/{id}`  
#
# - the URL itself may be used to target more specific data
# - You may see the term `URI` used instead (Uniform Resource Identifier)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `GET` and `POST` HTTP methods
#
# Our focus will be on `GET` and `POST` methods (also known as **requests**), which are the methods typcially needed to **access data** from a web API.
#
# `GET`: used to **request data** from the given resource  
# `POST`: used to **send data** to create or update a resource

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `GET` requests
#
# `GET` requests can contain a **query string** of `key=value` pairs in the URL to request more specific data
# - for example: `https://api.spotify.com/v1/browse/new-releases?country=SE&limit=10`
# - the endpoint is followed by a `?` and `key=value` pairs, each separated by `&`
# - these URLs can be cached, bookmarked, or held in the browser history; *not secure*

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `POST` requests
#
# `POST` requests can send data within the **request body**
# - not cached, more secure; we'll use these for **authorization** to access data via the API
# - although we're sending data, the term **request** is usually appropariate since we require a **response**

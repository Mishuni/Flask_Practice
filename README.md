# Flask_Practice
Practice a Flask Basic


After this command, Nothing changes from how you¡¯ve been running your project so far. FLASK_APP is still set to flaskr and flask run still runs the application, but you can call it from anywhere, not just the flask-tutorial directory.
```sh
$ pip install -r
$ pip list
```

Create Secret Key
```sh
$ python -c 'import os; print(os.urandom(16))' 
```

 The development server is provided by Werkzeug for convenience, but is not designed to be particularly efficient, stable, or secure.
 You need to tell Waitress about your application, but it doesn¡¯t use FLASK_APP like flask run does. You need to tell it to import and call the application factory to get an application object.
 ```sh
$ waitress-serve --call 'flaskr:create_app'

Serving on http://0.0.0.0:8080
 ```


#### there are some ideas for what to try next:
- A detail view to show a single post. Click a post¡¯s title to go to its page.
- Like / unlike a post.
- Comments.
- Tags. Clicking a tag shows all the posts with that tag.
- A search box that filters the index page by name.
- Paged display. Only show 5 posts per page.
- Upload an image to go along with a post.
- Format posts using Markdown.
- An RSS feed of new posts.


## Reference
[Flask Tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/)
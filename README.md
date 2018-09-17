# News Highlight

<p align = "center">
    <b>By Rreuben</b>  
</p>

### Description
This application allows a user to get news from different credible sources. In the app, the user can read a snippet of the given news articles provided by the sources. The user can then proceed on to the website of the article that interests them.

***
#### The app specifications 
The app will:

    Display news sources for the user.
    Allow the user to select the news source they prefer.
    Display all the news articles from the selected source.
    Display an image description for the article.
    Display the time an article was written.
    Take the user to the full article should they choose to read it.

#### Technologies
* Python
* Flask (in Python)
* Bootstrap (for styling)
* HTML 5

View the source code at [GitHub](https://github.com/Rreuben/news)

#### Installation/Setup
You need to have Python 3.6 installed to run this program.

`$ git clone <this-repository>`<br />

Create a virtual enironment and activate it.

`$ virtualenv -p python`<br />
`$ source virtual/bin/acivate` and `(virtual)$ deactivate` is to deactivate the environment.

In the virtual environment:

`(virtual)$ pip install -r requirements.txt`<br />

Running the app.

    Prepare the environment variables.
    
        (virtual)$exportDATABASE_URL='postgresqlpsycopg2://username:password@localhost/pitch'`<br/>
        `(virtual)$ export SECRET_KEY='Your secret key'

    Run Database Migrations.

        (virtual)$ python manage.py db init
        (virtual)$ python manage.py db migrate -m "Initial migration"
        (virtual)$ python manage.py db upgrade

    Run the app.

        (virtual)$ touch start.sh

        Put #!/usr/bin/env bash as the first line in start.sh
        Put python3.6 manage.py server as the second line in start.sh

        (virtual)$ chmod a+x start.sh
        (virtual)$ ./start.sh

#### Alternatively

* Open browser (Mozilla Firefox Recommended)
* Visit the live [website](https://pewnews.herokuapp.com/)

#### Further Exploration

    Styling the news page and adding burger menu as the navigation system.
    Creating account registration.
    Creating 'Favourites' section for users who like to save stuff.

***

<p align = "center">
    <a href = "https://github.com/Rreuben/news/blob/master/LICENSE">LICENSE</a>
</p>

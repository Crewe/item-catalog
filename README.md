Item Catalog
------------

A python web application that utilizes Flask, SQLAlchemy, to create an
item catalog that users can log into with their Google+ account, via
it an OAuth2 client.

Users can add items and edit their own. As well as view what is in the
catalog. Theres is also as JSON endpoint for seeing what's in the database.

Steps
-----

1. Follow the steps found [here](https://www.udacity.com/wiki/ud197/install-vagrant) for installing vagrant.
1. Then clone this repo to a folder you wish to run it from
1. From the root directory enter the command: __vagrant up__ (If this is the first time you're doing this, you will need an active internet connection, it could take some time.)
1. Change directories into */item-catalog*
1. Connect to the virtual machine with: __vagrant ssh__
1. Change directories to */vagrant/item-catalog*

Since I did run into issues with serialization and authorization so to be safe
downgrade the follow packages by running the following:

    sudo pip install werkzeug==0.8.3
    sudo pip install flask==0.9
    sudo pip install Flask-Login==0.1.3

1. Now install the PyRSS2Gen library:

        cd PyRSS2Gen
        sudo python setup.py install
        cd ..

1. Next run __python database_setup.py__
1. Then run __python seed_database.py__ to add some items to the database
1. Start up the webserver __python project.py__
1. Fnially, navigate to [http://localhost:8000](http://localhost:8000)

API Routes:
* [http://localhost:8000/catalog/categories.json](http://localhost:8000/catalog/categories.json)
* [http://localhost:8000/catalog/items.json](http://localhost:8000/catalog/items.json)

RSS Feed:
* [http://localhost:8000/catalog/rss.xml](http://localhost:8000/catalog/rss.xml)

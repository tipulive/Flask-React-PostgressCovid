# Flask-React-Postgress

# Flask-React-Postgress Preview 
![demoapp](https://user-images.githubusercontent.com/80526946/174002907-0392d2ac-89a6-4a63-bdcc-f314f5da9505.gif)


## Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://git-scm.com/) or any Terminal(command)
* [Python](https://www.python.org/) 
* [pgAdmin](https://www.pgadmin.org/download/) (postgresdl dashboard ui) 
* [Google Chrome](https://google.com/chrome/) or any others browsers


## APP Installation('Windows')

* Open Your Terminal or Git Console
* Type `git clone https://github.com/tipulive/Flask-React-PostgressCovid.git` 
* Type `cd Flask-React-PostgressCovid`

* ### Backend installation(PYTHON) and Run Backend
* Type `cd backend`   
* `under backend Folder open .env.example fill`
- DB_NAME `this is Database Name please check your Database Name on postgresql or create one`
- DB_USERNAME `this is Database username on postgresql`
- DB_PASSWORD `this is Database password on postgresql`

* `change .env.example file to .env`
* Under backend Type `pipenv shell` to activate environment
* Under backend Type `pipenv install` to install all dependencies from pipfile
* Under backend Type `python init_db.py` to create Database Table schema
* Under backend Type `Flask run` to run App or start this backend 


* ### FrontEnd installation(React) and Run Front end
* Open New Terminal Type `cd client`   
* Type `npm install` this will install all nodes modules packages
- under client open package.json change your proxy link to your server running link
- under client Type `npm start` to run front end App 


### Note

* i have decided here to use RAW SQL instead of ORM to show you that i can be able to write SQL 



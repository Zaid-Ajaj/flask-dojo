# Flask Dojo

Code demo and snippets for the workshop of [introductory web developement](https://zaid-ajaj.github.io/web-dev-workshop/index.html) 

### Minimal Requirement
 - Python 3.0
 - Pip

Although optional, [Postman](https://www.getpostman.com/) is really nice to work with for debugging

### Getting started

```bash
# clone this repo
git clone https://github.com/Zaid-Ajaj/flask-dojo.git 

# move the directory of the application
cd flask-dojo 

# install pipenv 
pip install pipenv 

# install local packages
pipenv install

# run the web server
pipenv run python app.py
```
# Freezing dependencies
```
pipenv run pip freeze > requirements.txt
```
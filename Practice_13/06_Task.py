# Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

'''

on default python interpreter pip freeze > requirement.txt

now create virtual environment by "virtualenv env3"

activate it by ".\env3\Scripts\activate.ps1"

now install all modules in requirement.txt  in env3 by 

"pip install -r .\requirement.txt"

all default python interpreter module got downloaded into virtual environment name "env3"

'''

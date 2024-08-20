# Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

'''
first open a terminal and set a virtual environment by "virtualenv env1" name env1

activate it by ".\env1\Scripts\activate.ps1"

install some module in it
and save into a text file  "pip freeze > requirements.txt"

then deactivate it by "deactivate"

then create another virtual environment by "virtualenv env2" name env2

activate it by ".\env2\Scripts\activate.ps1"

install module of virtual environment env1 into env2 by "pip install -r .\requirements.txt" 

'''


# Setup Virtual Env 

## Python2 / 3

In case if you haven't setup virtual environment for python2, follow these steps

- Install virtualenv and virtualenvwrapper
  ```bash
  sudo pip install virtualenv virtualenvwrapper
  ```

- Open ~/.bashrc or ~/.zshrc if you are using ZSH, and add the following (you might have different paths for python2, to check use 'which python2'
  ```bash
  #virtualenvwrapper
  export WORKON_HOME=$HOME/.virtualenvs
  export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
  export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
  source /usr/local/bin/virtualenvwrapper.sh
  ```
- Then source the bashrc :
  ```bash
  source ~/.zshrc # or source ~/.bashrc 
  ```

- Create a new environment for your project:
  ```bash
  mkvirtualenv opencv -p python2 
  ```


## Python3 

- If it is not already installed, install venv :
  ```bash
  sudo apt install python3-venv
  ```

- To create a virtual environment in a given directory, type:
  ```bash
  python3 -m venv [directorypath]
  ```
  This will create `[directorypath]` if it doesn't exist, also will create directories underneath which includes python interpreter, standart libraries and misc supporting files. 

  It also creates a folder .venv.

- Once the environment is created, we need to activate it:
  ```bash
  /directorypath/Scripts/activate 
  ```
- To deactive 
  ```bash
  deactivate
  ```



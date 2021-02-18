# Python Virtual Environments

Go to the command prompt on your device and make a directory to install python in in a location you want to put these in. For this example adding to Users/username folder on device.

``` DOS
mkdir pythonver
```

Also create a project directory

``` DOS
mkdir pythonproj
```

Download version of Python you want to install and begin the python installation.

I chose to add python to the path.

When the advanced options dialogue appears asking for installation location change to the "pythonver" folder you created earlier and also add a directory for the version you are installing so you can also have multliple versions installed if required. For example installing version 3.9.1

``` DOS
C:\Users\<your username>\pythonver\python391
```

Once installed go back to the command prompt and navigate to the python project folder you set up "pythonproj".

- venv = virtual environment
- my_project = project name

``` DOS
C:\Users\<User Name>\pythonver\python391\python -m venv my_project
```

This will have created a python installation under the "my_project" directory.

From the Python project folder "pythonproj" you can type the following command into the Command Prompt to activate the virtual environment.

```DOS
my_project\Scripts\activate
```

This will change the prompt on the screen to the virtual environment

```DOS
(my_project)C:\Users\<User Name>\pythonproj
```

You can now start python by typing python into the command prompt

```DOS
python
```

You can exit python using the "exit()" command

```Python
exit()
```

You can close the virtual environment by typing the following when you have exitited the python environment

```DOS
deactivate
```

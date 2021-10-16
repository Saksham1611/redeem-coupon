## DIRECTORY NAVIGATION

![Directory Structure](/Instructions/directory.png)

#### Activate virtual environment

So, you can do a conda installation or simple python v-env . I have gone with python one ! As there I dont need that 

```bash
python3- m venv environmentname(venv)
windows: activate venv(windows)
linux  : source environmentname/bin/activate  
```
```bash
pip install -r requirements.txt
```

#### Why venv ? Package version of project remains unaffected when you update any library in local environment 

```git
git clone <url of the project>
```

#### Optional One more thing to take care of is to attach a requirements file. If you add any new library into it.  
```bash
pip freeze > requirements.txt
```

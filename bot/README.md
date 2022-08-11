## setup venv ⚙️
```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ deactivate
```

## setup project interpreter (options, ide only)

## pip install
```
(venv) $ pip3 install -r requirements.txt
 or
(venv) $ pip3 install discord.py
(venv) $ pip3 install urllib3
```
* after installed new library, you need to update requirements.txt
```
(venv) $ pip3 freeze | tee requirements.txt
```
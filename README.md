# PlaylistSync

environment and dependency management:
`pipenv`

to run locally on Linux / Mac:
```
cd {project-directory}/src/playlistSync
export FLASK_APP=playlistSync
export FLASK_ENV=development
flask init-db
flask run
```



to run locally on Windows cmd / Powershell:
```
cd {project-directory}/src/playlistSync
set FLASK_APP=playlistSync
set FLASK_ENV=development
flask init-db
flask run
```

OR
```
cd {project-directory}/src/playlistSync
$env:FLASK_APP = "playlistSync"
$env:FLASK_ENV = "development"
flask init-db
flask run
```

then open browser to http://127.0.0.1:5000



flask tutorial:
http://flask.pocoo.org/docs/1.0/tutorial/layout/


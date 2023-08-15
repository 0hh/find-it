# find-it

## Architecture
[Angular]---[FastApi]---[db]
[prod]-> github action -> AWS


## MVP
- endpoint: create item with location ✅
- endpoint: get item, get breadcrumb trail of an item ✅
- endpoint: update item ✅
- endpoint: delete item
- authenticate at backend
- get item from inmemory db
- add Angular project
- call endpoints from frontend

## Git Workflow
- check-out dev
```
git checkout dev
git pull
```

- create feature branch 

    git checkout -b feat/branch-name

- use prefix for all branches either ´feat/branch-name´ or ´fix/branch-name´
- create code changes on feature branch, then
```
    git checkout dev
    git pull
    git checkout feat/red-nav-bar
    git rebase dev
    git add .
    git commit -m "Change nav bar color to red"
    git push
```
- create pull request for dev
- ask for code review
- merge feature with dev, squash commits option checked
- delete feature branch `git branch -D feat/branch-name`
- test your feature
- merge dev with qa
- test everything
- merge qa with prod

## CICD
- dev is manually merged to qa
- qa is merged with prod as 1:1, if tests fail reverted to latest working version, copy no exceptions
- on change prod is deloyed to cloud

## Installation
### Conda Environment
install miniconda
```
    conda create -n fastapi python=3.8.16
    conda activate fastapi
    pip freeze > requirements.txt
    pip install -r requirements.txt
```

### FastAPI
start uvicorn webserver with

    cd fastapi/find-it-app/
    uvicorn main:app --reload

(books.py contains app endpoint calling webserver uvicorn  --reload flag enables live reloading during development

Uvicorn running on http://127.0.0.1:8000 by default

## Data Structure
file:///readme_img/data_structure.jpg

# rdb
n:n in relational dbms 
- one data type for all items can become containers
- moving an item with all its content is easy by replacing parent id
- infinite sub locations
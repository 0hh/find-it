# find-it

## Architecture
[Angular]---[FastApi]---[db]
[prod]-> github action -> AWS


## MVP
- authenticate at backend
- create item with location

## Git Workflow
- check-out dev

    git pull

- create feature branch 

    git checkout -b feat/branch-name

- use prefix for all branches either ´feat/branch-name´ or ´fix/branch-name´
- create code changes on feature branch, then


    git checkout dev
    git pull
    git checkout feat/red-nav-bar
    git rebase dev
    git add .
    git commit -m "Change nav bar color to red"
    git push

- create pull request for dev
- ask for code review
- merge feature with dev
- delete feature branch
- test
- merge dev with qa
- test more
- merge qa with prod

## CICD
- dev is manually merged to qa
- qa is merged with prod as 1:1 copy no exceptions
- on change prod is deloyed to cloud

## Installation
### FastAPI
start uvicorn webserver with

    fastapi % uvicorn items:app --reload

(books.py contains app endpoint calling webserver uvicorn )
### Conda Environment
install miniconda 
    conda create -n fastapi python=3.8.16
    conda activate fastapi
pip freeze > requirements.txt
pip install -r requirements.txt
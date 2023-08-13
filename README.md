# find-it

## Architecture
[Angular]---[FastApi]---[db]

## MVP
- authenticate in backend
- create item with location

## Git Workflow
- check-out dev
- git pull
- create feature branch ´git checkout -b feat/feature_name´ or fix
- code feature or fix
- git rebase dev
- create pull request for dev
- code review
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
pip install fastapi

### Conda Environment
install miniconda
conda create -n fastapi python=3.8.16
conda activate fastapi

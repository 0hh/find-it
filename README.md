# find-it

## Architecture
[Angular]---[FastApi]---[db]
[prod]-> github action -> AWS


## MVP
- endpoint: create item with location ✅
- endpoint: get item, get breadcrumb trail of an item ✅
- endpoint: update item ✅
- endpoint: delete item ✅
- endpoint: move item ✅
- endpoint: get by tag ✅
- get item from inmemory db ✅
- authenticate at backend
- add Path validations to endpoints (77)
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
- create code changes on feature branch
- format python code with black ```black main.py```, js with prettier?
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

### SQLite

Using sqlite as fast in-memory db for development only, not safe for production.

    sudo apt install sqlite3
    sqlite3 --version



    sqlite3 items.db
    sqlite> 
    INSERT INTO items (id, item_name, location_id, contains_ids, tags, owner_id) 
    VALUES (1,'Abstellkammer', null, 2, 'tag1', 1);

    INSERT INTO items (id, item_name, location_id, contains_ids,  tags, owner_id)
    VALUES (2,'Oberstes Regal', 1, 3, 'tag1', 1);

    INSERT INTO items (id, item_name, location_id, contains_ids,  tags, owner_id)
    VALUES (3,'Klebeband', 2, 2,'tag1', 1);

    INSERT INTO items (id, item_name, location_id, contains_ids, tags,  owner_id)
    VALUES (4,'Werkzeugkasten', 2, 5, 'tag1', 1);

    INSERT INTO items (id, item_name, location_id, contains_ids,  tags, owner_id)
    VALUES (5,'Hammer', 4, null, 'tag1', 1);

    INSERT INTO items (id, item_name, location_id, contains_ids,  tags, owner_id)
    VALUES (6,'Zange', 4,null, 'tag1', 1);

    sqlite> .mode table

    sqlite> SELECT * FROM items;
    ┌────┬────────────────┬─────────────┬──────────────┬──────┬──────────┐
    │ id │   item_name    │ location_id │ contains_ids │ tags │ owner_id │
    ├────┼────────────────┼─────────────┼──────────────┼──────┼──────────┤
    │ 1  │ Abstellkammer  │             │ 2            │ tag1 │ 1        │
    │ 2  │ Oberstes Regal │ 1           │ 3            │ tag1 │ 1        │
    │ 3  │ Klebeband      │ 2           │ 2            │ tag1 │ 1        │
    │ 4  │ Werkzeugkasten │ 2           │ 5            │ tag1 │ 1        │
    │ 5  │ Hammer         │ 4           │              │ tag1 │ 1        │
    │ 6  │ Zange          │ 4           │              │ tag1 │ 1        │
    └────┴────────────────┴─────────────┴──────────────┴──────┴──────────┘


    INSERT INTO users (id, email, username, full_name, hashed_password, is_active, role) VALUES (1,'dimi@mail.com', 'Ouzo61', 'Dimi Tru', 'P4$$w0rd', 1, 'admin');
    INSERT INTO users (id, email, username, full_name, hashed_password, is_active, role) VALUES (2,'theo@mail.com', 'PsychboyJack', 'Theo Geo', 'p4ss_wörd', 1, 'user');

    sqlite> SELECT * FROM users;
┌────┬───────────────┬──────────────┬───────────┬─────────────────┬───────────┬───────┐
│ id │     email     │   username   │ full_name │ hashed_password │ is_active │ role  │
├────┼───────────────┼──────────────┼───────────┼─────────────────┼───────────┼───────┤
│ 1  │ dimi@mail.com │ Ouzo61       │ Dimi Tru  │ P4$$w0rd        │ 1         │ admin │
│ 2  │ theo@mail.com │ PsychboyJack │ Theo Geo  │ p4ss_wörd       │ 1         │ user  │
└────┴───────────────┴──────────────┴───────────┴─────────────────┴───────────┴───────┘


---

# TODOs

- specify delete item behaviour
if item is deleted what happens to children? 
option A: parent becomes grandparent e.g. Workshop - Toolbox - Hammer -- Workshop - Hammer
option B: ask for new parent e.g. promt user for parameter of new location for children
if I delete Toolbox is the hammer in the Workshop, or is its location undefined?

- unpack endpoint
unpack toolbox -- Workshop -Toolbox - [Hammer, Pliers] becomes Workshop - [Hammer, Pliers]

- crud tag endpoints
- get all tags endpoint
- Path, Query validations
- implement HTTPExceptions
- move item
- item could have category: building, room, container, item

---

# Design Choices 

## Database
### Data Structure
file:///readme_img/data_structure.jpg

#### pros for relational database
- n:n in relational dbms
- logical because app is about relations of things, nosql would make more sense if app is about information on very things
- one data type for all items can become containers
- moving an item with all its content is easy by replacing parent id
- infinite sub locations
#### cons for relational database
- potentially slow, perfomance tests must be implemented and monitored
- lots of tables..

### LLM recommendation

    gpt4 , role: cs-expert, question1, question2, use FastAPI for backend communication, example data:            
    
    "example": {
                "item_name": "Fünfteiliges Bit-Set Bosch Professional",
                "location_id": 4,
                "contains_ids": [23, 24, 25, 26, 27],
                "tags": ["Akkuschrauber", "Bosch", "Werkzeug", "Kreuz", "Schlitz"],
            }

### 1. Which database type is suited best for a small but scalable project?
For small but scalable projects, both relational databases (RDBMS) like PostgreSQL, MySQL, SQLite and non-relational databases (NoSQL) like MongoDB, CouchDB, or Cassandra can be suitable. The best choice often depends on the nature of the data and the queries you expect:

Relational Databases (RDBMS): Well-suited for structured data with relationships between different entities. They can handle complex queries and transactions. However, they can become slower as the dataset grows if not optimized properly.

Non-Relational Databases (NoSQL): Good for projects where the data schema may evolve rapidly, or where you need high performance and scalability for write-heavy or distributed workloads. They are often faster with large datasets but may not support complex queries or transactions as efficiently.

### 2. Which database do you recommend if you have to choose one?
Considering the sample data, which seems structured and has relationships (e.g., items related to locations or other items they contain), I'd recommend a relational database. Among RDBMS options, PostgreSQL is a great choice due to its scalability, robustness, and rich set of features.
**Recommendation**: PostgreSQL

Now, let's design a simple schema for the inventory app:

Tables:
- users: To store user details.
- items: To store item details.
- locations: To store different locations.
- tags: To store different tags.
- item_tags: To associate items with tags.
- item_contains: To associate items with other items they contain.

Schema:

    CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        -- ... other user-related columns ...
    );

    CREATE TABLE locations (
        location_id SERIAL PRIMARY KEY,
        location_name VARCHAR(255) NOT NULL
    );

    CREATE TABLE tags (
        tag_id SERIAL PRIMARY KEY,
        tag_name VARCHAR(255) NOT NULL
    );

    CREATE TABLE items (
        item_id SERIAL PRIMARY KEY,
        item_name VARCHAR(255) NOT NULL,
        location_id INTEGER REFERENCES locations(location_id)
        -- ... other item-related columns ...
    );

    CREATE TABLE item_tags (
        item_id INTEGER REFERENCES items(item_id),
        tag_id INTEGER REFERENCES tags(tag_id),
        PRIMARY KEY (item_id, tag_id)
    );

    CREATE TABLE item_contains (
        parent_item_id INTEGER REFERENCES items(item_id),
        child_item_id INTEGER REFERENCES items(item_id),
        PRIMARY KEY (parent_item_id, child_item_id)
    );

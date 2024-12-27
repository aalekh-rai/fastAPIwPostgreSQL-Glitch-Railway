This is a prototype application deployed using Glitch and Railway. Database is stored in a PostgreSQL instance on Railway App and program files are stored on Glich.

#Setup your database on Railway

Step 1: Visit '[railway.com](https://railway.com/)' and create a database instance using PostgreSQL service.

Step 2: Name this service as 'Postgres', this is your database name.

Step 3: Open the service and Go to 'data' tab, create a table here, named as 'teams' with columns as 'id', 'name' and 'city'.

Step 4: Go to 'variables' tab for credentials like 'database url', 'username', 'password' etc.

#Setup your project on Glitch

Step 5: Go to '[https://glitch.com/](https://glitch.com/)' and create a new project.

Step 6: Upload all these 5 files from github to glitch, 'procfile', 'database.py', 'main.py', 'models.py', 'requirements.txt'.

Step 7: Create another file, name it as 'startup.sh'

Step 8: Copy Paste following content into it:

python3 -m pip install -U pip

python3 -m pip install -r requirements.txt

python3 main.py

#!/bin/bash

uvicorn main:app --host=0.0.0.0 --port=$PORT

Step 9: Go to .env file, create two variables, 'PYTHON_VERSION', assign it's value as 3.7 and another 'DATABASE_URL', copy paste the database url value from the 'railway app/variables' tab.

Step 10: Run your Glitch project, it should successfully be connected with your railway database instance. If you encounter any errors,try to solve them with the help of glitch logs. Check out some sample projects on Glitch with Python here: 'https://glitch.com/@python'.

#Run your application

Step 11: Once your application is running, simply open the link provided by glitch to test it. add '/docs' at the end of the url to check all the fastAPI endpoints.

For any help or assistance, connect aalekh.rai.futurense@gmail.com

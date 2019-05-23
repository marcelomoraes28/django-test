[![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)](https://img.shields.io/badge/python-3.6-blue.svg)

# Team Happiness
The "Team Happiness" is a django project that you can measure the happiness of your team.

## Getting Started

These instructions will help you to run the project.

**Basic requirements**
- python3.6
- npm 6.9.0

*Attention: This project has been tested using only these service versions.*

### External libraries

For tests:
- **coverage**
- **factory-boy**
- **freezegun**

Front-end:
- **bootrap@4.3.1**
- **jquery@3.4.1**
- **chart.js@2.8.0**
- **popper.js@1.15.0**

### Running the project

```
./run_dev.sh
```

### Resources

- **Home:** /
- **Answer happiness:** /poll/new
- **Happiness:** /poll
- **Admin**: /admin

### Running the tests

```
./run_test.sh
```

### Create super user
Go to the folder happiness and run the code below
```
python manage.py createsuperuser
```

*Obs: Check if if your venv is active*

## Business rules

### The Teams
Every user in the system must be in a Team.

**Rules:** The logged-in user will only see the metrics of their team (Happiness resource).

Add a user in a team
- Login with a superuser in /admin;
- Click in "Users" link;
- Search for the desired user and change the team in the combobox;

### Polls
The polls will show two charts with some important information about the happiness team.

*Bonus: "average per day", "average per week", "total per day", "total per week"*

**The first chart (Bar Chart)**
- **My Happiness:** My happiness level today
- **Average per day:** Average of happiness level of my team today
- **Average per week:** Average of happiness level of my team per week
- **Average from the beginning:** Average of happiness level of my team since the beginning

**The second chart (Pizza Chart)**
- **Total level per day level (n):** Total of votes of my team in the level (n) per day;
- **Total per week level (n):** Total of votes of my team in the level (n) per week;
- **Total (n):** Total of votes of my team in the level (n) since the beginning

# Star Wars: The Clone Wars REST API

REST API of Star Wars: The Clone Wars (animated series) chapter opening quotes.

![TCW-API](https://github.com/AstronautMarkus/sw_clonewars-api/assets/142458866/941ae4b0-d945-4d05-9689-3469d69bc8d1)

# Description

`Star_Wars_TheCloneWars_REST-API` is a REST API that provides opening quotes from the animated series Star Wars: The Clone Wars. It is built in Python using Flask and SQLite.

# How to Run Locally

1. **Create virtual environment:**

   - If you are using Windows, run `create_env.bat`.
   - If you are using bash, run `create_env.sh`.
   - The requirements will be installed automatically.\
2. **Start virtual environment**:
    - If you are using Windows, use `venv/Scripts/Activate` in your terminal.
    - If you are using bash, use   `source/venv/bin/activate` in your terminal.
    - With the virtual environment enabled, run `main.py`.

#### After completing these steps, the system will create the database and also insert the data, then it will start automatically.

## URLs

- **GET /quotes:** Returns the entire list of quotes.
- **GET /quotes/{language}:** Returns quotes in the specified language.
  - Example: `/quotes/english` Returns all quotes in English.
- **GET /quotes/quote_id:** Returns a quote by its ID.
  - Example: `/quotes/1` Returns the appointment with ID 1.
- **GET /quotes/random/{language}:** Returns a random quote in the specified language.
  - Example: `/quotes/random/english` Returns a random quote in English.
- **GET /languages:** Returns the complete list of available languages.

## Requirements

The requirements needed for this project are found in the file [`requirements.txt`](https://github.com/AstronautMarkus/Star_Wars_TheCloneWars_REST-API/blob/dev/requirements.txt).


## License

This project is under the GPL-3.0 license.


## Main Files

- `main.py`: Main file to run the application.
- `create_database.py`: Script to create the database. (It runs automatically, do not touch)
- `create_env.bat` & `create_env.sh`: Scripts to create the virtual environment.
- `requirements.txt`: File with the necessary dependencies.


## License

This project is licensed by [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).



---

#### **Repository:** [Star_Wars_TheCloneWars_REST-API](https://github.com/AstronautMarkus/Star_Wars_TheCloneWars_REST-API)
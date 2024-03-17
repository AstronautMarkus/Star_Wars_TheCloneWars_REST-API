# sw_clonewars-api

REST API of Star Wars: The Clone Wars (animated series) chapter opening quotes.

![TCW-API](https://github.com/AstronautMarkus/sw_clonewars-api/assets/142458866/941ae4b0-d945-4d05-9689-3469d69bc8d1)

# Description

## sw_clonewars-api is an API about Star Wars: The Clone Wars opening quotes, built in Python, using Flask and SQLite.

# How to Run Locally

1. Open `create_env.bat` if you're using Windows or `create_env.sh` for bash. The dependencies will install automatically.
2. Start the virtual environment by navigating to `sw_clonewars-api\venv\Scripts\Activate`, and with the environment open, run the `main.py` file.
3. Now, before using the API, you need to create the database table and insert the data. To do this, you need a database browser. I recommend using [DB Browser for SQLite](https://sqlitebrowser.org/). Then, create the table with `script_database.sql` and insert the data with `insert_data.sql`.
4. Write the changes to the database, and everything will be ready!

# URLs

You can use `/quotes` for the full quotes list or `/quotes/random` for a random list.

### For now, just that. I hope this API with inspiring phrases is useful to you! Hehe!

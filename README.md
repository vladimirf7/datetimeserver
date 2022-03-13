# Datetime Server

This server listens for TCP or UDP requests and returns current date and/or time in ISO 8601 format. Three request formats are currently supported:
- "date" --> returns the current date (YYYY-MM-DD)
- "time" --> returns the current time (hh:mm:ss, with timezone)
- "datetime" --> returns combined date and time (YYYY-MM-DDThh:mm:ss, with timezone)

The server does not use any pip packages hence virtual env is not being used.

## Things to added later
- pylint
- pytest
- click
- Add usage description
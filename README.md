# Datetime Server

This server listens for TCP or UDP requests and returns current date and/or time in ISO 8601 format. Three request formats are currently supported:
- "date" --> returns the current date (YYYY-MM-DD)
- "time" --> returns the current time (hh:mm:ss, with timezone)
- "datetime" --> returns combined date and time (YYYY-MM-DDThh:mm:ss, with timezone)

## Usage
PORT is optional for all scripts, defaults to 8000
### UDP Server
1. Start UDP server: `python server_udp.py PORT`
2. Start UDP client: `python client_udp.py PORT` It will make 3 requests to the server and output the replies

### TCP Server
1. Start TCP server: `python server_tcp.py PORT`
2. Start TCP client: `python client_tcp.py PORT` It will make 3 requests to the server and output the replies

## Things to improve
- Add virtual env
- Add pylint to follow code conventions
- Add pytest for unit tests
- Add click for better CLI experience
- Add usage information
- Extract duplicated code
- Rework send_request() for TCP

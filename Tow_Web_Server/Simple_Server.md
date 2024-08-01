# Simple HTTP Server

This project is a simple HTTP server written in Python. The server is designed to serve files from the current directory, using Python's built-in `http.server` and `socketserver` modules. It's a lightweight solution for quickly setting up a local web server for development or testing.

## How It Works

When you run this script, it will start an HTTP server on the local machine (`127.0.0.1`) on port `5555`. The server will serve files **from the same directory where the script is located**. 

You can access the server by opening a web browser and navigating to: http://127.0.0.1:5555

This URL will display the contents of the directory, allowing you to access any files stored there. The server will continue running and serve any files requested until you stop the program. 

**Note:** For the server to successfully serve the files, ensure that all the files you want to access are in the same directory as the script.


### Code Breakdown

- **Imports:**
  - `http.server`: Provides the `SimpleHTTPRequestHandler` class to serve files over HTTP.
  - `socketserver`: Provides a framework for network servers, including the `TCPServer` class.

- **Configuration:**
  - `Port = 5555`: Sets the port number for the server.
  - `Host = '127.0.0.1'`: Sets the host IP address (loopback address for local connections).

- **Server Initialization:**
  - `Handler = http.server.SimpleHTTPRequestHandler`: Defines the request handler.
  - `server = socketserver.TCPServer((Host, Port), Handler)`: Creates an instance of `TCPServer`, binding it to the specified host and port.

- **Run Function:**
  - `def run()`: A function that starts the server, prints a message indicating the server's status, and enters an infinite loop to handle incoming requests.

- **Starting the Server:**
  - The `run()` function is called, which initiates the server to start listening on the configured port and handle requests indefinitely.

## Installation

No special installation is required. The script uses Python's standard library modules.

## Usage

1. **Start the Server:**
   Run the script in the terminal:

   ```bash
   python server.py
   
This will start the server on port 5555 by default.

### Access the Server:
Open a web browser and go to: http://127.0.0.1:5555

This URL will display the contents of the directory where the script is located.

### Stop the Server:
To stop the server, interrupt the process (e.g., by pressing `Ctrl+C` in the terminal).

## Customization
- **Port Number:** Modify the `Port` variable to change the port the server listens on.
- **Host Address:** Modify the `Host` variable to change the IP address the server binds to. Note that `127.0.0.1` restricts access to the local machine.

## License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests for improvements or new features.



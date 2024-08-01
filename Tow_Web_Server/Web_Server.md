# Custom HTTP Server

This project is a simple HTTP server written in Python, using the `http.server` module. It handles HTTP GET requests and responds with a basic HTML message. This server is a good starting point for building more complex web servers.

## How It Works

When you run the script, it starts an HTTP server on your local machine (`127.0.0.1`) on port `5566`. The server serves files from the directory where the script is located. 

### Accessing the Server

To see the server in action:
1. Run the script by executing the following command in your terminal:

    ```bash
    python server.py
    ```

2. Open a web browser and navigate to:

    ```
    http://127.0.0.1:5566
    ```

   You will see the HTML message `<h1> Write Html code</h1>`.

### Stopping the Server

To stop the server:
- Interrupt the process by pressing `Ctrl+C` in the terminal where the server is running.

## Code Breakdown

Here’s a brief overview of how the server script is structured:

- **Imports:**
  - `BaseHTTPRequestHandler` from `http.server` handles HTTP requests.
  - `HTTPServer` from `http.server` creates the server.

- **Configuration:**
  - `Host = "127.0.0.1"`: The server is only accessible from the local machine.
  - `Port = 5566`: The port number on which the server listens.

- **RequestHandler Class:**
  - Inherits from `BaseHTTPRequestHandler`.
  - The `do_GET` method responds to GET requests with a simple HTML message.

- **HTTPServer Class:**
  - Inherits from `HTTPServer`.
  - The `__init__` method sets up the server with the host, port, and request handler.

- **run_server Function:**
  - Creates an instance of `HTTPServer` with the specified host and port.
  - Starts the server to handle incoming requests.

## Customization

You can customize the server by modifying the following:

- **Port Number:** Change the `Port` variable to use a different port.
- **Host Address:** Update the `Host` variable to bind the server to a different IP address. Note that `127.0.0.1` limits access to the local machine only.

## License

This project is open-source and licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! You can fork this repository and submit pull requests for improvements or new features.

---

Feel free to adjust the details as needed for your project. This format provides a clear and accessible explanation of the server, its functionality, and how to use and customize it.

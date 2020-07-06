- The key is the `XMLHttpRequest` object
    - `var xhttp = new XMLHttpRequest();` should do it.

Methods
=======
- `open(method,url,async,user,psw)` 
    - Specifies the request
    - method: the request type GET or POST
    - url: the file location
    - async: true (asynchronous) or false (synchronous)
    - user: optional user name
    - psw: optional password
`send()` 
    - Sends the request to the server; Used for GET requests
`send(string)` 
    - Sends the request to the server; Used for POST requests

XMLHttpRequest Object Properties
================================

Property                            Description
-----------------------------------------------
`onreadystatechange` 	            Defines a function to be called when the readyState property changes
`readyState`                        Holds the status of the XMLHttpRequest.
                                        - 0: request not initialized
                                        - 1: server connection established
                                        - 2: request received
                                        - 3: processing request
                                        - 4: request finished and response is ready
`responseText` 	                    Returns the response data as a string
`responseXML` 	                    Returns the response data as XML data
`status` 	                        Returns the status-number of a request
                                        - 200: "OK"
                                        - 403: "Forbidden"
                                        - 404: "Not Found"
`statusText`                    	Returns the status-text (e.g. "OK" or "Not Found")

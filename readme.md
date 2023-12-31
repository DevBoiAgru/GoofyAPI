# Very goofy Python wrapper for a goofy API
## By DevBoiAgru

You can make http calls yourself [here](https://sussyworkshop.pythonanywhere.com/).


### Functions:
1. ```ip()```: Returns a randomly generated **FAKE** ip address (returns a string)
2. ```Quote()```: Returns a random quote from the baby blue club in the following format: [author, quote] (returns a python list)
3. ```password(length)```: Returns a random password of specified length (returns a string)


## How to use:
- Download goofy.py
- Put it in your root folder
- Import the whole module using ```import goofy``` or import functions separately using ```from goofy import <function name>```
- Use as usual!


## Requirements:
- requests module

<hr>

# HTTP Calls

If you are not using python, or just don't want to put a goofy.py in your directory, you can use the following endpoints to fetch data. <br>

Base url: <code>https://sussyworkshop.pythonanywhere.com</code>

Add a "code" header with whatever content you want so that it doesnt return you the HTML page!

## Quote

Method:   <code>GET</code>      <br>
Endpoint: <code>/quote</code>      <br>
Sample response: <br>
>{<br>
    "author": "themuye", <br>
	"error": "None", <br>
	"quote": "If ya wanna become monke press f "<br>
}


## IP

Method:   <code>GET</code>      <br>
Endpoint: <code>/ip</code>      <br>
Sample response: <br>
>{<br>
	"error": "None",<br>
	"ip": "69.69.69.69"<br>
}


## Password

Method:   <code>GET</code>       <br>
Endpoint: <code>/password</code>       <br>
Supported query string: <code>length</code> <br>
Sample response: <br>
>{<br>
	"error": "None",<br>
	"password": "`1072d+'GIH6"<br>
}<br>







## More coming soon!

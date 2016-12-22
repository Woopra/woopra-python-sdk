Track customers directly in Python using Woopra's Python SDK

The purpose of this SDK is to allow our customers who have servers running Python to track their users by writing only Python code. Tracking directly in Python will allow you to track your users through the back-end without having to handle http requests manually.

## Installation
```python
 pip install git+https://github.com/Woopra/woopra-python-sdk.git
```

## Usage
The first step is to setup the tracker SDK. To do so, configure the tracker instance as follows (replace mybusiness.com with your website as registered on Woopra):

```python
#import the SDK
from woopra import WoopraTracker

woopra = WoopraTracker("mybusiness.com")
```

You can configure the cookie value - To Woopra, this is equivalent to the browser cookie or anonymous user ID - required only if the user is not identified with an email or an id property
```python
woopra.set_cookie('ABCXYAZ111')
```

You can also configure the timeout (in milliseconds, defaults to 30000 - equivalent to 30 seconds) after which the event will expire and the visit will be marked as offline:

```python
# set the timeout to 15 seconds:
woopra.set_idle_timeout(15000)
```

You can also configure the source ip address:
```python
woopra.set_ip_address('66.228.55.188')
```

You can also configure the user agent:
```python
woopra.set_user_agent('Mozilla/Agent..............)
```

You can also configure the secure (https) tracking:

```python
woopra.set_secure(True)
```

To identify a user, you should use the <code>identify()</code> function. You can choose to identify the visitor with his EMAIL, or with a UNIQUE_ID of your choice (in this case, make sure to re-use the same ID for a given visitor accross different visits).

```
woopra.identify(
	{
		'email' : 'tigi@mail.com',
		'name' : 'Tigi Brombo',
		'admin' : False
	}
)
```

And you're ready to start tracking events:
```python
woopra.track("play", {
	"artist" : "Dave Brubeck",
	"song" : "Take Five",
	"genre" : "Jazz"
})
```

Or just push the user information (without event tracking) by doing:
```python
woopra.push()
```


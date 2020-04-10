[Русский](https://github.com/wultes/vkbotsapi/blob/master/README.md) | [English](https://github.com/wultes/vkbotsapi/blob/master/README_ENG.md)

# vkbotsapi

This module allows you to work with VK API.

### ❗️ Warning 

Module works with BotLongPoll. That is, you can use this module **only on behalf of the community**. 

### 💿 Install 

You can [download](https://github.com/wultes/vkbotsapi/archive/master.zip) or clone module using command:

```bash
git clone https://github.com/wultes/vkbotsapi
```

Or you can use ```pip```:

```bash
pip install vkbotsapi
```



### 🚀 Using

In order to use this module, you need to import it.

```python
from vkbotsapi.api import VKAPI
```

Next, create an object with the class `` VKAPI`` and pass it the token and group ID.

```python
from vkbotsapi.api import VKAPI

vk_api = VKAPI(token='', group_id='')
```

Now, you can use module. Example:

```python
from vkbotsapi.api import VKAPI
import random

vk_api = VKAPI(token='', group_id='')
vk_api.sendMessage(
	message='Hello World',
    	peer_id='1',
    	random_id=random.randint(1, 10 ** 8)
	)
```



### 📃 License

This module is licensed. [MIT](https://choosealicense.com/licenses/mit/).  
Copyright © 2020 [Wultes](https://github.com/wultes/).



### ✉️ Communication

If you have questions about the module, you can always contact me through [Telegram](https://t.me/wultes).




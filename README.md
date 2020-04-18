[Русский](https://github.com/wultes/vkbotsapi/blob/master/README.md) | [English](https://github.com/wultes/vkbotsapi/blob/master/README_ENG.md)

# vkbotsapi

Данный модуль позволяет работать с VK API. 

### ❗️ Предупреждение 

Модуль работает с BotLongPoll. То есть, использовать данный модуль вы сможете **только от лица сообщества**. 

### 💿 Установка 

Вы можете [cкачайте](https://github.com/wultes/vkbotsapi/archive/master.zip) или склонировать модуль используя команду:

```bash
git clone https://github.com/wultes/vkbotsapi
```

Или вы можете использовать ```pip```:

```bash
pip install vkbotsapi
```



### 🚀 Использование

Для того, чтобы использовать данный модуль, его нужно импортировать.

```python
from vkbotsapi.api import VKAPI
```

Далее, создайте объект с классом ```VKAPI``` и передайте ему токен и ID группы.

```python
from vkbotsapi.api import VKAPI

vk_api = VKAPI(token='', group_id='')
```

Теперь вы можете использовать модуль. Например:

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



### 🔌 Описание функций

Описание функций вы можете посмотреть в [Wiki](https://github.com/wultes/vkbotsapi/wiki)



### 📃 Лицензия

Данный модуль распространяется под лицензией [MIT](https://choosealicense.com/licenses/mit/).  
Copyright © 2020 [Wultes](https://github.com/wultes/).



### ✉️ Связь

Если у вас есть вопросы насчет модуля, то всегда можете связаться со мной через [Telegram](https://t.me/wultes).




![BGLogger logo](https://media.discordapp.net/attachments/1078425365095133366/1143160563699032165/119_20230821153145.png?width=1037&height=392)
# BGLogger 1.2.0
BGLogger is a simple module for logging in Python.
## How to install the module
Before using the module, you have to first install it. You can do this using the pip package manager in CMD or another terminal:
```python
pip install BGLogger
```
Or you can move the BGLogger package from repository to your project.
## Get started
You should initialize instance of the Log class. In the module, each instance of the Log class refers to a specific process. It means you must name every logging process.
```python
log = Log(process_name='SOME PROCESS', record=True, return_every_log=False, output_style=OutputStyle.UNDERLINE, color=True)
```

|argument|type|description|
|--------|----|-----------|
|process_name|str|Name of your logging process|
|record|bool|Recording logs for output to a file|
|return_every_log|bool|Returning every log line|
|output_style|OutputStyle|Style of output in the console (May be BOLD/UNDERLINE/REGULAR)|
|color|bool|Colors each log in a specific color. If the colors are displayed incorrectly, it is better to turn off the coloring|

## Logging
Now that you have initialized Log object you are able to log every action.
But what methods allow you to do it? Let is find out from the table:

|method|log level|arguments|
|------|---------|---------|
|s|SUCCESS|tag, message|
|w|WARNING|tag, message|
|i|INFO|tag, message|
|f|FATAL|tag, message, exit_type, exception|
|e|ERROR|tag, message|
|d|DEBUG|tag, message|

As you noticed, each method has tag and message arguments. The table below describes each of them:
|argument|methods|type|descrition|
|--------|-------|----|----------|
|tag|s, w, i, f, e, d|str|Tag of your log|
|message|s, w, i, f, e, d|str|Message of your log|
|exit_type|f|ExitType|Type of stopping your program when calling a fatal log (May be RAISE_EXCEPTION or EXIT)|
|exception|f|Exception|Exception that will be raised if exit_type is equals to RAISE_EXCEPTION|

`ExitType` attributes and what they mean:
|attribute|description|
|---------|-----------|
|RAISE_EXCEPTION|Raise an exception|
|EXIT|Stop the program with exit code `1`|

Example of using different logging methods:
```python
import BGLogger
from BGLogger import *

log = Log(process_name='TESTING LOG SYSTEM', record=True, return_every_log=False, output_style=OutputStyle.UNDERLINE, color=True)

log.d(tag='TEST', message='DEBUG LOG IS COOL')
log.i(tag='TEST', message='INFO LOG IS COOL')
log.e(tag='TEST', message='ERROR LOG IS COOL')
log.s(tag='TEST', message='SUCCESS LOG IS COOL')
log.w(tag='TEST', message='WARNING LOG IS COOL')
log.f(tag='TEST', message='OH NO! FATAL EXCEPTION!!!', exit_type=ExitType.RAISE_EXCEPTION)
```
## Save logs to a file
To save logs to a file you should call `save_logs_to_file()`, which has the following argument:
|argument|type|description|
|--------|----|-----------|
|file_name|str|The file where the logs will be saved|

Example:
```python
from BGLogger.BGLogger import *

log = Log(process_name='TESTING LOG SYSTEM', record=True, return_every_log=False, output_style=OutputStyle.UNDERLINE, color=True)

log.d(tag='TEST', message='DEBUG LOG IS COOL')
log.i(tag='TEST', message='INFO LOG IS COOL')
log.e(tag='TEST', message='ERROR LOG IS COOL')
log.s(tag='TEST', message='SUCCESS LOG IS COOL')
log.w(tag='TEST', message='WARNING LOG IS COOL')
log.save_logs_to_file('logging result')
log.f(tag='TEST', message='FATAL LOG WILL BE THE LAST IN YOUR ALIVE PROGRAM. That\'s why you should save your logs to a file first', exit_type=ExitType.RAISE_EXCEPTION)
```

The logging result will be saved to a TXT file. 

```
---*--- "TESTING LOG SYSTEM" LOGGING RESULT ---*---
DEBUG -*- 2023-08-22 20:05:15.716821 -*- [TEST]   'DEBUG LOG IS COOL'
INFO -*- 2023-08-22 20:05:15.716893 -*- [TEST]   'INFO LOG IS COOL'
ERROR -*- 2023-08-22 20:05:15.716950 -*- [TEST]   'ERROR LOG IS COOL'
SUCCESS -*- 2023-08-22 20:05:15.716991 -*- [TEST]   'SUCCESS LOG IS COOL'
WARNING -*- 2023-08-22 20:05:15.717025 -*- [TEST]   'WARNING LOG IS COOL'

----------- *** -----------
DEBUG LOGS: 1
INFO LOGS: 1
WARNING LOGS: 1
ERROR LOGS: 1
SUCCESS LOGS: 1
FATAL LOGS: 0


### SAVE DATE: 2023-08-22 20:05:15.717221 ###
```

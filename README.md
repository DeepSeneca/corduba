Corduba
-------
A provisioning server for the DeepSeneca App based on Python and FastAPI. Since Corduba is currently in the proof-of-concept stage, I recommend running it only in a secure network environment, such as a local network.

Prerequisites
-------------
#### Python
The provisioning server is implemented in Python using FastAPI. The minimum required Python version is **3.12 or higher**.

#### Uvicorn
Uvicorn is an asynchronous web server implementation based on the ASGI (Asynchronous Server Gateway Interface) standard. It is designed to serve ASGI applications, which are a modern replacement for the older WSGI standard. This is used to run FastAPI apps, on which Corduba is based.

Installation
------------
After cloning the project, create a python environment and run 

```
pip install -r requirements.txt
```
to install the dependencies required for running corduba.

Running corduba
---------------
Corduba has been tested on Windows 10. As there are no exotic dependencies, it may work on other systems as well.
#### Windows 10

Corduba uses Uvicorn as a wrapper. In order to run corduba either use the included
```
run_corduba.bat
``` 
batch file (don't forget to update the IP address and port as necessary for your system) **OR** run
```
uvicorn corduba.main:app --host [your ip address] --port [your port] --reload
```
in your activated Python environment. If successfull, Corduba will greet you with a message including the version.

````
###################################
##                               ##
##  Corduba provisioning server  ##
##  Version: 1.0.0               ##
##                               ##
###################################
````

Daily tasks file
----------------
#### Purpose
The daily task file is a template which describes the tasks and their attributes for one day. You can view this as a 
complete daily routine. Gets fetched by the Seneca Android app. I included an example file for demo purposes.
#### Structure
The filename is structured as:
```
"user_" + [user_number].csv
```
The included example is ```user_0.csv```. Daily tasks files always start with ```user_```. The ```user_number``` element is used as a 
parameter for the ```/provision_day/{user}/``` REST-endpoint (see also below). If you connect to endpoint
```
/provision_day/0/
```
, Corduba will load ```user_0.csv``` from the ```data``` directory and provide this structure to the app.

#### Example entries of a Daily Task File:

```
senTaskId,taskname,tasktype,ispomo,duration
1,"Demo Item 1, inclusive comma (from server)",8,true,-1
2,"Continuing Item 1 (from server)",4,true,-1
3,"Continuing Item 2 (from server)",4,true,-1
4,"Ün Ümläütext",1,true,-1
5,"Continuing item 3 (from server)",4,true,-1
6,"Continuing item 4 (from server)",4,true,-1
7,"Demo Item 3 (from server)",2,true,-1
8,"Timed item 1",10,false,28
9,"Untimed item 2",10,false,-1
```

The columns of the **.csv** file are defined as follows:

|Column| Description                                                                                                                                                                                                                                                                           |
| --- |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|senTaskId| A unique id for the task. This is used by the app to reference the task.                                                                                                                                                                                                              |
|taskname| The name of the task as displayed in the app                                                                                                                                                                                                                                          |
|tasktype| The type of task. Is used by the SenecaAI for further categorization. You can choose a number freely for the task, as long as it is consistent across the days.                                                                                                                       |
|ispomo| true if this is a timed Pomodoro task. These represent flexible tasks during the day (e.g. if you are working on a project, you may want to reserve a certain amount of "Pomo"-tasks for the day which you can customize on the go. The duration of such tasks can be set in the app. |
|duration| A value for timed tasks. E.g if you want to do physical exercise each day for 10 minutes, the value of duration would be 10. The task becomes timed as soon as you set this value not to -1.                                                                                          |

The first entry ```1,"Demo Item 1, inclusive comma (from server)",8,true,-1``` in our example above therefore means:

```1```: the id of the task

```"Demo Item 1, inclusive comma (from server)"```: The name as displayed in the app.

```8```: The task type, could be any number, the meaning is up to you (e.g. physical exercise, music, etc.)

```true```: Signals that this task is a 'Pomo' task. This means it is timed by the app.

```-1```: No duration is set, timing is determined by app settings. If you would have a timed task that does not fit in
the 'Pomo' task category, you would set this value to the number of minutes you like.

Refer to ```/data/user_0.csv``` in the repository directory for an example.

REST endpoints
--------------

| Endpoint                    | Description                                                                                                                                                                       |HTTP method|
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| --- |
| /                           | General info endpoint, returns the version of Corduba                                                                                                                             |GET|
| /items/{item_id}/| Deprecated, will be removed                                                                                                                                                       |GET|
| /items/{item_id}/| Deprecated, will be removed                                                                                                                                                       |PUT|
|/provision_day/{user}| Get the "user_{user}.csv" file which represents all tasks of one day. Parameter user should be an integer. Daily task files should be placed in "/data" directory.|GET|
|/current_model| Returns the current trained model. Currently located at "/data/current_model/model.ptl". The model is not yet provided by this repository, feel free to put one in the directory. |GET|
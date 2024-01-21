# Air Hockey
This is a multiplayer online game completed by socket. The client part is written in python, while the server side has two versions: c++ and python.


![\[!\[IMAGE ALT TEXT\](https://youtu.be/qF6PpO1Rw2U)\](https://youtu.be/qF6PpO1Rw2U "Unity Snake Game")](<video/Multiple Players Multiple Pucks  Win.gif>)

## Operation
If you want to play in a multiplayer mode, you must first execute the server. Then, the client will connect to the server and wait for other players to join the game. Ensure that the IP address and port are set to your computer's IP so that you can enjoy the game on your PC

## Environment

***client***
```
Enviroment     -> Windows
Python Version -> Python 3.12.1
Pygame Version -> Pygame 2.5.2
```

***server***
Python
```
Enviroment     -> Windows
Python Version -> Python 3.12.1
```
C++
```
Enviroment     -> buntu1 22.04
C++ Version    -> gcc 11.4.0
```

***client***

It put in client_src
```
python3 client_connect.py
```

***server***

It put in server_src

C++
```
make
```
python
```
python3 server.cpp
```
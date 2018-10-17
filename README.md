# snakes_on_lan
Snakes on LAN

## Initial thoughts
### Classes

#### Common side
1. Snake
	1. size
	+ position - as list?
	+ initial_size
	+ is_alive
	+ eat/grow
+ Mannager
	1. from each snake on board - as a dict?
		+ color
		+ id - can be the IP address too
		+ position
	+ make food
	+ informations to canvas

#### Server side
1. Server - socket

#### Client Side
1. Client - socket
+ Canvas
	1. where to draw
	+ get information from mannager

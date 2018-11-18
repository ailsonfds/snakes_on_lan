from test import snake
from test import arena

try:
    print('Initializing Snake class test\n')
    i=0
    while i<10:
        print('Test ' + str(i+1))
        snake.main()
        i=i+1

    arena.main()
except KeyboardInterrupt:
    sys.exit()

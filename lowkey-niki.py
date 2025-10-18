import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush() 
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nUs in a king-size, keep it a secret", 0.1),
        ("Say I'm your queen, I don't wanna leave this", 0.09),
        ("Low-low-low-low, low-low-low lowkey", 0.13),
    ]
    delays = [0.3, 3.0, 6.3, 10.0, 3.0, 16.5, 19.9, 21.7, 23.3]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
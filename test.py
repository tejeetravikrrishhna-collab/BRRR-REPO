import time
import sys

def blinking_hello():
    print("Press Ctrl+C to stop...")
    
    try:
        while True:
            # Print 'Hello World.' with the dot
            # \r moves cursor to start of line, flush=True ensures it prints immediately
            print("\rHello World.", end="", flush=True)
            time.sleep(0.5)
            
            # Print 'Hello World ' (replacing dot with a space)
            print("\rHello World ", end="", flush=True)
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        # This block runs when you press Ctrl+C to exit cleanly
        print("\nGoodbye!")

if __name__ == "__main__":
    blinking_hello()
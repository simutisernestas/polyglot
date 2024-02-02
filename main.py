import subprocess
from pynput import keyboard
import os
from translate import translate_text

# Flag to indicate termination
terminate = False

# Function to be called when a key is pressed
def on_press(key):
    global terminate
    try:
        if key.char == 'q':  # Check if 'q' is pressed
            terminate = True
    except AttributeError:
        pass


# Listener that monitors keyboard
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Step 1: Command to be executed
command = ["./stream", "-m", "./models/ggml-base.en.bin", "-t",
           "16", "--step", "0", "--length", "5000", "-vth", "0.8"]
whisper_dir = os.path.expanduser("~/code/whisper.cpp")
# Step 2: Start the subprocess and open a pipe to its stdout
process = subprocess.Popen(
    command,
    cwd=whisper_dir,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True)

try:
    while not terminate:
        output = process.stdout.readline()

        # [00:00.000 --> 00:03.024]   test.
        # find this pattern and extract text after the second ]

        if output == '' and process.poll() is not None:
            break
        if output:
            # print(output.strip())  # Use the output in your main process
            if ']' in output and ']' in output:
                text = " ".join(output.split("]")[1:]).strip()
                if "BLANK_AUDIO" in text:
                    continue
                if text == "":
                    continue
                # print(text)
                translation = translate_text(text)
                print(translation)
finally:
    process.kill()  # Ensure the process is killed when done
    listener.stop()  # Stop the listener

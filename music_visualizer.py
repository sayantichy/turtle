import turtle
import numpy as np
import pyaudio

# Set up the screen
screen = turtle.Screen()
screen.title("Music Visualizer")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Number of bars in the visualizer
num_bars = 20
bars = []

# Create bars
for i in range(num_bars):
    bar = turtle.Turtle()
    bar.speed(0)
    bar.shape("square")
    bar.color("cyan")
    bar.shapesize(stretch_wid=1, stretch_len=1)
    bar.penup()
    bar.goto(-350 + i * 35, 0)
    bars.append(bar)

# Audio stream setup
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

def update_visualizer():
    try:
        screen.update()
        
        # Read audio data
        data = np.frombuffer(stream.read(1024, exception_on_overflow=False), dtype=np.int16)
        if data.size == 0:
            return  # Avoid empty buffer processing
        
        amplitude = np.abs(np.fft.rfft(data))[:num_bars]
        
        # Avoid division by zero error
        if amplitude.max() > 0:
            amplitude = np.interp(amplitude, (amplitude.min(), amplitude.max()), (1, 15))
        else:
            amplitude = np.ones(num_bars)
        
        # Update bar heights
        for i in range(num_bars):
            bars[i].shapesize(stretch_wid=amplitude[i], stretch_len=1)
        
    except Exception as e:
        print("Error in audio processing:", e)
    
    screen.ontimer(update_visualizer, 50)

update_visualizer()
screen.mainloop()

# Close stream on exit
stream.stop_stream()
stream.close()
p.terminate()

import sounddevice
from scipy.io.wavfile import write

fps = 44100
duration = 5
print ("Recording.........")
recording = sounddevice.rec(int(duration*fps), samplerate = fps, channels = 2)
sounddevice.wait()
print("Donne!")

write("Output2.wav", fps, recording)

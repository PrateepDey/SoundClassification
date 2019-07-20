import librosa
import matplotlib.pyplot as plt
import librosa.display
import csv

audio_path1 = 'sound1.wav'
x,sr = librosa.load(audio_path1, sr=44100)
librosa.display.waveplot(x,sr=sr)
n0 = 9000
n1 = 9100
zero_crossings1 = librosa.zero_crossings(x[n0:n1], pad=False)
print(sum(zero_crossings1))
plt.figure(figsize=(14, 5))
plt.plot(x[n0:n1])
plt.grid()
plt.show()
audio_path2 = 'sound2.wav'
x,sr = librosa.load(audio_path2, sr=44100)
librosa.display.waveplot(x,sr=sr)
n0 = 9000
n1 = 9100
zero_crossings2 = librosa.zero_crossings(x[n0:n1], pad=False)
print(sum(zero_crossings2))
plt.figure(figsize=(14, 5))
plt.plot(x[n0:n1])
plt.grid()
plt.show()
csvData = [['Sound','No. of Zero Crossings'],['Sound1',zero_crossings1],['Sound2',zero_crossings2]]
with open('soundData.csv','w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()

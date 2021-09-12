import wavToHz
import runTime
import exportCsv
import os

weblink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
properTitle = runTime.runTime(weblink)
prefixed = [filename for filename in os.listdir('.') if filename.startswith(properTitle)]
print("Prefixed is:")
print(prefixed[0])
pitches = wavToHz.convert(prefixed[0])
exportCsv.writeFile(pitches)
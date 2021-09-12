import wavToHz
import runTime
import os

weblink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
properTitle = runTime(weblink)
prefixed = [filename for filename in os.listdir('.') if filename.startswith(properTitle)]
wavToHz.convert(prefixed)
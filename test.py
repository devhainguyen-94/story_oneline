import gtts
from playsound import playsound
t1 = gtts.gTTS(text="t là máy đọc truyện  " , lang='vi' )
t1.save("upload/welcome.mp3")
# playsound("welcome.mp3")
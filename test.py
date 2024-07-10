import gtts
from pydub import AudioSegment
t1 = gtts.gTTS(text="t là máy đọc truyện  " , lang='vi' )
t1.save("upload/welcome.mp3")
# playsound("welcome.mp3")

# # Tải các tệp MP3
main_audio = AudioSegment.from_file("welcome2.mp3")
background_music = AudioSegment.from_file("nhacnen.mp3")

# Điều chỉnh âm lượng của nhạc nền
background_music = background_music - 5  # Giảm âm lượng nhạc nền xuống 20dB

# Lặp lại nhạc nền cho đến khi bằng độ dài của tệp chính
background_music = background_music * (len(main_audio) // len(background_music) + 1)

# Cắt nhạc nền sao cho có độ dài bằng với tệp chính
background_music = background_music[:len(main_audio)]

# Trộn nhạc nền vào tệp chính
combined = main_audio.overlay(background_music)

# Xuất tệp âm thanh kết hợp
combined.export("output_with_background.mp3", format="mp3")
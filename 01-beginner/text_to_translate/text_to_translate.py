from gtts import gTTS


text = input("Enter text: ")

voice = gTTS(text=text, lang="en")

voice.save("tts.mp3")

print("voiced saved....🥇🥇")


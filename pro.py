# from gtts import gTTS
# import os
# text_val = 'me ja raha hu ghumne'
# language = 'hi'
# obj = gTTS(text=text_val, lang=language, slow=False)

# obj.save("exam.mp3")
# os.system("start exam.mp3") 

# from gtts import gTTS
# import os


# text_val = 'Digiquest consultancy me apka svagat hai'


# language = 'hi'


# obj = gTTS(text=text_val, lang=language, slow=False)


# save_path = "C:/Users/Dell/music/exam.mp3"

# obj.save(save_path)

# print(f"Audio saved at {save_path}")

# os.system(f"start {save_path}")  


from gtts import gTTS
import os
import time


text_val = 'welcome to digiconsultancy services private limited we are provide multiple services like social media and doctor management system'


language = 'hi'


obj = gTTS(text=text_val, lang=language, slow=False)


timestamp = time.strftime("%Y%m%d-%H%M%S")
filename = f"exam_{timestamp}.mp3"
save_path = f"C:/Users/Dell/music/{filename}"


obj.save(save_path)

print(f"Audio saved at {save_path}")


os.system(f"start {save_path}")


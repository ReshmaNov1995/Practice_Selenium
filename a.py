from cryptography.fernet import Fernet
from gtts import gTTS
import os
fernet = Fernet(b'RSWEVqkKcr7nnYC8XDoC63mqg--B9ECyHtXzrzze1iI=')
decMessage = fernet.decrypt(b'gAAAAABk6CsbMElUjg-VAncxr6PW6PyhvBlJAKQnuFyf_hOn7jU_EyVEvZOtMuwiUtdHKmLgCiykudnYrBK2OOrsvDjpHb6nKg==').decode()
language = 'en'
myobj = gTTS(text=decMessage, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")

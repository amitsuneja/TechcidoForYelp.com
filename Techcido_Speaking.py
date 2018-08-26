from gtts import gTTS
import os
import speech_recognition as sr
import YelpCrowler


class MyTechcidoClass(object):
	
	def __init__(self):
		self.vlc_player = "D:\\ProgramFiles\\VideoLAN\\VLC\\vlc.exe --intf dummy --play-and-exit "
		self.techcido_welcome_message = "Hey, I am techcido, Tell me product to want to search in yelp.com"
		self.mp3_file = "D:\\YelpScrappedData\\my_file.mp3"
		self.voice_recogniser = sr.Recognizer()
		self.mic = sr.Microphone()
		self.techcido_asking_location_msg = "Tell me the location in USA for your product"

	def play_welcome_message(self):
		tts = gTTS(text=self.techcido_welcome_message, lang='en')
		MyTechcidoClass.tts_save_play_remove(self, tts)
		print("now you can speak")
		product = MyTechcidoClass.let_user_give_input(self)
		tts = gTTS(text="you said" + product, lang='en')
		MyTechcidoClass.tts_save_play_remove(self, tts)
		tts = gTTS(text=self.techcido_asking_location_msg, lang='en')
		MyTechcidoClass.tts_save_play_remove(self, tts)
		print("now you can speak")
		location = MyTechcidoClass.let_user_give_input(self)
		tts = gTTS(text="you said" + location + "now sit and relax , I am searching" + product + "in" + location,
						lang='en')
		MyTechcidoClass.tts_save_play_remove(self, tts)
		return [product, location]

	def let_user_give_input(self):
		with self.mic as source:
			self.voice_recogniser.adjust_for_ambient_noise(source, duration=0.5)
			audio = self.voice_recogniser.listen(source)
		return self.voice_recogniser.recognize_google(audio)

	def tts_save_play_remove(self, tts):
		tts.save(self.mp3_file)
		os.system(self.vlc_player + self.mp3_file)
		os.remove(self.mp3_file)


mytechcido = MyTechcidoClass()
myList = mytechcido.play_welcome_message()
K = YelpCrowler.MyWebSite(myList[0], myList[1])
K.searching_product_in_city()

# K = YelpCrowler.MyWebSite(mytechcido., "orlando, FL")
# K.searching_product_in_city()
#

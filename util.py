import os.path
import base64
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error


def create_mix(tracklist, cover):
	total = 0
	cassete = cover
	print(cassete)
	for track in tracklist:
		print(track)
		print(os.path.isfile(track))
		if os.path.isfile(track):
			print("test")
			temp = AudioSegment.from_mp3(track)
			total += len(temp)
			print(total)
			if total > 1800000:
				print("not")
				continue
			else:
			    if tracklist.index(track) == 0:
			    	print("here")
			    	output = temp
			    else:
			    	print(track)
			    	output += temp
	output.export("./My Tape.mp3", format="mp3")

	audio = MP3('My Tape.mp3', ID3=ID3)
	try:
	    audio.add_tags()
	except error:
	    pass
	
	
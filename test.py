import shutil
import os
import eyed3
import eyed3.id3
import os.path


total = 0
destination = open('My Tape.mp3', 'wb')
cassette = open('./tapes/cover.jpg', 'rb').read()

tracklist = open('tracklist.txt')
for track in tracklist:
	track = track.rstrip('\n')
	if os.path.isfile(track):
		temp = eyed3.load(track)
		total += temp.info.time_secs
		print(total)
		if total > 1800:
			continue
		else:
			shutil.copyfileobj(open(track, 'rb'), destination)
	

output = eyed3.load('everything.mp3')
if output.tag is None:
	output.tag = eyed3.id3.Tag()
	output.tag.file_info = eyed3.id3.FileInfo("foo.id3")
output.tag.images.set(3, cassette, "image/jpeg", u"cassette")
output.tag.title =u'My mix'
output.tag.artist = u'Varius Artist'
output.tag.album = u'Mixtape'
output.tag.save()

print(output.info.time_secs)
destination.close()

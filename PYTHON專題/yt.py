import pytube
from pytube.cli import on_progress
from os.path import expanduser

def download():

	url=input('Enter youtube video link: ')

	try:
		video=pytube.YouTube(url,on_progress_callback=on_progress)
		print('\nTitle: '+video.title+'\n')

		for i in video.streams:
			print(str(video.streams.index(i)+1)+'\tType: '+str(i.mime_type)+' | Res: '+str(i.resolution)+' | FPS: '+str(i.fps))


		ii=int(input('\nEnter index of needed video options: '))
		stream=video.streams.filter(mime_type=video.streams[ii-1].mime_type,resolution=video.streams[ii-1].resolution)
		stream.first().download()

	except  EOFError as err:
		print(err)

	else:
		print('Done!')



download()
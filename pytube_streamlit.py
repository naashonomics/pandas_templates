import streamlit as st
import pandas as pd
from pytube import YouTube
import base64
from io import BytesIO
def main():
	path = st.text_input('Enter URL of any youtube video')
	option = st.selectbox(
     'Select type of download',
     ('audio', 'highest_resolution', 'lowest_resolution'))
	
	matches = ['audio', 'highest_resolution', 'lowest_resolution']
	if st.button("download"): 
		video_object =  YouTube(path)
		st.write("Title of Video: " + str(video_object.title))
		st.write("Number of Views: " + str(video_object.views))
		if option=='audio':
			video_object.streams.get_audio_only().download() 		#base64.b64encode("if file is too large").decode()	
		elif option=='highest_resolution':
			video_object.streams.get_highest_resolution().download()
		elif option=='lowest_resolution':
			video_object.streams.get_lowest_resolution().download()
	if st.button("view"): 
		st.video(path) 
if __name__ == '__main__':
	main()
	

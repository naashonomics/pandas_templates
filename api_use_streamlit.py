import json,os,openai
import streamlit as st 
#pip3 install openai 
# python>=3.7.1

st.header("DALLE2 Image Generator") 
api_key=st.text_input("Enter your openai API Key")
image_description=st.text_area("Enter your images description")

button= st.button("Generate Images")



def generate_images(api_key,image_description):
	openai.api_key = api_key 

	# API Documenttaion https://beta.openai.com/docs/guides/images/introduction
	response=openai.Image.create(
	  prompt=image_description,
	  n=1,
	  size="1024x1024"
	)

	#temp2=response.json(o2) 
	image_url = response['data'][0]['url']
	if image_url:
		st.image(image_url,
            width=800, # Manually Adjust the width of the image as per requirement
        )

if api_key and image_description  and button:
	generate_images(str(api_key),str(image_description))
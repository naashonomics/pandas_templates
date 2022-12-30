import json,os,openai
#pip3 install openai 
# python>=3.7.1
openai.api_key = 'Enter Your api_key'  

# API Documenttaion https://beta.openai.com/docs/guides/images/introduction
o2=openai.Image.create(
  prompt="NASA spacecraft landing in Jupiter",
  n=2,
  size="1024x1024"
)

#temp2=response.json(o2) 
print(o2)
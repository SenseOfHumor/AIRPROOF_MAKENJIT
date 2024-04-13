import streamlit as st
import requests, json
import time
import google.generativeai as genai
from dotenv import load_dotenv
import os


def weather(city_name):
    # import required modules
    
    # Enter your API key here
    api_key = os.getenv("OWM_API_KEY")
    
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Give city name
    city_name = city_name
    
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    
    # json method of response object 
    # convert json format data into
    # python format data
    x = response.json()
    
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
    
        # store the value of "main"
        # key in variable y
        y = x["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        current_temperature = round((current_temperature - 273.15) * 1.8 + 32, 2)
    
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
    
        # store the value corresponding 
        # to the "description" key at 
        # the 0th index of z
        weather_description = z[0]["description"]
    
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature ) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))
    
    else:
        print(" City Not Found ")

    return f"TemperatureTemperature🌡️ in {city_name} is : {current_temperature}°F |\nAtmospheric Pressure: {current_pressure} |\n Humidity: {current_humidity} |\n Description: {weather_description}"
    # res = "Temperature in " + city_name + " is : " + str(current_temperature) + "°C \nAtmospheric Pressure: " + str(current_pressure) + " \n Humidity: " + str(current_humidity) + " \n Description: " + str(weather_description)
    # return res


st.sidebar.title("LOOK UP THE WEATHER ☁️")
weatherInfo = """17:49:43
Sensor 1, 1616.36. Sensor 2, 2.41
17:49:45
Sensor 1, 1593.30. Sensor 2, 2.41
17:49:47
Sensor 1, 1593.30. Sensor 2, 2.41
17:49:49
Sensor 1, 1593.30. Sensor 2, 2.41
17:49:51
Sensor 1, 1593.30. Sensor 2, 2.41"""

if 'data' not in st.session_state:
    st.sidebar.session_state.data = []

st.sidebar.markdown("Enter the city name to get the weather details")

if weather_prompt := st.sidebar.text_input("Enter the city name"):
    with st.sidebar.chat_message("user"):
        try:
            st.sidebar.markdown(weather_prompt)
            if weather_prompt:
                st.sidebar.markdown(weather(weather_prompt))

            st.sidebar.write("-------------------------------------------------")

            #weatherInfo = weather(weather_prompt)
            

        except Exception as e:
            st.sidebar.markdown("City Not Found/Please enter a valid city name")
            print(e)
            pass

## gemini initialization
#initialize the dotenv to load the environment variables
load_dotenv()

#configure the API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')


st.title("ASK ME ABOUT THE WEATHER! ☁️")

## initializing the message history
if "messages" not in st.session_state:
    st.session_state.messages = []

## initializing the chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


## display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        
## context for the model doc
context = """You are a weather expert and povide the user with useful info based on the
current air quality and data, you also need to make sure that the user is okay and ask questions to provide a 
resonable suggestion. You will consider the data from both the sensor and explain the data to the user.
history:{history} 
weather:{weatherInfo}"""


## get user input
if prompt := st.chat_input("say something nice"):
    # displaying the user message in teh caht message container
    with st.chat_message("user"):
        st.markdown(prompt)
        if prompt:
                # Append the user's message to the chat history
            st.session_state['chat_history'].append({'role': 'me ', 'content': prompt})

            # Format the history for the model
            history = '\n'.join([f"{message['role']}: {message['content']}" for message in st.session_state['chat_history']])

            # Add the history to the context
            full_context = context.format(history=history, weatherInfo=weatherInfo)

            # Generate the model's response
            response = model.generate_content(full_context)

            # Append the model's response to the chat history
            st.session_state['chat_history'].append({'role': 'assistant', 'content': response.text})

            # Append the model's response to the message history
            st.session_state.messages.append({"role": "user", "content": prompt})


    # displaying the response in the chat message container
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # add assistant response to the message history
    st.session_state.messages.append({"role": "assistant", "content": response.text})



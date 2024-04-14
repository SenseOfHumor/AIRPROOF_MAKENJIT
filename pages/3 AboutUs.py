import streamlit as st

st.header("Hey  What's up? 🌟")

st.write("---")  # Creates a horizontal separator

st.subheader("This is AIRPROOF : Prove the air you breathe in")
st.markdown("""This is a web application that helps you be aware of the air quality of your city.
                This project is made as a part of MakeNJIT 2024. The project utilizes a variety of sensors along
            with a large language model to analyze and visualize air quality data. Every record is an immutable
            record on the blockchain essentially making it public and Opensource which is crucial for
            a sustainable way of living. The project also provides a location visualizer to help you visualize the""")


st.write("---")

st.subheader("Made By 🚀")

st.write("Dave ")
st.write("Swapnil")
st.write("Steven")
st.write("Yasmeen")

st.write("_" * 50)  # Creates a horizontal line

st.subheader("Made with")

# Create columns for side-by-side image display
col1, col2, col3 = st.columns(3)

# Display images with captions in respective columns
with col1:
  st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg", width=40, caption="arduino")

with col2:
  st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", width=40, caption="python")

with col3:
  st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg", width=40, caption="cplusplus")

# Repeat for remaining images, creating new columns if needed
col1, col2 = st.columns(2)

with col1:
  st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", width=40, caption="html5")

with col2:
  st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg", width=40, caption="css3")

col1 = st.columns(1)[0]  # Access the first element of the list

with col1:
  st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/anaconda/anaconda-original.svg", width=40, caption="anaconda")

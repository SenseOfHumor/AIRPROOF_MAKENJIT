import streamlit as st

st.header("Hey  What's up?")

st.write("---")  # Creates a horizontal separator

st.subheader("This is AIRPROOF : Prove the air you breathe in")

st.write("---")

st.subheader("About Us")

st.write("✨ Creating bugs since ...")
st.write(" I'm currently learning ...")
st.write(" Goals: ...")
st.write(" Fun fact: ...")

st.write("---")

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

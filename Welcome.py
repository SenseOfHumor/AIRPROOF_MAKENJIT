import streamlit as st

def app():
    st.balloons()
    st.title('Welcome to AIRPROOF! 💨')
    st.write('Air Quality made public and open source.')
    st.write("_________________________________________________________________________________________")
    

    st.write('The use of a large langyage mdoel to help users was an added bonus!')

    st.markdown("""
    ## NavigationNavigation 🗺️
                - Home: This page.
                - Air Quality: Get the air quality of your city
                  and ask follow up questions to an AI.
                - Location Visualizer: Visualize the location on a map.
                - About Us: Learn more about the creators of this project.
                """)
    st.write("_________________________________________________________________________________________")

    st.subheader('Thanks to Makerspace for providing the resources to build this project. 🛠️')
    st.write('This project is made as a part of MakeNJIT 2024:')

app()
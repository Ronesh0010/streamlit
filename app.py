import requests 
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Ronesh here!",page_icon=":crown:", layout="centered")

def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code !=200:
                return None
        return r.json()
#--- load Animation---
lottie_coding =load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_2glqweqs.json")


selected = option_menu(
        menu_title=None,
        options=["Home","Images","Videos"],
        icons=["house-fill","file-image-fill","camera-video-fill"],
        orientation="horizontal",
)

if selected == "Home":
        st.header("You are landing on my web-app")
        st.subheader("Hello, I am Ronesh Tarenia from the department of Electronics and Telecommunication")
        st.write("I love coding")
        st_lottie(lottie_coding, height=300, key="coding")

#---Image selected---        
if selected == "Images":
        
        
        selectedimg = option_menu(
        menu_title=None,
        options = ["Select Image from file"],
        icons = ["file-image"],
        orientation="horizontal",
        )
        
        #---"Select image from file" is selected
        if selectedimg == "Select Image from file": 
             #--uploading image--
             st.title("uploading image")
             st.markdown("---")
             image=st.file_uploader("please upload an image",type=["png","jpg","jpeg","gif"])
             if image is not None:
                st.image(image)


#---Video selected---               
if selected == "Videos":
    # Option menu after selecting Video
    selectedvid = option_menu(
    menu_title=None,
    options = ["Select Video from file"],
    icons = ["file-play"],
    orientation="horizontal",
    )
    
    #--"Select video from file" is selected--
    if selectedvid == "Select Video from file":
        #--Uploading a video--
        st.title("uploading video")
        st.markdown("---")
        video = st.file_uploader("Please upload an video", type = ["mp4","mov","wmv","flv","avi","mpg"])
        if video is not None:
            st.video(video)
           
    

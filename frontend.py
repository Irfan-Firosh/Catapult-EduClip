import streamlit as st
from videoOperations import *

st.title("Try EduClip")


col1, col2 = st.columns(2, gap = "large")

if "title_disabled" not in st.session_state:
    st.session_state['title_disabled'] = False

if "form_disabled" not in st.session_state:
    st.session_state['form_disabled'] = False

def disable_title():
    st.session_state['title_disabled'] = True

def disable_form():
    st.session_state['form_disabled'] = True
    

with col1:
    st.write("What do you want to learn today?")

    title_prompt = st.text_input(
        label="Enter search query",
        placeholder="Say Something....",
        disabled=st.session_state.title_disabled,
        on_change = disable_title
    )

    selected_vid = None

    if title_prompt:
        with st.form("choose_vid"):
            # Generate your options here
            options = main(title_prompt)
            st.cache_data.clear()
            selected_vid = st.selectbox(
                "Which video would you like to convert?", options.values(),
                index = None,
                placeholder = "Choose video",
                #disabled=st.session_state.form_disabled,
                key = 'selected_vid'
            )
            submit_button = st.form_submit_button(label='Submit Video')
        st.write(st.session_state.selected_vid)
        

    if selected_vid:
        with st.spinner('Fetching Video...'):
            clear_downloads()
            downloadID(selected_vid, options)
        st.success('Done!')

        with col2:
            learn_query = st.text_area(
                label = "Type what you want to learn",
                disabled=st.session_state.form_disabled,
                placeholder="Say something...."
            )
            if learn_query:
                with st.form("view_video"):
                    vidPath = get_video_path()
                    videoFile = open(vidPath, 'rb')
                    videoBytes = videoFile.read()
                    st.video(videoBytes)
                    submitted = st.form_submit_button(label="Done")
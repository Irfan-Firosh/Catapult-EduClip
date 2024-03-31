import streamlit as st
from videoOperations import *
from GeminiPull import *
from editor import *
import time

st.title("Try EduClip")

def getVidId(options, name):
    for key in options:
        if options[key] == name:
            return key

def get_num_files():
    directory_path = "metadata/qna"
    files_list = os.listdir(directory_path)
    num_files = len(files_list)
    return num_files


video_id = None
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
                index = 1,
                placeholder = "Choose video",
                #disabled=st.session_state.form_disabled,
                key = 'selected_vid'
            )
            time.sleep(5)
            video_id = getVidId(options, selected_vid)
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
                os.remove("metadata/qna/question.txt")
                os.remove("metadata/qna/answer.txt")
                with st.spinner('Generating Exercises....'):
                    user_request(learn_query)
                    while(get_num_files() != 0):
                        time.sleep(2)
                    st.page_link("pages/questions.py", label="Exercises", icon="❓")

            if learn_query:
                with st.spinner('Clipping Video'):
                    with st.form("view_video"):
                        vidPath = get_video_path()
                        path = clipper(vidPath, video_id, learn_query)
                        videoFile = open(path, 'rb')
                        videoBytes = videoFile.read()
                        st.video(videoBytes)
                        submitted = st.form_submit_button(label="Done")
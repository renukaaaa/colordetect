import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["Home", "Live"],  # required

            styles={
                "container": {"padding": "10" ,"background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",

                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )


if selected == "Live":
    import cv2
    import streamlit as st

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 220)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        cx = int(width / 2)
        cy = int(height / 2)

        # Pick pixel value
        pixel_center = hsv_frame[cy, cx]
        hue_value = pixel_center[0]
        color = "Undefined"
        if hue_value < 3.5:
            color = "RED"
        elif hue_value < 8:
            color = "BROWN"
        elif hue_value < 15:
            color = "REDISH-PINK"
        elif hue_value < 30:
            color = "orange"
        elif hue_value < 33:
            color = "YELLOW"
        elif hue_value < 66:
            color = "YELLOW-GREEN"
        elif hue_value < 78:
            color = "GREEN"
        elif hue_value < 173:
            color = "BLUE"
        elif hue_value < 131:
            color = "BLUE"
        elif hue_value < 170:
            color = "VIOLET"
        elif hue_value < 335:
            color = "PINK"
        else:
            color = "red"

        pixel_center_bgr = frame[cy, cx]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

        cv2.putText(frame, color, (18, 70), 0, 1.5, (b, g, r), 2)
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
        print(pixel_center)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()






if selected == "Home":
    import json

    import requests  # pip install requests
    import streamlit as st  # pip install streamlit
    from streamlit_lottie import st_lottie  # pip install streamlit-lottie


    def header(url):
        st.markdown(f'<p style="background-color:none;color:green;font-size:50px;width:100%;align:centre;">{url}</p>',
                    unsafe_allow_html=True)


    header('COLOR DETECTION ')




    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_Foy93lnLYC.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        width=280,
    )

    st.write('It is an app. That will show the color of the object inside circle.You need to click on live to start and press Esc to stop')


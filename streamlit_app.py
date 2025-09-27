import streamlit as st
import random
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64("newdarkstbg.jpg")  # ganti path sesuai lokasi filenya

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image}");
        background-position: center top;
        background-attachment: fixed;
        background-size: cover;
        background-repeat: no-repeat;
    }}
    </style>
    """,unsafe_allow_html=True)


st.markdown("<h1 style= 'text-align: center;font-family: 'Cera CY', Helvetica, Arial, sans-serif;color:white'>Tempat Duduk Generator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style= 'text-align: center;font-family: cursive;color:white'>khusus kelas 10 (semua subkelas 10 bisa :D)</h4>", unsafe_allow_html=True)
def seatgen(subclass):
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,29,30,31,32]
    random.shuffle(list)
    #10.1
    if subclass == 'X-1':
        data = {1: 'L', 2: 'L', 3: 'L', 4: 'P', 5: 'P', 6: 'L', 7: 'P', 8: 'P', 9: 'L', 10: 'L', 11: 'L', 12: 'P', 13: 'L', 14: 'L', 15: 'P', 16: 'P', 17: 'P', 18: 'L', 19: 'P', 20: 'L', 21: 'L', 22: 'L', 23: 'P', 24: 'P', 25: 'L', 26: 'P', 27: 'L', 28: 'L', 29: 'P', 30: 'P', 31: 'P', 32: 'L'}
    #10.2
    if subclass == 'X-2':
        data = {1: 'L', 2: 'P', 3: 'P', 4: 'L', 5: 'L', 6: 'P', 7: 'L', 8: 'P', 9: 'P', 10: 'P', 11: 'P', 12: 'P', 13: 'P', 14: 'P', 15: 'L', 16: 'P', 17: 'L', 18: 'L', 19: 'L', 20: 'L', 21: 'L', 22: 'P', 23: 'L', 24: 'P', 25: 'L', 26: 'L', 27: 'P', 28: 'L', 29: 'P', 30: 'L', 31: 'L', 32: 'L'}
    #10.3
    if subclass == 'X-3':
        data = {1: 'L', 2: 'L', 3: 'L', 4: 'L', 5: 'L', 6: 'L', 7: 'L', 8: 'P', 9: 'P', 10: 'P', 11: 'P', 12: 'L', 13: 'L', 14: 'P', 15: 'L', 16: 'L', 17: 'P', 18: 'L', 19: 'L', 20: 'L', 21: 'P', 22: 'P', 23: 'L', 24: 'P', 25: 'P', 26: 'P', 27: 'L', 28: 'P', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
    #10.4
    if subclass == 'X-4':
        data = {1: 'L', 2: 'P', 3: 'L', 4: 'P', 5: 'P', 6: 'L', 7: 'L', 8: 'L', 9: 'P', 10: 'L', 11: 'L', 12: 'P', 13: 'P', 14: 'P', 15: 'P', 16: 'P', 17: 'L', 18: 'P', 19: 'P', 20: 'L', 21: 'L', 22: 'L', 23: 'L', 24: 'P', 25: 'L', 26: 'L', 27: 'L', 28: 'L', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
    #10.5
    if subclass == 'X-5':
        data = {1: 'P', 2: 'L', 3: 'L', 4: 'P', 5: 'P', 6: 'P', 7: 'L', 8: 'P', 9: 'L', 10: 'P', 11: 'L', 12: 'P', 13: 'L', 14: 'P', 15: 'P', 16: 'L', 17: 'L', 18: 'L', 19: 'P', 20: 'L', 21: 'L', 22: 'L', 23: 'L', 24: 'L', 25: 'P', 26: 'L', 27: 'L', 28: 'P', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
    #10.6
    if subclass == 'X-6':
        data = {1: 'P', 2: 'P', 3: 'L', 4: 'L', 5: 'L', 6: 'P', 7: 'L', 8: 'L', 9: 'L', 10: 'P', 11: 'P', 12: 'L', 13: 'L', 14: 'L', 15: 'P', 16: 'P', 17: 'L', 18: 'L', 19: 'P', 20: 'P', 21: 'P', 22: 'P', 23: 'L', 24: 'L', 25: 'L', 26: 'L', 27: 'P', 28: 'P', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}

    st.markdown("""<div style="font-size: 1.5rem;font-family: Times New Roman;text-align:center;font-weight:bold;background-color:#04a0d4;border-radius:8px;padding:0.05px">Tata Letak Tempat Duduk Baru!</div>""", unsafe_allow_html=True)
    st.markdown("""
        <style>
        hr {
            border: solid;
            height: 20px;
            background-color: white;
            margin: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<hr style= 'height:2px;background-color:white';border-radius:20px>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="
            background-color: #9a9c9a;
            color: black;
            padding: 1px;
            border-radius: 5px;
            text-align: center;
            font-weight: bold;
            width: 200px;
            margin: auto;
        ">
            PAPAN TULIS
        </div>
        """,
        unsafe_allow_html=True)
    match subclass:
        case 'X-1' | 'X-2' | 'X-3' | 'X-4':
            st.markdown(
                """
                <div style="
                    background-color: #ba6900;
                    color: black;
                    padding: 1px;
                    border-radius: 5px;
                    text-align: center;
                    font-weight: bold;
                    font-size: 0.85rem;
                    display: block;
                    width: 70px;
                    margin: 0 auto;
                    transform: translateX(70px);
                ">
                    Meja Guru
                </div>
                """,
                unsafe_allow_html=True
            )
        case 'X-5' | 'X-6':
            st.markdown(
                 """
                <div style="
                    background-color: #ba6900;
                    color: black;
                    padding: 1px;
                    border-radius: 5px;
                    text-align: center;
                    font-weight: bold;
                    font-size: 0.85rem;
                    display: block;
                    width: 70px;
                    margin: 0 auto;
                    transform: translateX(-70px);
                ">
                    MejaGuru
                </div>
                """,
                unsafe_allow_html=True
               )
    counter = 1
    for i in range(4):
        st.write()
        counter -= 1
        rcount = 0
        rows = ['', '', '', '']
        for i in range(4):
            for j in range(2):
                while True:
                    try:
                        idk = random.choice(list)
                    except IndexError:
                        rows[3] += "&nbsp;&nbsp&nbsp;[XX]"
                        break
                    if data[idk] == 'L' and (counter % 2 != 0 or counter % 2 == 0) and not 'P' in data.values():
                        output = f"[<span style = 'color : blue'>{idk:0>2}</span>]"
                        rows[rcount] += output
                        del data[idk]
                        list.remove(idk)
                        break
                    if data[idk] == 'P' and (counter % 2 != 0 or counter % 2 == 0) and not 'L' in data.values():
                        output = f"[<span style = 'color : #e91ef7'>{idk:0>2}</span>]"
                        rows[rcount] += output
                        del data[idk]
                        list.remove(idk)
                        break
                    if data[idk] == "P":
                        if counter % 2 != 0:
                            output = f"[<span style = 'color : #e91ef7'>{idk:0>2}</span>]"
                            counter += 1
                            rows[rcount] += output
                            del data[idk]
                            list.remove(idk)
                            break
                        else:
                            continue
                    if data[idk] == "L":
                        if counter % 2 == 0:
                            output = f"[<span style = 'color : blue'>{idk:0>2}</span>]"
                            counter += 1
                            rows[rcount] += output
                            del data[idk]
                            list.remove(idk)
                            break
                        else:
                            continue
            if j != 2 and i != 3:
                rows[rcount] += '&nbsp;&nbsp;&nbsp;'
            rows[rcount] = rows[rcount].strip()
        st.markdown(f"""
        <div style="text-align:center;max-width: 100%; margin: auto;font-size:0.82rem"> 
            <span style= "text-align:center !important;background-color: black;border-radius:3px;padding:3px">{rows[rcount]}</span>
        </div>""", unsafe_allow_html=True)
        rcount += 1
    st.markdown("<hr style= 'height:2px;background-color:white';border-radius:20px>", unsafe_allow_html=True)
    st.markdown("""
            <style>
            .stAlert {
                background-color: #00d907 ;
                opacity: 0.5 ;
                border-radius: 30px ;
            }
            </style>
        """, unsafe_allow_html=True)
    st.success(f'Pengacakan Berhasil!! 🥳🥳🥳 (kamu dah rolling {st.session_state.count} kali)')

st.markdown(
    """
    <style>
    div[data-baseweb="select"] > div:first-child {
        margin-top: -15px; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <span style = "color:white;margin: 0">
    Mau rolling tempat duduk di kelas berapa? 🔢
    </span>
    """,
    unsafe_allow_html=True
)
subclass = st.selectbox('', ['Kosong','X-1','X-2','X-3','X-4','X-5','X-6'])
if 'count' not in st.session_state:
    st.session_state.count = 0
if st.button("Lakuin Rolling tempat duduk! 🎲"):
    if subclass != 'Kosong':
        seatgen(subclass)
        st.session_state.count += 1
    elif subclass == 'Kosong':
        st.markdown("""<div style='background-color:rgba(255,0,0,0.8);opacity:0.9;border-radius:30px;text-align:left;padding:13px;
                    color: #000000'>Pilih kelas dulu lah kocak... 😐</div>""", unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stAlert {
            background-color: #e8c100 ;
            opacity: 0.5 ;
            border-radius: 30px ;
        }
        </style>
    """, unsafe_allow_html=True)

    st.warning("Pilih Kelasmu! 📚")

st.markdown("""
        <span style='color:white;margin:0px;text-shadow:-2px -2px 0 red;font-weight:bold'>Credits:</span>""", unsafe_allow_html=True)
st.markdown("""
        <span style='color:lime;text-shadow:-2px -2px 0 blue;font-weight:bold'>1.) Gw yang namanya cuma satu kata (Pembuat projek)</span>""", unsafe_allow_html=True)
st.markdown("""
        <span style='color:lime;text-shadow:-2px -2px 0 blue;font-weight:bold'>2.) Si tukang elektronik/komputer itu (Bugfixer)</span>""", unsafe_allow_html=True)

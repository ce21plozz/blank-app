import streamlit as st
import random
import base64

st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1">
""", unsafe_allow_html=True)

st.set_page_config(page_title="Tempat Duduk Generator", page_icon="icon.jpg")

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Amaranth:ital,wght@0,400;0,700;1,400;1,700&family=Anta&family=Convergence&family=Fredoka:wght@550&family=Patrick+Hand&display=swap');
</style>""", unsafe_allow_html=True)
st.markdown("""
<style>
.fredoka-e {
  font-family: "Fredoka", sans-serif;
  font-optical-sizing: auto;
  font-weight: 550;
  font-style: normal;
  font-size: 3rem;
  font-variation-settings:
    "wdth" 100;
}
.patrick-hand-regular {
  font-family: "Patrick Hand", cursive;
  font-weight: 400;
  font-style: normal;
}
.anta-regular {
  font-family: "Anta", sans-serif;
  font-weight: 400;
  font-style: normal;
}
.amaranth-regular {
  font-family: "Amaranth", sans-serif;
  font-weight: 400;
  font-style: normal;
}
.convergence-regular {
  font-family: "Convergence", sans-serif;
  font-weight: 400;
  font-style: normal;
}

</style>""", unsafe_allow_html=True)

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64("newdarkstbg.jpg")
link_image = get_base64("placeholder_kasual.jpg")

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


st.markdown("""
            <div style="background-color:#4377ab;border-radius:8px;padding:10px;line-height:0.95;">
                <div class="fredoka-e" style= 'text-align: center;color:white;font-size:2.5rem;'>Tempat Duduk Generator</div>
                <br style="margin-top:0px;line-height:0.625;">
                <div class="anta-regular" style= 'text-align: center;color:white;font-size:1.525rem;'>khusus untuk semua kelas 10</div>
            </div>""", unsafe_allow_html=True)
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
    def luminance(r, g, b):
        return 0.2126*r + 0.7152*g + 0.0722*b
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = luminance(r, g, b)
    if color > 128:
        result_color = 'black'
    else:
        result_color = 'white'
    st.markdown(f"""<div style="font-size: 1.1rem;font-family: Times New Roman;text-align:center;font-weight:bold;background-color: rgb({r},{g},{b});border-radius:8px;padding:0.05px;color:{result_color}">Tata Letak Tempat Duduk Baru!</div>""", unsafe_allow_html=True)
    st.markdown("<hr style= 'height:2px;background-color:white';border-radius:20px;margin:0px>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="
            background-color: #9a9c9a;
            color: black;
            padding: 0px;
            border-radius: 5px;
            text-align: center;
            font-weight: bold;
            width: 240px;
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
                    font-size: 0.75rem;
                    display: block;
                    width: 55px;
                    margin: 0 auto;
                    transform: translateX(92px);
                ">
                    MejaGuru
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
                    font-size: 0.75rem;
                    display: block;
                    width: 55px;
                    margin: 0 auto;
                    transform: translateX(-92px);
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
        <div style="text-align:center;max-width: 100%; margin: auto;"> 
            <span style= "text-align:center !important;background-color: #c7b29b;border-radius:3px;padding:3px;font-size:1rem">{rows[rcount]}</span>
        </div>""", unsafe_allow_html=True)
        rcount += 1
    if subclass == "X-6":
        st.markdown("""  
<br>
<div style="text-align:center;max-width: 100%; margin: auto;">
    <span style="text-align: center; background-color: black;border-radius:5px">  
      <span style="  
        background: linear-gradient(90deg, red, orange, yellow, lime,blue, cyan,violet, pink);  
        -webkit-background-clip: text;  
        -webkit-text-fill-color: transparent;  
        font-size: 0.95rem;  
      ">  
        ☝️Senin-Kamis sesuai ini☝️ Jumat bebas!! ✨  
      </span>  
    </span>
</div> 
""", unsafe_allow_html=True)
    st.markdown("<hr style= 'height:2px;background-color:white';border-radius:20px;margin: 0px>", unsafe_allow_html=True)
    st.markdown("""
            <style>
            .stAlert {
                background-color: #00d907 ;
                opacity: 0.5 ;
                border-radius: 30px ;
            }
            </style>
        """, unsafe_allow_html=True)
    st.markdown(f"""<div class="amaranth-regular" style='background-color:rgba(0,175,0,0.8);opacity:0.9;border-radius:20px;text-align:left;padding:13px;
                    color: #000000; max-width:85%;'><i>Pengacakan Berhasil!! 🥳🥳🥳<br>(kamu dah rolling {st.session_state.count} kali)</i></div>""", unsafe_allow_html=True)

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
    <span class="patrick-hand-regular" style = "color:white;margin: 0;font-size:1.1rem">
    Rolling tempat duduk kelas berapa? 🔢
    </span>
    """,
    unsafe_allow_html=True
)
subclass = st.selectbox('', ['Kosong','X-1','X-2','X-3','X-4','X-5','X-6'])
if 'count' not in st.session_state:
    st.session_state.count = 1
if st.button("Lakuin Rolling tempat duduk! 🎲"):
    if subclass != 'Kosong':
        seatgen(subclass)
        st.session_state.count += 1
    elif subclass == 'Kosong':
        st.markdown("""<div class="amaranth-regular" style='background-color:rgba(255,0,0,0.8);opacity:0.9;border-radius:30px;text-align:left;padding:13px;
                    color: #000000;max-width:78%'><i>Pilih kelas dulu lah kocak... 😐</i></div>""", unsafe_allow_html=True)
else:
    st.markdown("""<div class="amaranth-regular" style='background-color:rgba(242,210,0,0.8);opacity:0.9;border-radius:30px;text-align:left;padding:13px;
                    color: #000000;max-width:55%;'><i>Pilih Kelasmu! 📚</i></div>""", unsafe_allow_html=True)

st.markdown("""
        <br>
        <span style='color:white;margin:0px;text-shadow:-2px -2px 0 red;font-weight:bold'>App diprogram oleh:</span>
        <br>
        <span style='color:lime;text-shadow:-2px -2px 0 blue;font-weight:bold;font-size:0.85rem'>1.) Gw yg namanya cuma sekata</span> <span style='color:orange;text-shadow:-2px -2px 0 #994708;font-weight:bold;font-size:0.85rem'>(Pembuat Projek)</span>
        <br>
        <span style='color:lime;text-shadow:-2px -2px 0 blue; font-weight:bold;font-size:0.85rem'>2.) Si tukang elektronik/komputer itu</span> <span style='color:orange;font-weight:bold;text-shadow:-2px -2px 0 #994708;font-size:0.85rem'>(Bugfixer)</span>
        <br>
        <span style='color:white;margin:0px;text-shadow:-2px -2px 0 red;font-weight:bold'>Kredit tambahan:</span>
        <br>
        <span style='color:lime;text-shadow:-2px -2px 0 blue;font-weight:bold;font-size:0.85rem'>1.) Jeconia Kellysta Hokky (aku dah dapet izin dari dia untuk make nama aslinya)</span> <span style='color:orange;text-shadow:-2px -2px 0 #994708;font-weight:bold;font-size:0.85rem'>(Promosi)</span>
        
        """, unsafe_allow_html=True)
st.markdown(f"""
            <br>
            <div style="text-align:center;font-size:1.6rem;background-color:#4377ab;border-radius:8px;padding:10px;">
                <span style='color:white;margin:0px;text-shadow:-2px -2px 0 red;font-weight:bold'> 🛠️🎨 EXTRA 🎨🛠️ </span>
            </div>
            <br>
            <div class="convergence-regular" style='color:yellow;text-shadow:-3px -3px 0 #7b00ff;font-weight:bold;font-size:1.2rem;text-align:center'>Kelompok Generator</div> 
            <div style="text-align:center">
                <span class="convergence-regular" style='color:#02eba9;font-weight:bold;text-shadow:-3px -3px 0 #254e94;font-size:0.9rem'>(Jumlah cowo & cewe tiap kelompok yang dibuat langsung adil, pencet gambar di bawah untuk nyoba)</span>
            </div>
            
            <br>
            <div style="text-align:center">
                <a href="https://kelompok.streamlit.app/">
                    <img src="data:image/jpg;base64,{link_image}"
                    alt = "placeholder"
                    target = "_blank"
                    style="border-radius:20px;
                    cursor:pointer;
                    width:250px;
                    border: 5px solid black;
                    ">               
                </a>
            </div>""", unsafe_allow_html=True)
#wow baris pi(π) nih, tapi dikali 100...

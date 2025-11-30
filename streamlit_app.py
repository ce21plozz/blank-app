import streamlit as st
import random
import base64
from ekstra import ekstra
from rating import rating
from streamlit_extras.stylable_container import stylable_container

st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1">
""", unsafe_allow_html=True)

st.set_page_config(page_title="Tempat Duduk Generator", page_icon="icon.jpg")

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Amaranth:ital,wght@0,400;0,700;1,400;1,700&family=Anta&family=Convergence&family=Fredoka:wght@550&family=Patrick+Hand&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Galdeano&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Arima:wght@100..700&family=BBH+Sans+Bogle&family=Momo+Trust+Display&family=Rowdies:wght@300;400;700&display=swap');            
.momo-trust-display-regular {
font-family: "Momo Trust Display", sans-serif;
font-weight: 400;
font-style: normal;
}
.bbh-sans-bogle-regular {
font-family: "BBH Sans Bogle", sans-serif;
font-weight: 400;
font-style: normal;
}
</style>""", unsafe_allow_html=True)
st.markdown("""
<style>
.galdeano-regular {
  font-family: "Galdeano", sans-serif;
  font-weight: 400;
  font-style: normal;
}
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

params = st.query_params

btn_css_property = """
                    button {
                    background-color: lightgray;
                    margin: .35em;
                    border: 2px solid #003bba;
                    transition: all .25s ease;
                    color: black;
                    box-shadow : 0 0 10px #007ab8;
                    }
                    button:hover {
                    opacity: .75;
                    transition: all .25s ease;
                    }
                    """
with st.sidebar:
    with stylable_container(key="utama", css_styles=btn_css_property):
        if st.button("Utama", key="btn_utama"):
            st.query_params.clear()
            st.query_params['select'] = 'utama'
    with stylable_container(key="ekstra", css_styles=btn_css_property):
        if st.button("Extra", key="btn_ekstra"):
            st.query_params.clear()
            st.query_params['select'] = 'ekstra'
    with stylable_container(key="rating", css_styles=btn_css_property):
        if st.button("Rating", key="btn_rating"):
            st.query_params.clear()
            st.query_params['select'] = 'rating'

select = st.query_params.get('select', 'utama')

st.markdown(
    f"""
    <style>
    .stApp {{
    background: transparent;
    }}
    .stApp::before {{
        --c1 : #19202e;
        --c2 : #101727;
        content: "";
        z-index: -1;
        inset: 0;
        width: 200%;
        height: 200%;
        position: fixed;
        background: linear-gradient(135deg, var(--c1) 25%, var(--c2)25%, var(--c2) 50%,var(--c1) 50%, var(--c1) 75%, var(--c2) 75%);
        background-size: 100px 100px;
        animation: BGmove 4500ms linear infinite;    
    }}
    
    @keyframes BGmove {{
        to {{transform: translate(-100px, -100px);}}
    }}
    </style>
    """, unsafe_allow_html=True)

if  select == 'utama':
    st.markdown("""
                <div style="background-color:#4377ab;border-radius:20px;padding:20px;line-height:0.85;border: .35rem solid cornflowerblue;box-shadow: 0 0 10px 0 black inset;">
                    <div class="bbh-sans-bogle-regular" style= 'text-align: center;color:white;font-size:2.5rem;letter-spacing:.2rem;'>Tempat Duduk Generator</div>
                    <br style="margin-top:0px;line-height:0.625;">
                    <div class="fredoka-e" style= 'text-align: center;color:#d1d1d1;font-size:1rem;letter-spacing:.025rem'>Untuk kelas 10 (TA 2025-2026)</div>
                </div>""", unsafe_allow_html=True)

    def seatgen(subclass):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                30, 31, 32]
        # 10.1
        if subclass == 'X-1':
            data = {1: 'L', 2: 'L', 3: 'L', 4: 'P', 5: 'P', 6: 'L', 7: 'P', 8: 'P', 9: 'L', 10: 'L', 11: 'L', 12: 'P',
                    13: 'L', 14: 'L', 15: 'P', 16: 'P', 17: 'P', 18: 'L', 19: 'P', 20: 'L', 21: 'L', 22: 'L', 23: 'P',
                    24: 'P', 25: 'L', 26: 'P', 27: 'L', 28: 'L', 29: 'P', 30: 'P', 31: 'P', 32: 'L'}
        # 10.2
        if subclass == 'X-2':
            data = {1: 'L', 2: 'P', 3: 'P', 4: 'L', 5: 'L', 6: 'P', 7: 'L', 8: 'P', 9: 'P', 10: 'P', 11: 'P', 12: 'P',
                    13: 'P', 14: 'P', 15: 'L', 16: 'P', 17: 'L', 18: 'L', 19: 'L', 20: 'L', 21: 'L', 22: 'P', 23: 'L',
                    24: 'P', 25: 'L', 26: 'L', 27: 'P', 28: 'L', 29: 'P', 30: 'L', 31: 'L', 32: 'L'}
        # 10.3
        if subclass == 'X-3':
            data = {1: 'L', 2: 'L', 3: 'L', 4: 'L', 5: 'L', 6: 'L', 7: 'L', 8: 'P', 9: 'P', 10: 'P', 11: 'P', 12: 'L',
                    13: 'L', 14: 'P', 15: 'L', 16: 'L', 17: 'P', 18: 'L', 19: 'L', 20: 'L', 21: 'P', 22: 'P', 23: 'L',
                    24: 'P', 25: 'P', 26: 'P', 27: 'L', 28: 'P', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
        # 10.4
        if subclass == 'X-4':
            data = {1: 'L', 2: 'P', 3: 'L', 4: 'P', 5: 'P', 6: 'L', 7: 'L', 8: 'L', 9: 'P', 10: 'L', 11: 'L', 12: 'P',
                    13: 'P', 14: 'P', 15: 'P', 16: 'P', 17: 'L', 18: 'P', 19: 'P', 20: 'L', 21: 'L', 22: 'L', 23: 'L',
                    24: 'P', 25: 'L', 26: 'L', 27: 'L', 28: 'L', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
        # 10.5
        if subclass == 'X-5':
            data = {1: 'P', 2: 'L', 3: 'L', 4: 'P', 5: 'P', 6: 'P', 7: 'L', 8: 'P', 9: 'L', 10: 'P', 11: 'L', 12: 'P',
                    13: 'L', 14: 'P', 15: 'P', 16: 'L', 17: 'L', 18: 'L', 19: 'P', 20: 'L', 21: 'L', 22: 'L', 23: 'L',
                    24: 'L', 25: 'P', 26: 'L', 27: 'L', 28: 'P', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
            names = ["Agnes", "Alfon", "Ricad", "Ara", "Quincy", "Cayla", "Tian", "Aurel", "Dion", "Eva", "Gebung", "Gratia", "Hiero", "Janice", "Kelly", "Joshua", "Marvin", "Mirace", "Naneo", "Honey", "Nelson", "Nicho", "Owen", "Aan", "rosa", "Abner", "Sean", "Sera", "Tascha", "Liona", "Will", "Fanya"]
            nama = [name.center(6, '-').title() for name in names]
        # 10.6
        if subclass == 'X-6':
            data = {1: 'P', 2: 'P', 3: 'L', 4: 'L', 5: 'L', 6: 'P', 7: 'L', 8: 'L', 9: 'L', 10: 'P', 11: 'P', 12: 'L',
                    13: 'L', 14: 'L', 15: 'P', 16: 'P', 17: 'L', 18: 'L', 19: 'P', 20: 'P', 21: 'P', 22: 'P', 23: 'L',
                    24: 'L', 25: 'L', 26: 'L', 27: 'P', 28: 'P', 29: 'P', 30: 'P', 31: 'L', 32: 'P'}
            names = ['abi','agnes','alden','andre','andrew','aurel','yefta','caleb','candra','dinda','chatln','anton','daniel','andra','gaby','sharon','faith','jojo','joyce','kiseki','maria','michel','nathan','otniel','owen','pedro','queen','rachel','kai','talita','destra','yohana',]
            nama = [name.center(6,'-').title() for name in names]
        def luminance(r, g, b):
            return 0.2126 * r + 0.7152 * g + 0.0722 * b

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = luminance(r, g, b)
        if color > 128:
            result_color = 'black'
        else:
            result_color = 'white'
        st.markdown(
            f"""<div style="font-size: 1.1rem;font-family: Times New Roman;text-align:center;font-weight:bold;background-color: rgb({r},{g},{b});border-radius:8px;padding:0.05px;color:{result_color}">Tata Letak Tempat Duduk Baru!</div>""",
            unsafe_allow_html=True)
        st.markdown("<hr style= 'height:2px;background-color:white;border-radius:20px;margin:25px 20px'>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div id="whiteboard">
                PAPAN TULIS
            </div>
            <style>
            #whiteboard {{
                background-color: #9a9c9a;
                color: black;
                padding: 0px;
                border-radius: 5px;
                text-align: center;
                font-weight: bold;
                width: {475 if subclass == "X-5" or subclass == "X-6" else 240}px;
                margin: auto;
            }}
            
            @media (max-width: 600px) and (min-width: 471px) {{
                #whiteboard {{
                    width: {420 if subclass == "X-5" or subclass == "X-6" else 240}px;
                }}
            }}
            @media (max-width: 470px) {{
                #whiteboard {{
                    width: {320 if subclass == "X-5" or subclass == "X-6" else 240}px;
                }}
            }}
            </style>
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
                   <div id="mejaguru">
                       Meja Guru
                   </div>
                   <style>
                   #mejaguru {
                       background-color: #ba6900;
                       color: black;
                       padding: 1px;
                       border-radius: 5px;
                       text-align: center;
                       font-weight: bold;
                       font-size: 0.75rem;
                       display: block;
                       width: 100px;
                       margin: 0 auto;
                       transform: translateX(-187px);
                   }
                   
                   @media (max-width: 600px) and (min-width: 471px) {
                    #mejaguru {
                        transform: translateX(-161px);
                    }
                   }
                   @media (max-width: 470px) {
                    #mejaguru {
                        transform: translateX(-125px);
                        width: 70px;
                    }
                   }
                   </style>
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
                            output = f"[<span style = 'color : blue'>{nama[idk-1] if subclass == "X-6" or subclass == "X-5" else str(idk).rjust(2, "0") }</span>]"
                            rows[rcount] += output
                            del data[idk]
                            list.remove(idk)
                            break
                        if data[idk] == 'P' and (counter % 2 != 0 or counter % 2 == 0) and not 'L' in data.values():
                            output = f"[<span style = 'color : #e91ef7'>{nama[idk-1] if subclass == "X-6" or subclass == "X-5" else str(idk).rjust(2, "0") }</span>]"
                            rows[rcount] += output
                            del data[idk]
                            list.remove(idk)
                            break
                        if data[idk] == "P":
                            if counter % 2 != 0:
                                output = f"[<span style = 'color : #e91ef7'>{nama[idk-1] if subclass == "X-6" or subclass == "X-5" else str(idk).rjust(2, "0") }</span>]"
                                counter += 1
                                rows[rcount] += output
                                del data[idk]
                                list.remove(idk)
                                break
                            else:
                                continue
                        if data[idk] == "L":
                            if counter % 2 == 0:
                                output = f"[<span style = 'color : blue'>{nama[idk-1] if subclass == "X-6" or subclass == "X-5" else str(idk).rjust(2, "0") }</span>]"
                                counter += 1
                                rows[rcount] += output
                                del data[idk]
                                list.remove(idk)
                                break
                            else:
                                continue
                if j != 2 and i != 3:
                    rows[rcount] += '&nbsp;&nbsp;'
                rows[rcount] = rows[rcount].strip()
            st.markdown(f"""
            <div class="res-container" style="text-align:center;max-width: 100%; margin: 0;"> 
                <span class="result" style= "">{rows[rcount]}</span>
            </div>
            
            <style>
            .res-container{{
            margin: 0 auto;
            display: flex;
            justify-content: center;
            }}
            
            .result {{
                font-family: monospace;
                letter-spacing:-0.025em;
                background-color: #c7b29b;
                border-radius:3px;
                padding:1.5px;
                line-height: auto;
                font-size: {0.8 if subclass == "X-5" or subclass == "X-6" else 0.75}rem;
                }}
            
            @media (max-width: 600px) and (min-width: 471px){{
                .result {{
                letter-spacing:-0.05em;
                padding:1px;
                font-size: .75rem;
                }}
            }}
            @media (max-width: 470px){{
                .result {{
                letter-spacing:-0.07rem;
                padding:1px .1px;
                font-size: {0.65 if subclass == "X-5" or subclass == "X-6" else 0.85}rem;
                line-height: -1.9rem;
                display: flex;
                justify-content: center;
                margin: 0 auto;
                }}
            }}
            </style>
            
            """, unsafe_allow_html=True)
            rcount += 1
        st.markdown("""
                    <style>
                    .rainbow {
                    background: linear-gradient(90deg, red, orange, yellow, lime, cyan,violet, pink);  
            -webkit-background-clip: text;  
            -webkit-text-fill-color: transparent;
                    }
                    </style>
                    """,unsafe_allow_html=True)
        if subclass == "X-6":
            st.markdown("""  
    <br>
    <div style="text-align:center;max-width: 100%; margin: auto;line-height: 0.25;">
        <span style="text-align: center; background-color: black;border-radius:5px">
            <span>☝️</span>         
            <span class='rainbow' style="font-size: 0.95rem;">  
                Senin-Kamis sesuai ini </span>
            <span>☝️</span> 
            <span class='rainbow'>Jumat bebas!!</span>
            <span>✨</span> 
            </span>  
        </span>
    </div> 
    """, unsafe_allow_html=True)
        st.markdown("<hr style= 'height:2px;background-color:white;border-radius:20px;margin:25px 20px;'>",
                    unsafe_allow_html=True)
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
                        color: #000000; max-width:85%;'><i>Pengacakan Berhasil!! 🥳🥳🥳<br>(kamu dah rolling {st.session_state.count} kali)</i></div>""",unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        div[data-baseweb="select"] > div:first-child {
            margin-top: -15px; 
        }
        </style>
        """,unsafe_allow_html=True)

    st.markdown(
        """
        <span class="patrick-hand-regular" style = "color:white;margin: 0;font-size:1.1rem">
        Rolling tempat duduk kelas berapa? 🔢
        </span>
        """,
        unsafe_allow_html=True
    )
    subclass = st.selectbox('', ['Kosong', 'X-1', 'X-2', 'X-3', 'X-4', 'X-5', 'X-6'])
    if 'count' not in st.session_state:
        st.session_state.count = 1
    if st.button("Lakuin Rolling tempat duduk! 🎲"):
        if subclass != 'Kosong':
            seatgen(subclass)
            st.session_state.count += 1
        elif subclass == 'Kosong':
            st.markdown("""<div class="amaranth-regular" style='background-color:rgba(255,0,0,0.8);opacity:0.9;border-radius:30px;text-align:left;padding:13px;
                        color: #000000;max-width:78%'><i>Pilih kelas dulu lah kocak... 😐</i></div>""",
                        unsafe_allow_html=True)
    else:
        st.markdown("""<div class="amaranth-regular" style='background-color:rgba(242,210,0,0.8);opacity:0.9;border-radius:30px;text-align:left;padding:13px;
                        color: #000000;max-width:55%;'><i>Pilih Kelasmu! 📚</i></div>""", unsafe_allow_html=True)

    st.html("""
            <div class="credits">
                <span style='color:white;margin:0px;text-shadow:-2px -2px 0 red;font-weight:bold'>App diprogram oleh:</span>
                <br>
                <span style='color:lime;text-shadow:-2px -2px 0 blue;font-weight:bold;font-size:0.85rem'>1.) Gw yg namanya cuma sekata</span> <span style='color:orange;text-shadow:-2px -2px 0 #994708;font-weight:bold;font-size:0.85rem'>(Developer utama dalam projek)</span>
                <br>
                <span style='color:lime;text-shadow:-2px -2px 0 blue; font-weight:bold;font-size:0.85rem'>2.) Si tukang elektronik/komputer itu</span> <span style='color:orange;font-weight:bold;text-shadow:-2px -2px 0 #994708;font-size:0.85rem'>(Helper & Tester)</span>
                <br>
                <span style='color:white;margin:0px;text-shadow:-2px -2px 0 red;font-weight:bold'>Kredit tambahan:</span>
                <br>
                <span style='color:lime;text-shadow:-2px -2px 0 blue;font-weight:bold;font-size:0.85rem'>1.) Jeconia Kellysta Hokky</span> <span style='color:orange;text-shadow:-2px -2px 0 #994708;font-weight:bold;font-size:0.85rem'>(Promosi website & pembuat database X-5)</span>
            </div>
            
            <style>
            .credits {
                display: flex;
                justify-content: center;
                align-items: center;
                border: 3px solid black;
                flex-direction: column;
                margin: 2rem 0;
                background-image: linear-gradient(20deg, transparent 35%, #0a112b 55%, #0e1d52), repeating-linear-gradient(-10deg,transparent 45px, #1f1f1f 45px, #1f1f1f 48px,transparent 48px, transparent 80px), repeating-linear-gradient(80deg,black 45px, #1f1f1f 45px, #1f1f1f 48px,black 48px, black 80px);
                border-radius: 50px 0 ;
                box-shadow: 0 0 5px 0 #858585, 0 0 15px 0 #2e3d73 inset;
                padding: 8px;
            }
            </style>
            """)
elif select == "ekstra":
    ekstra()
elif select == 'rating':
    rating()

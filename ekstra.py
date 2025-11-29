import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
def ekstra():
    st.markdown(f"""
                <br>
                <div style="text-align:center;font-size:1.6rem;background-color:#4377ab;border-radius:15px;padding:10px;border:.35rem solid cornflowerblue;box-shadow: 0 0 10px 0 black inset;">
                    <span style='color:white;margin:0px;text-shadow: 0 0 15px cyan;font-weight:bold'> 🛠️🎨 EXTRA 🎨🛠️ </span>
                </div>
                <br>
                <div class=" judultop convergence-regular" style='color:yellow;text-shadow:-3px -3px 0 #7b00ff;font-weight:bold;font-size:1.2rem;text-align:center'>Kelompok Generator</div> 
                <div style="text-align:center">
                    <span class="isi convergence-regular" style='color:#02eba9;font-weight:bold;text-shadow:-3px -3px 0 #254e94;font-size:0.9rem'>Jumlah cowo & cewe tiap kelompok yang dibuat langsung adil, pencet gambar di bawah untuk nyoba</span>
                </div>
                """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="ultimate-img-wrapper">
        <div class="img-wrapper" style="text-align:center;margin:25px 0;">
          <a draggable="false" href="https://kelompok.streamlit.app" target="_blank">
            <img  src="data:image/jpg;base64,{get_base64("images/extra_img2.jpg")}"
                 alt="placeholder"
                 class="kelompok">
          </a>
          <div class="arrow" id="panah1"></div>
          <div class="arrow" id="panah2"></div> 
        </div>
    </div>
    <div class="judul convergence-regular" style='color:yellow;text-shadow:-3px -3px 0 #7b00ff;font-weight:bold;font-size:1.2rem;text-align:center'>Spelling Bee</div> 
                <div style="text-align:center">
                    <span class="isi convergence-regular" style='color:#02eba9;font-weight:bold;text-shadow:-3px -3px 0 #254e94;font-size:0.9rem'>Nih website tu tujuan sebenernya cuma untuk STS TIK/Informatika doang, pencet gambar di bawah untuk nyoba</span>
                </div>
    <div class="ultimate-img-wrapper">    
        <div class="img-wrapper" style="text-align:center;margin:25px 0;">
          <a draggable="false" href="https://kelompok.streamlit.app" target="_blank">
            <img src="data:image/jpg;base64,{get_base64("images/spelling bee img.jpg")}"
                 alt="placeholder"
                 class="kelompok">
          </a>
          <div class="arrow" id="panah1"></div>
          <div class="arrow" id="panah2"></div>     
        </div>
    </div>
    
    <style>
    .judul {{
    margin-top: 40px;
    }}
    
    .kelompok {{
      border-radius: 20px;
      cursor: pointer;
      width: 215px;
      border: 5px solid #d1d07d;
      transition: all 0.35s ease;
      margin: 0;
      position: relative;
      box-shadow: 0 0 15px 0 black; 
    }}

    .kelompok:hover {{
      border: 5px solid #e09151;
      transition: all 0.35s ease;
    }}

    .kelompok:active {{
        width: 220px;
        border: 5px solid #85ff8b;
        transition: all 0.2s ease;
    }}    
    
    a {{
        z-index: 1;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    
    .arrow {{
        height: 25%;
        width: 25%;
        position: absolute;
        transform: translate(0,0);
        background-color: #e3cc49;
        box-shadow: 0 0 15px 0 black inset;
    }}
    
    #panah1 {{
        pointer-events: none;
        clip-path: polygon(75% 0%, 100% 50%, 75% 100%, 40% 100%, 65% 50%, 40% 0);
        transition: all 0.2s ease;
        z-index: 0;    
    }}
    a:hover ~ #panah1 {{
        transform: translateX(-125%);
        transition: all 0.2s ease;
    }}
    
    #panah2 {{
        pointer-events: none;
        clip-path: polygon(25% 0, 0 50%, 25% 100%, 60% 100%, 35% 50%, 60% 0);
        transition: all 0.2s ease; 
    }}
    a:hover ~ #panah2 {{
        transform: translateX(125%);
        transition: all 0.2s ease;
    }}
    
    .img-wrapper {{
    display: flex;
    justify-content: center;
    align-items: center;
    }}
    
    .ultimate-img-wrapper {{
    box-sizing: content-box;
    }}
    
    @media (max-width: 700px) {{
        .kelompok {{
        width: 175px;
        }}
        
        .arrow {{ 
        height: 15%;
        width: 18%;
        }}
        
        a:hover ~ #panah1 {{
        transform: translateX(-220%);
        }}
        a:hover ~ #panah2 {{
        transform: translateX(220%);
        }}
    }}
    </style>
    """, unsafe_allow_html=True)
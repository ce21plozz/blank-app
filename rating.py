import streamlit as st
def rating():
    st.markdown(f"""<div style="text-align:center;font-size:1.6rem;background-color:#4377ab;border-radius:15px;padding:10px;border:.35rem solid cornflowerblue;box-shadow: 0 0 10px 0 black inset;">
                    <span style='color:white;margin:5px;text-shadow: 0 0 15px cyan;font-weight:bold'>⭐RATING⭐</span>
                </div><br>""", unsafe_allow_html=True)
    st.markdown(f"""
                <form class="fblayout"
                  action="https://formspree.io/f/mwprrgkn"
                  method="POST"
                >
                  <label for="rating" class="label galdeano-regular">Kasih rating dalam bintang</label>
                  <br>
                  <div class="rating">
                    <label class="labelradio galdeano-regular" for="1">1⭐</label>
                    <input class="widgetstar" type="radio" name="rating" value='1' id="1" required>
                    <label class="labelradio galdeano-regular" for="2">2⭐</label>
                    <input class="widgetstar" type="radio" name="rating" value='2' id="2">
                    <label class="labelradio galdeano-regular" for="3">3⭐</label>
                    <input class="widgetstar" type="radio" name="rating" value='3' id="3">
                    <label class="labelradio galdeano-regular" for="4">4⭐</label>
                    <input class="widgetstar" type="radio" name="rating" value='4' id="4">
                    <label class="labelradio galdeano-regular" for="5">5⭐</label>
                    <input class="widgetstar" type="radio" name="rating" value='5' id="5">
                  </div>
                  <br>  
                  <label class="label galdeano-regular">
                    Kasih Feedback (saran atau kritik)
                    <br>
                    <textarea class='widget' name="feedback" rows="3" cols="32" placeholder="Tulis Feedback (maks 250 karakter)" maxlength="250" required></textarea>
                  </label>
                  <br>
                  <button class="widget" type="submit">Kirim Feedback</button>
                </form>
                """, unsafe_allow_html=True)
    # form's css stuff
    st.markdown("""
                <style>
                .rating {
                display: flex;
                justify-content: left;
                }
                .labelradio:first-child {
                margin-left: 0;
                }
                
                .fblayout {
                flex-direction: rows;
                }

                .label {
                color:white;
                font-size:1.1rem;
                text-align:center;
                }
                .labelradio {
                color:yellow;
                font-size:.8rem;
                margin-left: 20px;
                }

                .widget, .widgetstar {
                border-radius: 10px;
                border: 3px solid #5495a1;
                transition: all 0.2s ease;
                width: auto;
                line-height: 1em;
                padding: .4em;
                }
                .widgetstar {
                transform: scale(1.2)
                }
                .widgetstar:checked {
                background-color: yellow;
                }
                .widget:hover {
                border-radius: 10px;
                border: 3px solid #29ba44;
                transition: all 0.2s ease;
                background-color: #333;
                }
                </style>
                """, unsafe_allow_html=True)

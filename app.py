import streamlit as st

# Настройки вкладки браузера
st.set_page_config(page_title="С Днем Рождения, Надюша! ✨", page_icon="🌸", layout="centered")

# ЖЕСТКАЯ ЗАЩИТА ОТ ПЕРЕВОДА НА УРОВНЕ КОДА ХТМЛ
st.markdown("""
    <html lang="ru" class="notranslate" translate="no">
    <head>
        <meta name="google" content="notranslate" />
    </head>
    </html>
""", unsafe_allow_html=True)

# Дизайн (сиреневый, белый, голубой)
st.markdown("""
    <style>
    /* Мягкий пастельный font: сиренево-голубой перелив */
    .stApp {
        background: linear-gradient(135deg, #E6E6FA 0%, #D8BFD8 50%, #B0E0E6 100%) !important;
    }
    
    /* Огромный белый заголовок с голубой тенью */
    .main-title {
        font-family: 'Arial Black', 'Arial', sans-serif !important;
        color: #FFFFFF !important; 
        text-align: center !important;
        font-size: 65px !important;
        font-weight: 900 !important;
        padding-top: 40px !important;
        padding-bottom: 10px !important;
        letter-spacing: 2px !important;
        line-height: 1.2 !important;
        text-shadow: 3px 3px 15px rgba(70, 130, 180, 0.8), -2px -2px 10px rgba(70, 130, 180, 0.5) !important;
    }
    
    /* Красивое белое облако для текста */
    .wish-text {
        font-family: 'Arial', sans-serif !important;
        font-size: 24px !important;
        color: #2C3E50 !important;
        line-height: 1.8 !important;
        text-align: center !important;
        background: rgba(255, 255, 255, 0.95) !important;
        border: 4px solid #87CEEB !important;
        padding: 40px !important;
        border-radius: 25px !important;
        box-shadow: 0px 15px 35px rgba(0,0,0,0.1) !important;
        margin-top: 30px !important;
    }
    
    /* Закругление для фото из интернета */
    .stImage img {
        border-radius: 15px !important;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.1) !important;
    }
    </style>
""", unsafe_allow_html=True)

st.balloons()

# Заголовок с защитой от перевода
st.markdown("<p class='main-title notranslate' translate='no'>С ДНЕМ РОЖДЕНИЯ, НАДЮША!</p>", unsafe_allow_html=True)

# --- БЛОК ДЛЯ МУЗЫКИ ---
st.markdown("<p style='text-align:center; color:#2C3E50; font-size:18px; font-weight:bold;'>Включи музыкальное сопровождение ✨</p>", unsafe_allow_html=True)

# ЗАМЕНИ ЭТУ ССЫЛКУ НА СВОЮ СКОПИРОВАННУЮ ССЫЛКУ НА MP3 ФАЙЛ!
audio_link = "https://filebin.net/13faqy7bgd4h8fjd"

st.audio(audio_link, format="audio/mp3", loop=True)
# ----------------------

# --- СПИСОК ССЫЛОК НА ТВОИ ФОТО ИЗ ИНТЕРНЕТА ---
photo_urls = [
    "https://i.postimg.cc/TPNkQ1Zr/IMG-0026.avif",
"https://i.postimg.cc/LsWTL71C/IMG-0125.avif",
"https://i.postimg.cc/y8VvH0KN/IMG-0255.avif",
"https://i.postimg.cc/cH8cmmR7/IMG-0262.avif",
"https://i.postimg.cc/66vHL9ck/IMG-0567.jpg",
"https://i.postimg.cc/g2YNW3pV/IMG-0737.jpg",
"https://i.postimg.cc/RhhJdVxm/IMG-20230512-174218-675-Original.jpg",
"https://i.postimg.cc/3Nq4c53G/IMG-20230616-212808-529-Original.jpg",
"https://i.postimg.cc/zD2gBWTV/IMG-20230621-213100-239-Original.jpg",
"https://i.postimg.cc/nVSDz7qX/IMG-20231006-160507-443-Original.jpg",
"https://i.postimg.cc/PfVwxZ1Q/IMG-20231023-184313-867-Original.jpg",
"https://i.postimg.cc/h4ZdjxVs/IMG-20231102-141804-016-Original.jpg",
"https://i.postimg.cc/026JJQCY/IMG-20240415-160556-853.jpg",
"https://i.postimg.cc/8PFrr5bm/IMG-20240529-152151-990.jpg",
"https://i.postimg.cc/SNXzzsG1/IMG-20250620-182809-426-Original.jpg",
"https://i.postimg.cc/9FvwPh8R/IMG-20250622-160716-275-Original.jpg",
"https://i.postimg.cc/qMtCCRGF/IMG-20250719-172115-621-Original.jpg",
"https://i.postimg.cc/T1sL4MTp/IMG-4081.jpg",
"https://i.postimg.cc/TPKjd9HZ/IMG-4160.avif",
"https://i.postimg.cc/qqFh5Vpx/IMG-4374.jpg",
"https://i.postimg.cc/VkCM26rr/IMG-4398.jpg",
"https://i.postimg.cc/025w5n68/IMG-4704.avif",
"https://i.postimg.cc/Ghp4npNy/IMG-4822.jpg",
"https://i.postimg.cc/L8Yhhb2N/IMG-4872.jpg",
"https://i.postimg.cc/BvfZbZhN/IMG-6061.jpg",
"https://i.postimg.cc/MTWW0PJq/IMG-6513.jpg",
"https://i.postimg.cc/xC0zk3sT/IMG-6579.jpg",
"https://i.postimg.cc/W32kDw9z/IMG-6652.avif",
"https://i.postimg.cc/TwCWn5SJ/IMG-6830.jpg",
"https://i.postimg.cc/ydvS035h/IMG-7021.jpg",
"https://i.postimg.cc/KzJgt3VJ/IMG-7951.jpg",
"https://i.postimg.cc/JnPBjHg2/IMG-7952.jpg",
"https://i.postimg.cc/C1mfbnt3/IMG-7953.jpg",
"https://i.postimg.cc/3RnD20VM/IMG-7954.jpg",
"https://i.postimg.cc/4dBhpHqk/IMG-7955.jpg",
"https://i.postimg.cc/yYJSSdPq/IMG-8444.avif"
]

if photo_urls:
    st.write("")
    cols = st.columns(3)
    for i, url in enumerate(photo_urls):
        with cols[i % 3]:
            st.image(url, use_container_width=True)
# ----------------------------------------------------

# Твой точный текст, полностью защищенный от любого перевода (класс notranslate)
st.markdown("""
<div class='wish-text notranslate' translate='no'>
    Дорогая моя! <br><br>
    Сегодня всё должно быть на высшем уровне, поэтому я и решила сделать этот сюрприз. <br><br>
    Поздравляю тебя с твоим днём! Желаю счастья, здоровья, успеха, денег побольше, верных друзей рядом. Чтобы учёба легкая твоя была. Оставайся такой же улыбчивой и невероятной! ❤️🌟
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# Кнопка
if st.button("✨ НАЖМИ СЮДА ✨", use_container_width=True):
    st.balloons()

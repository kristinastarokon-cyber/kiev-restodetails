import streamlit as st
import os
from PIL import Image

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
    /* Мягкий пастельный фон: сиренево-голубой перелив */
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
    </style>
""", unsafe_allow_html=True)

# Эффект праздничных шаров
st.balloons()

# Заголовок с защитой от перевода
st.markdown("<p class='main-title notranslate' translate='no'>С ДНЕМ РОЖДЕНИЯ, НАДЮША!</p>", unsafe_allow_html=True)

# --- НАДЕЖНЫЙ БЛОК ОТКРЫТИЯ ИЗОБРАЖЕНИЙ ЧЕРЕЗ PIL ---
# Папка photos лежит прямо в одной папке с app.py
image_folder = "photos"

if os.path.exists(image_folder):
    allowed_ext = ['.jpg', '.jpeg', '.png', '.webp', '.PNG', '.JPG', '.heic', '.HEIC']
    photos = [f for f in os.listdir(image_folder) if os.path.splitext(f)[1] in allowed_ext]
    
    if photos:
        st.write("")
        # Создаем сетку из 3 колонок
        cols = st.columns(3)
        for i, photo_name in enumerate(photos):
            photo_path = os.path.join(image_folder, photo_name)
            try:
                # Открываем изображение напрямую через библиотеку PIL
                img = Image.open(photo_path)
                with cols[i % 3]:
                    st.image(img, use_container_width=True)
            except Exception:
                # Если какой-то HEIC файл не прочитался на Windows, пропускаем его без падения сайта
                pass
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

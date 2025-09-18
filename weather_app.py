import streamlit as st
import requests
import datetime
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/"

# 设置网页信息
st.set_page_config(page_title="天气预报", page_icon="⛅", layout="centered")

st.title("🌤️ 天气预报网站")
city = st.text_input("请输入城市名称（支持英文）", "Beijing")

if st.button("查询天气"):
    # 获取实时天气
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric&lang=zh_cn"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        st.subheader(f"📍 {data['name']} 当前天气")
        st.write(f"🌡️ 温度: {data['main']['temp']} °C")
        st.write(f"💧 湿度: {data['main']['humidity']}%")
        st.write(f"🌪️ 风速: {data['wind']['speed']} m/s")
        st.write(f"☁️ 天气状况: {data['weather'][0]['description']}")

        # 获取未来预报
        forecast_url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric&lang=zh_cn"
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        # 整理未来天气数据
        forecast_list = forecast_data["list"]
        dates = []
        temps = []
        for item in forecast_list:
            dt = datetime.datetime.fromtimestamp(item["dt"])
            dates.append(dt)
            temps.append(item["main"]["temp"])
        
        df = pd.DataFrame({"时间": dates, "气温 (°C)": temps})
        st.line_chart(df.set_index("时间"))
    else:
        st.error("❌ 未能获取天气数据，请检查城市名称或 API Key。")

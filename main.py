import streamlit as st
import subprocess
import sys

def main():
    st.write("Hello from weather-frontend!")

def run_streamlit():
    """使用编程方式启动 Streamlit 应用"""
    # 方法1: 使用 subprocess 启动 streamlit
    subprocess.run([sys.executable, "-m", "streamlit", "run", __file__, "--server.headless", "true"])

if __name__ == "__main__":
    # 检查是否在 Streamlit 环境中运行
    try:
        # 如果这个导入成功，说明我们在 Streamlit 环境中
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        if get_script_run_ctx() is not None:
            # 在 Streamlit 环境中，运行主应用逻辑
            main()
        else:
            # 不在 Streamlit 环境中，启动 Streamlit 服务器
            run_streamlit()
    except ImportError:
        # 如果导入失败，启动 Streamlit 服务器
        run_streamlit()
import streamlit as st
import psutil

def launch_dashboard():
    st.title("🖥️ System Health Dashboard")
    st.metric("CPU Usage", f"{psutil.cpu_percent()}%")
    st.metric("Memory Usage", f"{psutil.virtual_memory().percent}%")
    st.write("Troubleshooting Suggestions:")
    if psutil.cpu_percent() > 80:
        st.warning("High CPU usage detected. Consider closing unused apps.")
    if psutil.virtual_memory().percent > 85:
        st.warning("Memory pressure detected. Try restarting background services.")

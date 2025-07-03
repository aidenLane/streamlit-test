import streamlit as st
import pandas as pd

def main():

    st.set_page_config(page_title="Test Title", page_icon="📈", layout="wide")

    st.title("Test 1")

    with st.sidebar:
        st.header("Parameters")
        
        date_range = st.slider("Year Range", 2026, 2035) #Should be a filter?

        interest_rate = st.number_input("Interest Rate", min_value=0.0, value=1.5, step=0.25)
    
    st.subheader("Test 2")

    col1,col2=st.columns(2)

    with col1:
        st.metric("Interest Rate", f"{interest_rate}%")
    with col2:
        st.metric("Year", f"{date_range}")

    
if __name__ == '__main__':
    main()


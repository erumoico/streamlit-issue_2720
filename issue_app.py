# -*- coding: utf-8 -*-

import streamlit as st

from LoremIpsum import lorem_ipsum

# Set page config
st.set_page_config(page_title="Issue 2720", layout="wide") # Must be called before content of page

def main():
    with st.sidebar:
        reverse = st.checkbox('Descending order')
    
    keys = sorted(range(10), reverse=reverse)
    
    for key in keys:
        f"Here is lorem_ipsum_{key}:"
        lorem_ipsum(key=f"{key}")

if __name__ == "__main__":
    main()

# EOF


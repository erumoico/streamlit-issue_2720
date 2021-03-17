# Streamlit Issue 2720 example

This is a minimal example for [Streamlit Issue 2720](https://github.com/streamlit/streamlit/issues/2720).

Just run:
```
make
streamlit run issue_app.py
```
and then open a browser at the displayed URL.
When you switch the `Descending order` checkbox, you will see that some instances of `LoremIpsum` component are empty.
Close the sidebar or change the window size and then empty instances will fill up. But their height of iframe is static.

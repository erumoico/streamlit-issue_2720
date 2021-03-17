# -*- coding: utf-8 -*-

import os
import streamlit.components.v1 as components

import socket

_RELEASE = True

if not _RELEASE:
	# local dev server via `npm run start`
	_lorem_ipsum = components.declare_component(
		"lorem_ipsum",
		url=f"http://{socket.getfqdn()}:3001",
	)
else:
	# release build via `npm run build`
	parent_dir = os.path.dirname(os.path.abspath(__file__))
	build_dir = os.path.join(parent_dir, "frontend/build")
	_lorem_ipsum = components.declare_component("lorem_ipsum", path=build_dir)


# Wrapper function for the component
def lorem_ipsum(key=None):
	"""Create a new instance of "lorem_ipsum".
	
	Parameters
	----------
	key: str or None
	    An optional key that uniquely identifies this component. If this is
	    None, and the component's arguments are changed, the component will
	    be re-mounted in the Streamlit frontend and lose its current state.
	
	Returns
	-------
	None
	
	"""
	return _lorem_ipsum(key=key)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run ExtractiveReaderAnswer/__init__.py`
if not _RELEASE:
	import streamlit as st
	
	st.subheader("Test Component `lorem_ipsum()`")
	
	"Hello World, this is LoremIpsum component!"
	
	lorem_ipsum()

# EOF

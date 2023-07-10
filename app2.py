import streamlit as st
import pickle
from typing import List, Tuple
from streamlit_searchbox import st_searchbox
import logging
from crp_model import TrieNode
from crp_model import Trie

logging.getLogger("streamlit_searchbox").setLevel(logging.DEBUG)


st.set_page_config(page_title="VeePee", page_icon=":sparkles:", layout="centered")


# Load your model using pickle
@st.cache_resource
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


@st.cache_data
def get_autocomplete_suggestions(search_term: str) -> List[Tuple[str, any]]:
    if not search_term:
        return []
    # Implement your function to return autocomplete suggestions based on the model
    suggestions = model.suggestion(search_term.lower())[:5]
    return [
        (suggestion, suggestion)
        for suggestion in suggestions
    ]


# Load your model here
model_path = 'trie.pkl'
model = load_model(model_path)

st.markdown("<h1 style='text-align: center; color: pink;'>Bienvenue Chez VeePee</h1>", unsafe_allow_html=True)

with st.sidebar:
        selected_value = st_searchbox(
            search_function=get_autocomplete_suggestions,
            placeholder="Recherchez une marque, un produit...",
            default="SOME DEFAULT",
            label="get_autocomplete_suggestions",
            clear_on_submit=False,
            clearable=True,
            key="get_autocomplete_suggestions",
        )
        st.info(f"{selected_value}")

import streamlit as st
import joblib
model = joblib.load('spam-ham')
st.title('SPAM HAM CLASSIFIER')
ip = st.text_input('Enter the Message')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])

import pickle
import streamlit as st

# membaca model
ai_model = pickle.load(open('ai_model.sav','rb'))

# judul web
st.title('Data Mining Prediksi AI Dev Productivity')

# membagi kolom
col1, col2 = st.columns(2)

with col1 :
    hours_coding = st.text_input('Input Nilai Hours_Coding')

with col2 :
    coffee_intake_mg = st.text_input('Input Nilai coffee_intake_mg')

with col1 :
    distractions = st.text_input('Input Nilai distractions')

with col2 :
    sleep_hours = st.text_input('Input Nilai sleep_hours')

with col1 :
    commits = st.text_input('Input Nilai commits')

with col2 :
    bugs_reported = st.text_input('Input Nilai bugs_reported')

with col1 :
    ai_usage_hours = st.text_input('Input Nilai ai_usage_hours')

with col2 :
    cognitive_load = st.text_input('Input Nilai cognitive_load')

# code untuk prediksi
dev_productivity = ''

# membuat tombol untuk prediksi
if  st.button('Test Prediksi Developer') :
    ai_prediction = ai_model.predict([[hours_coding,coffee_intake_mg,distractions,sleep_hours,commits,bugs_reported,ai_usage_hours,cognitive_load]])

    if(ai_prediction[0] == 1):
           dev_productivity = 'task success'

    else :
           dev_productivity = 'task tidak success'

    st.success(dev_productivity)
      

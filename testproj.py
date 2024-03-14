
#cd Desktop/testfolder 
#streamlit run testproj.py

#----------------
#import libraries
#----------------
import streamlit as st
import numpy as np
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode
import pandas as pd
import datetime as dt


#------------------
#page configuration
#------------------
st.set_page_config(page_title="Menu", page_icon="🐬", layout="wide",initial_sidebar_state="collapsed")


#----------------
#pull in data
#----------------
projectGallery = pd.read_excel('projectdata.xlsx')
displayColumns = projectGallery[["Title","Vendor","ProjectStatus"]]

#----------------
#set variables
#----------------
if 'selectedChartName' not in st.session_state:
    st.session_state.selectedChartName = 0
if 'selectedChartID' not in st.session_state:
    st.session_state.selectedChartID = 0

if 'selectedProjectName' not in st.session_state:
    st.session_state.selectedProjectName = 0
if 'selectedProjectID' not in st.session_state:
    st.session_state.selectedProjectID = 0

if 'selectedEncounterName' not in st.session_state:
    st.session_state.selectedEncounterName = 0
if 'selectedEncounterID' not in st.session_state:
    st.session_state.selectedEncounterID = 0

if 'selectedDiagnosisName' not in st.session_state:
    st.session_state.selectedDiagnosisName = 0
if 'selectedDiagnosisID' not in st.session_state:
    st.session_state.selectedDiagnosisID = 0

#--------------------------
#page content starts here:
#--------------------------
st.markdown("<h1 style='text-align: center; color: red;'>MR Coder</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Select a project</h3>", unsafe_allow_html=True)



builder = GridOptionsBuilder.from_dataframe(projectGallery)
#builder.configure_pagination(enabled=False)
builder.configure_selection(selection_mode='single', use_checkbox=False)
builder.configure_column('Title', editable=False)
grid_options = builder.build()
column_defs = grid_options["columnDefs"]
columns_to_hide = ["AddEq","DeleteEq"]
for col in column_defs:
    if col["headerName"] in columns_to_hide:
        col["hide"] = True
# Display AgGrid
return_value = AgGrid(projectGallery, gridOptions=grid_options,columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS)
if return_value['selected_rows']:
    system_name = return_value['selected_rows'][0]['ID']
    st.session_state.selectedProjectID = system_name
    system_name1 = return_value['selected_rows'][0]['Title']
    st.session_state.selectedProjectName = system_name1
    nav_chartreviewpage = st.button('Review '+f"{system_name1}", type = "primary")
    if nav_chartreviewpage:
        switch_page("projectdetailpage")
else:
    st.write("No project selected")


nav_newprojectpage = st.button("Add new project", type = "secondary")
if nav_newprojectpage:
    switch_page("newprojectpage")
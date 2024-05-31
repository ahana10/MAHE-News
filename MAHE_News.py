# Import necessary libraries
from GoogleNews import GoogleNews
from PIL import Image
import datetime
import streamlit as st
import pandas as pd
import webbrowser

# Function to make URLs clickable in a DataFrame
def make_clickable(val):
    return f'<a href="{val}" target="_blank">{val}</a>'

# Page 1: Display basic details
def page1():
    image_new = Image.open('edu.png')
    st.image(image_new, width=750)
    st.title("MANIPAL ACADEMY OF HIGHER EDUCATION")
    st.write("MAHE Manipal is one of India's leading academic and research institutions. It has been granted Institution of Eminence status by the Ministry of Education, Government of India.")
    st.image("nirf_img.png", use_column_width=True)
    st.image("TIMES_img.png", use_column_width=True)
    st.image("rank_img.png", caption="Ranking of MAHE in various ranking system", use_column_width=True)
    st.image("mahe_sdg.png", use_column_width=True)

# Page 2: Display SDG goals
def page2():
    st.title("Sustainable Development Goals")
    image_sdg = Image.open('sdg.png')
    st.image(image_sdg, width=750)
    st.image("sdg_1.png", use_column_width=True)
    st.image("sdg_2.png", use_column_width=True)
    st.image("sdg_3.png", use_column_width=True)

# Page 3: Filter news articles based on user input
def page3():
    image_new = Image.open('edu.png')
    st.image(image_new, width=750)
    st.title("MAHE News")

    # Campus, year, and SDG goals selection
    campus = st.selectbox('Select Campus', ['All', 'Manipal', 'Bangalore', 'Mangalore'])
    #year = st.selectbox('Select Year', ['All'] + [str(year) for year in range(2019, 2024)])
    sdg_goals = st.multiselect('Select SDG Goals', [
        "No Poverty", "Zero Hunger", "Good Health and Well-Being",
        "Quality Education", "Gender Equality", "Clean Water and Sanitation",
        "Affordable and Clean Energy", "Decent Work and Economic Growth",
        "Industry, Innovation and Infrastructure", "Reduced Inequalities",
        "Sustainable Cities and Communities", "Responsible Consumption and Production",
        "Climate Action", "Life Below Water", "Life on Land",
        "Peace, Justice and Strong Institutions", "Partnerships for the Goals"
    ])

    # Load news data from Excel file
    df = pd.read_csv('filtered_articles_with_sdg_1.csv')
    #df["Link"]=df["Link"].apply(make_clickable)
    
    if sdg_goals:
        print(sdg_goals)
        sdg_goals=str(sdg_goals)
        sdg_goals=sdg_goals.replace("[","")
        sdg_goals=sdg_goals.replace("]","")
        sdg_goals=sdg_goals.replace("'","")
        print("NEW SDG ",sdg_goals)
        ls=[]
        for i in range (0, len(df)):
            if(df[sdg_goals][i])=="yes":
                ls.append(i)
        count=0
        for i in ls:
            count+=1
            st.write(df["Date"][i])
            st.write(df["Title"][i])
            link=df["Link"][i]
            #st.write(df["Link"][i],unsafe_allow_html=True)
            #st.markdown(f'<a href="{df["Link"][i]}" target="_blank">Read more</a>', unsafe_allow_html=True)
            if st.button(f"Open Article{count}"):
              webbrowser.open_new_tab(link)
            
            
           


# Combine pages using Streamlit's sidebar for navigation
def main():
    st.sidebar.title("")
    page = st.sidebar.radio("Go to", ["Home", "SDG Goals", "News"])

    if page == "Home":
        page1()
    elif page == "SDG Goals":
        page2()
    elif page == "News":
        page3()

if __name__ == '__main__':
    main()

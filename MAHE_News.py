# Import necessary libraries
from GoogleNews import GoogleNews
from PIL import Image
import datetime
import streamlit as st
import pandas as pd
import webbrowser
import time
import streamlit.components.v1 as components

# Function to make URLs clickable in a DataFrame
def make_clickable(val):
    return f'<a href="{val}" target="_blank">{val}</a>'

# Page 1: Display basic details
def page1():
    image_new = Image.open('edu.png')
    st.image(image_new, width=750)
    st.title("MANIPAL ACADEMY OF HIGHER EDUCATION")
    st.write("MAHE Manipal is one of India's leading academic and research institutions. It has been granted Institution of Eminence status by the Ministry of Education, Government of India.")
    #st.image("nirf_img.png", use_column_width=True)
    #st.image("Times rank.png", use_column_width=True)
    #st.image("rank_img.png", caption="Ranking of MAHE in various ranking system", use_column_width=True)
    #st.image("mahe_sdg.png", use_column_width=True)
    frame_placeholder = st.empty()
    frames=["Times rank.jpeg","the rank.jpeg","the rank_2.jpeg","QS rank.jpeg","QS total.jpeg","nirf_new.png","The week rank.jpeg","SCIMAGO rank.jpeg","mahe_sdg.png"]

  
    while True:
        for i in (frames):
            
            
            frame_placeholder.image(i)
            time.sleep(2)



# Load your image (replace 'sunrise.jpg' with the actual path to your image)
image = Image.open('logo.jpg')
# Display the image with an optional caption
st.sidebar.image(image, width=200)


# Page 2: Display SDG goals
def page2():
    st.title("Sustainable Development Goals")
    image_sdg = Image.open('sdg.png')
    st.image(image_sdg, width=750)
    #st.image("sdg_1.png", use_column_width=True)
    #st.image("sdg_2.png", use_column_width=True)
    #st.image("sdg_3.png", use_column_width=True)
    
    
    #Dictionary for column 1
    dict1={"Goal 1: No Poverty":"End poverty in all its forms everywhere","Goal 3: Good Health and Well-Being":"Ensure healthy lives and promote well-being for all at all ages","Goal 5: Gender Equality":"Achieve gender equality and empower all women and girls","Goal 7: Affordable and Clean Energy":"Ensure access to affordable, reliable, sustainable and modern energy for all","Goal 9: Industry, Innovation and Infrastructure": "Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation","Goal 11: Sustainable Cities and Communities":"Make cities and human settlements inclusive, safe, resilient and sustainable","Goal 13: Climate Action":"Take urgent action to combat climate change and its impacts","Goal 15: Life on Land":"Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land degradation and halt biodiversity loss","Goal 17: Partnerships for the Goals":"Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development"}
    #Create a similar dict for column2 (Goals 11 to 17)
    dict2={"Goal 2: Zero Hunger":"End hunger, achieve food security and improved nutrition and promote sustainable agriculture","Goal 4: Quality Education":"Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all","Goal 6: Clean Water and Sanitation":"Ensure availability and sustainable management of water and sanitation for all","Goal 8: Decent Work and Economic Growth":"Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all","Goal 10: Reduced Inequalities":"Reduce inequality within and among countries", "Goal 12: Responsible Consumption and Production":"Ensure sustainable consumption and production patterns","Goal 14: Life Below Water":"Conserve and sustainably use the oceans, seas and marine resources for sustainable development","Goal 16: Peace, Justice and Strong Institutions":"Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels"}




    col1,col2=st.columns(2)
    # HTML and CSS for multiple flip boxes
    flip_boxes_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interactive Flip Boxes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            .dashboard {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                align-items: center;
                padding: 20px;
                gap: 20px;
            }
            .flip-box {
                background-color: transparent;
                width: 300px;
                height: 300px;
                border: 1px solid #ccc;
                perspective: 1000px;
                margin: 20px;
            }
            .flip-box-inner {
                position: relative;
                width: 100%;
                height: 100%;
                text-align: center;
                transition: transform 0.6s;
                transform-style: preserve-3d;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                
            }
            .flip-box-front, .flip-box-back {
                position: absolute;
                width: 100%;
                height: 100%;
                backface-visibility: hidden;
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 1.5em;
                
            }
            .flip-box-front {
                background-color:#2980b9;
                color: black;
            }
            .flip-box-back {
                background-color: #2980b9;
                color: white;
                transform: rotateY(180deg);
            }
            .flipped {
                transform: rotateY(180deg);
            }
        </style>
    </head>
    <body>
        <div class="dashboard">
    """


    flip_boxes_html1 = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Interactive Flip Boxes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            .dashboard {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                align-items: center;
                padding: 20px;
                gap: 20px;
            }
            .flip-box {
                background-color: transparent;
                width: 300px;
                height: 300px;
                border: 1px solid #ccc;
                perspective: 1000px;
                margin: 20px;
            }
            .flip-box-inner {
                position: relative;
                width: 100%;
                height: 100%;
                text-align: center;
                transition: transform 0.6s;
                transform-style: preserve-3d;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            }
            .flip-box-front, .flip-box-back {
                position: absolute;
                width: 100%;
                height: 100%;
                backface-visibility: hidden;
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 1.5em;
            }
            .flip-box-front {
                background-color: #2980b9;
                color: black;
            }
            .flip-box-back {
                background-color: #2980b9;
                color: white;
                transform: rotateY(180deg);
            }
            .flipped {
                transform: rotateY(180deg);
            }
        </style>
    </head>
    <body>
        <div class="dashboard">
    """






    with col1:

        # Adding flip boxes for each goal
        for item,value in dict1.items():
            flip_boxes_html += f"""
                <div class="flip-box" ondblclick="flipCard(this)">
                    <div class="flip-box-inner">
                        <div class="flip-box-front">
                            <h2>{item}</h2>
                        </div>
                        <div class="flip-box-back">
                            <p>{value}</p>
                        </div>
                    </div>
                </div>
            """

        # Closing tags for HTML
        flip_boxes_html += """
            </div>
            <script>
                function flipCard(element) {
                    const flipBoxInner = element.querySelector('.flip-box-inner');
                    flipBoxInner.classList.toggle('flipped');
                }
            </script>
        </body>
        </html>
        """
        
        

        # Embed the HTML in the Streamlit app
        components.html(flip_boxes_html, height=111200)

    with col2:
        # Adding flip boxes for each goal
        for item,value in dict2.items():
            print(item)
            flip_boxes_html1 += f"""
                <div class="flip-box" ondblclick="flipCard(this)">
                    <div class="flip-box-inner">
                        <div class="flip-box-front">
                            <h2>{item}</h2>
                        </div>
                        <div class="flip-box-back">
                            <p>{value}</p>
                        </div>
                    </div>
                </div>
            """

        # Closing tags for HTML
        flip_boxes_html1 += """
            </div>
            <script>
                function flipCard(element) {
                    const flipBoxInner = element.querySelector('.flip-box-inner');
                    flipBoxInner.classList.toggle('flipped');
                }
            </script>
        </body>
        </html>
        """

        # Embed the HTML in the Streamlit app
        components.html(flip_boxes_html1, height=111200)

        
        
        

# Page 3: Filter news articles based on user input
def page3():
    image_new = Image.open('edu.png')
    st.image(image_new, width=750)
    st.title("MAHE News")

    # Campus, year, and SDG goals selection
    campus = st.selectbox('Select Campus', ['None', 'Manipal', 'Bangalore', 'Mangalore'])
    #year = st.selectbox('Select Year', ['All'] + [str(year) for year in range(2019, 2024)])
    sdg_goals = st.selectbox('Select SDG Goals', [
        "None","No Poverty", "Zero Hunger", "Good Health and Well-Being",
        "Quality Education", "Gender Equality", "Clean Water and Sanitation",
        "Affordable and Clean Energy", "Decent Work and Economic Growth",
        "Industry, Innovation and Infrastructure", "Reduced Inequalities",
        "Sustainable Cities and Communities", "Responsible Consumption and Production",
        "Climate Action", "Life Below Water", "Life on Land",
        "Peace, Justice and Strong Institutions", "Partnerships for the Goals"
    ])

    # Load news data from Excel file
    df = pd.read_csv('update_data_keywords_campus.csv')
    #df["Link"]=df["Link"].apply(make_clickable)
    
    if sdg_goals!="None" and campus=="None":
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
            # if st.button(f"Open Article{count}"):
            #   webbrowser.open_new_tab(link) 
            button_key = f"button_{count}"

            if st.button(f"Open Article {count}", key=button_key):
                js = f"window.open('https://{link}')"
                html = f"<script>{js}</script>"
                st.components.v1.html(html)
            # st.markdown(f'<a href="{link}" target="_blank">Open Article {count}</a>', unsafe_allow_html=True)
            # st.link_button(f"Open Article{count}", link)
            
            
    elif sdg_goals!="None" and campus!="None":
        print(sdg_goals)
        sdg_goals=str(sdg_goals)
        sdg_goals=sdg_goals.replace("[","")
        sdg_goals=sdg_goals.replace("]","")
        sdg_goals=sdg_goals.replace("'","")
        
        campus=str(campus)
        campus=campus.replace("[","")
        campus=campus.replace("]","")
        campus=campus.replace("'","")
        print("NEW SDG ",sdg_goals)
        print("Campus",campus)
        ls=[]
        for i in range (0, len(df)):
            if(df[sdg_goals][i])=="yes" and df[campus][i]=="yes" :
                ls.append(i)
        count=0
        for i in ls:
            count+=1
            st.write(df["Date"][i])
            st.write(df["Title"][i])
            link=df["Link"][i]
            #st.write(df["Link"][i],unsafe_allow_html=True)
            #st.markdown(f'<a href="{df["Link"][i]}" target="_blank">Read more</a>', unsafe_allow_html=True)
            # if st.button(f"Open Article{count}"):
            #   webbrowser.open_new_tab(link) 
            button_key = f"button_{count}"

            if st.button(f"Open Article {count}", key=button_key):
                js = f"window.open('https://{link}')"
                html = f"<script>{js}</script>"
                st.components.v1.html(html)
            
            
           


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

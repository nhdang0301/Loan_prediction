import pickle
import streamlit as st
from PIL import Image

model_load = pickle.load(open('./Model/lastest_prediction_model', 'rb'))

def run():
    
    img1 = Image.open('image2.jpg')
    st.header("Bank loan prediction using Machine Learning")
    st.image(img1, use_column_width=False)
    st.subheader("Fill your information here")

    #Full name
    full_name = st.text_input("Full name")

    #Gender
    gen_display = ('---', 'Female', 'Male')
    gen_option = list(range(len(gen_display)))
    gender = st.selectbox('Gender', gen_option, format_func=lambda x:gen_display[x])
    if gender == 0:
        st.write("None")
    elif gender == 1:
        st.write(gen_display[1])
    else:
        st.write(gen_display[2])
    #Age
    age = st.number_input("Age")

    #Income
    imcome = st.number_input("Income")

    #CCAvg
    ccavg = st.number_input("CCAvg")

    #Mortage
    mortgage = st.number_input("Mortgage")

    #Family
    family_2 = 0
    family_3 = 0
    family_4 = 0
    family_display = ('1', '2', '3', '4')
    family_option = list(range(len(family_display)))
    family = st.selectbox('Number of Family Members', family_option, format_func=lambda x: family_display[x])
    if family == 0:
        family_2 = 0
        family_3 = 0
        family_4 = 0
    elif family == 1:
        family_2 = 1
    elif family == 2:
        family_3 = 1
    else:
        family_4 = 1

    #Education
    education_2 = 0
    education_3 = 0
    edu_display = ('1', '2', '3')
    edu_option = list(range(len(edu_display)))
    education = st.selectbox('Level of Education', edu_option, format_func=lambda x: edu_display[x])
    if education == 0:
        education_2 = 0
        education_3 = 0
    elif education == 1:
        education_2 = 1
    else:
        education_3 = 1

    #Securities account
    security_account_1 = 0
    securities_display = ('Yes', 'No')
    securities_option = list(range(len(securities_display)))
    securities_account = st.selectbox('Do you have a security account?', securities_option, format_func=lambda x: securities_display[x])
    if securities_account == 0:
        security_account_1 = 1
    else:
        security_account_1 = 0

    #CD account
    cd_account_1 = 0
    CD_display = ('Yes', 'No')
    CD_option = list(range(len(CD_display)))
    CD_account = st.selectbox('Do you have a CD account?', CD_option, format_func=lambda x: CD_display[x])
    if CD_account == 0:
        cd_account_1 = 1
    else:
        cd_account_1 = 0

    #Online
    online_1 = 0
    Onl_display = ('Yes', 'No')
    Onl_option = list(range(len(Onl_display)))
    Online_banking = st.selectbox('Do you use internet Banking?', Onl_option, format_func=lambda x: Onl_display[x])
    if Online_banking == 0:
        online_1 = 1
    else:
        online_1 = 0


    #Credit
    credit_1 = 0
    Credit_display = ('Yes', 'No')
    Credit_option = list(range(len(Credit_display)))
    Credit = st.selectbox('Do you use credit?', Credit_option, format_func=lambda x: Credit_display[x])
    if Credit == 0:
        credit_1 = 1
    else:
        credit_1 = 0

    #Region
    central = 0
    los = 0
    sou = 0
    sup = 0
    Region_display = ('Bay Area', 'Central', 'Los Angeles Region', 'Southern', 'Superior')
    Region_option = list(range(len(Region_display)))
    Region = st.selectbox('Where do you live?', Region_option, format_func=lambda x: Region_display[x])
    if Region == 0:
        central = 0
        los = 0
        sou = 0
        sup = 0
    elif Region == 1:
        central = 1
    elif Region == 2:
        los = 1
    elif Region == 3:
        sou = 1
    else:
        sup = 1

    if st.button("Submit"):

        features = [[age, imcome, ccavg, mortgage, family_2, family_3, family_4, education_2, education_3, security_account_1, cd_account_1, online_1, credit_1, central, los, sou, sup]]
        prediction = model_load.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Hello: " + full_name + ':( xin lỗi bạn'
            )
        else:
            st.success(
                "Hello: " + full_name + ' Congratulations!! các bạn được ngân hàng cho vay rồi nè'
            )

run()

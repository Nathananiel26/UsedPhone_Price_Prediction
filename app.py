import streamlit as st
import joblib

st.title('📱 USED PHONE PRICE PREDICTION')
scaler = joblib.load("scaler_used")

with st.form(key = 'phone'):
    brandName = st.selectbox(label='Select your brand name: ',options=['Honor', 'Others', 'HTC', 'Huawei', 'Infinix', 'Lava', 'Lenovo',
       'LG', 'Meizu', 'Micromax', 'Motorola', 'Nokia', 'OnePlus', 'Oppo','Realme', 'Samsung', 'Vivo', 'Xiaomi', 'ZTE', 'Apple', 'Asus',
       'Coolpad', 'Acer', 'Alcatel', 'BlackBerry', 'Celkon', 'Gionee','Google', 'Karbonn', 'Microsoft', 'Panasonic', 'Sony', 'Spice',
       'XOLO'])
    brandName_val = 0
    if brandName == 'Honor':
        brandName_val = 1
    elif brandName == 'HTC':
        brandName_val = 2
    elif brandName == 'Huawei':
        brandName_val = 3
    elif brandName == 'Infinix':
        brandName_val = 4
    elif brandName == 'Lava':
        brandName_val = 5
    elif brandName == 'Lenovo':
        brandName_val = 6
    elif brandName == 'LG':
        brandName_val = 7
    elif brandName == 'Meizu':
        brandName_val = 8
    elif brandName == 'Micromax':
        brandName_val = 9
    elif brandName == 'Motorola':
        brandName_val = 10
    elif brandName == 'Nokia':
        brandName_val = 11
    elif brandName == 'OnePlus':
        brandName_val = 12
    elif brandName == 'Oppo':
        brandName_val = 13
    elif brandName == 'Realme':
        brandName_val = 14
    elif brandName == 'Samsung':
        brandName_val = 15
    elif brandName == 'Vivo':
        brandName_val = 16
    elif brandName == 'Xiaomi':
        brandName_val = 17
    elif brandName == 'ZTE':
        brandName_val = 18
    elif brandName == 'Apple':
        brandName_val = 19
    elif brandName == 'Asus':
        brandName_val = 20
    elif brandName == 'Coolpad':
        brandName_val = 21
    elif brandName == 'Acer':
        brandName_val = 22
    elif brandName == 'Alcatel':
        brandName_val = 23
    elif brandName == 'BlackBerry':
        brandName_val = 24
    elif brandName == 'Celkon':
        brandName_val = 25
    elif brandName == 'Gionee':
        brandName_val = 26
    elif brandName == 'Google':
        brandName_val = 27
    elif brandName == 'Karbonn':
        brandName_val = 28
    elif brandName == 'Microsoft':
        brandName_val = 29
    elif brandName == 'Panasonic':
        brandName_val = 30
    elif brandName == 'Sony':
        brandName_val = 31
    elif brandName == 'Spice':
        brandName_val = 32
    elif brandName == 'XOLO':
        brandName_val = 33
    else :
        brandName_val = 34


    


    os = st.selectbox(label='Select your OS',options=['Android', 'Others', 'iOS', 'Windows'])
    os_val = 0
    if os == 'Android':
        os_val = 1
    elif os == 'iOS':
        os_val = 2
    elif os == 'Windows':
        os_val = 3
    else :
        os_val = 4



    screenSize = st.number_input('Enter the screen size',min_value=0,max_value=200000)

    g4 = st.selectbox(label='Do you 4G ?',options=['Yes','No'])
    g4_val = 1 if g4 == 'Yes' else 0

    g5 = st.selectbox(label='Do you 5G ?',options=['Yes','No'])
    g5_val = 1 if g5 == 'Yes' else 0

    main_camera_mp = st.number_input('Enter the main camera mp',min_value=0,max_value=200000)

    selfie_camera_mp = st.number_input('Enter the selfie_camera_mp',min_value=0,max_value=200000)

    int_memory = st.number_input('Enter the int_memory',min_value=0,max_value=200000)

    ram = st.number_input('Enter the ram',min_value=0,max_value=200000)

    battery = st.number_input('Enter the battery capacity',min_value=0,max_value=200000)

    weight = st.number_input('Enter the weight',min_value=0,max_value=200000)

    release_year  = st.number_input('Enter the release year ',min_value=0,max_value=200000)

    days_used = st.number_input('Enter the days_used',min_value=0,max_value=200000)

    new_price = st.number_input('Enter the new_price',min_value=0,max_value=200000)

    

    
 

    display_button = st.form_submit_button(label='Predict')
if display_button:
     model = joblib.load('Used_Price_model')
     result = model.predict([[brandName_val ,screenSize, os_val , g4_val , g5_val , main_camera_mp , selfie_camera_mp , int_memory , ram , battery , weight          ,release_year,days_used , new_price ]])
     st.success(f'Your used phone Price is :{result[0]}')
     st.balloons()


# # Fields that need scaling
#     scale_features = [screenSize, main_camera_mp, selfie_camera_mp, int_memory, ram,
#                       battery, weight, release_year, days_used, new_price]

#     # Fields that do not need scaling
#     other_features = [brandName_val, os_val, g4_val, g5_val]

#     # Scale only the necessary fields
#     scaled_features = scaler.transform([scale_features])[0]

#     # Combine scaled and non-scaled features
#     input_data = other_features + scaled_features.tolist()

#     # Load the model and make predictions
#     model = joblib.load('Used_Price_model')
#     result = model.predict([input_data])

#     st.success(f'Your used phone price is: ${result[0]:.2f}')
#     st.balloons()





    

import streamlit as st
import numpy as np
import heartdiseaseprediction as model


def set_zero_one(gender,fastingBS,exerciseAngina):
    if gender == "Male":
        gender = 1
    else:
        gender = 0
        
    if fastingBS == "Above 120":
        fastingBS = 1
    else:
        fastingBS = 0
        
    if exerciseAngina == "Yes":
        exerciseAngina = 1
    else:
        exerciseAngina = 0
        
    return gender,fastingBS,exerciseAngina
        
    

def setValues(var,map):
    for key , value in map.items():
        if value == var:
            return key    


def window():
    st.header("Heart Disease Prediction")

    age = st.slider("Select you Age : ",10,100,25)
    gender = st.radio("Gender:",("MALE","FEMALE"))
    chestPainType = st.radio("Chest Pain Type : \n TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic" ,('ATA' ,'NAP' ,'ASY' ,'TA'))
    restingBP = st.slider("Resting Blood Pressure : (resting blood pressure [mm Hg])",60,220,120)
    cholesterol = st.slider("Cholesterol : (serum cholesterol [mm/dl])" , 60,750,120)
    fastingBS = st.radio("Fasting Blood Sugar :",("Above 120" , "Below 120"))
    restingECG = st.radio("Resting ECG :\n Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria",('Normal', 'ST' ,'LVH'))
    maxHR = st.slider("Maximum Heart Rate :(maximum heart rate achieved)",60,200,65)
    exerciseAngina = st.radio("Exercise induced angina : (exercise-induced angina)",("YES" , "NO"))
    oldPeak = st.slider("OldPeak = ST (Numeric value measured in depression) :" , -10,10,1)
    st_slope = st.radio("ST_Slope :\nUp: upsloping, Flat: flat, Down: downsloping",('Up', 'Flat' ,'Down'))

    gender,fastingBS,exerciseAngina = set_zero_one(gender,fastingBS,exerciseAngina)
    
    chestPainType = setValues(chestPainType,model.chestPain_map)
    restingECG = setValues(restingECG,model.restingECG_map)
    st_slope = setValues(st_slope,model.st_slope_map)
    
        
        
    x_test = np.array([age,gender,chestPainType,restingBP,cholesterol,fastingBS,restingECG,maxHR,exerciseAngina,oldPeak,st_slope])

    if st.button("Predict",type="primary"):
        result = model.rf_classifier.predict([x_test])
        if result == 1:
            st.warning("You have been diagnosed with a Heart Disease")
        else:
            st.write("You do not have a Heart Disease")
            
    
    st.text("It is always better to visit a doctor in these type of cases")




if __name__ == "__main__":
    window()
    

    




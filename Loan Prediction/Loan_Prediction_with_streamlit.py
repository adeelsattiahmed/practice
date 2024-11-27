import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split

df=pd.read_csv('Loan_dataset.csv')
st.title("Loan Prediction")
df=df.dropna()
df.Loan_Status=df.Loan_Status.map({'Y':1,'N':0})
#Changing the 3+ to 4 bcz we cannot apply model on 3+
df.Dependents=df.Dependents.replace({'3+':4})

#Now replacing the catagories of columns to integers
df.replace({'Gender':{'Male':1,'Female':0},
            'Married':{'Yes':1,'No':0},
            'Education':{'Graduate':1,'Not Graduate':0},
            'Self_Employed':{'Yes':1,'No':0},
            'Property_Area':{'Rural':0,'Urban':1,'Semiurban':2}},inplace=True)

X=df.drop(['Loan_ID','Loan_Status'],axis=1)
y=df.iloc[:,-1]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1,stratify=y)

#Now Applying the model 
from sklearn.svm import SVC
model=SVC(kernel='linear')

model.fit(X_train,y_train)


loan_id=st.text_input('What is your Loan_ID ?')
Gender=st.radio('Gender',('Male','Female'),index=None)
if Gender=='Male':
    Gender=1
else:
    Gender=0    

Married=st.radio('Marital Status ',('Yes','No'),index=None)
if Married=='Yes':
    Married=1
else:
    Married=0    
  
Dependents=st.radio('In Family , How many person are Dependent on you ?',(0,1,2,3,4),index=None)
     
     
Education=st.radio('What is your Education ? ',('Graduate','Not Graduate'),index=None)
if Education=='Graduate':
    Education=1
else:
    Education=0    
  
Self_Employed=st.radio('You are Self_Employed ?',('Yes','No'),index=None)
if Self_Employed=='Yes':
    Self_Employed=1
else:
    Self_Employed=0    

Credit_History=st.radio('Do you have took loan Before ?',('Yes','No'),index=None)
if Credit_History=='Yes':
    Credit_History=1
else:
    Credit_History=0   

Property_Area=st.radio('Where do you live ? ',('Rural','Urban','Semiurban'),index=None)
if Property_Area=='Rural':
    Property_Area=0
elif Property_Area=='Urban':
    Property_Area=1  
else:
     Property_Area=2
  
Applicant=st.text_input('What is  your Income ?')
# Try to convert the input to an integer
try:
    ApplicantIncome = int(Applicant)
except ValueError:
    st.error("Invalid input in your income . Please enter a valid integer.")
    
Coapplicant=st.text_input('Enter the income of your Coapplicant ?')
# Try to convert the input to an integer
try:
    CoapplicantIncome = int(Coapplicant)
except ValueError:
    st.error("Invalid input on CoapplicantIncome . Please enter a valid integer.")
    
Loan=st.text_input('How much Loan Do you want to take ?')
# Try to convert the input to an integer
try:
    LoanAmount = int(Loan)
except ValueError:
    st.error("Invalid input on Loan you entered . Please enter a valid integer.")
    
Loan_Amount=st.text_input('Enter your Loan_Amount_Term :')
# Try to convert the input to an integer
try:
    Loan_Amount_Term = int(Loan_Amount)
except ValueError:
    st.error("Invalid input on Loan_Amount_Term you entered . Please enter a valid integer.")
    
prediction=model.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])

if st.button('Check status'):
    prediction=model.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
    if prediction==1:
        st.markdown('Your Loan Would be approved')
    else :
        st.markdown('Your Loan Would  not be approved')        
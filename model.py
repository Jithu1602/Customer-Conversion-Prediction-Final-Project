import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def Insurance_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person will not Claim Insurance'
    else:
        return 'The person will Claim Insurance'


def main():
    # giving a title
    st.title('Insurance Claim Prediction Web App')

    # getting the input data from the user

    Age = st.text_input('Age of the Person')
    J = st.text_input('Job Type')
    Job = 0
    if J == 'blue-collar':
        Job = 1
    elif J == 'entrepreneur':
        Job = 2
    elif J == 'housemaid':
        Job = 3
    elif J == 'services':
        Job = 4
    elif J == 'technician':
        Job = 5
    elif J == 'self-employed':
        Job = 6
    elif J == 'admin':
        Job = 7
    elif J == 'management':
        Job = 8
    elif J == 'unemployed':
        Job = 9
    elif J == 'retired':
        Job = 10
    elif J == 'student':
        Job = 11
    Job = st.write(Job)
    M = st.text_input('Marital Status')
    Marital = 0
    if M == 'married':
        Marital = 1
    elif M == 'divorced':
        Marital = 2
    elif M == 'single':
        Marital = 3
    Marital = st.write(Marital)
    E = st.text_input('Education Status')
    Education_qual = 0
    if E == 'primary':
        Education_qual = 1
    elif E == 'secondary':
        Education_qual = 2
    elif E == 'tertiary':
        Education_qual = 3
    Education_qual = st.write(Education_qual)
    C = st.text_input('Contact communication type')
    Call_Type = 0
    if C == 'unknown':
        Call_Type = 1
    elif C == 'telephone':
        Call_Type = 2
    elif C == 'cellular':
        Call_Type = 3
    Call_Type = st.write(Call_Type)
    Day = st.text_input('Last contact day of the month (numeric)')
    Mo = st.text_input('Last contact month of year')
    Month = 0
    if Mo == 'may':
        Month = 1
    elif Mo == 'jul':
        Month = 2
    elif Mo == 'jan':
        Month = 3
    elif Mo == 'nov':
        Month = 4
    elif Mo == 'jun':
        Month = 5
    elif Mo == 'aug':
        Month = 6
    elif Mo == 'feb':
        Month = 7
    elif Mo == 'apr':
        Month = 8
    elif Mo == 'oct':
        Month = 9
    elif Mo == 'sep':
        Month = 10
    elif Mo == 'dec':
        Month = 11
    elif Mo == 'mar':
        Month = 12
    Month = st.write(Month)
    Dur = st.text_input('Last contact duration, in seconds (numeric)')
    Num_calls = st.text_input('Number of contacts performed during this campaign and for this client')
    P = st.text_input('Outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")')
    Prev_outcome = 0
    if P == 'unknown':
        Prev_outcome = 1
    elif P == 'failure':
        Prev_outcome = 2
    elif P == 'other':
        Prev_outcome = 3
    elif P == 'success':
        Prev_outcome = 4
    Prev_outcome = st.write(Prev_outcome)

    # code for Prediction
    Insurance = ''

    # creating a button for Prediction

    if st.button('Insurance Claim Response'):
        Insurance = Insurance_prediction(
            [Age, Job, Marital, Education_qual, Call_Type, Day, Month, Dur, Num_calls, Prev_outcome])

    st.success(Insurance)


if __name__ == '__main__':
    main()
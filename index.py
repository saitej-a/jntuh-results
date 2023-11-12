
import requests
import streamlit as st
import pandas as pd

import numpy as np
import json

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")
htno=(st.text_input("Enter Hall Ticket Number")).upper()
if st.button('Get Report'):

#htno="21UD1A0555"
    response=requests.post(
    "https://jntuhresults-web-four.vercel.app/api/academicresult?htno={}".format(htno))
    response=response.json()
    details=response['data']["Details"]
    details_df=pd.DataFrame(columns=["Name","Hallticket","Code","Father Name"])
    print(response)
    for i in range(len([details])):
        details_df.loc[i]=[details["NAME"],details["Roll_No"],details["COLLEGE_CODE"],details['FATHER_NAME']]
    st.table(details_df)

    results_df=pd.DataFrame(columns=["Subject Code",'Subject Name',"Internals","Externals","Total",'Grade',"Credits"])

    results1=response['data']["Results"]
    #print(results1["1-1"]["total"])
    k=0
    total=0
    credits=0
    Cgpa=0
    Total=0
    total_s=0
    for i in (results1):

        k=0

        st.header(i)
        if(i=='Total'):
            Total=results1[i]
            st.subheader(Total)
            break
        for j in (results1[i]):
            total_s = (
                        len(
                            results1[
                                i]) - 3)


            if (k<total_s):
                results_df.loc[
                    k] = [
                    results1[
                        i][
                        j][
                        "subject_code"],
                    results1[
                        i][
                        j][
                        "subject_name"],
                    results1[
                        i][
                        j][
                        "subject_internal"],
                    results1[
                        i][
                        j][
                        "subject_external"],
                    results1[
                        i][
                        j][
                        "subject_total"],
                    results1[
                        i][
                        j][
                        "subject_grade"],
                    results1[
                        i][
                        j][
                        "subject_credits"]]
                k = k + 1

            elif(k>=total_s):

                if (j == 'total'):
                    total = str(results1[i][j])

                if (j == 'credits'):
                    credits = str(
                        results1[
                            i][
                            j])

                if (j == 'CGPA'):
                    k=0
                    Cgpa = results1[
                        i][
                        j]


                    break






        st.table(results_df)
        results_df = pd.DataFrame(
            columns=[
                "Subject Code",
                'Subject Name',
                "Internals",
                "Externals",
                "Total",
                'Grade',
                "Credits"])

        st.write(
            "Total = ",
            total)
        st.write("Credits = ",credits)

        st.write("Cgpa = ",Cgpa)


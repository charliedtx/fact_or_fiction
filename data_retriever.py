import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly as py

dhs = {
    'table1':pd.read_excel("data/fy_data/fy2017_table1.xlsx", header=3, skipfooter=2, na_values=['-','D']),
    'table2':pd.read_excel("data/fy_data/fy2017_table2.xlsx",header=3 ,skipfooter=24, na_values=['-','D']),
    'table3':pd.read_excel("data/fy_data/fy2017_table3d.xlsx",header=3 ,skipfooter=6, na_values=['-','D']),
    'table4':pd.read_excel("data/fy_data/fy2017_table4.xlsx",header=3, skipfooter=3, na_values=['-','D']),
    'table5':pd.read_excel("data/fy_data/fy2017_table5.xlsx", header=3, skipfooter=2, na_values=['-','D']),
    'table6':pd.read_excel("data/fy_data/fy2017_table6.xlsx",header=3, skipfooter=4, na_values=['-','D']),
    'table7':pd.read_excel("data/fy_data/fy2017_table7d.xlsx",header=3, skipfooter=3, na_values=['-','D']),
    'table8':pd.read_excel("data/fy_data/fy2017_table8.xlsx",header=3, skipfooter=2, na_values=['-','D']),
    'table9':pd.read_excel("data/fy_data/fy2017_table9d.xlsx", header=3, skipfooter=3, na_values=['-','D']),
    'table10':pd.read_excel("data/fy_data/fy2017_table10d.xlsx", header=3, skipfooter=4, na_values=['-','D']),
    'table11':pd.read_excel("data/fy_data/fy2017_table11d.xlsx", header=3, skipfooter=4, na_values=['-','D']),
    'table12':pd.read_excel("data/fy_data/fy2017_table12d.xlsx", header=3, skipfooter=4, na_values=['-','D']),
    'table13':pd.read_excel("data/fy_data/fy2016_table13.xls", header=3, skipfooter=2, na_values=['-','D']),
    'table14':pd.read_excel("data/fy_data/fy2016_table14d.xls", header=3, skipfooter=7, na_values=['-','D']),
    'table15':pd.read_excel("data/fy_data/fy2016_table15d.xls", header=3, skipfooter=4, na_values=['-','D']),
    'table16':pd.read_excel("data/fy_data/fy2016_table16.xls", header=3, skipfooter=1, na_values=['-','D']),
    'table17':pd.read_excel("data/fy_data/fy2016_table17d.xls", header=3, skipfooter=5, na_values=['-','D']),
    'table18':pd.read_excel("data/fy_data/fy2016_table18d.xls", header=3, skipfooter=5, na_values=['-','D']),
    'table19':pd.read_excel("data/fy_data/fy2016_table19d.xls", header=3, skipfooter=5, na_values=['-','D']),
    'table20':pd.read_excel("data/fy_data/fy2017_table20.xlsx", header = 5, skipfooter=6, na_values=['-','D']),
    'table21':pd.read_excel("data/fy_data/fy2017_table21d.xlsx", header = 3, skipfooter=6, na_values=['-','D']),
    'table22':pd.read_excel("data/fy_data/fy2017_table22.xlsx", header = 3, skipfooter=3, na_values=['-','D']),
    'table23':pd.read_excel("data/fy_data/fy2017_table23.xlsx", header=4, skipfooter=2, na_values=['-','D']),
    'table24':pd.read_excel("data/fy_data/fy2017_table24.xlsx", header=4, skipfooter=3, na_values=['-','D']),
    'table25':pd.read_excel("data/fy_data/fy2017_table25d.xlsx", header=2, skipfooter=10, na_values=['-','D']),
    'table26':pd.read_excel("data/fy_data/fy2017_table26d.xlsx", header=3, skipfooter=16, na_values=['-','D']),
    'table27':pd.read_excel("data/fy_data/fy2017_table27d.xlsx", header=3, skipfooter=9, na_values=['-','D']),
    'table28':pd.read_excel("data/fy_data/fy2017_table28d.xlsx", header=3, skipfooter=20, na_values=['-','D']),
    'table29':pd.read_excel("data/fy_data/fy2017_table29.xlsx", header=3, skipfooter=8, na_values=['-','D']),
    'table30':pd.read_excel("data/fy_data/fy2017_table30.xlsx", header=3, skipfooter=9, na_values=['-','D']),
    'table31':pd.read_excel("data/fy_data/fy2017_table31.xlsx", header=3, skipfooter=8, na_values=['-','D']),
    'table32':pd.read_excel("data/fy_data/fy2017_table32d.xlsx", header=3, skipfooter=16, na_values=['-','D'])
    }

dhs_descriptions = {
    "table1":"Persons Obtaining Lawful Permanent Resident Status: Fiscal Years 1820 to 2017",
    "table2":"Persons Obtaining Lawful Permanent Resident Status by Region and Selected Country of Last Residence: Fiscal Years 2015 to 2017",
    "table3":"Persons Obtaining Lawful Permanent Resident Status by Region and Country of Birth: Fiscal Years 2015 to 2017",
    "table4":"Persons Obtaining Lawful Permanent Resident Status by State or Territory of Residence: Fiscal Years 2015 to 2017",
    "table5":"Persons Obtaining Lawful Permanent Resident Status by Core Based Statistical Area (CBSA) of Residence: Fiscal Years 2015 to 2017",
    "table6":"Persons Obtaining Lawful Permanent Resident Status by Type and Major Class of Admission: Fiscal Years 2015 to 2017",
    "table7":"Persons Obtaining Lawful Permanent Resident Status by Type and Detailed Class of Admission: Fiscal Year 2017",
    "table8":"Persons Obtaining Lawful Permanent Resident Status by Sex, Age, Marital Status, and Occupation: Fiscal Year 2017",
    "table9":"Persons Obtaining Lawful Permanent Resident Status by Broad Class of Admission and Selected Demographic Characteristics: Fiscal Year 2017",
    "table10":"Persons Obtaining Lawful Permanent Resident Status by Broad Class of Admission and Region and Country of Birth: Fiscal Year 2017",
    "table11":"Persons Obtaining Lawful Permanent Resident Status by Broad Class of Admission and Region and Country of Last Residence: Fiscal Year 2017",
    "table12":"Immigrant Orphans Adopted by U.S. Citizens by Sex, Age, and Region and Country of Birth: Fiscal Year 2017",
    "table13":"Refugee Arrivals: Fiscal Years 1980 To 2016",
    "table14":"Refugee Arrivals By Region And Country Of Nationality: Fiscal Years 2014 To 2016",
    "table15":"Refugee Arrivals By Relationship To Principal Applicant And Sex, Age, And Marital Status: Fiscal Year 2016",
    "table16":"Individuals Granted Asylum Affirmatively Or Defensively: Fiscal Years 1990 To 2016",
    "table17":"Individuals Granted Asylum Affirmatively By Region And Country Of Nationality: Fiscal Years 2014 To 2016",
    "table18":"Individuals Granted Asylum Affirmatively By Relationship To Principal Applicant And Sex, Age, And Marital Status: Fiscal Year 2016",
    "table19":"Individuals Granted Asylum Defensively By Region And Country Of Nationality: Fiscal Years 2014 To 2016",
    "table20":"Petitions for Naturalization Filed, Persons Naturalized, and Petitions for Naturalization Denied: Fiscal Years 1907 to 2017",
    "table21":"Persons Naturalized by Region and Country of Birth: Fiscal Years 2015 to 2017",
    "table22":"Persons Naturalized by State or Territory of Residence: Fiscal Years 2015 to 2017",
    "table23":"Persons Naturalized by Core Based Statistical Area (CBSA) of Residence: Fiscal Years 2015 to 2017",
    "table24":"Persons Naturalized by Sex, Age, Marital Status, and Occupation: Fiscal Year 2017",
    "table25":"Nonimmigrant Admissions by Class of Admission: Fiscal Years 2015 to 2017",
    "table26":"Nonimmigrant Admissions (I-94 Only) by Region and Country of Citizenship: Fiscal Years 2015 to 2017",
    "table27":"Nonimmigrant Admissions (I-94 Only) by Region and Country of Residence: Fiscal Years 2015 to 2017",
    "table28":"Nonimmigrant Admissions (I-94 Only) by Selected Category of Admission and Region and Country of Citizenship: Fiscal Year 2017",
    "table29":"Nonimmigrant Admissions (I-94 Only) by Selected Category of Admission, Age, And Sex: Fiscal Year 2017",
    "table30":"Nonimmigrant Admissions (I-94 Only) by Selected Category of Admission and State or Territory of Destination: Fiscal Year 2017",
    "table31":"Nonimmigrant Admissions (I-94 Only) by Selected Category of Admission and Month of Arrival: Fiscal Year 2017",
    "table32":"Nonimmigrant Temporary Worker Admissions (I-94 Only) by Region and Country of Citizenship: Fiscal Year 2017"
}

bp = {
    'table1': pd.read_csv("./data/clean_data/bp_apps-yearly-apprehensions.csv")
}
bp_descriptions = {
    'table1':"Yearly Apprehensions"
}

def get_dhs_data_by_table_number(table_number):
    return dhs.get(f'table{table_number}')

def get_dhs_description_by_table_number(table_number):
    return dhs_descriptions.get(f'table{table_number}')

def get_bp_data_by_table_number(table_number):
    return bp.get(f'table{table_number}')

def get_bp_description_by_table_number(table_number):
    return bp_descriptions.get(f'table{table_number}')
'''
Name: Main file for HW1 of FE 595
Intro: This file should scrape the characters off theyfightcrime.org and save the males in one file and the females in
another.
Author: William Long
Date : 09/22/2019
'''

import pandas as pd
import numpy as np
import requests
import re
import time

# 1st, we need to make the function to get our text.

def getcrimetext():
    '''This should get the text from theyfightcrime.org and then return the male and female character info.
     Inputs:
     None
     Outputs:
     2-List: List of character info.
     '''
    get_resp = requests.get('https://theyfightcrime.org/')
    crime_group = re.search('(He\'s.*crime!)', get_resp.text)
    male_group = re.search("(He's.*?She's)", crime_group.group(0))
    female_group = re.search("(She.*?They fight)", crime_group.group(0))
    male_text1 = male_group.group(0).replace("He's ", "")
    male_text = male_text1.replace(" She's", "")
    female_text1 = female_group.group(0).replace("She's ", "")
    female_text = female_text1.replace(" They fight", "")
    text_list = [male_text, female_text]
    return text_list

# Now, we need to do this 50 times.
def getcharlist(N):
    '''This should do getcrimetext() N times and return the info as a dataframe.
    Inputs:
    N: Int, the number of times we get the data
    Output:
    Dataframe: This should be the char info.
    '''
    male = []
    female = []
    for i in range(0, N):
        time.sleep(0.01) # This should stop us from overloading the site.
        x = getcrimetext()
        male.append(x[0])
        female.append(x[1])
    chdata = {'Male': male, 'Female': female}
    charlist = pd.DataFrame(data=chdata)
    #charlist = [male, female]
    return charlist

'''
def whydoIhaveto(N):
    
    male = []
    female = []
    m = N//10
    r = N - m * 10
    for i in range(0, m):
        char = getcharlist(10)
        male.extend(char[0])
        female.extend(char[1])
'''





'''
get_resp = requests.get('https://theyfightcrime.org/')
crime_group = re.search('(He\'s.*crime!)', get_resp.text)
male_group = re.search("(He's.*?\\.)", crime_group.group(0))
female_group = re.search("(She's.*?\\.)", crime_group.group(0))
male_text = male_group.group(0).replace("He's ", "")
female_text = female_group.group(0).replace("She's ", "")
text_list = [male_text, female_text]

text_list = getcharlist(15)
print(text_list)
'''


if __name__=="__main__":


    N = 50
    charlist = getcharlist(N)



    charlist.to_csv(r'Male_data.csv', columns=['Male'])
    charlist.to_csv(r'Female_data.csv', columns=['Female'])




    print(charlist)


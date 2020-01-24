__author__ = 'Akhil Jha'

import pandas

in_file = input("Enter name of the input file (with extension): ")
eid_file = input("Enter name of the file with Emp ID: ")
managerName = input("Enter Manager's Name: ")
outputFile = input("Enter output file name: ")

dataFrame = pandas.read_csv(in_file)

file = open(eid_file,"r")
eidList = []
for eid in file.readlines():
    eidList.append(eid)


dataFrame.Name = dataFrame.Name.str.split("(",expand=True)

dataFrameEid=pandas.DataFrame(eidList,columns=["Eid"])

dataFrameEid = dataFrameEid["Eid"].fillna(0).astype(int)
NewDataFrame = dataFrame[["Eid","APAC","EMEA","WH - India"]].fillna(0).astype(int)
NewDataFrame.insert(1,"Name",dataFrame.Name)
intersection_dataframe = pandas.merge(dataFrameEid, NewDataFrame, how='inner', on='Eid')
intersection_dataframe.insert(2,"Manager Name", managerName)
intersection_dataframe.to_csv("~/Desktop/FinalReport.csv")

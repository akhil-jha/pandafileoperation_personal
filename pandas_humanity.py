__author__ = 'Akhil Jha, Apoorva Jagtap and Arpit Jain'

import pandas

in_file = input("Enter name of the input file (with extension): ")

outputFile = input("Enter output file name: ")

dataFrame = pandas.read_csv(in_file)


dataFrame.Name = dataFrame.Name.str.split("(",expand=True)

dataFrame = dataFrame[["Eid","Name","APAC","EMEA","WH - India"]].fillna({'Eid':''})
dataFrame = dataFrame[dataFrame.Name != 'Total']
# NewDataFrame.insert(1,"Name",dataFrame.Name)
# intersection_dataframe = pandas.merge(dataFrameEid, NewDataFrame, how='inner', on='Eid')
dataFrame.index = dataFrame.index + 1

dataFrame.to_csv("~/Desktop/{}.csv".format(outputFile))
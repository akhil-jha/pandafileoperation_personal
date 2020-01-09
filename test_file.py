import pandas

dataFrame = pandas.read_csv('1000 Sales Records.csv')
pandas.set_option('display.max_rows', None)           # \
pandas.set_option('display.max_columns', None)        #  To display the entire output on the console. By some are hidden due to screen size buffer.
pandas.set_option('display.width', None)              # /
pandas.set_option('display.max_colwidth', -1)         #/

dataFrame.index = dataFrame.index+1 # By default the indexing starts from 0. This changes it and make it start from 1. PS Better viewing
print(dataFrame.fillna({'Country': 'Bhutan','Item Type':'Clothes','Order Priority':'M'})) # fills NaN with desired value, and printing
# Check pandas docs for other attributes. Interpolate(method = '<>')


# print(dataFrame) #printing the dataframe

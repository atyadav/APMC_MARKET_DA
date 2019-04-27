#import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

#Reading CSV file
df=pd.read_csv('New.csv')
#,names=['MARKET_NAME','Arrival_Date','Arrivals_Tonnes'])

#df.drop(['Variety','MinPrice_PerQuintal'],axis=1)
#print(df.shape[0])
#print(df.columns.tolist())
#print(df.head)

df.replace(' ', np.nan, inplace=True)
filtered_df = df[df['Arrivals_Tonnes'].notnull()]
filtered_df=filtered_df['Arrivals_Tonnes'].dropna()
#print(filtered_df.shape[0])
#print(filtered_df.head())
#filtered_df.to_csv('out.csv')

#Drop rows with any empty cells
#df=df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
#print(df.shape[0])

#Print Market Names
df_Market=df['MARKET_NAME'].dropna().unique()
#df_Market.insert(0,"Entries",'Any Value')
#print(df)

#Number of Markets 
shape_Market = df_Market.shape
print("Number of Markets= {}\n".format(shape_Market[0]))

#print(df.dtypes)

#for c in df.columns:
df['Arrivals_Tonnes'] = pd.to_numeric(df['Arrivals_Tonnes'], errors='coerce')
#print(df.dtypes)

grouped= df.groupby('MARKET_NAME')
#print(grouped.groups)
print(grouped['Arrivals_Tonnes'].agg(np.mean))

Arrivals=grouped['Arrivals_Tonnes'].agg(np.mean)
#Arrivals.to_csv('arrivals.csv')
Arrivals.dropna(inplace = True) 
plt.figure()
Arrivals.plot.bar()
plt.show()

#df_New= filtered_df.groupby['MARKET_NAME'].mean()[['Arrivals_Tonnes']]

#.mean()[['Arrivals_Tonnes']]
#print(df_New.head(5))

# empty list
#myList = []
# printing the list using loop 
#for x in range(len(df_Market)):
	#print(df_Market[x])
	#Work with one market
	#Market equals to one Market
	#print(df_Market[x])
	#is_Market=df['MARKET_NAME']==df_Market[x]
	#print(is_Market)
	#df_OneMarket=df[is_Market]
	#df_Market_x =df[df['MARKET_NAME']==df_Market[x]]
#	df_New= df_Market_x.groupby('MARKET_NAME').mean()[['Arrivals_Tonnes]]
	#print(df_Market_x.Arrivals_Tonnes.sum)
	#print(df_Market_x.sum)
	#print(df_OneMarket)
	# number of entries in market
	#print("{}									 {}".format(df_Market[x],df_Market_x.shape[0]))
	#Assign number of entries into Market df
	#myList.append(df_OneMarket.shape[0])

#df_New= df.groupby('MARKET_NAME').mean()
#[['Arrivals_Tonnes']]
#print(df_New)
#print(len(myList))
#df_Market=df_Market.assign('Entries'=myList)
#df_Market(1,"Entries",myList,True)
#df_Market['Entries']='Any Value'
#Find Biggest Market

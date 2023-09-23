import pandas as pd

import matplotlib.pyplot as plt

tata_motors=pd.read_csv("C:/Users/ROHIT/Downloads/stock/TATAMOTORS.csv")
tata_steel=pd.read_csv("C:/Users/ROHIT/Downloads/stock/TATASTEEL.csv")
tcs=pd.read_csv("C:/Users/ROHIT/Downloads/stock/TCS.csv")
tata_motors.shape


tata_motors.info()



tata_motors.isna().sum()


tata_motors.duplicated().sum()

tata_steel.duplicated().sum()

tcs.duplicated().sum()


tata_motors.describe().round(2)


tata_motors["Date"]=pd.to_datetime(tata_motors["Date"])
tata_steel["Date"]=pd.to_datetime(tata_steel["Date"])
tcs["Date"]=pd.to_datetime(tcs["Date"])


tata_motors=tata_motors.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1)
tata_steel=tata_steel.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1)
tcs=tcs.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1)


tata_motors['Month']=tata_motors["Date"].dt.month

tata_motors['Year']=tata_motors["Date"].dt.year

tata_motors['Day']=tata_motors["Date"].dt.day


tata_steel['Month']=tata_steel["Date"].dt.month

tata_steel['Year']=tata_steel["Date"].dt.year

tata_steel['Day']=tata_steel["Date"].dt.day


tcs['Day']=tcs['Date'].dt.day

tcs['Year']=tcs['Date'].dt.year

tcs['Month']=tcs['Date'].dt.month


plt.figure(figsize=(20,7))

plt.plot(tata_motors['Date'],tata_motors['Open'],color='blue',label='Tata Motors')

plt.plot(tata_steel['Date'],tata_steel['Open'],color='grey',label='Tata Steel')

plt.plot(tcs['Date'],tcs['Open'],color='orange',label='TCS')


plt.title("Relation between Tata Motors, Tata Steel and TCS Price")

plt.xlabel("Year")

plt.ylabel("Price")

plt.legend(title="")

plt.show()


plt.figure(figsize=(20,7))

plt.plot(tata_motors['Date'],tata_motors['Volume'],color='blue',label='Tata Motors')

plt.plot(tata_steel['Date'],tata_steel['Volume'],color='grey',label='Tata Steel')

plt.plot(tcs['Date'],tcs['Volume'],color='orange',label='TCS')



plt.title("Relation between Tata Motors, Tata Steel and TCS Volume")

plt.xlabel("Year")

plt.ylabel("Volume")

plt.legend(title="")

plt.show()


sumTM=0 #total amount invested in Tata Motors

s1=0 #number of shares owned by Tata Motors

#calcuating total amount invested and number of shares owned in Tata Motors

for i in range(len(tata_motors)):

    if tata_motors.loc[i,'Day']==30:

        sumTM+=tata_motors.loc[i,'Open']

        s1+=1

#displaying basic results

print("Total Invested in Tata Motors = Rs",round(sumTM,2))

print("Shares Owned of Tata Motors =",s1)

print("Average Investmentment of 1 share = Rs",round((sumTM/s1),2))



tm_end=298.2 #last open price of Tata Motors on 2021-04-30

#obtained by looking at the data or can be seen after executing tata_motors.tail()

#calculating investment results

result1=round((tm_end*s1)-sumTM,2)

roiTM=round((result1/sumTM)*100,2)


#displaying investment results

print("nInvestment Result:")


if result1<0:

    print("Net Unrealised Loss = Rs",result1)

else:

    print("Net Unrealised Profit = Rs",result1)



print("Tata Motors ROI from 2000-1-3 to 2021-04-30 =",roiTM,"%")


# In[14]:


sumTS=0 #total amount invested in Tata Steel

s2=0 #number of shares owned by Tata Steel

#calcuating total amount invested and number of shares owned in Tata Steel

for i in range(len(tata_steel)):

    if tata_steel.loc[i,'Day']==30:

        sumTS+=tata_steel.loc[i,'Open']

        s2+=1


#displaying basic results

print("Total Invested in Tata Steel = Rs",round(sumTS,2))

print("Shares Own of Tata Steel =",s2)

print("Average Investmentment of 1 share = Rs",round((sumTS/s2),2))



ts_end=1024 #last open price of Tata Steel on 2021-04-30

#obtained by looking at the data or can be seen after executed tata_steel.tail()


#calculating investment results

result2=round((ts_end*s2)-sumTS,2)

roiTS=round((result2/sumTS)*100,2)



#displaying investment results

print("nInvestment Result:")



if result2<0:

    print("Net Unrealised Loss = Rs",result2)

else:

    print("Net Unrealised Profit = Rs",result2)

print("Tata Steel ROI from 2000-1-3 to 2021-04-30 =",roiTS,"%")


# In[15]:


sumTCS=0 #total amount invested in TCS

s3=0 #number shares owned of TCS




#calcuating total amount invested and number of shares owned in TCS

for i in range(len(tcs)):

    if tcs.loc[i,'Day']==30:

        sumTCS+=tcs.loc[i,'Open']

        s3+=1




#displaying basic results

print("Total Invested in TCS = Rs",round(sumTCS,2))

print("Shares Owned of TCS =",s3)

print("Average Investmentment of 1 share = Rs",round((sumTCS/s3),2))




tcs_end=3099 #last open price of TCS on 2021-04-30

#obtained by looking at the data or can be seen after executed tcs.tail()




#calculating investment results

result3=round((tcs_end*s3)-sumTCS,2)

roiTCS=round((result3/sumTCS)*100,2)




#displaying investment results

print("nInvestment Result:")




if result3<0:

    print("Net Unrealised Loss = Rs",result3)

else:

    print("Net Unrealised Proift = Rs",result3)




print("Tata Steel ROI from 2004-08-25 to 2021-04-30 =",roiTCS,"%")


# In[16]:


plt.figure(figsize=(5,7))

stock=['Tata Motors','Tata Steel','TCS']

amt=[result1,result2,result3]

col=['Blue','Grey','Orange']




plt.bar(stock,amt,color=col)




plt.title("Profit/Loss")

plt.xlabel("Stocks")

plt.ylabel("Amount")


plt.figure(figsize=(5,7))

stock=['Tata Motors','Tata Steel','TCS']

shares=[s1,s2,s3]

col=['Blue','Grey','Orange']



plt.pie(shares,labels=stock,autopct="%1.2f%%",colors=col)

plt.legend(title="",loc="upper left")

plt.title("Portfolio Allocation")



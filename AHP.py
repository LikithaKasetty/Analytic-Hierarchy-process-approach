import pandas
import streamlit as st

#Analytic Hierarchy process approach(AHP)
#Goal: Buying a wallet
#Attributes: Price, size, brand, look
#Alternatives: wallet1, wallet2, wallet3, wallet4

#Create a list of attributes and Alternatives
att = ["price", "size", "brand", "look"]
alt = ["wallet1","wallet2","wallet3","wallet4"]

w, h = 4, 4
#creating two-d array
arr = [[0 for x in range(w)] for y in range(h)]

#To display saaty's scale
scale = pandas.read_csv('saaty_table.csv')
print(scale)

#Create a matrix to compare the attributes
for i in range(len(alt)):
  for j in range(len(att)):
    if i == j:
      arr[i][j] = 1
    elif j > i:
      arr[i][j] = int(input("How important {} is wrt {}".format(att[i],att[j])))
      arr[j][i] = 1/ arr[i][j]
    else:
      pass

#Normalise and find the weight of each attribute
sum = [0] * 4
for j in range(len(att)):
  for i in range(len(att)):
    sum[j] += arr[i][j]

for j in range(len(att)):
  for i in range(len(att)):
    arr[i][j] = arr[i][j] / sum[j]

weight = [0] * 4
for j in range(len(att)):
  for i in range(len(att)):
    weight[j] = (weight[j] + arr[j][i])
  weight[j] = weight[j]/4

#print the attribute of maximum value
max_weight = max(weight)
ind = weight.index(max_weight)
print("Maximum weight is {} corresponds to the attibute {}".format(max_weight,att[ind]))

#assigning weightage to attributes
brand_dict ={"Gucci": "1","MichealKors":"3","Fossil":"2","LV": "1" }
look_dict ={"regular":"2","bad":"1","good":"3"}
size_dict={"medium":"2","big":"3","small":"1"}

#Converting the attributes to corresponding weightage
lst1 =[]
df = pandas.read_csv('att_vs_alt.csv')
for index, row in df.iterrows():
  n = str(row[att[ind]])
  if att[ind] == "look":
    lst1.append(int(look_dict[n]))
  elif att[ind] == "brand":
    lst1.append(int(brand_dict[n]))
  elif att[ind] == "size":
    lst1.append(int(size_dict[n]))
  else:
    lst1.append(int(row['price']))

st.title("Analytic Hierarchy Process Approach (AHP)")
st.subheader("#Goal : Buying a wallet  #Attributes: Price, brand, size, look  #Alternatives: wallet1, wallet2, wallet3, wallet4")
st.write("Below is the table and graph of maximum weight attribute vs Alternatives")

df = pandas.DataFrame({
#creating a dictionary
'Alternatives' : ['wallet_1', 'wallet_2', 'wallet_3', 'wallet_4'],
att[ind] : lst1})
st.write(df)
st.bar_chart(df)





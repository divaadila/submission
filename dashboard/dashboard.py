import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("day.csv")
st.title("Dashboard Penyewaan Sepeda")

st.subheader("Perbandingan Pengguna Casual dan Registered")
total_casual = data['casual'].sum()
total_registered = data['registered'].sum()
labels = ['Casual', 'Registered']
total_users = [total_casual, total_registered]

plt.figure(figsize=(8, 5))
sns.barplot(x=labels, y=total_users, color='blue')
plt.title('Perbandingan Pengguna Casual dan Registered')
plt.ylabel('Jumlah Penyewaan')
plt.xlabel('Tipe Pengguna')
plt.ylim(0, max(total_users) * 1.1)
st.pyplot(plt)

years = ['2011', '2012']
total_rentals = [1243103, 2049576]
plt.figure(figsize=(8, 5))
sns.lineplot(x=years, y=total_rentals, marker='o', color='blue')
plt.title('Peningkatan Penyewaan Sepeda dari 2011 ke 2012')
plt.ylabel('Total Penyewaan')
plt.xlabel('Tahun')
plt.xticks(years)
plt.ylim(0, max(total_rentals) * 1.1)
st.pyplot(plt) 
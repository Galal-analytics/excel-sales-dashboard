import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# عنوان التطبيق
st.title("Excel Sales Analysis Dashboard")

# قراءة ملف Excel
df = pd.read_excel("sales_data.xlsx")

# حساب إجمالي المبيعات
df["Total"] = df["Quantity"] * df["Price"]
total_sales = df["Total"].sum()

# أعلى منتج
top_product = df.groupby("Product")["Total"].sum().idxmax()

# أفضل مدينة
top_city = df.groupby("City")["Total"].sum().idxmax()

# عرض النتائج
st.subheader("Key Metrics")
st.write("Total Sales:", total_sales)
st.write("Top Product:", top_product)
st.write("Best City:", top_city)

# رسم بياني للمبيعات حسب المنتج
st.subheader("Sales by Product")

sales_by_product = df.groupby("Product")["Total"].sum()

fig, ax = plt.subplots()
sales_by_product.plot(kind="bar", ax=ax)

st.pyplot(fig)
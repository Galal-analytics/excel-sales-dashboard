import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Excel Sales Analysis Dashboard")

# رفع الملف
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # حساب الإجمالي
    df["Total"] = df["Quantity"] * df["Price"]

    total_sales = df["Total"].sum()
    top_product = df.groupby("Product")["Total"].sum().idxmax()
    top_city = df.groupby("City")["Total"].sum().idxmax()

    # عرض KPIs بشكل احترافي
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Sales", f"{total_sales:,.0f}")
    col2.metric("Top Product", top_product)
    col3.metric("Top City", top_city)

    # الرسم البياني
    st.subheader("Sales by Product")

    sales_by_product = df.groupby("Product")["Total"].sum()

    fig, ax = plt.subplots()
    sales_by_product.plot(kind="bar", ax=ax)
    st.pyplot(fig)

    # عرض البيانات
    st.subheader("Data Preview")
    st.dataframe(df)
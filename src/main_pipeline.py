# B. Please propose and design a system and its components to deploy this model in production.
# With schematic representation and written description.

import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt

true_data = pd.read_csv("src/csv_files/Spotawheel_case_study.csv")

with open("src/data.pkl", "rb") as data:
    X_train, X_test, y_train, y_test, y_pred = pickle.load(data)

with open("src/model.pkl", "rb") as md:
    model = pickle.load(md)

st.text("Original data")
st.dataframe(data=true_data)

st.text('Labels of data')
chart = st.line_chart(true_data["Price"])

st.text('Labels of data in distribution')
hist_values = np.histogram(true_data["Price"].values, bins=200)[0]
st.bar_chart(hist_values)

st.text('Log labels of data in distribution')
hist_values2 = np.histogram(np.log(true_data["Price"].values, ), bins=200)[0]
st.bar_chart(hist_values2)


st.text('prediction results')

st.text("validation MAE %s" % mean_absolute_error(np.exp(y_pred), np.exp(y_test)))
st.text("validation explained variance: r2 ,%s" % r2_score(y_pred, y_test))
st.text("validation mean squared error %s " % mean_squared_error(np.exp(y_pred), np.exp(y_test)))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(
    y_test,
    y_pred,
)

ax.set_xlabel("actual")
ax.set_ylabel("predictions")

st.write(fig)


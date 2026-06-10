import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

df = pd.read_csv("Superstore_Sales/data/SuperStoreOrders.csv")

print(df.head(10))
from random import seed
import pandas as pd
import sqlite3
from setting import Setting
import numpy as np
import glob
from pprint import pprint as pp

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import xgboost as xgb


s = Setting()
db_list = glob.glob("db/*.db")

db_list = glob.glob("db/*.db")
df = pd.DataFrame()
for i in db_list:
    with sqlite3.connect(i) as conn:
        d = pd.read_sql('select * from features30', con=conn)  # ここで窓選ぶ
        df = pd.concat([df, d])

df = df.drop(["id", "id_count", "timestamp_from", "timestamp_to", "blinkSpeed_min",
             "blinkStrength_min", "eyeMoveUp_min", "eyeMoveDown_min", "eyeMoveLeft_min", "eyeMoveRight_min"], axis=1)
df = df.sample(frac=1, random_state=0)
features = df.drop(["label"], axis=1).values
target = df["label"].values.astype("int")


model = xgb.XGBClassifier(random_state=0)

# ここから実装して書く！
arr = np.ndarray([])
fi = {}

model.fit(features, target)

imp = model.feature_importances_
for i, c in zip(imp, df.columns):
    if(i != 0):
        fi[c] = np.round(i, 3)

s = sorted(fi.items(), key=lambda i: i[1], reverse=True)

np.set_printoptions(suppress=True)
pp(s)

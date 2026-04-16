import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

# LOAD DATA
df = pd.read_csv(
    "bank-additional-full-1.csv",
    sep=';',
    engine='python',
    quoting=3
)

# CLEAN COLUMN NAMES
df.columns = df.columns.str.replace('"', '').str.strip()

# SELECT FEATURES
selected_cols = ['age','job','housing','loan','poutcome','campaign']
df = df[selected_cols + ['y']]

# 🔥 CLEAN VALUES (VERY IMPORTANT FIX)
for col in df.columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace('"','')
        .str.replace('.','')
    )

# REMOVE INVALID TARGET
df = df[df['y'].isin(['yes','no'])]

print("Cleaned shape:", df.shape)

# ENCODING
encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# SPLIT
x = df[selected_cols]
y = df['y']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# TRAIN
model = RandomForestClassifier()
model.fit(x_train, y_train)

# SAVE
pickle.dump(model, open("train.pkl","wb"))
pickle.dump(encoders, open("encoders.pkl","wb"))

print("✅ MODEL TRAINED SUCCESSFULLY")
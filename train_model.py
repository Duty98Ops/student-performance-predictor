import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

# Load data mentah
df = pd.read_csv('data/StudentsPerformance.csv')

# Buat fitur baru dan label
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
df['Passed'] = df['average_score'].apply(lambda x: 1 if x >= 60 else 0)

# Mapping data kategorik ke label original (bukan yang versi Indonesia)
# agar pipeline tetap sinkron saat digunakan di app.py
X = df[[  
    'gender',
    'race/ethnicity',
    'parental level of education',
    'lunch',
    'test preparation course',
    'math score',
    'reading score',
    'writing score'
]]
y = df['Passed']

# Preprocessing
cat_features = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
], remainder='passthrough')

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Split & train
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# Simpan model pipeline
os.makedirs('model', exist_ok=True)
joblib.dump(pipeline, 'model/pipeline.pkl')
print("✅ Model pipeline disimpan ulang ke model/pipeline.pkl")

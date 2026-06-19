import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(
    "data/merged_attendance.csv"
)

df["Target"] = df["Eligibility"].map(
    {
        "Eligible":1,
        "Not Eligible":0
    }
)

X = df[
    [
        "Present_Days",
        "Total_Days",
        "Attendance_Percentage"
    ]
]

y = df["Target"]

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train,y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("Accuracy:",accuracy)

pickle.dump(
    model,
    open(
        "models/eligibility_model.pkl",
        "wb"
    )
)

print("Model Saved")
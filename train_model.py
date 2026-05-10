import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv('dataset.csv')

# Features and labels
X = df['url']
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ML Pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', RandomForestClassifier())
])

# Train model
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Save model
joblib.dump(model, 'phishing_model.pkl')

print('Model trained successfully!')
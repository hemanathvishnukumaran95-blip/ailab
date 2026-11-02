# AI Cattle Health Monitoring System
# Using Decision Tree Algorithm

from sklearn.tree import DecisionTreeClassifier

# Training data
# [Temperature, Heart Rate, Activity]
X = [
    [38.5, 70, 80],
    [38.7, 75, 75],
    [38.9, 72, 85],
    [39.0, 78, 70],
    [40.2, 95, 30],
    [40.5, 100, 20],
    [40.8, 105, 15],
    [41.0, 110, 10]
]

# 0 = Healthy, 1 = Abnormal
y = [0, 0, 0, 0, 1, 1, 1, 1]

# Create and train AI model
model = DecisionTreeClassifier()
model.fit(X, y)

print("===================================")
print("   AI CATTLE HEALTH MONITORING")
print("===================================")

# Get sensor values
temperature = float(input("Enter body temperature (°C): "))
heart_rate = float(input("Enter heart rate (BPM): "))
activity = float(input("Enter activity level (0-100): "))

# Prediction
data = [[temperature, heart_rate, activity]]
prediction = model.predict(data)

# Display result
print("\n----------- AI ANALYSIS -----------")

if prediction[0] == 0:
    print("Health Status : HEALTHY")
    print("Alert         : No abnormal condition detected")
else:
    print("Health Status : ABNORMAL")
    print("Alert         : Health check required!")

print("-----------------------------------")

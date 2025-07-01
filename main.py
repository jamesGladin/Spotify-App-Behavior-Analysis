import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\gladi\Downloads\spotify_user_behavior_sample.csv")

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Retention metric approximation: Daily active users (DAU)
daily_active = df.groupby('date')['user_id'].count()
daily_active.plot(title='Daily Active Users')
plt.xlabel('Date')
plt.ylabel('Users')
plt.tight_layout()
plt.show()

# Engagement: Average session time
print("Average session duration (min):", df['session_duration_min'].mean())

# A/B Test Simulation: Premium vs Free - Average Session Duration
premium = df[df['is_premium'] == 1]['session_duration_min']
free = df[df['is_premium'] == 0]['session_duration_min']
print("Premium Mean:", premium.mean())
print("Free Mean:", free.mean())

# Boxplot comparison
sns.boxplot(data=df, x='is_premium', y='session_duration_min')
plt.xticks([0, 1], ['Free', 'Premium'])
plt.title("Session Duration Comparison")
plt.show()

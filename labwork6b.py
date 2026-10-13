import pandas as pd
import matplotlib.pyplot as plt

data = {
    'math': [85, 90, 78, 92, 65, 70, 88],
    'python': [90, 82, 85, 95, 72, 68, 91],
    'db': [78, 88, 80, 89, 60, 75, 84]
}
df = pd.DataFrame(data)

plt.figure(figsize=(6, 5))
plt.scatter(df['math'], df['python'], color='blue', label='Math vs Python')
plt.scatter(df['math'], df['db'], color='red', label='Math vs DB')
plt.title('Student Scores Scatter Plot')
plt.xlabel('Math Score')
plt.ylabel('Other Course Scores')
plt.legend()
plt.tight_layout()
plt.savefig('scattered.png')
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

df['math'].plot(kind='hist', ax=axes[0], title='Math Marks', color='skyblue', edgecolor='black')
axes[0].set_xlabel('Marks')

df['python'].plot(kind='hist', ax=axes[1], title='Python Marks', color='lightgreen', edgecolor='black')
axes[1].set_xlabel('Marks')

df['db'].plot(kind='hist', ax=axes[2], title='DB Marks', color='salmon', edgecolor='black')
axes[2].set_xlabel('Marks')

plt.tight_layout()
plt.savefig('histo.png')
plt.close()

plt.figure(figsize=(6, 5))
df[['math', 'python', 'db']].boxplot()
plt.title('Box Plot for Math, Python, DB')
plt.ylabel('Marks')
plt.tight_layout()
plt.savefig('box.png')
plt.close()

print("Đã tạo và lưu thành công 3 file: scattered.png, histo.png, box.png!")s
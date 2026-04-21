import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df2 = pd.read_csv("4laptops.csv")

# Define properties properly
flierprops = dict(marker='o', markerfacecolor='red', markersize=5)
meanprops = dict(marker='D', markerfacecolor='blue', markersize=6)

# Boxplot 1
plt.boxplot(df2["Screen_size_inches"],
            notch=True,
            vert=False,
            showmeans=True,
            sym="*",
            patch_artist=True,
            widths=0.1,
            flierprops=flierprops,
            meanprops=meanprops)

plt.xlabel('Screen Size (inches)')
plt.ylabel('Distribution')
plt.show()

# Boxplot 2
plt.boxplot(df2['Weight_kg'])
plt.xlabel('Columns')
plt.ylabel('Weight (kg)')
plt.show()

# Seaborn Boxplot 1
sns.boxplot(x=df2['Weight_kg'])
plt.show()

# Seaborn Boxplot 2
sns.boxplot(x=df2['Weight_kg'], y=df2['RAM'])
plt.show()

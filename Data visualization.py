import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("/content/sample_data/SUN.csv")

fig, ax = plt.subplots(3,1,figsize = (18,8))

close = data["Close"]
min = str(data['Close'].min())
mean = str(data['Close'].mean())
max = str(data['Close'].max())

ax1y = data['Close']
ax2y = data['Volume']

date = [i for i in range(1,243)]
date = pd.Series(date)

ax[0].set_title("Interdisplinary Studies Team 1 ")
ax[0].plot(date, close, color='red', label="Close")
ax[0].set_xlabel('days')
ax[0].set_ylabel('Prices (Baht)')
ax[0].legend()

ax[1].set_title("min = "+min[:3]+", mean = "+mean[:3]+", max = "+max[:4])
ax[1].hist(ax1y,color='red',bins = 9,label='Close')
ax[1].set_xlabel('prices')
ax[1].legend()


ax[2].bar(date,ax2y, color='red', label="Volume",width=1)
ax[2].set_xlabel('days')
ax[2].legend()

fig.tight_layout()
plt.show()

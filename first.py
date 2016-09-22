import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

def sayhello():
    print("hello")
    return

def getPercDifs(nums):
    return [100 * (nums[i] / nums[i - 1] - 1) for i in range(1, len(nums))]

snp = pd.read_csv('snp.csv')
lev = pd.read_csv('snpLev.csv')
# print(df)

difsSnp = getPercDifs(snp['Adj Close'])
difsLev = getPercDifs(lev['Adj Close'])

# val mults = snpLevChanges.zip(snpChanges).map {
#     case (lev, reg) if math.abs(lev) <= 0.0001 || math.abs(reg) <= 0.0001 => 0
# case (lev, reg) => lev / reg
# }

mults = list(map(lambda x: x[1] / x[0], zip(difsSnp, difsLev)))

# Create random data with numpy
import numpy as np

N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

print(sorted(mults))

# Plot and embed in ipython notebook!
# plot([go.Scatter(x=df['Date'], y=df['Adj Close'])])

plot(dict(
    data=[
        go.Scatter(
            x=difsSnp,
            y=[2 for i in difsLev],
            name="Target Multiplier"
        ),
        go.Bar(
            x=difsLev,
            y=mults,
            name="Actual Multiplier"
        )
    ],
    layout=dict(
        xaxis=dict(title="Index % Change"),
        yaxis=dict(title="Multiplier (goal of 2)")
    )
))

# plot([
#     go.Bar(
#         x=difsSnp,
#         y=mults,
#     ),
#     # go.Scatter(
#     #     x=snp['Date'],
#     #     y=difsLev
#     # ),
#     # go.Scatter(
#     #     x=snp['Date'],
#     #     y=difsSnp
#     # ),
# ])

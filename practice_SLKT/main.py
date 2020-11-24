# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# scikit-learn ライブラリの読み込み
from sklearn import datasets

# 手書き文字セットを読み込む
digits = datasets.load_digits()

# どのようなデータか、確認してみる
import matplotlib.pyplot as plt
plt.matshow(digits.images[0], cmap="Greys")
plt.show()


# %%
# 手書き文字セットを読み込む
# datas = datasets.load_digits()
# 手書き文字の画像データ
datas = datasets.load_boston()

import pandas as pd
boston = pd.DataFrame(datas.data, columns=datas.feature_names)

# print("aaa")
# import matplotlib.pyplot as plt #matplot: グラフ作成ライブラリ
# plt.title("per capita crime rate by town") #グラフのタイトルを設定（日本語は表示不可）
# plt.hist(datas.data["CRIM"], color = "blue", rwidth = 0.9) #XのCRIMのヒストグラムを生成
# plt.show() #生成したヒストグラムを表示



# %% [markdown]
# ### こうするのか
# 

# %%



# %%



# %%



# %%




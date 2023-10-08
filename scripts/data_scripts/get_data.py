from catboost.datasets import rotten_tomatoes
train, test = rotten_tomatoes()
train.to_csv("train.csv", index=False)
test.to_csv("test.csv", index=False)

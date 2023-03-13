import matplotlib.pyplot as plt
import japanize_matplotlib

x1 = [0, 1, 2, 3]
x2 = [0.3, 1.3, 2.3, 3.3]
x = ["XGBoost", "RandomForest", "AdaBoost", "SVC"]
y_acc = [0.885, 0.878, 0.769, 0.666]
y_auc = [0.945, 0.946, 0.843, .725]

fig = plt.figure()

plt.bar(x1, y_acc, color="blue", label="Accuracy",
        width=0.3, alpha=0.5)
plt.bar(x2, y_auc, color="green", label="AUC",
        width=0.3, alpha=0.5)

plt.title("Score Comparison")
fig.autofmt_xdate(rotation=60)
fig.tight_layout()
plt.legend()
plt.ylim(bottom=0.5)
plt.ylim(top=1)
plt.xticks([0.25, 1.25, 2.25, 3.25], x)
fig.savefig('test.png', bbox_inches="tight", pad_inches=0.05)
#plt.show()

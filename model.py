import pandas as pd
import sqlite3
import numpy as np
import glob
from pprint import pprint as pp

from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
import xgboost as xgb


# prepare features and target
db_list = glob.glob("db/*.db")
df = pd.DataFrame()
for i in db_list:
    with sqlite3.connect(i) as conn:
        d = pd.read_sql('select * from features30', con=conn)  # ここで窓選ぶ
        df = pd.concat([df, d])

df = df.drop(["id", "id_count", "timestamp_from", "timestamp_to", "blinkSpeed_min",
             "blinkStrength_min", "eyeMoveUp_min", "eyeMoveDown_min", "eyeMoveLeft_min", "eyeMoveRight_min"], axis=1)
df = df.sample(frac=1)
features = df.drop(["label"], axis=1).values
target = df["label"].values.astype("int")


def cross_validation():
    scoring = {"acc": "accuracy",
               "f1": "f1",
               "logloss": "neg_log_loss",
               "auc": "roc_auc"
               }
    estimators = [
        RandomForestClassifier(),
        SVC(probability=True),
        AdaBoostClassifier(),
        xgb.XGBClassifier()
    ]
    for e in estimators:
        print(e.__class__.__name__+":")
        cv = cross_validate(estimator=e, X=features,
                            y=target, scoring=scoring, cv=5)
        for idx, i in enumerate(cv):
            if idx <= 1:
                continue
            print("    {}: {:.3f}".format(i, np.mean(cv[i])))
        print()


def grid_search():
    model = xgb.XGBClassifier(n_estimators=10000)
    params = {
        'subsample': [0.9, 1.0],
        'reg_alpha': [0.1, 0.3],
        'learning_rate': [0.1, 0.3],
        'gamma': [0.05]
    }

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)
    clf = GridSearchCV(estimator=model, param_grid=params,
                       cv=skf, scoring="accuracy", n_jobs=1, verbose=1)
    clf.fit(features, target)

    print("Best score: %.4f" % (clf.best_score_))

    print(clf.best_params_)


def compare_windows():
    scoring = {
        "acc": "accuracy",
        "f1": "f1",
        "logloss": "neg_log_loss",
        "auc": "roc_auc"
    }
    e = xgb.XGBClassifier(seed=0)
    print(e.__class__.__name__+":")
    cv = cross_validate(estimator=e, X=features,
                        y=target, scoring=scoring, cv=5)
    for idx, i in enumerate(cv):
        if idx <= 1:
            continue
        print("    {}: {:.3f}".format(i, np.mean(cv[i])))
    print()


# cross_validation()
# grid_search()
compare_windows()

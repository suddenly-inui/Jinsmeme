import pandas as pd
import sqlite3
from setting import Setting
from database import Database
import glob

db_list = glob.glob("db/*.db")
s = Setting()
for i in db_list:
    print(i)
    with sqlite3.connect(i) as conn:
        df = pd.read_sql('select * from currentData', con=conn)

    #df = df.query(f"label == {m.LABEL}")
    features = pd.DataFrame()
    window = s.WINDOW_SIZE
    n = len(df) // window
    db = Database(i)

    for idx, i in enumerate(range(n+1)):
        d = df[0+(window*i):window+(window*i)]
        stat = d[["blinkSpeed", "blinkStrength", "eyeMoveUp",
                  "eyeMoveDown", "eyeMoveLeft", "eyeMoveRight"]]

        features.loc[idx, "id_count"] = d.id.count()
        features.loc[idx, "timestamp_from"] = d.head(1).iloc[0, 1]
        features.loc[idx, "timestamp_to"] = d.tail(1).iloc[0, 1]

        features.loc[idx, "accx_mean"] = d.accx.mean()
        features.loc[idx, "accx_std"] = d.accx.std()
        features.loc[idx, "accx_max"] = d.accx.max()
        features.loc[idx, "accx_min"] = d.accx.min()

        features.loc[idx, "accy_mean"] = d.accy.mean()
        features.loc[idx, "accy_std"] = d.accy.std()
        features.loc[idx, "accy_max"] = d.accy.max()
        features.loc[idx, "accy_min"] = d.accy.min()

        features.loc[idx, "accz_mean"] = d.accz.mean()
        features.loc[idx, "accz_std"] = d.accz.std()
        features.loc[idx, "accz_max"] = d.accz.max()
        features.loc[idx, "accz_min"] = d.accz.min()

        features.loc[idx, "ptich_mean"] = d.pitch.mean()
        features.loc[idx, "ptich_std"] = d.pitch.std()
        features.loc[idx, "ptich_max"] = d.pitch.max()
        features.loc[idx, "ptich_min"] = d.pitch.min()

        features.loc[idx, "roll_mean"] = d.roll.mean()
        features.loc[idx, "roll_std"] = d.roll.std()
        features.loc[idx, "roll_max"] = d.roll.max()
        features.loc[idx, "roll_min"] = d.roll.min()

        features.loc[idx, "yaw_mean"] = d.yaw.mean()
        features.loc[idx, "yaw_std"] = d.yaw.std()
        features.loc[idx, "yaw_max"] = d.yaw.max()
        features.loc[idx, "yaw_min"] = d.yaw.min()

        features.loc[idx, "blink_count"] = len(
            d) - len(stat[(stat.blinkSpeed == 0) & (stat.blinkStrength == 0)])

        features.loc[idx, "blinkSpeed_mean"] = d.blinkSpeed.mean()
        features.loc[idx, "blinkSpeed_std"] = d.blinkSpeed.std()
        features.loc[idx, "blinkSpeed_max"] = d.blinkSpeed.max()
        features.loc[idx, "blinkSpeed_min"] = d.blinkSpeed.min()

        features.loc[idx, "blinkStrength_mean"] = d.blinkStrength.mean()
        features.loc[idx, "blinkStrength_std"] = d.blinkStrength.std()
        features.loc[idx, "blinkStrength_max"] = d.blinkStrength.max()
        features.loc[idx, "blinkStrength_min"] = d.blinkStrength.min()

        features.loc[idx, "eyeMoveUp_count"] = len(
            d) - len(stat[stat.eyeMoveUp == 0])
        features.loc[idx, "eyeMoveUp_mean"] = d.eyeMoveUp.mean()
        features.loc[idx, "eyeMoveUp_std"] = d.eyeMoveUp.std()
        features.loc[idx, "eyeMoveUp_max"] = d.eyeMoveUp.max()
        features.loc[idx, "eyeMoveUp_min"] = d.eyeMoveUp.min()

        features.loc[idx, "eyeMoveDown_count"] = len(
            d) - len(stat[stat.eyeMoveDown == 0])
        features.loc[idx, "eyeMoveDown_mean"] = d.eyeMoveDown.mean()
        features.loc[idx, "eyeMoveDown_std"] = d.eyeMoveDown.std()
        features.loc[idx, "eyeMoveDown_max"] = d.eyeMoveDown.max()
        features.loc[idx, "eyeMoveDown_min"] = d.eyeMoveDown.min()

        features.loc[idx, "eyeMoveLeft_count"] = len(
            d) - len(stat[stat.eyeMoveLeft == 0])
        features.loc[idx, "eyeMoveLeft_mean"] = d.eyeMoveLeft.mean()
        features.loc[idx, "eyeMoveLeft_std"] = d.eyeMoveLeft.std()
        features.loc[idx, "eyeMoveLeft_max"] = d.eyeMoveLeft.max()
        features.loc[idx, "eyeMoveLeft_min"] = d.eyeMoveLeft.min()

        features.loc[idx, "eyeMoveRight_count"] = len(
            d) - len(stat[stat.eyeMoveRight == 0])
        features.loc[idx, "eyeMoveRight_mean"] = d.eyeMoveRight.mean()
        features.loc[idx, "eyeMoveRight_std"] = d.eyeMoveRight.std()
        features.loc[idx, "eyeMoveRight_max"] = d.eyeMoveRight.max()
        features.loc[idx, "eyeMoveRight_min"] = d.eyeMoveRight.min()

        features.loc[idx, "label"] = d.label.iloc[0]

    print(features)
    db.recreate_table("features", ws=5)
    for i in range(len(features)):
        db.insert_features(features.iloc[i], ws=5)

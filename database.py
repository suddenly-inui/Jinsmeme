import sqlite3


class Database:
    def __init__(self, db):
        self.dbname = db
        self.conn = sqlite3.connect(self.dbname)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "create table if not exists currentData(id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp, accx, accy, accz, blinkSpeed, blinkStrength, eyeMoveUp, eyeMoveDown, eyeMoveRight, eyeMoveLeft, pitch, roll, yaw, walking, noiseStatus, fitError, powerLeft, sequenceNumber, label)"
        )
        self.cur.execute(
            "create table if not exists features(id INTEGER PRIMARY KEY AUTOINCREMENT, id_count, timestamp_from, timestamp_to, accx_mean, accx_std, accx_max, accx_min, accy_mean, accy_std, accy_max, accy_min, accz_mean, accz_std, accz_max, accz_min, ptich_mean, ptich_std ,ptich_max, ptich_min, roll_mean, roll_std, roll_max, roll_min, yaw_meam, yaw_std, yaw_max, yaw_min, blink_count, blinkSpeed_mean, blinkSpeed_std, blinkSpeed_max, blinkSpeed_min, blinkStrength_mean, blinkStrength_std, blinkStrength_max, blinkStrength_min, eyeMoveUp_count, eyeMoveUp_mean, eyeMoveUp_std, eyeMoveUp_max, eyeMoveUp_min, eyeMoveDown_count, eyeMoveDown_mean, eyeMoveDown_std, eyeMoveDown_max, eyeMoveDown_min, eyeMoveLeft_count, eyeMoveLeft_mean, eyeMoveLeft_std, eyeMoveLeft_max, eyeMoveLeft_min, eyeMoveRight_count, eyeMoveRight_mean, eyeMoveRight_std, eyeMoveRight_max, eyeMoveRight_min, label)"
        )
        self.cur.execute(
            "create table if not exists features5(id INTEGER PRIMARY KEY AUTOINCREMENT, id_count, timestamp_from, timestamp_to, accx_mean, accx_std, accx_max, accx_min, accy_mean, accy_std, accy_max, accy_min, accz_mean, accz_std, accz_max, accz_min, ptich_mean, ptich_std ,ptich_max, ptich_min, roll_mean, roll_std, roll_max, roll_min, yaw_meam, yaw_std, yaw_max, yaw_min, blink_count, blinkSpeed_mean, blinkSpeed_std, blinkSpeed_max, blinkSpeed_min, blinkStrength_mean, blinkStrength_std, blinkStrength_max, blinkStrength_min, eyeMoveUp_count, eyeMoveUp_mean, eyeMoveUp_std, eyeMoveUp_max, eyeMoveUp_min, eyeMoveDown_count, eyeMoveDown_mean, eyeMoveDown_std, eyeMoveDown_max, eyeMoveDown_min, eyeMoveLeft_count, eyeMoveLeft_mean, eyeMoveLeft_std, eyeMoveLeft_max, eyeMoveLeft_min, eyeMoveRight_count, eyeMoveRight_mean, eyeMoveRight_std, eyeMoveRight_max, eyeMoveRight_min, label)"
        )
        self.cur.execute(
            "create table if not exists features15(id INTEGER PRIMARY KEY AUTOINCREMENT, id_count, timestamp_from, timestamp_to, accx_mean, accx_std, accx_max, accx_min, accy_mean, accy_std, accy_max, accy_min, accz_mean, accz_std, accz_max, accz_min, ptich_mean, ptich_std ,ptich_max, ptich_min, roll_mean, roll_std, roll_max, roll_min, yaw_meam, yaw_std, yaw_max, yaw_min, blink_count, blinkSpeed_mean, blinkSpeed_std, blinkSpeed_max, blinkSpeed_min, blinkStrength_mean, blinkStrength_std, blinkStrength_max, blinkStrength_min, eyeMoveUp_count, eyeMoveUp_mean, eyeMoveUp_std, eyeMoveUp_max, eyeMoveUp_min, eyeMoveDown_count, eyeMoveDown_mean, eyeMoveDown_std, eyeMoveDown_max, eyeMoveDown_min, eyeMoveLeft_count, eyeMoveLeft_mean, eyeMoveLeft_std, eyeMoveLeft_max, eyeMoveLeft_min, eyeMoveRight_count, eyeMoveRight_mean, eyeMoveRight_std, eyeMoveRight_max, eyeMoveRight_min, label)"
        )
        self.cur.execute(
            "create table if not exists features30(id INTEGER PRIMARY KEY AUTOINCREMENT, id_count, timestamp_from, timestamp_to, accx_mean, accx_std, accx_max, accx_min, accy_mean, accy_std, accy_max, accy_min, accz_mean, accz_std, accz_max, accz_min, ptich_mean, ptich_std ,ptich_max, ptich_min, roll_mean, roll_std, roll_max, roll_min, yaw_meam, yaw_std, yaw_max, yaw_min, blink_count, blinkSpeed_mean, blinkSpeed_std, blinkSpeed_max, blinkSpeed_min, blinkStrength_mean, blinkStrength_std, blinkStrength_max, blinkStrength_min, eyeMoveUp_count, eyeMoveUp_mean, eyeMoveUp_std, eyeMoveUp_max, eyeMoveUp_min, eyeMoveDown_count, eyeMoveDown_mean, eyeMoveDown_std, eyeMoveDown_max, eyeMoveDown_min, eyeMoveLeft_count, eyeMoveLeft_mean, eyeMoveLeft_std, eyeMoveLeft_max, eyeMoveLeft_min, eyeMoveRight_count, eyeMoveRight_mean, eyeMoveRight_std, eyeMoveRight_max, eyeMoveRight_min, label)"
        )
        self.cur.execute(
            "create table if not exists features45(id INTEGER PRIMARY KEY AUTOINCREMENT, id_count, timestamp_from, timestamp_to, accx_mean, accx_std, accx_max, accx_min, accy_mean, accy_std, accy_max, accy_min, accz_mean, accz_std, accz_max, accz_min, ptich_mean, ptich_std ,ptich_max, ptich_min, roll_mean, roll_std, roll_max, roll_min, yaw_meam, yaw_std, yaw_max, yaw_min, blink_count, blinkSpeed_mean, blinkSpeed_std, blinkSpeed_max, blinkSpeed_min, blinkStrength_mean, blinkStrength_std, blinkStrength_max, blinkStrength_min, eyeMoveUp_count, eyeMoveUp_mean, eyeMoveUp_std, eyeMoveUp_max, eyeMoveUp_min, eyeMoveDown_count, eyeMoveDown_mean, eyeMoveDown_std, eyeMoveDown_max, eyeMoveDown_min, eyeMoveLeft_count, eyeMoveLeft_mean, eyeMoveLeft_std, eyeMoveLeft_max, eyeMoveLeft_min, eyeMoveRight_count, eyeMoveRight_mean, eyeMoveRight_std, eyeMoveRight_max, eyeMoveRight_min, label)"
        )
        self.cur.execute(
            "create table if not exists features60(id INTEGER PRIMARY KEY AUTOINCREMENT, id_count, timestamp_from, timestamp_to, accx_mean, accx_std, accx_max, accx_min, accy_mean, accy_std, accy_max, accy_min, accz_mean, accz_std, accz_max, accz_min, ptich_mean, ptich_std ,ptich_max, ptich_min, roll_mean, roll_std, roll_max, roll_min, yaw_meam, yaw_std, yaw_max, yaw_min, blink_count, blinkSpeed_mean, blinkSpeed_std, blinkSpeed_max, blinkSpeed_min, blinkStrength_mean, blinkStrength_std, blinkStrength_max, blinkStrength_min, eyeMoveUp_count, eyeMoveUp_mean, eyeMoveUp_std, eyeMoveUp_max, eyeMoveUp_min, eyeMoveDown_count, eyeMoveDown_mean, eyeMoveDown_std, eyeMoveDown_max, eyeMoveDown_min, eyeMoveLeft_count, eyeMoveLeft_mean, eyeMoveLeft_std, eyeMoveLeft_max, eyeMoveLeft_min, eyeMoveRight_count, eyeMoveRight_mean, eyeMoveRight_std, eyeMoveRight_max, eyeMoveRight_min, label)"
        )
        self.cur.execute(
            "create table if not exists features90(id INTEGER PRIMARY KEY AUTOINCREMENT, id_count, timestamp_from, timestamp_to, accx_mean, accx_std, accx_max, accx_min, accy_mean, accy_std, accy_max, accy_min, accz_mean, accz_std, accz_max, accz_min, ptich_mean, ptich_std ,ptich_max, ptich_min, roll_mean, roll_std, roll_max, roll_min, yaw_meam, yaw_std, yaw_max, yaw_min, blink_count, blinkSpeed_mean, blinkSpeed_std, blinkSpeed_max, blinkSpeed_min, blinkStrength_mean, blinkStrength_std, blinkStrength_max, blinkStrength_min, eyeMoveUp_count, eyeMoveUp_mean, eyeMoveUp_std, eyeMoveUp_max, eyeMoveUp_min, eyeMoveDown_count, eyeMoveDown_mean, eyeMoveDown_std, eyeMoveDown_max, eyeMoveDown_min, eyeMoveLeft_count, eyeMoveLeft_mean, eyeMoveLeft_std, eyeMoveLeft_max, eyeMoveLeft_min, eyeMoveRight_count, eyeMoveRight_mean, eyeMoveRight_std, eyeMoveRight_max, eyeMoveRight_min, label)"
        )
        self.cur.execute(
            "create table if not exists features120(id INTEGER PRIMARY KEY AUTOINCREMENT, id_count, timestamp_from, timestamp_to, accx_mean, accx_std, accx_max, accx_min, accy_mean, accy_std, accy_max, accy_min, accz_mean, accz_std, accz_max, accz_min, ptich_mean, ptich_std ,ptich_max, ptich_min, roll_mean, roll_std, roll_max, roll_min, yaw_meam, yaw_std, yaw_max, yaw_min, blink_count, blinkSpeed_mean, blinkSpeed_std, blinkSpeed_max, blinkSpeed_min, blinkStrength_mean, blinkStrength_std, blinkStrength_max, blinkStrength_min, eyeMoveUp_count, eyeMoveUp_mean, eyeMoveUp_std, eyeMoveUp_max, eyeMoveUp_min, eyeMoveDown_count, eyeMoveDown_mean, eyeMoveDown_std, eyeMoveDown_max, eyeMoveDown_min, eyeMoveLeft_count, eyeMoveLeft_mean, eyeMoveLeft_std, eyeMoveLeft_max, eyeMoveLeft_min, eyeMoveRight_count, eyeMoveRight_mean, eyeMoveRight_std, eyeMoveRight_max, eyeMoveRight_min, label)"
        )
        self.conn.commit()
        self.conn.close()

    def insert_current_data(self, json, label):
        self.conn = sqlite3.connect(self.dbname)
        self.cur = self.conn.cursor()
        sql = (
            f"insert into currentData(timestamp, accx, accy, accz, blinkSpeed, blinkStrength, eyeMoveUp, eyeMoveDown, eyeMoveRight, eyeMoveLeft, pitch, roll, yaw, walking, noiseStatus, fitError, powerLeft, sequenceNumber, label) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        )
        self.cur.execute(sql, [json['timestamp'], json['accX'], json['accY'], json['accZ'], json['blinkSpeed'], json['blinkStrength'], json['eyeMoveUp'], json['eyeMoveDown'], json['eyeMoveRight'],
                         json['eyeMoveLeft'], json['pitch'], json['roll'], json['yaw'], json['walking'], json['noiseStatus'], json['fitError'], json['powerLeft'], json['sequenceNumber'], label])
        self.conn.commit()
        self.conn.close()

    def recreate_table(self, name, ws=0):
        self.conn = sqlite3.connect(self.dbname)
        self.cur = self.conn.cursor()
        if name == "features":
            self.cur.execute(
                f"drop table features{ws}"
            )
            self.cur.execute(
                f"create table if not exists features{ws}(id INTEGER PRIMARY KEY AUTOINCREMENT, id_count, timestamp_from, timestamp_to, accx_mean, accx_std, accx_max, accx_min, accy_mean, accy_std, accy_max, accy_min, accz_mean, accz_std, accz_max, accz_min, ptich_mean, ptich_std ,ptich_max, ptich_min, roll_mean, roll_std, roll_max, roll_min, yaw_meam, yaw_std, yaw_max, yaw_min, blink_count, blinkSpeed_mean, blinkSpeed_std, blinkSpeed_max, blinkSpeed_min, blinkStrength_mean, blinkStrength_std, blinkStrength_max, blinkStrength_min, eyeMoveUp_count, eyeMoveUp_mean, eyeMoveUp_std, eyeMoveUp_max, eyeMoveUp_min, eyeMoveDown_count, eyeMoveDown_mean, eyeMoveDown_std, eyeMoveDown_max, eyeMoveDown_min, eyeMoveLeft_count, eyeMoveLeft_mean, eyeMoveLeft_std, eyeMoveLeft_max, eyeMoveLeft_min, eyeMoveRight_count, eyeMoveRight_mean, eyeMoveRight_std, eyeMoveRight_max, eyeMoveRight_min, label)"
            )
        elif name == "currentData":
            self.cur.execute(
                "drop table features"
            )
            self.cur.execute(
                "create table if not exists currentData(id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp, accx, accy, accz, blinkSpeed, blinkStrength, eyeMoveUp, eyeMoveDown, eyeMoveRight, eyeMoveLeft, pitch, roll, yaw, walking, noiseStatus, fitError, powerLeft, sequenceNumber, label)"
            )
            self.conn.commit()
            self.conn.close()

    def insert_features(self, features, ws=0):
        self.conn = sqlite3.connect(self.dbname)
        self.cur = self.conn.cursor()
        self.cur.execute(
            f"insert into features{ws}(id_count, timestamp_from, timestamp_to, accx_mean, accx_std, accx_max, accx_min, accy_mean, accy_std, accy_max, accy_min, accz_mean, accz_std, accz_max, accz_min, ptich_mean, ptich_std ,ptich_max, ptich_min, roll_mean, roll_std, roll_max, roll_min, yaw_meam, yaw_std, yaw_max, yaw_min, blink_count, blinkSpeed_mean, blinkSpeed_std, blinkSpeed_max, blinkSpeed_min, blinkStrength_mean, blinkStrength_std, blinkStrength_max, blinkStrength_min, eyeMoveUp_count, eyeMoveUp_mean, eyeMoveUp_std, eyeMoveUp_max, eyeMoveUp_min, eyeMoveDown_count, eyeMoveDown_mean, eyeMoveDown_std, eyeMoveDown_max, eyeMoveDown_min, eyeMoveLeft_count, eyeMoveLeft_mean, eyeMoveLeft_std, eyeMoveLeft_max, eyeMoveLeft_min, eyeMoveRight_count, eyeMoveRight_mean, eyeMoveRight_std, eyeMoveRight_max, eyeMoveRight_min, label) values({features['id_count']}, {features['timestamp_from']}, {features['timestamp_to']},{features['accx_mean']},{features['accx_std']},{features['accx_max']},{features['accx_min']},{features['accy_mean']},{features['accy_std']},{features['accy_max']},{features['accy_min']},{features['accz_mean']},{features['accz_std']},{features['accz_max']},{features['accz_min']},{features['ptich_mean']},{features['ptich_std']},{features['ptich_max']},{features['ptich_min']},{features['roll_mean']},{features['roll_std']},{features['roll_max']},{features['roll_min']},{features['yaw_mean']},{features['yaw_std']},{features['yaw_max']},{features['yaw_min']},{features['blink_count']},{features['blinkSpeed_mean']},{features['blinkSpeed_std']},{features['blinkSpeed_max']},{features['blinkSpeed_min']},{features['blinkStrength_mean']},{features['blinkStrength_std']},{features['blinkStrength_max']},{features['blinkStrength_min']},{features['eyeMoveUp_count']},{features['eyeMoveUp_mean']},{features['eyeMoveUp_std']},{features['eyeMoveUp_max']},{features['eyeMoveUp_min']},{features['eyeMoveDown_count']},{features['eyeMoveDown_mean']},{features['eyeMoveDown_std']},{features['eyeMoveDown_max']},{features['eyeMoveDown_min']},{features['eyeMoveLeft_count']},{features['eyeMoveLeft_mean']},{features['eyeMoveLeft_std']},{features['eyeMoveLeft_max']},{features['eyeMoveLeft_min']},{features['eyeMoveRight_count']},{features['eyeMoveRight_mean']},{features['eyeMoveRight_std']},{features['eyeMoveRight_max']},{features['eyeMoveRight_min']},{features['label']})"
        )
        self.conn.commit()
        self.conn.close()

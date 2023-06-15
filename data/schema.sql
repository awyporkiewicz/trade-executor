BEGIN TRANSACTION;
DROP TABLE IF EXISTS trade;
CREATE TABLE trade
(
    id         INTEGER PRIMARY KEY,
    update_id  INTEGER NOT NULL,
    symbol     TEXT NOT NULL,
    price      DECTEXT NOT NULL,
    quantity   DECTEXT NOT NULL,
    timestamp DATETIME DEFAULT (STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))
);
COMMIT;

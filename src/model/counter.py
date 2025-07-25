
from dataclasses import dataclass
import duckdb


@dataclass
class Counter:
    count: int = 0

    def __post_init__(self):
        if self.count == 0:
            conn = duckdb.connect("counter.duckdb")
            conn.execute(
                "CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, value INTEGER)"
            )
            result = conn.execute(
                "SELECT value FROM counter WHERE id=1"
            ).fetchone()
            conn.close()
            if result:
                self.count = result[0]

    def save_to_db(self, db_path: str = "counter.duckdb"):
        conn = duckdb.connect(db_path)
        conn.execute(
            "CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, value INTEGER)"
        )
        result = conn.execute(
            "SELECT COUNT(*) FROM counter WHERE id=1"
        ).fetchone()
        if result and result[0] > 0:
            conn.execute("UPDATE counter SET value=? WHERE id=1", [self.count])
        else:
            conn.execute(
                "INSERT INTO counter (id, value) VALUES (1, ?)", [self.count]
            )
        conn.close()

    @staticmethod
    def load_from_db(db_path: str = "counter.duckdb"):
        conn = duckdb.connect(db_path)
        conn.execute(
            "CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, value INTEGER)")
        result = conn.execute(
            "SELECT value FROM counter WHERE id=1"
        ).fetchone()
        conn.close()
        if result:
            return Counter(count=result[0])
        return Counter()

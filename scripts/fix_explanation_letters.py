"""One-off data fix: after answer options were shuffled, 241 explanations still began with
"The correct answer is X: <text>" using the *old* letter. The <text> still matches the real
correct option, so we rewrite the letter to the current correct_answer. Idempotent."""
import os
import re
import sqlite3
import sys

DB = os.getenv("DATABASE_PATH") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database.db")


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    fixed = 0
    for table in ("questions_v2", "questions"):
        rows = cur.execute(
            f"SELECT id, correct_answer, explanation FROM {table} WHERE explanation LIKE 'The correct answer is _:%'"
        ).fetchall()
        for qid, correct, expl in rows:
            m = re.match(r"The correct answer is ([A-D]):", expl)
            if m and correct and m.group(1) != correct.strip().upper():
                new = "The correct answer is %s:" % correct.strip().upper() + expl[m.end():]
                cur.execute(f"UPDATE {table} SET explanation = ? WHERE id = ?", (new, qid))
                fixed += 1
    conn.commit()
    conn.close()
    print(f"Fixed {fixed} explanation(s) in {DB}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

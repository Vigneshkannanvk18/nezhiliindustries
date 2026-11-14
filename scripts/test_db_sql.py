import sqlite3

# Test SQL schema compatibility (using standard SQL)
sql = """
CREATE TABLE IF NOT EXISTS negizhi_rfq_leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    client_name TEXT NOT NULL DEFAULT '',
    company_name TEXT NOT NULL DEFAULT '',
    email TEXT NOT NULL DEFAULT '',
    phone TEXT NOT NULL DEFAULT '',
    part_name TEXT NOT NULL DEFAULT '',
    material TEXT NOT NULL DEFAULT '',
    quantity TEXT NOT NULL DEFAULT '',
    tooling_status TEXT NOT NULL DEFAULT '',
    notes TEXT,
    ip_address TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'New'
);
"""

conn = sqlite3.connect(":memory:")
conn.execute(sql)
conn.execute("INSERT INTO negizhi_rfq_leads (created_at, client_name, part_name) VALUES ('2026-11-14 15:30:00', 'Test Client', 'Helical Gear')")
cursor = conn.execute("SELECT * FROM negizhi_rfq_leads")
row = cursor.fetchone()
print("SQL Schema verified successfully! Sample row:", row)


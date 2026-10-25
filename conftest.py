import sqlite3
def pytest_runtest_logreport(report):
 if report.when=="call":
  with sqlite3.connect("results.db") as db:
   db.execute("CREATE TABLE IF NOT EXISTS outcomes(test TEXT,outcome TEXT)")
   db.execute("INSERT INTO outcomes VALUES(?,?)",(report.nodeid,report.outcome))

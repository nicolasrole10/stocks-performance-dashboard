"""Descarga cierres diarios de Yahoo Finance para todas las ideas de data/trades.csv + SPY y QQQ.

Escribe data/prices.csv (date + una columna por ticker). Lo corre GitHub Actions.
"""
import csv
import datetime as dt
import pathlib

import yfinance as yf

ROOT = pathlib.Path(__file__).resolve().parents[1]
START = "2025-10-01"  # cubre YTD y 1 año para los índices
BENCH = ["SPY", "QQQ"]

with open(ROOT / "data/trades.csv", newline="") as f:
    tickers = sorted({r["ticker"].strip().upper() for r in csv.DictReader(f) if r["ticker"].strip()})
cols = tickers + BENCH

end = (dt.date.today() + dt.timedelta(days=1)).isoformat()
df = yf.download(cols, start=START, end=end, auto_adjust=False, progress=False)["Close"]
df = df[cols].dropna(how="all").ffill().round(2)

missing = [c for c in cols if df[c].isna().all()]
if missing:
    raise SystemExit(f"Yahoo no devolvió precios para: {missing}. Revisa el ticker en data/trades.csv.")

df.index = df.index.strftime("%Y-%m-%d")
df.index.name = "date"
df.to_csv(ROOT / "data/prices.csv", lineterminator="\n")
print(f"{len(df)} días, {len(cols)} tickers, último cierre {df.index[-1]}")

import yfinance as yf, json, datetime

SYMBOLS = ["ACS.MC","IBE.MC","VIS.MC","LOG.MC","VID.MC","REP.MC","TRE.MC",
           "IDR.MC","ENG.MC","EBRO.MC","MCM.MC","ANA.MC","ITX.MC","CBAV.MC",
           "RED.MC","ACX.MC","GCO.MC","BBVA.MC","GEST.MC","NTGY.MC"]

quotes = []
for sym in SYMBOLS:
    try:
        t = yf.Ticker(sym)
        i = t.fast_info
        price = i.last_price
        prev  = i.previous_close
        quotes.append({
            "symbol":    sym,
            "price":     round(float(price), 3) if price else None,
            "changePct": round((price-prev)/prev*100, 2) if price and prev else None,
            "high52":    round(float(i.year_high), 3) if i.year_high else None,
            "low52":     round(float(i.year_low),  3) if i.year_low  else None,
            "pe":        None,
            "marketCap": int(i.market_cap) if i.market_cap else None,
            "ma200":     round(float(i.two_hundred_day_average), 3) if i.two_hundred_day_average else None,
        })
        print(f"OK {sym}: {price}")
    except Exception as e:
        print(f"ERR {sym}: {e}")

result = {
    "updated": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "quotes": [q for q in quotes if q.get("price")]
}
with open("datos.json","w") as f:
    json.dump(result, f)
print(f"TOTAL: {len(result['quotes'])} acciones")

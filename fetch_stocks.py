import urllib.request, json, datetime

SYMBOLS = [
    "ACS.MC","IBE.MC","VIS.MC","LOG.MC","VID.MC","REP.MC","TRE.MC","IDR.MC",
    "ENG.MC","EBRO.MC","MCM.MC","ANA.MC","ITX.MC","CBAV.MC","RED.MC","ACX.MC",
    "GCO.MC","BBVA.MC","GEST.MC","NTGY.MC"
]
FIELDS = ("regularMarketPrice,regularMarketChangePercent,"
          "fiftyTwoWeekHigh,fiftyTwoWeekLow,trailingPE,marketCap,twoHundredDayAverage")
url = (f"https://query1.finance.yahoo.com/v7/finance/quote"
       f"?symbols={','.join(SYMBOLS)}&fields={FIELDS}")
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as r:
    data = json.loads(r.read())
result = {
    "updated": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "quotes": [{"symbol":q.get("symbol"),"price":q.get("regularMarketPrice"),
                "changePct":q.get("regularMarketChangePercent"),
                "high52":q.get("fiftyTwoWeekHigh"),"low52":q.get("fiftyTwoWeekLow"),
                "pe":q.get("trailingPE"),"marketCap":q.get("marketCap"),
                "ma200":q.get("twoHundredDayAverage")} for q in data["quoteResponse"]["result"]]
}
with open("datos.json","w") as f: json.dump(result, f)
print(f"OK - {len(result['quotes'])} acciones")

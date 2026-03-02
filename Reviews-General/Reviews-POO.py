class CryptoAsset:
    def __init__ (self, ticker, price, limit):
        self.ticker = ticker
        self.price = price
        self.limit = limit
    def check_alert(self):
            if self.price > self.limit:
             return f"Alerta {self.ticker}: Vender agora!"
            else:
                return f"Status {self.ticker}: Estável, aguarde."
price_BTC = CryptoAsset("BTC",69458,67000)
price_XRP = CryptoAsset("XRP",1.40,1.20)
print(price_BTC.check_alert())
print(price_XRP.check_alert())
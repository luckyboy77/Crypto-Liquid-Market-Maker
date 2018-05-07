import authorize, requests, config

def send_trade(pair, side, size, price):
  trade = {
    "size": size,
    "price": price,
    "side": side,
    "product_id": pair
  }
  api_url = config.url
  auth = authorize.run_GdaxAuth()

  test_trade = requests.post(api_url + 'orders', json=trade, auth=auth)
  return test_trade
  
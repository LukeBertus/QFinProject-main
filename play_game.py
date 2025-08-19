import platform
import sys
import os



original_sys_path = sys.path.copy()

current_dir = os.path.dirname(os.path.abspath(__file__))
os_name = platform.system()

if os_name == "Linux":
    sys.path.insert(0, os.path.join(current_dir, "bin/linux_version"))
    from bin.linux_version.game_setup import run_game
elif os_name == "Windows":
    sys.path.insert(0, os.path.join(current_dir, "bin/windows_version"))
    from bin.windows_version.game_setup import run_game
elif os_name == "Darwin":
    sys.path.insert(0, os.path.join(current_dir, "bin/mac_version"))
    from bin.mac_version.game_setup import run_game
else:
    raise ValueError("Unsupported OS")

from base import Product

print("Imports Completed")

sys.path = original_sys_path

# ======================Do Not Change Anything above here====================

# The following variables represent the values we will use when assessing your bot
# You may change them for testing purposes
#   (e.g. you may reduce num_timestamps when testing so that you can run simulations faster)
#   (e.g. you may set fine to 0 to see if your strategy is first profiable without position penalties)

# Custom Imports 
import pandas as pd


from your_algo import PlayerAlgorithm

uec = Product("UEC", mpv=0.1, pos_limit=200, fine=20)

products = [uec]


player_bot = PlayerAlgorithm(products)
player_bot.set_idx(1)
num_timestamps = 5
your_pnl = run_game(player_bot, num_timestamps, products)

print(your_pnl)


# Custome code to save trade prices
csv_path = "trade_prices.csv"
new_data = player_bot.values
column_name = "Price_n"

if os.path.exists(csv_path) and os.path.getsize(csv_path) > 10:
    df = pd.read_csv(csv_path)
    max_len = max(len(df), len(new_data))
    # Reindex the whole DataFrame to the new max length
    df = df.reindex(range(max_len))
    # Add the new column, padding if necessary
    df[column_name] = pd.Series(new_data).reindex(range(max_len), fill_value=pd.NA)
else:
    df = pd.DataFrame({column_name: new_data})

df.to_csv(csv_path, index=False)
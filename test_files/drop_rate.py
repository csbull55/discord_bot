import fractions as fc
import pandas as pd
import numpy as np
import osrs_sim

# reads the drop rates csv
drop_rates = pd.read_csv("F:\Projects\Programming_projects\Discord_bot\mumble_bot\drop_rates.csv")


# returns df with rates extracted for inputted boss
def roll_df(boss):
    # new df for boss inputted
    df_roll = drop_rates[drop_rates['Boss'] == boss.title()]

    # extracts denominator from rate
    df_roll['d_rate'] = df_roll['Rate'].apply(lambda x: fc.Fraction(x).denominator)

    # finds lcm and creates new column on # of rolls
    lcm = osrs_sim.lcm_multi(df_roll['d_rate'])
    df_roll['rolls'] = lcm / df_roll['d_rate']
    return df_roll


def boss_lcm(boss):
    # new df for boss inputted
    df_roll = drop_rates[drop_rates['Boss'] == boss.title()]

    # extracts denominator from rate
    df_roll['d_rate'] = df_roll['Rate'].apply(lambda x: fc.Fraction(x).denominator)

    # finds lcm and creates new column on # of rolls
    lcm = osrs_sim.lcm_multi(df_roll['d_rate'])
    return lcm


kc = 200
boss = 'arma'
# creates an array of rolls for kc entered, uses function to find lcm for boss
roll = np.random.randint(1, boss_lcm(boss), size=kc)

item_df = roll_df(boss)

drops = []

print(item_df.head(1))

# checks rolls against drop table, returns item and adds to 'drops' list

item_key = pd.DataFrame(columns=['key', 'item'])
i = 1
for index, row in item_df.iterrows():
    count = int(item_df['rolls'][index])
    while count > 0:
        item_key.loc[i] = [str(i), item_df.loc[index]['Item']]
        count -= 1
        i += 1

for item in item_key['key']:
    if int(item) in roll:
        drops.append((item_key['item'][int(item)]))

print(drop_rates)
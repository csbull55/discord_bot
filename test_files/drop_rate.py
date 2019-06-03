import fractions as fc
import frac_functions as ff
import pandas as pd
import numpy as np

# reads the drop rates csv
drop_rates = pd.read_csv("F:\Projects\Programming_projects\Discord_bot\mumble_bot\drop_rates.csv")


# returns df with rates extracted for inputted boss
def roll_df(boss):
    # new df for boss inputted
    df_roll = drop_rates[drop_rates['Boss'] == boss.title()]

    # extracts denominator from rate
    df_roll['d_rate'] = df_roll['Rate'].apply(lambda x: fc.Fraction(x).denominator)

    # finds lcm and creates new column on # of rolls
    lcm = ff.lcm_multi(df_roll['d_rate'])
    df_roll['rolls'] = lcm / df_roll['d_rate']
    return df_roll


def boss_lcm(boss):
    # new df for boss inputted
    df_roll = drop_rates[drop_rates['Boss'] == boss.title()]

    # extracts denominator from rate
    df_roll['d_rate'] = df_roll['Rate'].apply(lambda x: fc.Fraction(x).denominator)

    # finds lcm and creates new column on # of rolls
    lcm = ff.lcm_multi(df_roll['d_rate'])
    return lcm

kc = 50
boss = 'arma'
# creates an array of rolls for kc entered, uses function to find lcm for boss
roll = np.random.randint(1, boss_lcm(boss), size=kc)

item_df = roll_df(boss)
lcm = boss_lcm('Arma')

drops = []

print(item_df.head(1))

# checks rolls against drop table, returns item and adds to 'drops' list
drop_array = list(range(0, int(lcm)))

item_key = pd.DataFrame(columns=['key', 'item'])
i = 1
for index, row in item_df.iterrows():
    count = int(item_df['rolls'][index])
    while count > 0:
        item_key.loc[i] = [str(i), item_df.loc[index]['Item']]
        count -= 1
        i += 1

print(item_key)
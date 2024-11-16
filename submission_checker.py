import pandas as pd
import numpy as np

def get_positions(pos_dict):
    pos = pd.Series(pos_dict)
    pos = pos.replace([np.inf, -np.inf], np.nan)
    pos = pos.dropna()
    pos = pos / pos.abs().sum()
    pos = pos.clip(-0.1, 0.1)
    if pos.abs().max() / pos.abs().sum() > 0.1:
        raise ValueError(f"Portfolio too concentrated {pos.abs().max()=} / {pos.abs().sum()=}")
    return pos


def get_submission_dict(
        pos_dict,
        your_team_name: str = "2.5 Asians",
        your_team_passcode: str = "tate",
):
    return {
        **get_positions(pos_dict).to_dict(),
        **{
            "team_name": your_team_name,
            "passcode": your_team_passcode,
        },
    }


# Calling
# the
# function
# with the following parameters:
#     get_submission_dict(
#         {**{f"strat_{i}": 0.1 for i in range(10)}, "strat_bad": np.nan, "strat_bad2": -np.inf}
#     )
# Results in:
#
# {'strat_0': 0.1,
#  'strat_1': 0.1,
#  'strat_2': 0.1,
#  'strat_3': 0.1,
#  'strat_4': 0.1,
#  'strat_5': 0.1,
#  'strat_6': 0.1,
#  'strat_7': 0.1,
#  'strat_8': 0.1,
#  'strat_9': 0.1,
#  'team_name': 'a_great_team_name',
#  'passcode': 'a_strong_p4$$c0d3'}

# {'strat_0': -0.02506836490110994, 'strat_1': -0.021935066511735588, 'strat_2': -0.025887655028912028, 'strat_3': -0.025016217297574864, 'strat_4': 0.1, 'strat_5': 0.1, 'strat_6': 0.019253382596929776, 'strat_7': -0.01954197710059942, 'strat_8': 0.030927991184080517, 'strat_9': -0.031343264433949095, 'strat_10': -0.029058819355568144, 'strat_11': -0.02662936555994409, 'strat_12': 0.017983580344628984, 'strat_13': -0.01994450354973542, 'strat_14': 0.025119327992129455, 'strat_15': 0.018015530503726042, 'strat_16': -0.02359176142886434, 'strat_17': -0.020338182955029795, 'strat_18': 0.02786588730552577, 'strat_19': 0.018670558795517423, 'strat_20': 0.026812063211310563, 'strat_21': -0.02584379047263364, 'strat_22': -0.02849689045055855, 'strat_23': -0.027783598598966168, 'strat_24': 0.029033289658349087, 'strat_25': -0.02043842236187923, 'strat_26': 0.022665803177995027, 'strat_27': -0.023831542398687917, 'strat_28': 0.025570102985529093, 'strat_29': 0.022886137421805147, 'strat_30': 0.019012507648951883, 'strat_31': 0.019780818544639846, 'strat_32': 0.03599965155328511, 'strat_33': 0.01809530230932719, 'strat_34': 0.01846360105893677, 'team_name': '2.5 Asians', 'passcode': 'tate'}

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
        your_team_name: str = "a_great_team_name",
        your_team_passcode: str = "a_strong_p4$$c0d3",
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

# {'strat_0': -0.007593797677997352, 'strat_1': 0.008507078968786929, 'strat_2': -0.0012338590941682992, 'strat_3': 0.004515314744893131, 'strat_4': 0.37505957926425776, 'strat_5': 0.3854329476822053, 'strat_6': 0.0015294715021528461, 'strat_7': -0.005812587181846247, 'strat_8': 0.00506822325783669, 'strat_9': 0.00872849890066405, 'strat_10': -0.009838608377627006, 'strat_11': -0.010021802109994215, 'strat_12': 0.003564908746297098, 'strat_13': 0.011750187638272491, 'strat_14': 0.0008726774677568729, 'strat_15': 5.8524582482701115e-05, 'strat_16': 0.009219592734459684, 'strat_17': -0.0012697015935346863, 'strat_18': -0.015343211246079827, 'strat_19': -0.0006845034144181358, 'strat_20': -0.01757044468733013, 'strat_21': 0.03152747636713451, 'strat_22': 0.015867981859595072, 'strat_23': -0.010257847358854853, 'strat_24': 0.0232717926745598, 'strat_25': 0.022416266316949936, 'strat_26': 0.004759963160773647, 'strat_27': 0.00422446377155059, 'strat_28': 0.003998687617520117, 'team_name': '2.5 Asians', 'passcode': 'tate'}

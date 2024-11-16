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
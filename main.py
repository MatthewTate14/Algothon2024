import pandas as pd
import cryptpandas as crp
import strategy as strat
import submission_checker as sc
from submission_checker import get_positions

strategy = strat.strategy(4571, "WPcFk8FofuBmfUzO")

strategy = sc.get_submission_dict(strategy)
print(strategy)

#add team name and passcode
form_name = 'https://docs.google.com/forms/d/e/1FAIpQLSeUYMkI5ce18RL2aF5C8I7mPxF7haH23VEVz7PQrvz0Do0NrQ/formResponse'

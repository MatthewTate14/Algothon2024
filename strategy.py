import pandas as pd

import numpy as np

import cryptpandas

# Function to calculate Weighted Moving Average

def weighted_moving_average(series, window):
    weights = np.arange(1, window + 1)

    return series.rolling(window).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)


# Function to calculate Exponential Moving Average (EMA)

def exponential_moving_average(series, window):
    return series.ewm(span=window, adjust=False).mean()

# Find the best strategy based on the highest momentum score

def select_best_strategy(momentum_scores):
    # Get the most recent momentum scores

    latest_scores = momentum_scores.iloc[-1]

    return latest_scores

# Normalize the strategy weights

def normalize_weights(selected_strategies):
    # Get the latest returns of the selected strategies

    abs_sum = sum(abs(value) for value in selected_strategies.values)

    print(abs_sum)

    # Normalize so the sum of absolute values is 1

    normalized_weights = {strat: value / abs_sum for strat, value in selected_strategies.items()}

    abs_sum = sum(abs(value) for value in normalized_weights.values())

    print(abs_sum)

    return normalized_weights

def distribute_weights(submission):
    print(submission)

    while np.sum(np.array([abs(val) for val in submission.values()]) > 0.1) != 0:

        data_items = submission.items()

        print(submission)

        for key, data in data_items:

            print("========")

            if abs(data) > 0.1:

                print("distributing")

                distribute = abs(data) - 0.1

                count = len(submission) - np.sum(np.array([abs(val) for val in submission.values()]) >= 0.1)

                if data < 0:

                    submission[key] = -0.1

                else:

                    submission[key] = 0.1

                print(distribute)

                print(count)

                val = distribute / count

                print(val)

                for key2, data2 in data_items:

                    if data2 < 0.1 and data2 > 0:

                        submission[key2] = data2 + val

                    elif data2 > -0.1 and data2 < 0:

                        submission[key2] = data2 - val

    print(submission)

def strategy(file, passcode):
    data = cryptpandas.read_encrypted(path=f"encrypted_data/release_{file}.crypt", password=passcode)

    df = pd.DataFrame(data)

    print(df.columns)

    # Parameters

    momentum_window = 10  # Number of periods to calculate momentum

    top_n = 26  # Number of top strategies to select

    momentum_scores = df.apply(weighted_moving_average, window=momentum_window)

    best_strategies = select_best_strategy(momentum_scores)

    print("Best Strategies:\n", best_strategies)
    submission = normalize_weights(best_strategies)

    result = {key: float(submission[key]) for key in submission.keys()}

    distribute_weights(result)

    result = {key: float(result[key]) for key in result.keys()}

    print(sum(abs(r) for r in result.values()))
    return result
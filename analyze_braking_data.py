import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load braking data from a CSV file.

    Parameters:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    df = pd.read_csv(filepath)
    return df


def compute_metrics(df: pd.DataFrame) -> dict:
    """
    Compute simple metrics from braking data.

    Parameters:
        df (pd.DataFrame): DataFrame containing braking data.

    Returns:
        dict: Dictionary with computed metrics.
    """
    metrics = {
        "initial_velocity": df["velocity"].iloc[0],
        "final_velocity": df["velocity"].iloc[-1],
        "max_brake_pressure": df["brake_pressure"].max(),
        "time_to_stop": df[df["velocity"] <= 0.5]["time"].min() if (df["velocity"] <= 0.5).any() else None
    }
    return metrics


def plot_braking(df: pd.DataFrame) -> None:
    """
    Plot velocity and brake pressure over time.

    Parameters:
        df (pd.DataFrame): DataFrame containing braking data.
    """
    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Plot velocity
    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("Velocity [km/h]", color="tab:blue")
    ax1.plot(df["time"], df["velocity"], color="tab:blue", label="Velocity")
    ax1.tick_params(axis="y", labelcolor="tab:blue")

    # Plot brake pressure on second axis
    ax2 = ax1.twinx()
    ax2.set_ylabel("Brake Pressure [%]", color="tab:red")
    ax2.plot(df["time"], df["brake_pressure"], color="tab:red", linestyle="--", label="Brake Pressure")
    ax2.tick_params(axis="y", labelcolor="tab:red")

    plt.title("Braking Data Analysis")
    fig.tight_layout()
    plt.show()


def main():
    filepath = "sample_braking_data.csv"
    df = load_data(filepath)

    print("Loaded dataset:")
    print(df.head())

    metrics = compute_metrics(df)
    print("\nComputed metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value}")

    plot_braking(df)


if __name__ == "__main__":
    main()

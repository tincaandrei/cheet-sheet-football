import pandas as pd


def summarise_player_defence(
    all_games_df: pd.DataFrame,
    n_games: int,
    n_top: int = 5,
    team: str | None = None,
) -> pd.DataFrame:
    """
    Aggregate defensive stats per (team, player) over all games and
    return the top `n_top` foulers per game.
    """
    if all_games_df.empty:
        return all_games_df

    player_totals = all_games_df.groupby(level=["team", "player"]).sum(numeric_only=True)

    if team is not None:
        # keep only rows for the requested team
        try:
            player_totals = player_totals.xs(team, level="team", drop_level=False)
        except KeyError:
            # no rows for this team
            return player_totals.iloc[0:0][
                ["fouls_committed", "yellow_cards", "tackles_won", "min"]
            ]

    most_fouls_committed = player_totals.sort_values(
        by="fouls_committed",
        ascending=False,
    )

    top_foulers = most_fouls_committed.head(n_top).copy()

    top_foulers["min"] = top_foulers["min"] / n_games
    top_foulers["fouls_committed"] = top_foulers["fouls_committed"] / n_games
    top_foulers["tackles_won"] = top_foulers["tackles_won"] / n_games

    return top_foulers[["fouls_committed", "yellow_cards", "tackles_won", "min"]]

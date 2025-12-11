from typing import List

import pandas as pd
import soccerdata as sd


def get_fbref_reader(
    league: str = "ENG-Premier League",
    season: str = "2526",
) -> sd.FBref:
    """Create an FBref reader for a given league and season."""
    return sd.FBref(leagues=league, seasons=season)


def get_last_games_ids(
    fbref: sd.FBref,
    team: str,
    n_games: int,
) -> List[str]:
    """Return the last `n_games` finished match ids for `team`."""
    schedule = fbref.read_schedule()

    mask_team = (schedule["home_team"] == team) | (schedule["away_team"] == team)
    mask_finished = schedule["score"].notna()
    team_games = schedule[mask_team & mask_finished]

    last_games = team_games.tail(n_games)
    return last_games["game_id"].tolist()


def build_defensive_stats_for_games(
    fbref: sd.FBref,
    match_ids: List[str],
) -> pd.DataFrame:
    """
    For a list of match ids, download per‑match 'misc' player stats and
    return a single DataFrame with defensive stats.
    """
    all_games_data: List[pd.DataFrame] = []

    for match_id in match_ids:
        print(f"Scraping game: {match_id}")
        player_stats = fbref.read_player_match_stats("misc", match_id=match_id)

        cols = [
            ("min", ""),
            ("Performance", "CrdY"),
            ("Performance", "Fls"),
            ("Performance", "TklW"),
        ]

        player_stats_useful = player_stats[cols].copy()
        player_stats_useful.columns = [
            "min",
            "yellow_cards",
            "fouls_committed",
            "tackles_won",
        ]

        all_games_data.append(player_stats_useful)

    if not all_games_data:
        return pd.DataFrame(
            columns=["min", "yellow_cards", "fouls_committed", "tackles_won"]
        )

    return pd.concat(all_games_data)


def get_team_defensive_stats(
    team: str,
    n_games: int = 5,
    league: str = "ENG-Premier League",
    season: str = "2526",
) -> pd.DataFrame:
    """
    High‑level helper that returns defensive stats for the last `n_games`
    of `team` in the given league/season.
    """
    fbref = get_fbref_reader(league=league, season=season)
    match_ids = get_last_games_ids(fbref, team=team, n_games=n_games)
    return build_defensive_stats_for_games(fbref, match_ids)


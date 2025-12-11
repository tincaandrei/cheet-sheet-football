import argparse

from aggregate_defence import summarise_player_defence
from scrape_fbref import get_team_defensive_stats


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scrape FBref defensive stats for the last N games of a team.",
    )
    parser.add_argument(
        "--team",
        default="Chelsea",
        help="Team name as used on FBref (default: Chelsea).",
    )
    parser.add_argument(
        "--games",
        type=int,
        default=5,
        help="Number of last finished games to include (default: 5).",
    )
    parser.add_argument(
        "--league",
        default="ENG-Premier League",
        help='League ID for FBref (default: \"ENG-Premier League\").',
    )
    parser.add_argument(
        "--season",
        default="2526",
        help='Season code for FBref, e.g. \"2526\" (default: 2526).',
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Show top N players by fouls committed per game (default: 5).",
    )

    args = parser.parse_args()

    all_games_df = get_team_defensive_stats(
        team=args.team,
        n_games=args.games,
        league=args.league,
        season=args.season,
    )

    print("\nAll defensive stats (all games):")
    print(all_games_df)

    top_foulers = summarise_player_defence(
        all_games_df,
        n_games=args.games,
        n_top=args.top,
        team=args.team,
    )

    print("\n--- Top players with most fouls committed (per game) ---")
    print(top_foulers)


if __name__ == "__main__":
    main()

def rank_sports_teams(teams_data):
    """
    teams_data: List of tuples -> (team_name, matches_won, matches_drawn, goal_difference)
    """
    ranked_list = []
    for team, won, drawn, gd in teams_data:
        points = (won * 3) + (drawn * 1)
        ranked_list.append((team, points, gd))

    # Sort by points descending, then by goal difference descending (tie-breaker)
    ranked_list.sort(key=lambda x: (x[1], x[2]), reverse=True)

    print("\n--- Case Study 47: Sports Tournament Ranking ---")
    for rank, (team, pts, gd) in enumerate(ranked_list, start=1):
        print(f"Rank {rank}: {team} - {pts} Points (Goal Difference: {gd:+d})")


# Example Usage
teams = [("Team Alpha", 5, 2, 8), ("Team Beta", 6, 0, 12), ("Team Gamma", 5, 2, 10)]
rank_sports_teams(teams)
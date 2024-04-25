class Solutions:
    def gibonacci_done(self, n, x, y):
        if n < 2:
            return n
        else:
            g = []
            g.append(x)
            g.append(y)
            for i in range(2, n + 1):
                g.append(g[i - 1] - g[i - 2])
            return g[n - 1] - g[n - 2]
    def gibonacci(self, n, m, k):
        # Helper function to check if two players have played against each other in at least one round

        # Iterate through all pairs of players and check if they have played against each other
        for player1 in range(1, n + 1):
            for player2 in range(player1 + 1, n + 1):
                if not self.played_against_each_other(player1, player2, n, k):
                    return False

        return True

    def played_against_each_other(self, player1, player2, n, k):
        for round_games in k:
            team1 = set(round_games[:n // 2])
            team2 = set(round_games[n // 2:])

            if (player1 in team1 and player2 in team2) or (player1 in team2 and player2 in team1):
                return True

        return False


if __name__ == '__main__':
    solutions = Solutions()
    print("Result = " + str(solutions.gibonacci(2, 1, [[1, 2]])))  # True
    print("Result = " + str(solutions.gibonacci(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]])))  # True
    print("Result = " + str(solutions.gibonacci(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]])))  # True
    print("Result = " + str(solutions.gibonacci(6, 6, [[1, 6, 3, 4, 5, 2], [6, 4, 2, 3, 1, 5], [4, 2, 1, 5, 6, 3],
                                                       [4, 5, 1, 6, 2, 3], [3, 2, 5, 1, 6, 4],
                                                       [2, 3, 6, 4, 1, 5]])))  # True
    print("Result = " + str(solutions.gibonacci(6, 6, [[3, 1, 4, 5, 6, 2], [5, 3, 2, 4, 1, 6], [5, 3, 6, 4, 2, 1],
                                                       [6, 5, 3, 2, 1, 4], [5, 4, 1, 2, 6, 3],
                                                       [4, 1, 6, 2, 5, 3]])))  # False

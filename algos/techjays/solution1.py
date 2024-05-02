


class SolutionsTechJays1:
    use_cases = [
        {
            "input_data": ['GeeksForGeeks', 'QuizGeeks'],
            "output_data": ["Geeks", 5]
        }, {
            "input_data": ['GeeksForGeeksQuiz', 'QuizGeeks'],
            "output_data": ["Geeks", 5]
        },
    ]
    def method_body(self, input_data):
        str1, str2 = input_data[0], input_data[1]
        # Initialize the matrix with zeros
        dp = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]

        # Initialize variables to keep track of the maximum length and the end position
        max_length = 0
        end_pos = 0

        # Build the table in bottom-up fashion
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                    # Update maximum length and end position
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        end_pos = i
                else:
                    dp[i][j] = 0

        # Extract the longest common substring
        start_pos = end_pos - max_length
        longest_common_substring = str1[start_pos:end_pos]

        return [longest_common_substring, max_length]

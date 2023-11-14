class Solutions:
    def givenNumber(self, n):
        counter = 0
        while n != 0:
            counter += 1
            n = int(n / 10)

        return counter

    def diffLarger(self, arr):
        max_value = 0
        for n in range(0, len(arr)):
            current_value = arr[n]
            for s in range(n, len(arr)):
                if current_value < arr[s]:
                    diff = arr[s] - current_value
                    if diff > max_value:
                        max_value = diff
        return max_value


if __name__ == '__main__':
    solutions = Solutions()
    print(solutions.diffLarger([8, 13, 2, 9, 5, 1, 3, 11, -1, 7]))  # 10
    print(solutions.diffLarger([7, 2, 8, 5, 9, 6, 2, 8]))  # 7
    print(solutions.givenNumber(56))  # 2
    print(solutions.givenNumber(-8698))  # 4
    print(solutions.givenNumber(12764))  # 5
    print(solutions.givenNumber(100))  # 3

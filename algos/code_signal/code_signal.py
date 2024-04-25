class CustomHashMap:
    def __init__(self):
        self.map = {}

    def insert(self, x, y):
        self.map[x] = y

    def get(self, x):
        return self.map.get(x, 0)

    def addToKey(self, x):
        new_map = {}
        for key, value in self.map.items():
            new_map[key + x] = value
        self.map = new_map

    def addToValue(self, y):
        for key in self.map:
            self.map[key] += y


def solution(queryTypes, queries):
    custom_hashmap = CustomHashMap()
    result_sum = 0

    for queryType, params in zip(queryTypes, queries):
        if queryType == "insert":
            custom_hashmap.insert(params[0], params[1])
        elif queryType == "get":
            result_sum += custom_hashmap.get(params[0])
        elif queryType == "addToKey":
            custom_hashmap.addToKey(params[0])
        elif queryType == "addToValue":
            custom_hashmap.addToValue(params[0])

    return result_sum


if __name__ == '__main__':
    # Example usage 1:
    queryTypes = ["insert", "insert", "addToValue", "get"]
    queries = [[1, 2], [2, 3], [2], [1]]

    result = solution(queryTypes, queries)
    print("Sum of results:", result)

    queryTypes = ["insert",
                  "insert",
                  "addToValue",
                  "addToKey",
                  "get"]
    queries = [[1, 2],
               [2, 3],
               [2],
               [1],
               [3]]

    result = solution(queryTypes, queries)
    print("Sum of results:", result)

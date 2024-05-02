


class SolutionsTechJays2:
    use_cases = [
        {
            "input_data": ['T', 'L'],
            "output_data": 1
        },
        {
            "input_data": ['L', 'T'],
            "output_data": 1
        },
        {
            "input_data": ['L', 'T', 'T'],
            "output_data": 1
        },
        {
            "input_data": ['L', 'T', 'L'],
            "output_data": 1
        },
        {
            "input_data": ['L', 'T', 'L', 'T'],
            "output_data": 2
        },
        {
            "input_data": ['L', 'T', 'E', 'L', 'T'],
            "output_data": 2
        },
        {
            "input_data": ['L', 'T', 'L', 'E', 'T'],
            "output_data": 1
        },
        {
            "input_data": ['L', 'L', 'L', 'T', 'T'],
            "output_data": 1
        }
    ]
    def method_body(self, arr):
        counter = 0
        local_list = []

        for each_animal in arr:

            if each_animal == "T":
                if 'L' in local_list:
                    counter = counter + 1
                    local_list.remove("L")
                else:
                    if 'T' not in local_list:
                        local_list.append(each_animal)

            elif each_animal == "L":
                if 'T' in local_list:
                    counter = counter + 1
                    local_list.remove("T")
                else:
                    if 'L' not in local_list:
                        local_list.append(each_animal)

            elif each_animal == "E":
                local_list.clear()

        return counter

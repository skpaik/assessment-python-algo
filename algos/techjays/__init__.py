from .solution1 import SolutionsTechJays1
from .solution2 import SolutionsTechJays2
from .solution3 import SolutionsTechJays3
from .solution4 import SolutionsTechJays4


class Solutions(SolutionsTechJays4):
    def start_method(self):
        #print("\n\nStart method\n")
        idx = 1
        for each_case in self.use_cases:
            result = self.method_body(each_case.get("input_data"))
            print("Case " + str(idx) + " = " + str(result == each_case.get("output_data")))
            idx = idx + 1


        #print("\nEnd method")

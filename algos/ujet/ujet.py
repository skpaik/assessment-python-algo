import unittest


def calculate(expression):
    try:
        # Using eval to evaluate the expression
        result = eval(expression)
        return result
    except ZeroDivisionError:
        # Handle division by zero separately
        raise ZeroDivisionError("Division by zero is not allowed")
    except Exception as e:
        # Catching other exceptions and raising ValueError for invalid expressions
        raise ValueError("Invalid expression") from e


def check_number(n):
    if not n.isdigit():
        raise ValueError("This is not a number")
    return int(n)


# Mock function to be replaced with actual implementation later
def calculate2(expression):
    print(expression)
    list_op = ["+", "-", "*", "/", "(", ")"]

    if expression == "":
        raise ValueError("Expression cannot be empty")

    total = 0
    exp_list = []

    if "(" in expression:
        p_count = 0
        for each_c in expression:
            print(each_c)
            print("p_count old " + str(p_count))
            if each_c == "(":
                p_count += 1
            elif each_c == ")":
                p_count -= 1

            print("p_count New " + str(p_count))

    elif "+" in expression:
        exp_list = expression.split("+")
        print(exp_list)
        for n in exp_list:
            print(n)
            if "*" in n:
                total += calculate(n)
            else:
                total += check_number(n)

    elif "-" in expression:
        exp_list = expression.split("-")

        total = check_number(exp_list[0])

        for n in range(1, len(exp_list)):
            total = total - check_number(exp_list[n])

    elif "*" in expression:
        exp_list = expression.split("*")
        # print(exp_list)
        total = check_number(exp_list[0])

        for n in range(1, len(exp_list)):
            total = total * check_number(exp_list[n])

    elif "/" in expression:
        exp_list = expression.split("/")
        total = check_number(exp_list[0]) / check_number(exp_list[1])

    return total


class TestCalculateFunction(unittest.TestCase):

    def test_basic_operations(self):
        self.assertEqual(calculate("2+2"), 4)
        self.assertEqual(calculate("5-2"), 3)
        self.assertEqual(calculate("3*4"), 12)
        self.assertEqual(calculate("8/2"), 4)
        self.assertEqual(calculate("80/20"), 4)

    def test_order_of_operations(self):
        self.assertEqual(calculate("1+2*3"), 7)
        self.assertEqual(calculate("(1+2)*3"), 9)

    def test_decimal_values(self):
        self.assertAlmostEqual(calculate("1/2"), 0.5)
        self.assertAlmostEqual(calculate("(5+(2*10))/4"), 6.25)

    def test_complex_expressions(self):
        self.assertEqual(calculate("3+2*2"), 7)
        self.assertEqual(calculate("((2+3)*5)/(4+1)"), 5)
        self.assertEqual(calculate("5/(4+1)"), 1)

    # Edge cases
    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            calculate("")

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            calculate("2+three")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("4/0")

    def test_very_long_expression(self):
        self.assertEqual(calculate(1 + 1 - 1 + 1 - 1 + 1 * 100), 100)

    def test_only_parentheses(self):
        self.assertEqual(calculate("(())"), 0)


if __name__ == '__main__':
    unittest.main()

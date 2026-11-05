class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        # pass
        curr_res = init
        for i in range(iterations):
            curr_res = curr_res - learning_rate * (2*curr_res)

        return round(curr_res, 5)

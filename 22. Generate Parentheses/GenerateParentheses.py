class Solution:
    # https://leetcode.com/problems/generate-parentheses/
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all valid combinations of set number of well-formed parentheses.
        
        :param n: The number of well-formed parentheses in each combination, between 1 and 8.
        :returns: All valid combinations of n well-formed parentheses.
        """
        # Initialize a dictionary of results with the string as its key and information on the number of closed/open parentheses in the string.
        results = {"(": (0, 1)}
        # Loop a number of times equal to the length of each finished string.
        for _ in range(2*n-1):
            # Create a new, empty results dictionary.
            newResults = {}
            # Iterate over each result in the dictionary.
            for result in results:
                # Find the number of closed and open parentheses in this particular string.
                numClosed = results[result][0]
                numOpen = results[result][1]
                # If the total number of left parentheses is less than the number that is possible, add a left paren to the end of the result and add it to the new results dictionary.
                if numClosed + numOpen < n:
                    newOpenResult = result + "("
                    newResults[newOpenResult] = (numClosed, numOpen + 1)
                # Also, if there is at least one open parenthesis, then add a right paren to the end of the result and add it to the new results dictionary.
                if numOpen > 0:
                    newClosedResult = result + ")"
                    newResults[newClosedResult] = (numClosed + 1, numOpen - 1)
            # Replace the results dictionary with the new results dictionary.
            results = newResults
        # Return all keys in the results dictionary as the solution.
        return list(results.keys())

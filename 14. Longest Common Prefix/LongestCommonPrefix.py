class Solution:
    # https://leetcode.com/problems/longest-common-prefix/
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix in a List of strings.

        :param strs: A List of lowercase English strings with a number of elements between 1 and 200 with each string having a length between 0 and 200. 
        :returns: The longest common prefix in every string of 'strs'.
        """
        # Handle simple case where there is only one string.
        if len(strs) == 1:
            # Since there is only a single string, the entire string is the longest common prefix.
            return strs[0]
        # Sort the strings in ascending order to find the shortest string and optimize each loop.
        strs = sorted(strs, key=len)
        # The longest common prefix can be at maximum the length of the shortest string, so assume that is the longest common prefix.
        prefix = strs[0]
        # Initialize a flag indicating whether the longest common prefix has been found, and assume true.
        found = True
        # Loop the code below a maximum number of times equal to the length of the prefix.
        for _ in range(len(prefix)):
            # Iterate over each string in the input.
            for s in strs:
                # Check if the string starts with the current prefix.
                if not s.startswith(prefix):
                    # If it doesn't, then indicate that the longest common prefix hasn't been found and stop iterating over each string in the input.
                    found = False
                    break
            # If every string matched the prefix, it is the longest common prefix, so return it.
            if found:
                return prefix
            # Since every string didn't match the prefix, remove the last character from it.
            prefix = prefix[:-1]
            # Reset the found flag.
            found = True
        # Since a longest common prefix wasn't found, return the current prefix, an empty string.
        return prefix

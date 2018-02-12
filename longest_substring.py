class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        count=0
        """will hold longest substring"""
        current_count=0
        """will hold current substring length"""

        """algorithm:  iterate through, find first longest substring, start at next character when previous
        substring terminates, subtract 1 from current substring length and continue from where the previous
        substring terminated as that's now the current longest substring, continue until first index of new
        substring to the end of the string is shorter than longest found substring"""

        aDict ={}
        start_index_of_second_loop=1
        second_loop_initialize = range(start_index_of_second_loop, len(s))

        if len(s) is 0:
            return 0
        if len(s) is 1:
            return 1
        for ch1 in s:
            aDict[ch1] = 1
            distance_from_end = len(s) - second_loop_initialize

            if distance_from_end < count: # in case the rest of the string is shorter than current longest substring
                return count
            for ch2 in s[second_loop_initialize, len(s)]:
                if aDict[ch2] is None:  # doesn't exist
                    current_count = current_count+1
                    count = current_count
                    aDict[ch2] = 1
                else:
                    aDict = {}  # reset dictionary
                    current_count = 0
                    start_index_of_second_loop = start_index_of_second_loop +1
                    second_loop_initialize = range(start_index_of_second_loop, len(s))

        return count

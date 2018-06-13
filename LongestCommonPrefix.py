class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if input list is empty return ''
        if not strs:
            return ''
        # if input list has only one string that's the longest common prefix
        elif len(set(strs)) == 1:
            return strs[0]
        else:
            len_map = {string:len(string) for string in strs}
            smallest = min(len_map, key=len_map.get)
            #print('smallest word', smallest)

            for i in range(len(smallest)):
                for string in strs:
                    if string[i] != smallest[i]:
                        return smallest[:i]
        return smallest

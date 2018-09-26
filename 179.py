# Proof of why sorting is correct

# Give a sorting rule: A > B if A concat B > B concat A
# Largest number would follow the decending sorting order of the numbers

# first we prove that it is sortable, if AB > BA and BC > CB then AC > CA

# AB > BA <=> A(logB+1) > B(logA+1) <=> AlogB > BlogA
# BC > CB <=> B(logC+1) > C(logB+1) <=> BlogC > ClogB
# => AlogB/ClogB > BlogA/BlogC => A/C > logA/logC => AlogC > ClogA => AC > CA

# second we prove that sorted list is the largest

# suppose we have a sorted sequence A,B,C,... with A the largest according to the sorting defined above
# next we can prove that A is always at the front most for largest number

# Suppose we have a largest number with A in the middle, like this ...XXXAXXX... we can always make this number larger by swapping A with the number in front of it



class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        comp=lambda a,b:1 if a+b>b+a else -1 if a+b<b+a else 0
        # convert nums into strings
        num=map(str,nums)
        # use comparator to sort reversely
        num.sort(cmp=comp,reverse=True)
        return str(int("".join(num)))

class Solution:
    def __init__(self, s, t):
        self.s = str(s)
        self.t = str(t)
        self.lenofs = len(self.s)
        self.lenoft = len(self.t)
        self.count_s = {}
        self.count_t = {}

    def Anagramconditions(self) -> bool:
        if self.lenofs != self.lenoft:
            return False

        self.count_s = {i: self.s.count(i) for i in set(self.s)}
        self.count_t = {i: self.t.count(i) for i in set(self.t)}

        print(self.count_s)
        print(self.count_t)

        return self.count_s == self.count_t


if __name__ == "__main__":
    s = "carrace"
    t = "racecar"

    solution = Solution(s, t)
    print(f"Are the given words Anagram? : {solution.Anagramconditions()}")
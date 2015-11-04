import string
import operator

class Question3_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;

    #####################################
    # ADD YOUR CODE HERE
    # Pr(x|y) = self.cpt.conditional_prob(x, y);
    # A word begins with "`" and ends with "`".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt.conditional_prob("a", "`") * \
    #    self.cpt.conditional_prob("b", "a") * \
    #    self.cpt.conditional_prob("`", "b");
    # query example:
    #    query: "qu--_--n";
    #    return "t";
    def solve(self, query):

        print(query)
        max_prob = -float("inf")
        res = ""
        query += "`"

        for c in string.ascii_lowercase:
            prob1 = {}
            prob2 = {}
            pre = "`"
            prob = 1.0

            for cur in query:
                if cur == "-":
                    if not bool(prob1):
                        for c1 in string.ascii_lowercase:
                            prob1[c1] = prob * self.cpt.conditional_prob(c1, pre)
                    else:
                        for c1 in prob1.keys():
                            for c2 in string.ascii_lowercase:
                                prob2[c1 + c2] = prob1[c1] * self.cpt.conditional_prob(c2, c1)
                        for c2 in prob2.keys():
                            if c2[1] in prob1.keys():
                                prob1[c2[1]] += prob2[c2]
                else:
                    if cur == "_":
                        cur = c
                    if not bool(prob1):
                        prob *= self.cpt.conditional_prob(cur, pre)
                    else:
                        for c1 in prob1.keys():
                            prob1[c1] *= self.cpt.conditional_prob(cur, c1)
                pre = cur

            temp_max = max(prob1.iteritems(), key = operator.itemgetter(1))[1]
            if temp_max > max_prob:
                max_prob = temp_max
                res = c

        print("result = " + res)
        return res


import string
import operator

class Question2_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;
        return;

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
    #    query: "que__ion";
    #    return ["s", "t"];
    def solve(self, query):

        prob1 = {}
        prob2 = {}
        pre = "`"
        query += "`"

        for cur in query:
            if cur == "_" and not bool(prob1):
                for c1 in string.ascii_lowercase:
                    prob1[c1] = self.cpt.conditional_prob(c1, pre)
            elif cur == "_" and bool(prob1):
                for c1 in prob1.keys():
                    for c2 in string.ascii_lowercase:
                        prob2[c1 + c2] = prob1[c1] * self.cpt.conditional_prob(c2, c1)
            elif pre == "_":
                for c2 in prob2.keys():
                    prob2[c2] *= self.cpt.conditional_prob(cur, c2[1])
                break
            pre = cur

        res = max(prob2.iteritems(), key = operator.itemgetter(1))[0]
        return [res[0], res[1]]



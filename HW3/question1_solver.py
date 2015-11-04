import string
import operator

class Question1_Solver:
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
    #    query: "ques_ion";
    #    return "t";
    def solve(self, query):

        prob = {}
        pre = "`"
        query += "`"

        for cur in query:
            if cur == "_":
                for c in string.ascii_lowercase:
                    prob[c] = self.cpt.conditional_prob(c, pre)
            if pre == "_":
                for c in prob.keys():
                    prob[c] *= self.cpt.conditional_prob(cur, c)
                break
            pre = cur

        return max(prob.iteritems(), key = operator.itemgetter(1))[0]



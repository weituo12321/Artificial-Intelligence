import string
import operator

class Question5_Solver:
    def __init__(self, cpt2):
        self.cpt2 = cpt2;
        return;

    #####################################
    # ADD YOUR CODE HERE
    #         _________
    #        |         v
    # Given  z -> y -> x
    # Pr(x|z,y) = self.cpt2.conditional_prob(x, z, y);
    #
    # A word begins with "``" and ends with "``".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt2.conditional_prob("a", "`", "`") * \
    #    self.cpt2.conditional_prob("b", "`", "a") * \
    #    self.cpt2.conditional_prob("`", "a", "b") * \
    #    self.cpt2.conditional_prob("`", "b", "`");
    # query example:
    #    query: "ques_ion";
    #    return "t";
    def solve(self, query):
        prob = {}
        pre1 = "`"
        pre2 = "`"
        query += "``"

        for cur in query:
            if cur == "_":
                for c in string.ascii_lowercase:
                    prob[c] = self.cpt2.conditional_prob(c, pre1, pre2)
            if pre2 == "_":
                for c in prob.keys():
                    prob[c] *= self.cpt2.conditional_prob(cur, pre1, c)
            if pre1 == "_":
                for c in prob.keys():
                    prob[c] *=self.cpt2.conditional_prob(cur, c, pre2)
                break
            pre1 = pre2
            pre2 = cur

        return max(prob.iteritems(), key = operator.itemgetter(1))[0]

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        for i in cpdomains:
            count, domain = i.split()
            count = int(count)
            sub = domain.split(".")
            for j in range(len(sub)):
                c = ".".join(sub[j:])
                if c not in dict:
                    dict[c] = count
                else:
                    dict[c] += count
        return ["{} {}".format(dom, c) for c, dom in dict.items()]
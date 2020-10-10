#    A website domain like "discuss.leetcode.com" consists of various
#    subdomains. At the top level, we have "com", at the next level,
#    we have "leetcode.com", and at the lowest level, "discuss.leetcode.com".
#    When we visit a domain like "discuss.leetcode.com", we will also visit
#    the parent domains "leetcode.com" and "com" implicitly.
#
#    Now, call a "count-paired domain" to be a count (representing the
#    number of visits this domain received), followed by a space,
#    followed by the address. An example of a count-paired domain might be
#    "9001 discuss.leetcode.com".
#
#    We are given a list cpdomains of count-paired domains.
#    We would like a list of count-paired domains,
#    (in the same format as the input, and in any order), that explicitly
#    counts the number of visits to each subdomain.


class Solution:
    def subdomainVisits(self, cpdomains):
        hashmap = {}
        res = []
        for elem in cpdomains:
            num, domain = elem.split()
            num = int(num)
            domains = domain.split('.')
            for ii in range(len(domains)):
                subdomain = ".".join(domains[~ii:])
                val = hashmap.get(subdomain, 0)
                val += num
                hashmap[subdomain] = val

        for subdomain in hashmap:
            res.append(" ".join([str(hashmap[subdomain]), subdomain]))
        return res


if __name__ == "__main__":
    testinput = ["900 google.mail.com", "50 yahoo.com",
                 "1 intel.mail.com", "5 wiki.org"]
    print(Solution.subdomainVisits(Solution, testinput))

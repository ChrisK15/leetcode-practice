"""
Problem 4: Gallery Subdomain Traffic

Your gallery has been trying to increase it's online presence by hosting several virtual galleries. Each virtual gallery's web traffic is tracked through domain names, where each domain may have subdomains.

A domain like "modern.artmuseum.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "artmuseum.com", and at the lowest level, "modern.artmuseum.com". When visitors access a domain like "modern.artmuseum.com", they also implicitly visit the parent domains "artmuseum.com" and "com".

A count-paired domain is represented as "rep d1.d2.d3" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.

    For example, "9001 modern.artmuseum.com" indicates that "modern.artmuseum.com" was visited 9001 times.

Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain. The order of the output does not matter.

def subdomain_visits(cpdomains):
    pass

Example Usage:

cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))

Example Output:

["9001 artmuseum.com", "9001 modern.artmuseum.com", "9001 com"]

["901 gallery.com", "50 impressionism.com", "900 abstract.gallery.com", "5 medieval.org", "5 org",
"1 contemporary.gallery.com", "951 com"]
"""

def subdomain_visits(cpdomains):
    retList = []
    d = {}
    for cp in cpdomains:
        split = cp.split(' ')
        times_visited = int(split[0])
        domain = split[1]
        split_domain = domain.split('.')
        subdomains = []
        for i in range(len(split_domain)):
            temp_domain = '.'.join(split_domain[i:])
            subdomains.append(temp_domain)
        for domain in subdomains:
            if domain in d:
                d[domain] += times_visited
            else:
                d[domain] = times_visited
    for domain, count in d.items():
        retList.append(f"{count} {domain}")
    return retList
        
cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mapping = {}
        for cpdomain in cpdomains:
            count_str, res = cpdomain.split()
            count = int(count_str)
            part_of_domain = res.split(".")
            for i in range(len(part_of_domain)):
                domain =".".join(part_of_domain[i:])
                mapping[domain] = mapping.get(domain, 0)+count
        response = [f"{count} {value}" for value, count in mapping.items()]
        return response

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        lists = []
        for i in range (len(responses)):
            sett = set(responses[i])
            for word in sett:
                lists.append(word)
        ctr = Counter(lists)
        max_keys = max(ctr.values())
        most_response = [key for key, val in ctr.items() if val == max_keys]
        most_response.sort()
        return most_response[0]

            

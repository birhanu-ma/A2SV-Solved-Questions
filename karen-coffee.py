
def karenCoffee(first_line, recipe, query):
    k = first_line[1]
    start_with = float("inf")
    end_at = 0
    for start, end in recipe:
       
        start_with = min(start, start_with)
        end_at = max(end, end_at)
    temp = [0]*((end_at-start_with)+2)
    for start, end in recipe:
        temp[start-start_with]+=1
        temp[(end-start_with)+1]-=1
    prefix_sum = []
    summ = 0
    for num in temp:
        summ+=num
        prefix_sum.append(summ)
    good = [0]*len(prefix_sum)
    for i in range(len(prefix_sum)):
        if prefix_sum[i] >= k:
            good[i] = 1

    good_prefix = [0]*len(good)
    s = 0
    for i in range(len(good)):
        s += good[i]
        good_prefix[i] = s
    
    for start, end in query:
        query_start = max(start, start_with) - start_with
        query_end = min(end, end_at) - start_with

        if query_start > query_end:
            print(0)
            continue

        if query_start == 0:
            ctr = good_prefix[query_end]
        else:
            ctr = good_prefix[query_end] - good_prefix[query_start - 1]

        print(ctr)




line1 = list(map(int, input().split()))
num_recipe= line1[0]
min_recipe_recomendation = line1[1]
num_query = line1[2]
first_line = [num_recipe, min_recipe_recomendation, num_query]
recipe = []
for _ in range(num_recipe):
    recipe_input = list(map(int, input().split()))
    recipe.append(recipe_input)

query = []
for _ in range(num_query):
    query_input = list(map(int, input().split()))
    query.append(query_input)

karenCoffee(first_line, recipe, query)

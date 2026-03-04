     prefix_mod = 0
     mod_seen = {0: -1}

     for i in range(len(nums)):
          prefix_mod = (prefix_mod + nums[i]) % k
          print(prefix_mod)

          if prefix_mod in mod_seen:
               if i - mod_seen[prefix_mod] > 1:
                  return True
          else:
               mod_seen[prefix_mod] = i
     return False

import math


def find_minimum(nums: list) -> int:
    min = float("inf")
    for num in nums:
        if num < min:
            min = num
    return min


def sum(nums: list) -> int:
    sum = 0
    for num in nums:
        sum += num
    return sum


def average(nums: list) -> float:
    if len(nums) > 0:
        return sum(nums) / len(nums)


def median(nums: list) -> float:
    if len(nums) == 0:
        return None
    nums = sorted(nums)
    l = len(nums)
    if l % 2 == 0:
        return (nums[l // 2 - 1] + nums[l // 2]) / 2
    else:
        return nums[l // 2]


def get_estimated_spread(audiences_followers):
    n = len(audiences_followers)
    if n == 0:
        return None
    return average(audiences_followers) * (n ** 1.2)


def geometric_sequenc(starting_value, rate, num_months):
    return starting_value * (rate ** num_months)


def get_follower_prediction(follower_count, influencer_type, num_months):
    rates = {
        "fitness": 4,
        "cosmetic": 3,
        "other": 2,
    }
    if influencer_type in rates:
        rate = rates[influencer_type]
    else:
        rate = rates["other"]
        
    return follower_count * (rate ** num_months)



def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)


def num_possible_orders(num_posts):
    if num_posts == 0:
        return 1
    else:
        return num_posts * num_possible_orders(num_posts - 1)
    

def exponential_decay_recursion(initial_value, decay_rate, steps):
    # Base case: no more steps left
    if steps == 0:
        return initial_value
    # Recursive case: apply decay rate and decrease the step count
    else:
        return exponential_decay_recursion(initial_value * decay_rate, decay_rate, steps - 1)


def exponential_decay(intl_followers, fraction_lost_daily, days):
    res = intl_followers * (1 - fraction_lost_daily) ** days
    return res

def log_scale(data, base):
    return [math.log(l, base) for l in data]

def find_max(nums):
    max = float("-inf")
    for num in nums:
        if num > max:
            max = num
    return max

def does_name_exist(first_names, last_names, full_name):
    full_name = full_name.split(" ")
    for f_name in first_names:
        if f_name == full_name[0]:
            for l_name in last_names:
                if l_name == full_name[1]:
                    return True
    return False


def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    len_lists = len(all_handles)
    for handle in all_handles:
        for name in handle:
            if brand_name in name:
                count += 1
    return count / len_lists
        
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return False

class Graph:
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        sorted_neibo = sorted(self.graph[current_vertex])
        for neibo in sorted_neibo:
            if neibo not in visited:
                self.depth_first_search_r(visited, neibo)

        # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result


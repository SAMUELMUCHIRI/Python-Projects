
def greedy_activity_scheduling(activities):
    lecture_halls = []
    lecture_halls.append([activities[0]])
    
    for activity in activities[1:]:
        added = False
        for hall in lecture_halls:
            if hall[-1][-1] <= activity[0]:
                hall.append(activity)
                added = True
                break
        
        if not added:
            lecture_halls.append([activity])
    
    return lecture_halls

# Driver Code

import random

# Generate activities
activities = []
start_time = 8
end_time = 21.5

while start_time < end_time:
    duration = round(random.uniform(1,3), 1)
    if start_time + duration > end_time:
        duration = end_time - start_time
    activities.append([start_time, start_time + duration])
    start_time += duration
    
greedy_activity_scheduling(activities)

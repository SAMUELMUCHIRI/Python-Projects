# Greedy Algorithm Pseudocode:

# Input: 
# n = 100 activities for the given day

# Output: 
# An efficient schedule of activities and their corresponding lecture halls

# 1. Initialize an empty list to store the activity and lecture hall assignments
# 2. Sort the activities in ascending order by starting time
# 3. Iterate through each activity
# 4. For each activity, iterate through the lecture halls
# 5. Check if the lecture hall is available for the duration of the activity
# 6. If the lecture hall is available, assign the activity to that lecture hall and mark it as unavailable for the duration of the activity
# 7. If the lecture hall is not available, move on to the next lecture hall
# 8. If all lecture halls are unavailable, return an error
# 9. Once all activities have been assigned, return the list of activity and lecture hall assignments

# Python Implementation:

# Initialize an empty list to store the activity and lecture hall assignments
activities = []

# Sort the activities in ascending order by starting time
activities.sort(key = lambda x: x[0])

# Iterate through each activity
for activity in activities:
    # For each activity, iterate through the lecture halls
    for lecture_hall in lecture_halls:
        # Check if the lecture hall is available for the duration of the activity
        if is_available(lecture_hall, activity):
            # If the lecture hall is available, assign the activity to that lecture hall and mark it as unavailable for the duration of the activity
            assign_activity(lecture_hall, activity)
            # Add the activity and lecture hall to the schedule
            schedule.append([activity, lecture_hall])
            break
        # If the lecture hall is not available, move on to the next lecture hall
        else:
            continue
    # If all lecture halls are unavailable, return an error
    else:
        return "Error: No lecture hall is available for this activity"

# Once all activities have been assigned, return the list of activity and lecture hall assignments
return schedule
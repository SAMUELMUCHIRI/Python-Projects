 #Devise an efficient greedy algorithm to determine which activity should use which lecture hall and implement it in Python. For driver code, you may generate at random n = 100 activities for a given day during business hours starting at 8 am and ending at 9:30 pm, where each activity lasts from 1 hour to 3 hours with a 30-minute increment.

def greedyLectureHallAllocation(activities):
  # Create a list to store the lecture halls 
  lecture_halls = []
  # Create a dictionary to store the allocated lecture hall for each activity
  allocated_lecture_halls = {}

  # Iterate through the activities
  for activity in activities:
    # Create a variable to store the lecture hall that has been allocated for the current activity
    allocated_hall = None
    # Iterate through the lecture halls
    for hall in lecture_halls:
      # Check if the current lecture hall can be used for the current activity
      if hall['start_time'] + hall['duration'] <= activity['start_time'] and hall['end_time'] >= activity['end_time']:
        # Allocate the current lecture hall for the current activity
        allocated_hall = hall
        print(hall)
        # Break out of the loop
        break
    # Check if a lecture hall has been allocated
    if allocated_hall is None:
      # Create a new lecture hall
      allocated_hall = {
        'start_time': activity['start_time'],
        'end_time': activity['end_time'],
        'duration': activity['end_time'] - activity['start_time']
      }
      # Append the new lecture hall to the list
      lecture_halls.append(allocated_hall)
    # Add the allocated lecture hall to the dictionary
    allocated_lecture_halls[activity['name']] = allocated_hall
  
  # Return the dictionary containing the allocated lecture hall for each activity
  return allocated_lecture_halls

# Driver code
# Generate n = 100 activities
activities = []
for i in range(100):
  activity = {
    'name': 'Activity ' + str(i),
    'start_time': 8 + (i % 3) + (i // 3 * 0.5),
    'end_time': 8 + (i % 3) + (i // 3 * 0.5) + (i % 3 + 1),
  }
  activities.append(activity)

# Call the function
allocated_lecture_halls = greedyLectureHallAllocation(activities)

# Print the results
for activity, hall in allocated_lecture_halls.items():
  print('Activity: ', activity)
  print('Start time: ', hall['start_time'])
  print('End time: ', hall['end_time'])
  print('Duration: ', hall['duration'])
  print()
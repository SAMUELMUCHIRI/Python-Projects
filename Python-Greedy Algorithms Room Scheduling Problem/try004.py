import random

def greedy_algorithm(activities):
  # Initialize lecture hall and time
  lecture_hall = 1
  time = 8;

  # Iterate through activities
  for activity in activities:
    # If the activity can fit in the current time slot, assign it to the current lecture hall
    if activity + time <= 21.5:
      print("Activity: " + str(activity) + " assigned to lecture hall " + str(lecture_hall) + " from " + str(time) + " to " + str(time + activity))
      time = time + activity
    # Otherwise, assign it to the next lecture hall
    else:
      lecture_hall = lecture_hall + 1
      time = 8
      print("Activity: " + str(activity) + " assigned to lecture hall " + str(lecture_hall) + " from " + str(time) + " to " + str(time + activity))
      time = time + activity

# Generate activities
activities = []
for i in range(100):
  activities.append(round(random.uniform(1, 3), 1))

# Run algorithm
greedy_algorithm(activities)
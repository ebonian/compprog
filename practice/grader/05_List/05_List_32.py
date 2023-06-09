queue = []
wait_list = []

current_index = 0
total_time = 0
completed_order = 0

n = int(input())

for k in range(n):
  command = input().split()


  if (command[0] == "reset"):
    queue_number = int(command[1])

  elif (command[0] == "new"):
    print("ticket", queue_number)

    queue.append(queue_number)
    queue.append(int(command[1]))

    wait_list.append(queue_number)
    
    queue_number += 1

  elif (command[0] == "next"):
    print("call", wait_list[current_index])
    current_index += 1

  elif (command[0] == "order"):
    current_queue = queue[(current_index - 1) * 2]
    waiting_time = int(command[1]) - queue[(current_index - 1) * 2 + 1]

    print("qtime", current_queue, waiting_time)

    total_time += waiting_time
    completed_order += 1

  elif (command[0] == "avg_qtime"):
    print("avg_qtime", total_time / completed_order)
# Final_Part4 DO NOT DELETE THIS LINE

class stack:
    # Task 1
    def __init__(self, size):  # DO NOT modify this line
        # remove pass and replace with you code
        self.capacity = size
        self.content = []
        for n in range(self.capacity):
            self.content.append(None)
        self.tos = 0

    # Task 2
    def __str__(self):  # DO NOT modify this line
        # remove pass and replace with you code
        stack = []
        stack.append("-----")
        for el in self.content:
            stack.append(str(el))
        stack.append("-----")

        stack[self.tos + 1] = "{}{}".format(stack[self.tos + 1], "*")

        stack.reverse()

        return "\n".join(stack)

    # Task 3

    def push(self, data):  # DO NOT modify this line
        # remove pass and replace with you code
        if (self.tos == self.capacity):
            print("ERROR: stack is full")
        else:
            self.content[self.tos] = data
            self.tos += 1

    # Task 4

    def pop(self):  # DO NOT modify this line
        # remove pass and replace with you code
        if (self.tos == 0):
            print("ERROR: stack is empty")
        else:
            pop_value = self.content[self.tos - 1]
            self.content[self.tos - 1] = None
            self.tos -= 1
            return pop_value


# Task 5
def main():
    pass
    # (1) get an integer number, n, from keyboard
    n = int(input())

    # (2) create an empty stack with capacity equal n + 1, and
    #     print the stack created
    s = stack(n + 1)
    print(s)

    # (3) get n integer numbers from keyboard one line at time
    #     each time the input is entered the data should be added to stack created in (2)
    #     print the stack after all data are added
    for i in range(n):
        data = int(input())
        s.push(data)
    print(s)
    content = [el for el in s.content if el is not None]
    print(sum(content[1::]))

    # (4) remove all elements except the bottom most of the stack, and calculate
    #     the summation of removed elements and print the summation to screen
    for i in range(n - 1):
        s.pop()

    # (5) print the stack properties (DO NOT use show_stack())
    print(s)

# ---------------------------------------
# DO NOTE MODIFY CODE AFTER THIS SECTION
# ---------------------------------------


def show_stack(s):
    print(s.capacity, s.tos, s.content)


def test_init():
    sizes = [2, 4, 5]
    for i in range(len(sizes)):
        s = stack(sizes[i])
        show_stack(s)


def test_str():
    s = stack(3)
    print(s)
    s.content = [1, None, None]
    s.tos = 1
    print(s)
    s.content = [1, 2, 4]
    s.tos = 3
    print(s)


def test_push():
    s = stack(3)
    print('initial')
    show_stack(s)
    print('-'*10)
    d = [2, 4, 5, 6]
    for e in d:
        print(f's.push({e})')
        print('return from push:', s.push(e))
        show_stack(s)
        print('-'*10)


def test_pop():
    s = stack(3)
    s.content = [2, 4, 5]
    s.tos = 3
    show_stack(s)
    for i in range(s.capacity):
        d = s.pop()
        print('->', d)
        show_stack(s)
    d = s.pop()
    print('->', d)
    show_stack(s)


cmd = int(input())
if cmd == 1:
    test_init()
elif cmd == 2:
    test_str()
elif cmd == 3:
    test_push()
elif cmd == 4:
    test_pop()
elif cmd == 5:
    main()

def main():
    input = 12
    num_elves = input

    base = curr = Elf(1)
    for i in range(2, input + 1):
        curr.next = tmp = Elf(i)
        tmp.prev = curr
        curr = curr.next

    base.prev = curr
    curr.next = base

    while base.next != base:
        # base.val = base.val + base.next.val
        # base.next.val = 0
        offset = num_elves // 2
        iter = base
        for i in range(offset):
            iter = iter.next

        #print(f"Elf {base.number} pops {iter.number}")
        iter.prev.next = iter.next
        iter.next.prev = iter.prev

        num_elves -= 1

        base = base.next

    print(base.number)

class Elf:
    def __init__(self, number):
        self.number = number
        self.val = 1
        self.prev = None
        self.next = None


if __name__ == "__main__":
    main()
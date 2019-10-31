
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

if __name__ == "__main__":
    print(sum((1, 3, 4 ,2, 12, 4, 8)))

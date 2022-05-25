from app import bubble_sort
import random


def main():
    list1 = random.sample(range(10), 10)
    list2 = random.sample(range(1, 20), 8)
    list3 = random.sample(range(1, 50), 10)
    list4 = random.sample(range(1, 1000000), 10)
    list5 = random.sample(range(900000, 10000000), 20)
    list6 = random.sample(range(20), 20)

    lists = [list1, list2, list3, list4, list5, list6]
    passed = True
    for list in lists:
        if bubble_sort(list) != sorted(list):
            print(f"{bubble_sort(list)} is not the same as {sorted(list)}")
            passed = False

    if passed:
        print("All tests passed succesfully")

if __name__ == "__main__":
    main()

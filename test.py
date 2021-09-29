from tqdm import tqdm
from time import sleep

if __name__ == "__main__":
    print("go")

    my_bar = tqdm(total=100)
    #
    # for i in range(10):
    #     my_bar.update(10)
    #     sleep(1)

    my_bar.close()

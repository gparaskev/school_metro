import pandas as pd
import matplotlib.pyplot as plt
import random
import time


def coin_toss(n):
    result = []
    for i in range(n):
        result.append(random.randint(0, 1))
    df = pd.DataFrame(result, columns=["result"])
    df["result"].replace(to_replace={0: "head", 1: "tails"}, inplace=True)
    return df



if __name__ == '__main__':
    n = input("Χαίρεται, δώσε τον αριθμό των επαναλήψεων της στοχαστικής διαδικασίας \n")
    x = coin_toss(int(n)).value_counts()
    r = (abs(x[0] - x[1]))
    print(f"Κορώνα ήρθε {x[0]} φορές, ενώ γράμματα ήρθε {x[1]} ")
    print("Στο παράθυρο που θα ανοίξει φαίνονται τα αποτελέσματα της διαδικασίας σχηματικά")
    time.sleep(3)
    plt.show()




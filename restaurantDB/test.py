import pickle


def main():
    score = pickle.load(open('total_ratings.pkl', 'rb'))
    return score

if __name__ == '__main__':
    score = main()
    print(score)
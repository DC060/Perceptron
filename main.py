# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def load_data(file_path):
    data_list = []
    labels_list = []

    with open(file_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            values = line.strip().split(',')
            data = [float(x) for x in values[:-1]]
            label = values[-1]

            data_list.append(data)
            labels_list.append(label)

    return data_list, labels_list

def count_classes(labels_list):
    classes = set()
    for label in labels_list:
        classes.add(label)

    return classes

def random_weights(features_count):
    weights = []
    for i in range(features_count):
        weights.append(random.random())
    return weights



if __name__ == '__main__':

    train_data, train_labels = load_data("Resources/perceptron.data")
    test_data, test_labels = load_data("Resources/perceptron.test.data")
    features_count = len(train_data[0])
    class_count = len(count_classes(train_labels))
    weights = random_weights(features_count)
    learning_const = 0.01


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


def classes_to_numbers(values):
    value = values[0]
    labels_list = []
    for i in range(len(values)):
        if value == values[i]:
            labels_list.append(1)
        else:
            labels_list.append(0)
    return labels_list


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


def training_perceptron(data, labels, weights, learning_const, epochs):
    threshold = 0

    for epoch in range(epochs):
        for i in range(len(data)):
            x_i = data[i]
            l_i = labels[i]
            suma = sum([w * x for w, x in zip(weights, x_i)]) - threshold
            output = 1 if suma >= 0 else 0
            error = l_i - output
            weights = [w + learning_const * error * x for w, x in zip(weights, x_i)]
            threshold += error * learning_const

    return weights, threshold


def using_perceptron(data, labels, weights, threshold):
    guesses = 0

    for i in range(len(data)):
        x_i = data[i]
        l_i = labels[i]
        suma = sum([w * x for w, x in zip(weights, x_i)]) - threshold
        output = 1 if suma >= 0 else 0
        error = l_i - output
        guesses += 1 if error == 0 else 0

    return guesses / len(data) * 100


if __name__ == '__main__':
    train_data, train_labels = load_data("Resources/perceptron.data")
    test_data, test_labels = load_data("Resources/perceptron.test.data")

    features_count = len(train_data[0])
    class_count = len(count_classes(train_labels))
    weights = random_weights(features_count)

    print("Podaj stałą uczenia")
    learning_const = float(input())

    print("Czy chcesz podać własny wektor? [1 / 2]")
    user_in = input()
    while user_in == "1":
        vector = input()
        vector = vector.strip().split(',')
        data = [float(x) for x in vector[:-1]]
        test_data.append(data)
        test_labels.append(vector[-1])
        print("Czy chcesz dodać kolejny? [1 / 2]")
        user_in = input()

    train_labels = classes_to_numbers(train_labels)
    test_labels = classes_to_numbers(test_labels)

    output, threshold = training_perceptron(train_data, train_labels, weights, learning_const, 100)
    accuracy = using_perceptron(test_data, test_labels, output, threshold)
    print("Accuracy: " + str(accuracy) + "%")

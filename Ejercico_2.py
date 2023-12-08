import csv


def main():
    with open("trips_2023.csv", newline="") as file:
        next(file)
        document = csv.reader(file, delimiter=",")

        dict_hot = dict()

        for row in document:
            time_hour = int(row[3].split(" ")[1].split(":")[0])
            if time_hour >= 6 and time_hour < 12:
                if row[5] not in dict_hot:
                    dict_hot.setdefault(row[5], 1)
                else:
                    dict_hot[row[5]] += 1

        stations_sort = sorted(dict_hot.items(), key=lambda item: item[1], reverse=True)

        for i in range(3):
            print(stations_sort[i])


if __name__ == "__main__":
    main()

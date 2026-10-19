
import numpy as np


class DataAnalytics:

    total_analyzers_created = 0

    def __init__(self, values=None):
        self.__data = np.array(values) if values is not None else None
        DataAnalytics.total_analyzers_created += 1

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, values):
        self.__data = np.array(values)

    def __validate_data(self):
        if self.__data is None:
            raise ValueError("Please create an array before performing operations.")

    def index_element(self, position):
        self.__validate_data()
        return self.__data[position]

    def slice_array(self, selection):
        self.__validate_data()
        return self.__data[selection]

    def combine(self, values, axis=0):
        self.__validate_data()

        if axis == 0:
            return np.vstack((self.__data, values))

        return np.hstack((self.__data, values))

    def split(self, sections, axis=0):
        self.__validate_data()
        return np.array_split(self.__data, sections, axis=axis)

    def add(self, values):
        self.__validate_data()
        return np.add(self.__data, values)

    def subtract(self, values):
        self.__validate_data()
        return np.subtract(self.__data, values)

    def multiply(self, values):
        self.__validate_data()
        return np.multiply(self.__data, values)

    def divide(self, values):
        self.__validate_data()
        return np.divide(self.__data, values)

    def dot_product(self, values):
        self.__validate_data()
        return np.dot(self.__data, values)

    def matrix_multiply(self, values):
        self.__validate_data()
        return np.matmul(self.__data, values)

    def search_value(self, target):
        self.__validate_data()
        return np.where(self.__data == target)

    def sort_array(self, axis=-1, ascending=True):
        self.__validate_data()

        result = np.sort(self.__data, axis=axis)

        if ascending is False:
            result = np.flip(result, axis=axis)

        return result

    def filter_values(self, condition):
        self.__validate_data()

        if condition.startswith(">="):
            mask = self.__data >= float(condition[2:].strip())
        elif condition.startswith("<="):
            mask = self.__data <= float(condition[2:].strip())
        elif condition.startswith(">"):
            mask = self.__data > float(condition[1:].strip())
        elif condition.startswith("<"):
            mask = self.__data < float(condition[1:].strip())
        elif condition.startswith("!="):
            mask = self.__data != float(condition[2:].strip())
        elif condition.startswith("=="):
            mask = self.__data == float(condition[2:].strip())
        elif condition.startswith("="):
            mask = self.__data == float(condition[1:].strip())
        else:
            raise ValueError("Invalid filter condition.")

        return self.__data[mask]

    def get_sum(self):
        self.__validate_data()
        return np.sum(self.__data)

    def get_mean(self):
        self.__validate_data()
        return np.mean(self.__data)

    def get_median(self):
        self.__validate_data()
        return np.median(self.__data)

    def get_std(self):
        self.__validate_data()
        return np.std(self.__data)

    def get_variance(self):
        self.__validate_data()
        return np.var(self.__data)

    def get_min(self):
        self.__validate_data()
        return np.min(self.__data)

    def get_max(self):
        self.__validate_data()
        return np.max(self.__data)

    def get_percentile(self, percentile):
        self.__validate_data()
        return np.percentile(self.__data, percentile)

    def get_correlation(self, values):
        self.__validate_data()
        return np.corrcoef(self.__data.flatten(), values.flatten())

    @classmethod
    def get_instance_count(cls):
        return cls.total_analyzers_created

    @staticmethod
    def parse_range(range_text):
        parts = [
            int(item.strip()) if item.strip() else None
            for item in range_text.split(":")
        ]

        if len(parts) == 1:
            return slice(parts[0], parts[0] + 1)

        if len(parts) == 2:
            return slice(parts[0], parts[1])

        if len(parts) == 3:
            return slice(parts[0], parts[1], parts[2])

        return slice(None)


def read_values(count):
    entered_values = input(
        f"Enter {count} elements separated by spaces: "
    ).split()

    if len(entered_values) != count:
        raise ValueError(f"Please enter exactly {count} elements.")

    return np.array([
        float(value) if "." in value else int(value)
        for value in entered_values
    ])


def main():
    analyzer = DataAnalytics()

    print("Welcome to the NumPy Analyzer!")
    print("=" * 40)

    while True:
        print("\nMain Menu")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nArray Types")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")

            array_type = input("Select array type: ").strip()

            if array_type == "1":
                size = int(input("Enter number of elements: "))
                analyzer.data = read_values(size)

            elif array_type == "2":
                rows = int(input("Enter number of rows: "))
                columns = int(input("Enter number of columns: "))

                values = read_values(rows * columns)
                analyzer.data = values.reshape(rows, columns)

            elif array_type == "3":
                depth = int(input("Enter dimension 1: "))
                rows = int(input("Enter dimension 2 (rows): "))
                columns = int(input("Enter dimension 3 (columns): "))

                values = read_values(depth * rows * columns)
                analyzer.data = values.reshape(depth, rows, columns)

            else:
                print("Invalid array type.")
                continue

            print("\nCreated Array:")
            print(analyzer.data)

            while True:
                print("\n1. Indexing")
                print("2. Slicing")
                print("3. Go Back")

                operation = input("Select operation: ").strip()

                if operation == "1":
                    position = tuple(
                        map(
                            int,
                            input("Enter comma-separated indices: ").split(",")
                        )
                    )
                    print("Selected Element:", analyzer.index_element(position))

                elif operation == "2":
                    if analyzer.data.ndim == 1:
                        selected_range = input("Enter range (start:end): ")
                        print(
                            analyzer.slice_array(
                                DataAnalytics.parse_range(selected_range)
                            )
                        )

                    elif analyzer.data.ndim == 2:
                        row_range = input("Enter row range (start:end): ")
                        column_range = input("Enter column range (start:end): ")

                        row_slice = DataAnalytics.parse_range(row_range)
                        column_slice = DataAnalytics.parse_range(column_range)

                        print(
                            analyzer.slice_array(
                                (row_slice, column_slice)
                            )
                        )

                    else:
                        print("Slicing is available here for 1D and 2D arrays.")

                elif operation == "3":
                    break

                else:
                    print("Invalid operation.")

        elif choice == "2":
            if analyzer.data is None:
                print("Please create an array first!")
                continue

            print("\nMathematical Operations")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Dot Product / Matrix Multiplication")

            operation = input("Select operation: ").strip()
            values = read_values(analyzer.data.size)
            second_array = values.reshape(analyzer.data.shape)

            print("\nOriginal Array:\n", analyzer.data)
            print("Second Array:\n", second_array)

            if operation == "1":
                print("Addition Result:\n", analyzer.add(second_array))

            elif operation == "2":
                print("Subtraction Result:\n", analyzer.subtract(second_array))

            elif operation == "3":
                print("Multiplication Result:\n", analyzer.multiply(second_array))

            elif operation == "4":
                print("Division Result:\n", analyzer.divide(second_array))

            elif operation == "5":
                if analyzer.data.ndim == 2:
                    print(
                        "Matrix Multiplication Result:\n",
                        analyzer.matrix_multiply(second_array)
                    )
                else:
                    print(
                        "Dot Product Result:\n",
                        analyzer.dot_product(second_array)
                    )

            else:
                print("Invalid operation.")

        elif choice == "3":
            if analyzer.data is None:
                print("Please create an array first!")
                continue

            print("\n1. Combine Arrays")
            print("2. Split Array")

            operation = input("Select operation: ").strip()

            if operation == "1":
                values = read_values(analyzer.data.size)
                second_array = values.reshape(analyzer.data.shape)

                print("Original Array:\n", analyzer.data)
                print("Second Array:\n", second_array)

                print(
                    "Combined Array (Vertical Stack):\n",
                    analyzer.combine(second_array)
                )

            elif operation == "2":
                sections = int(input("Enter number of splits: "))
                result = analyzer.split(sections)

                print("\nSplit Arrays:")

                for number, part in enumerate(result, start=1):
                    print(f"Split {number}:\n{part}")

            else:
                print("Invalid operation.")

        elif choice == "4":
            if analyzer.data is None:
                print("Please create an array first!")
                continue

            print("\n1. Search a Value")
            print("2. Sort the Array")
            print("3. Filter Values")

            operation = input("Select operation: ").strip()

            if operation == "1":
                target = float(input("Enter value to search: "))
                print("Value Locations:", analyzer.search_value(target))

            elif operation == "2":
                print("Original Array:\n", analyzer.data)
                print("Sorted Array:\n", analyzer.sort_array())
                print("Sorting is applied along the last axis.")

            elif operation == "3":
                condition = input(
                    "Enter condition (e.g., > 20 or <= 50): "
                ).strip()

                print("Filtered Values:\n", analyzer.filter_values(condition))

            else:
                print("Invalid operation.")

        elif choice == "5":
            if analyzer.data is None:
                print("Please create an array first!")
                continue

            print("\nStatistical Operations")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Minimum and Maximum")
            print("7. Percentile")

            operation = input("Select operation: ").strip()

            print("\nOriginal Array:\n", analyzer.data)

            if operation == "1":
                print("Sum:", analyzer.get_sum())

            elif operation == "2":
                print("Mean:", analyzer.get_mean())

            elif operation == "3":
                print("Median:", analyzer.get_median())

            elif operation == "4":
                print("Standard Deviation:", analyzer.get_std())

            elif operation == "5":
                print("Variance:", analyzer.get_variance())

            elif operation == "6":
                print("Minimum:", analyzer.get_min())
                print("Maximum:", analyzer.get_max())

            elif operation == "7":
                percentile = float(
                    input("Enter percentile (0-100): ")
                )

                if 0 <= percentile <= 100:
                    print(
                        f"{percentile}th Percentile:",
                        analyzer.get_percentile(percentile)
                    )
                else:
                    print("Percentile must be between 0 and 100.")

            else:
                print("Invalid operation.")

        elif choice == "6":
            print("\nThank you for using the NumPy Analyzer!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Select between 1 and 6.")


if __name__ == "__main__":
    main()

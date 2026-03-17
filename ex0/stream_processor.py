from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def  format_output(self, result: str) -> str:
        return f"Output: Processed {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return(f"Processing data: {data}")
        
    def validate(self, data: Any) -> bool:
        self.data = data #store the data inside the object so i can use it in formatoutput
        if (type(data) == list and all(type(i) in (int, float) for i in data)) \
                or type(data) in (int, float):
            return True
        else:
            raise ValueError("Only lists of numbers and individual numbers are supported")

    def  format_output(self, result: str) -> str:
        data = self.data
        if type(data) == list:
            i = 0
            total = 0
            for element in data:
                i += 1
                total += element
            avg = str((total / i))
            i = str(i)
            total = str(total)
            result = f"{i} numeric values, sum={total}, avg={avg}"
        elif type(data) in (int , float):
            result = f"1 numeric value"
        return f"Processed {result}"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return(f"Processing data: \"{data}\"")

    def validate(self, data: Any) -> bool:
        self.data = data
        if type(data) == str:
            return True
        else:
            raise ValueError("Only strings are supported")

    def  format_output(self, result: str) -> str:
        data = self.data
        count_words = 1
        count_characters = 0
        for c in data:
            count_characters += 1
            if c == " ":
                count_words += 1
        count_characters = str(count_characters)
        count_words = str(count_words)
        result = f"{count_characters} characters, {count_words} words"
        return f"Processed text: {result}"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return(f"Processing data: \"{data}\"")

    def validate(self, data: Any) -> bool:
        self.data = data
        my_data = data.split(":")
        if my_data[0] == "ERROR" or my_data[0] == "INFO":
            return True
        else:
            raise ValueError("Only logs are supported")

    def  format_output(self, result: str) -> str:
        data = self.data
        my_data = data.split(":")
        if my_data[0] == "ERROR":
            format3 = f"[ALERT] {my_data[0]} level detected:{my_data[1]}"
        elif my_data[0] == "INFO":
            format3 = f"[INFO] {my_data[0]} level detected:{my_data[1]}"
        return f"{format3}"



if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    try:
        num = NumericProcessor()
        data1 = [1, 2, 3, 4, 5]
        s1 = num.process(data1)
        print(s1)
        if num.validate(data1):
            print("Validation: Numeric data verified")
        output1 = num.format_output("")
        print(f"Output: {output1}")
    except ValueError as e:
        print(e)


    print("\nInitializing Text Processor...")
    try:
        text = TextProcessor()
        data2 = "Hello Nexus World"
        s2 = text.process(data2)
        print(s2)
        if text.validate(data2):
            output2 = text.format_output("")
            print(f"Output: {output2}")
    except ValueError as e:
        print(e)


    print("\nInitializing Log Processor...")
    try:
        log = LogProcessor()
        data3 = "ERROR: Connection timeout"
        s3 = log.process(data3)
        print(s3)
        if log.validate(data3):
            print("Validation: Log entry verified")
            output3 = log.format_output("")
            print(f"Output: {output3}")
    except ValueError as e:
        print(e)
    

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    try:
        dataa = [
            (NumericProcessor(), [1, 2, 3]),
            (TextProcessor(), "hello yousra"),
            (LogProcessor(), "INFO: System ready")
            ]

        i = 1
        for d in dataa:
            if d[0].validate(d[1]):
                print(f"Result {i}: {d[0].format_output("")}")
    except ValueError as e:
        print(e)

    print("\nFoundation systems online. Nexus ready for advanced streams.")
        
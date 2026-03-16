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
        if (type(data) == list and all(type(i) in (int, float) for i in data)) \
                or type(data) in (int, float):
            return True
        else:
            raise ValueError("Only lists of numbers and individual numbers are supported")

    def  format_output(self, result: str) -> str:
        return f"Processed {result}"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return(f"Processing data: \"{data}\"")

    def validate(self, data: Any) -> bool:
        if type(data) == str:
            return True
        else:
            raise ValueError("Only strings are supported")

    def  format_output(self, result: str) -> str:
        return f"Processed {result}"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return(f"Processing data: \"{data}\"")

    def validate(self, data: Any) -> bool:
        my_data = data.split(":")
        if my_data[0] == "ERROR" or my_data[0] == "INFO":
            return True
        else:
            raise ValueError("Only logs are supported")

    def  format_output(self, result: str) -> str:
        my_data = result.split(":")
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
        if type(data1) == list:
            i = 0
            total = 0
            for element in data1:
                i += 1
                total += element
            avg = str((total / i))
            i = str(i)
            total = str(total)
            format1 = f"{i} numeric values, sum={total}, avg={avg}"
        elif type(data1) in (int , float):
            format1 = f"1 numeric value"
        output1 = num.format_output(format1)
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
            print("Validation: Text data verified")
            count_words = 1
            count_characters = 0
            for c in data2:
                count_characters += 1
                if c == " ":
                    count_words += 1
            count_characters = str(count_characters)
            count_words = str(count_words)
            format2 = f"{count_characters} characters, {count_words} words"
            output2 = text.format_output(format2)
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
            output3 = log.format_output(data3)
            print(f"Output: {output3}")
    except ValueError as e:
        print(e)
    

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

        try:
            dataa = [
                d1 = NumericProcessor(),
                d2 = TextProcessor(),
                d3 = LogProcessor()
            ]
            i = 0
            for d in dataa:
                d1.process
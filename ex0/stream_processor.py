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
        pass


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return(f"Processing data: {data}")
        
    def validate(self, data: Any) -> bool:
        if (isinstance(data, list) and all(isinstance(i, (int, float)) for i in data))\
                    or isinstance(data, (int, float)): 
                    return True
        else:
            raise ValueError("Only lists of numbers and individual numbers are supported")

    def  format_output(self, result: str) -> str:
        return f"Output: Processed {result}"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return(f"Processing data: {data}")

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

    def  format_output(self, result: str) -> str:
        return f"Output: Processed {result}"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def  format_output(self, result: str) -> str:
        pass




    if __name__ == "__main__":
        try:
            num = NumericProcessor()
            data1 = [1, 2, 3, 4, 5]
            s1 = num.process(data1)
            print(s1)
            if num.validate(data1):
                print("Validation: Numeric data verified")
            if isinstance(data1,list):
                i = 0
                total = 0
                for element in data1:
                    i += 1
                    total += element
                avg = str((total / i))
                i = str(i)
                total = str(total)
                format1 = f"{i} numeric values, sum={total}, avg={avg}"
            elif isinstance(data1, (int , float)):
                format1 = f"1 numeric value"
            output1 = num.format_output(format1)
            print(output1)
        except ValueError as e:
            print(e)
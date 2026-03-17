class NumericProcessor:
    def process(self, data: Any) -> str:
        return(f"Processing data: {data}")
        
    def validate(self, data: Any) -> bool:
        self.data = data
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
    
if __name__ == "__main__":
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
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):
    def __init__(self, stream_id: str, type:str):
        self.stream_id = stream_id
        self.type = type
        self.count_data = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str, type:str):
        super().__init__(stream_id, type)
        self.avg = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.count_data = 0
        count = 0
        total = 0
        for d in data_batch:
            for k, v in d.items():
                self.count_data += 1
                if k == "temp":
                    count += 1
                    total += v
            
        self.avg = total / count
            
        # print("\nInitializing Sensor Stream...")
        # print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        formatted = [f"{k}:{v}" for d in data_batch for k, v in d.items()]
        return f"\nInitializing Sensor Stream...\
            Stream ID: {self.stream_id}, Type: {self.type}\
            Processing sensor batch: {formatted}"
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "total": self.count_data,
            "avg": self.avg
        }

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return [d for d in data_batch if any(v > 25 for v in d.values())]


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, type:str):
        super().__init__(stream_id, type)
        self.net = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.count_data = 0
        self.net = 0
        for d in data_batch:
            for k, v in d.items():
                self.count_data += 1
                if k == "buy":
                    self.net += v
                elif k == "sell":
                    self.net -= v
                    
        # print("\nInitializing Transaction Stream...")
        # print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        formatted = [f"{k}:{v}" for d in data_batch for k, v in d.items()]
        return f"\nInitializing Transaction Stream...\
            Stream ID: {self.stream_id}, Type: {self.type}\
            Processing transaction batch: {formatted}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "total": self.count_data,
            "net": self.net
        }

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return [d for d in data_batch if any(v > 100 for v in d.values())]


class EventStream(DataStream):
    def __init__(self, stream_id: str, type:str):
        super().__init__(stream_id, type)
        self.error = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.count_data = 0
        self.error = 0
        for value in data_batch:
            self.count_data += 1
            if value == "error":
                self.error += 1
                    
        # print("\nInitializing Event Stream...")
        # print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        return f"\nInitializing Event Stream...\
                Stream ID: {self.stream_id}, Type: {self.type}\
                Processing event batch: {data_batch}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "total": self.count_data,
            "error": self.error
        }

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return [e for e in data_batch if e == "error"]


class StreamProcessor:
    def __init__(self):
        self.streams: List[tuple] = []

    def add_stream(self, stream:DataStream, dataa):
        self.streams.append((stream, dataa))

    def proccess_all(self):
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
        for stream, data in self.streams:
            text = stream.process_batch(data)
            print(text)
            stats = stream.get_stats()

            if isinstance(stream, SensorStream):
                print(f"Sensor analysis: {stats['total']} readings processed, avg temp: {stats['avg']}°C")
            elif isinstance(stream, TransactionStream):
                net = stats['net']
                sign = "+" if net > 0 else ""
                print(f"Transaction analysis: {stats['total']} operations, net flow: {sign}{net} units")
            elif isinstance(stream, EventStream):
                print(f"Event analysis: {stats['total']} events, {stats['error']} error detected")

    def process_second_batch(self, second_batches: List[tuple]):
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        
        print("\nBatch 1 Results:")
        for stream, data in second_batches:
            stream.process_batch(data)
            stats = stream.get_stats()
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {stats['total']} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {stats['total']} operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {stats['total']} events processed")

    def apply_filters(self):
        print("\nStream filtering active: High-priority data only")
        for stream, data in self.streams:
            filtered = stream.filter_data(data)
            count = 0
            for _ in filtered:
                count += 1
            if isinstance(stream, SensorStream):
                print(f"Filtered results: {count} critical sensor alerts, ", end="")
            elif isinstance(stream, TransactionStream):
                print(f"{count} large transaction")
        print("\nAll streams processed successfully. Nexus throughput optimal.")



if __name__ == "__main__":
    sen = SensorStream("SENSOR_001", "Enrironmental Data")
    tran = TransactionStream("TRANS_001", "Financial Data")
    event = EventStream("EVENT_001", "System Events")

    pros = StreamProcessor()
    pros.add_stream(sen, [{"temp":22.5}, {"humidity":65}, {"pressure":1013}])
    pros.add_stream(tran, [{"buy":100}, {"sell":150}, {"buy":75}])
    pros.add_stream(event, ["login", "error", "logout"])

    pros.proccess_all()

    pros.process_second_batch([
    (sen, [{"temp": 30.0}, {"temp": 28.5}]),
    (tran, [{"buy": 50}, {"sell": 20}, {"buy": 30}, {"sell": 10}]),
    (event, ["login", "logout", "error"])
])
    pros.apply_filters()
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):
    def __init__(self, stream_id: str, type:str):
        self.stream_id = stream_id
        self.type = type

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
        count = 0
        for el in data_batch:
            count += 1
            
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        formatted = [f"{k}:{v}" for d in data_batch for k, v in d.items()]
        return f"Processing sensor batch: {formatted}"
    

class TransactionStream(DataStream):
    def __init__(self, stream_id: str, type:str):
        super().__init__(stream_id, type)
        self.net = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        formatted = [f"{k}:{v}" for d in data_batch for k, v in d.items()]
        return f"Processing transaction batch: {formatted}"


class EventStream(DataStream):
    def __init__(self, stream_id: str, type:str):
        super().__init__(stream_id, type)
        self.error = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        return f"Processing event batch: {data_batch}"


class StreamProcessor:
    def __init__(self):
        self.streams: List[tuple] = []

    def add_stream(self, stream:DataStream, dataa):
        self.streams.append((stream, dataa))

    def proccess_all(self):
        for stream, data in self.streams:
            text = stream.process_batch(data)
            print(text)


sen = SensorStream("SENSOR_001", "Enrironmental Data")
tran = TransactionStream("TRANS_001", "Financial Data")
event = EventStream("EVENT_001", "System Events")

pros = StreamProcessor()
pros.add_stream(sen, [{"temp":22.5}, {"humidity":65}, {"pressure":1013}])
pros.add_stream(tran, [{"buy":100}, {"sell":150}, {"buy":75}])
pros.add_stream(event, ["login", "error", "logout"])

pros.proccess_all()
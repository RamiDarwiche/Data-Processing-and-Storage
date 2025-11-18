class InMemoryDB:

    def __init__(self):
        self.database: dict = {}
        self.transaction_queue: dict = {}
        self.is_transacting: bool = False

    def begin_transaction(self) -> None:
        if self.is_transacting:
            raise RuntimeError("A transaction is already open")
        
        self.is_transacting = True
        self.transaction_queue = {}
        return print("Transaction began")


    def put(self, key, value) -> tuple:
        if not self.is_transacting:
            raise RuntimeError("A transaction must be started before inserting key-value pairs")
        
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        
        self.transaction_queue[key] = value
        return (key, value)



    def get(self, key) -> object:
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        
        if key not in self.database:
            return None

        return self.database[key]


    def commit(self) -> None:
        if not self.is_transacting:
            raise RuntimeError("A transaction has not been started")
        
        for key, value in self.transaction_queue.items():
            self.database[key] = value

        self.transaction_queue = {}
        self.is_transacting = False
        print("Commit successful") 


    def rollback(self) -> None:
        if not self.is_transacting:
            raise RuntimeError("A transaction has not been started")
        
        self.transaction_queue = {}
        self.is_transacting = False
        print("Rollback successful")

def main():
    inmemoryDB = InMemoryDB()
    inmemoryDB.begin_transaction();
    inmemoryDB.put("A", 5);
    inmemoryDB.get("A")
    inmemoryDB.put("A", 6)
    inmemoryDB.commit()
    inmemoryDB.get("A");


if __name__ == "__main__":
    main()
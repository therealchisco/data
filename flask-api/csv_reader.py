import pandas as pd

class CsvReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self, chunksize):
        chunks = pd.read_csv(self.file_path, chunksize=chunksize)
        return chunks

class CsvProcessor:
    def __init__(self, file_path, chunksize):
        self.reader = CsvReader(file_path)
        self.chunks = self.reader.read_csv(chunksize)
        self.iterable_chunks = iter(self.chunks)
    
    def __transform_chunk(self, chunk):
        # Here we are removing the columns
        # that are irrelevant from the chunk
        # DataFrame
        transformed_chunk = chunk.iloc[:,3:]
        return transformed_chunk

    def __process_next_chunk(self):
        # We try to iterate the chunks until exhausted
        try:
            chunk = next(self.iterable_chunks)
        except StopIteration:
            print("End of File and Iterator")
            chunk = None
        if chunk is not None:
            chunk = self.__transform_chunk(chunk)
        return chunk
    
    def json_chunk(self):
        # Here we create a DataFrame chunk
        # and use the to_json from the pandas library to
        # return it as JSON for our API
        self.chunk = self.__process_next_chunk()
        self.chunk = self.__transform_chunk(self.chunk)
        return self.chunk.to_json(orient='records')
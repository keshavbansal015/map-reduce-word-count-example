from mrjob.job import MRJob

class MRWordCount(MRJob):

    def mapper(self, _, line):
        # Splitting the line into words and yielding each with a count of 1
        for word in line.split():
            yield word, 1

    def reducer(self, word, counts):
        # Summing up all the counts for the word
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()
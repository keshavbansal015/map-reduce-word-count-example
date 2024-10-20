## Word Count

#### Problem
count the frequency of words in files

#### Workflow
- Mapper: split each record (line) into words  
input: <offset, line>  
output: <word, 1>

- Reducer: sum up the count for each word  
input: <word, (1, 1, ...)>  
output: <word, count>

#### Run the following commands to run the project:
##### Make sure to delete the "output" directory before you run it

For Java example, cd into the WordCount-Java directory and run these commands:
```
mvn clean install
hadoop jar target/WordCount-1.0-SNAPSHOT.jar Driver ../input/sample1.txt output
````

For Python example, cd into the WordCount-Python directory and run this:
```
pip install mrjob
python WordCount.py ../input/sample2.txt > output.txt
```

- You can experiment with changing the input file.

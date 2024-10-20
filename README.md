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
`shell
mvn clean install
hadoop jar target/WordCount-1.0-SNAPSHOT.jar Driver input/sample1.txt output
`
#/bin/sh
hadoop fs -put /home/hadoop/results.csv /user/hadoop/
hadoop fs -rmr /user/hadoop/output
hadoop jar /etc/hadoop-2.2.0/share/hadoop/tools/lib/hadoop-streaming-2.2.0.jar -file /home/hadoop/mapper.py -mapper /home/hadoop/mapper.py -file /home/hadoop/reducer.py -reducer /home/hadoop/reducer.py -input /user/hadoop/* -output /user/hadoop/output
hadoop fs -get /user/hadoop/output/part-00000 .
sort -rg part-00000 > out.log

# kafka-reassign-partitions-json-maker
this is a script that generates a json to perform a manual kafka reassign partitions


usage:
/bin/python3 kafka-partitions-json-generator.py [topic_name] [number of partition] [number of brokers (leaders)] [number of replica]

examle for a topic named my_topic with 30 partitions, 5 brokers and replica 3:
/bin/python3 kafka-partitions-json-generator.py my_topic 30 5 3

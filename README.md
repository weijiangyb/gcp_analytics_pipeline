# gcp_analytics_pipeline

How to build an analytics pipeline in Google Cloud Platform

In this short project, I would like to showcase how to pull data from a third part platform, load the data into a data warehouse, and build a dashboard in a quick way. In this short example, I will use CoinCap API as the data source.
![alt text](https://miro.medium.com/max/1400/1*aqCo6WTXTGAlbnxwkuWX6A.jpeg)


Pub/Sub: Pub/Sub offers similar functionality to Apache Kafka that message topics.
Google Cloud Storage: Goole Cloud Storage works as a temporary storage while the pipeline sends data into the warehouse.
BigQuery: BigQuery supports standard SQL syntax and allows easy connection with data analytics platforms for further business insights.
Cloud Dataflow: In Google Cloud Dataflow, we can define pipelines with an Apache Beam program. Dataflow also offers templates without coding. In this project, I would use the “Pub/sub topic to BigQuery” template to build a pipeline in few minutes.
ETL Code:
(1). get_exchange_data function pulls data from CoinCap API.
PubSubPublisher Class defines Pub/Sub classes that uses publish() method that publishes messages to Pub/Sub.
(2). get_exchange_data() function pulls data from CoinCap API

2. Create BigQuery Dataset and Table
(1).In the BigQuery UI, click 3 dots in the right side of the project id and click create dataset. Name the dataset id and click CREATE DATASET.
![alt text](https://miro.medium.com/max/1400/1*AgZ1GQrfmPrPgd7foju-6g.png)
(2).Open the dataset created above, click CREATE TABLE, name the table, and define table schema.
![alt text](https://miro.medium.com/max/1400/1*ZYHSdz3BBPMr1oBGelZ9MA.png)

3. Create Google Cloud Storage
In the Cloud Storage UI, click CREATE BUCKET, name the bucket, and click CREATE BUCKET.
![alt text](https://miro.medium.com/max/1400/1*J1EEILFuWWMsKwPbQXoLmw.png)

4. Create Pub/Sub Topic
In the Pub/Sub — Topic UI, click CREATE TOPIC and name the topic.
![alt text](https://miro.medium.com/max/1400/1*oCJSWI1sh7lby3A6ieI4PQ.png)

5. Build data pipeline using Dataflow template.
In the Dataflow UI, click CREATE DATAFLOW, name the Dataflow, select the Dataflow template and fill in the other required parameters. The “Pub/Sub Topic to BigQuery” template automatically connects the created topic with subscribers and build data pipeline from Pub/Sub to BigQuery without programming in Apache Beam.
![alt text](https://miro.medium.com/max/1400/1*WLUbS2_bmh932uVApCr0tA.png)
![alt text](https://miro.medium.com/max/1400/1*B0Rhr90ScVKSv_m3q3nfXA.png)

6.Connect BigQuery data to DataStudio and build live Dashboard
Goole DataStudio allows data connections between BigQuery and dashboards. In this example, I used a simple SQL syntax to pull the latest Cryptocurrency Exchange from BigQuery to DataStudio.
![alt text](https://miro.medium.com/max/1400/1*euakoAI5PmFRo_sASTumag.png)

Cryptocurrency exchanges rank dashboard:
https://datastudio.google.com/s/ia2fugDiKgI

![alt text](https://miro.medium.com/max/1400/1*7YyVTgXw5QC_3oEahv5h0A.png)

Future works:
In this project example, I didn’t build a real-time pipeline that updates real-time cryptocurrency data in the dashboard. This function can be accomplished by scheduling the “sample.py” job in the Cloud Composer built in Apache Airflow.








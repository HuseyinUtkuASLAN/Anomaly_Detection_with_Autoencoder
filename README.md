# Anomaly Detection with Autoencoder

Inspired by [Vegard Flovik's post on Medium](https://towardsdatascience.com/how-to-use-machine-learning-for-anomaly-detection-and-condition-monitoring-6742f82900d7)<br>
Data from [here](http://data-acoustics.com/measurements/bearing-faults/bearing-4/)
### Purpose:
We try to detect anomalies from "IMS Bearing Data". We used "Test1" data which has 8 channels;
<br><br>
Bearing 1 – Ch 1&2; Bearing 2 – Ch 3&4;<br>
Bearing 3 – Ch 5&6; Bearing 4 – Ch 7&8. <br>
<br>
Data recorded every 10 minutes (except the first 43 files were taken every 5 minutes).
<br>
At the end of the test-to-failure experiment, inner race defect occurred inbearing 3 and roller element defect in bearing 4.
#### Steps:
1. prepare data
2. visualize data
3. build autoencoder ANN
4. get results
5. ...
6. profit?
### How to run?
1. Create "data" folder.
2. Download data from [here](http://data-acoustics.com/measurements/bearing-faults/bearing-4/).
3. unzip "1st_test" folder to "data" folder we created.
4. run "anomaly_detection.ipynb" bu jupyter notebook.
<br>
Why I didn't automated downloading and unzipping? Because I was too lazy!

### What to do next?
1. Improve training accuracy (maybe after many steps, we can reach some kind of overfit which might be good for this task)

## Exercise 1:
max_bright value: 45000
min_bright value: 20000

We tested this in a fairly bright photonics lab room, so to achieve a dim light we considered casting a shadow with our hand over the photocell to qualify, and the value of 20000 for min_bright corresponded to a 0% duty cycle of the led when shadowing the photocell. 

The max bright value we found was 45000 and when shining a phone flashlight, with which we were able to achieve around 100% duty cycle with the led.

Here is a link to a video demonstrating functionality: https://drive.google.com/file/d/1MD91R06Ij8we5C2N15FImy1ggMwsIcr8/view?usp=sharing

And here is a sample screenshot of what our outputs looked like:

<img width="1444" alt="Screenshot 2024-09-16 at 8 28 27 PM" src="https://github.com/user-attachments/assets/f5f1e54d-9564-4941-86b1-f11adec7f790">


## Exercise 2:
We decided to play 'happy birthday'  using an array of frequencies and iterating through this array while simultaneously iterating through a second array for sound durations. We also added intermediate low frequencies to mimic pauses to make the song more accurate to the original.

Here is a link to a video of the speaker playing:
https://drive.google.com/file/d/1PU2-k-kd_ZVdn1fpAKioR1oSaS4RHwXk/view?usp=sharing

## Exercise 3: 
The two of us each took on one part of the exercise. Nikhil handled the computations stipulated in question 1, and Louis handled the cloud component stipulated in question 2. 

Nikhil included dictionary entries for the average reaction time, max time, min time, and score, doing the appropriate calculations with the variables given.

Louis set up a realtime database through Firebase and added code to connect the Pi Pico to a wireless network (we used an iPhone hotspot), as well as code to post the data from the dictionary to the database. 

We chose Firebase simply because it was recommended to us by the Professors. However, it came with the advantage of being free for small sets of data like ours. Furthermore, we were able to add multiple users to the database. Here is a screenshot showing multiple users on the database:

<img width="949" alt="Screenshot 2024-09-15 at 3 50 06 PM" src="https://github.com/user-attachments/assets/195aa16f-5d9a-4518-8aa3-a363bd265895">

The latter two users are our BU accounts -- the first account is Louis's personal email, which was needed to set up the database due to restrictions placed on BU email accounts surrounding creating projects through Google.

Here is a screenshot of what the database looks like. In this example, there are 4 different test cases posted (2 expanded, 2 collapsed) where all of the required data points are viewable:

<img width="1123" alt="Screenshot 2024-09-15 at 3 54 42 PM" src="https://github.com/user-attachments/assets/a1afbb3c-c7c9-47c3-a7d2-794abe5b190c">

We also added email/password identification. Here is a sample email we added for test purposes:
<img width="951" alt="Screenshot 2024-09-17 at 5 27 07 PM" src="https://github.com/user-attachments/assets/94494cda-d5e0-48f1-be95-8f7427f72164">


This is what our console looks like if authentication is successful:
<img width="626" alt="Screenshot 2024-09-17 at 5 22 06 PM" src="https://github.com/user-attachments/assets/20ec7096-14cd-4a54-b65c-6ea785a60fa9">


And this is what it looks like if authentication fails. Although a json is written, no data is uploaded.
<img width="1326" alt="Screenshot 2024-09-17 at 5 26 26 PM" src="https://github.com/user-attachments/assets/0a6100cf-5eef-4f22-9734-dedd3994e7c9">


Lastly, here is a video demonstrating functionality and showing the database update: https://drive.google.com/file/d/1mjBd9Gwlzm3PsBrJByQgrdvRtoOMUg8I/view?usp=sharing 

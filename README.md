# Smart Love Note 
This was an anniversary project for my girlfriend on our one year. Using a raspberry pi zero and a 2.9 inch E-paper display. The device output a message to a 2.9 inch E-Paper display updating multiple times a day with the ability to override the scheduled message displays. The stored text file can be added to and overridden for a 12 hour period. 

## Email   
I started learning about how to pull emails from the Gmail client.
Using an article by [Humberto Rochas,](https://humberto.io/blog/sending-and-receiving-emails-with-python/) on sending and receiving emails with python gave me a great start for getting emails from gmail to python. 

In order to get past Googles security I had to push past the security. To do that I navigated to 
````Google Account settings > Security > Less Secure App Access ```` at the bottom of the page, set that to __on__. This got me past the ````[AUTHENTICATIONFAILED] Invalid credentials (Failure)```` error that Rochas example was giving me. 

As for using the IMAP python function I found [this article](https://github.com/ikvk/imap_tools) very helpful with IMAP formatting. From there I was able to find a way to pull emails filtered my my name.

I ended up using two imap.search functions that worked for me. The first was helpful for reading emails specifically from my personal email to the project email, the second focused on the emails from me as well as making sure they were unread. Once read by the search function the email would be marked as read which is very helpful for the final product but not helpful for the testing phases of the code. 

````
status, data = mail.search(None, 'FROM Jamie') #use for testing
status, data = mail.search(None, 'FROM Jamie UNSEEN') #use for final version that will uncheck email
````

## E-Paper Display

This was a difficult part of coding for me, and out of my comfort zone for the most part. I had a lot of help from software engineer roommates and the manufacture website for the model of e-Paper display I had, the [2.9inch e-Paper Module B](https://www.waveshare.com/wiki/2.9inch_e-Paper_Module_(B)) was very helpful. Using the given example code for the display, I had a solid foundation for starting my love note output. Rather than creating something from scratch, I whiddled down the parts of the example code that worked for me. 

## Case

This was one of the areas that I was more comfortable in at the beginning of this project. I used OnShape a free CAD software with tons of video tutorials online. 

Most of the design process involved measurements. Most of my time was spent using calipers and measuring things multiple times, however these schematics for the [raspberry pi zero](https://i.stack.imgur.com/LHeqV.png), and the [e-Paper display](https://www.waveshare.com/img/devkit/LCD/2.9inch-e-Paper-Module/2.9inch-e-Paper-Module-size.jpg) from the manufacture website were very helpful.
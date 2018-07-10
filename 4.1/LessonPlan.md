## 4.1 Lesson Plan - Psst... Intro to Cryptography

### Overview

In today's class, students will receive their first exposure to the cryptography and encryption. They will spend a major portion of class focused on the Caesar cipher, learning it's basic mechanism, implementing it in code, and discussing the vulnerabilities present within it.   

### Class Objectives

* Students should be able to clearly define the words: "Cryptography", "Encryption". "Decryption", "Ciphertext", "Plaintext", and "Cipher Key".

* Students should be able to explain how the Caesar cipher works.

* Students should become more confident working in Python and understand, at a high-level, how the Python implementation of the Caesar cipher works. 

* Students should understand fundamentally how ciphers can be cracked and specifically explain why the Caesar cipher is vulnerable to brute force attacks.

### Instructor Notes

* Today's class marks students' first foray into the classic security topic of cryptography. Today's class centers around the Caesar cipher, a simple encryption mechanism that offers students an accessible foothold to the field. 

* Today's class is primarily split between thought exercises and code implementation. Treat each of these components as equally important. Let students know that the coding exercise is meant for them to reinforce their Python skills and help them understand how encryption can be implemented in practice. 

* Make an extra effort to stay on track of time. While many of your students will  struggle with the final step of the Caesar implementation, be sure to leave time for the final thought exercise ("The Barbarians Got Mail"). The exercise is both fun and *critical* for students to understand how ciphers can be cracked. For students wanting to spend more time on the coding exercise, offer to host a review during office hours. 

* Today's PowerPoint includes a number of quick engagement exercises meant to stimulate interaction in the classroom. Be sure to familiarize yourself with the slides thoroughly prior to class. 

* As always, have your TAs refer to the [Time Tracker](../Unit4_Cryptography.xlsx) to stay on track.

------

### 1. Instructor Do: Intro to Encryption and Caesar Cipher  (0:15)

* Begin class by presenting the [PowerPoint](Psst_Intro_to_Cryptography.pptx) slide sections titled "Intro to Encryption" and "The Caesar Cipher." These sections offer a high-level introduction to the concept of cryptography, its historic context, and the mechanism behind the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

* Make sure to cover the Caesar cipher's mechanism in depth. It is easy for students to *think* they understand how it works, only to be totally stumped when asked to implement it on their own. 

* Use the slides to guide your narrative and when prompted use the "Quick Activity!" slides to create moments of class engagement. 

![image-20180708233825908](assets/01-Crypto.png)

![image-20180708233622254](assets/02-Crypto.png)


### 2. Students Do: Caesar's Minions (0:10)

* When you arrive at the first formal activity ("Caesar's Minions"), break students into pairs of two. Then send them the following instructions (also specified on the slide):
  
  * **Instructions:**
   
    * Take a few moments to do the following:

      * Explain to your neighbor in 2-3 sentences how the Caesar Cipher works. 
      * Next write a one sentence message (hidden from your partner). 
      * Specify a shift-key and use it to encode the message.
      * Then provide your partner the encoded message and key.
      * Have your partner use the key to decode the intended message. Confirm that they were correct.
  
  * **Notes**: 

    * Use only this link <http://inventwithpython.com/cipherwheel/> to do your encoding / decoding. 

### 3. Instructor Do: Review the Caesar Cipher Decoder Ring  (0:05)

* Take a moment to review the activity as a class. Specifically:
  
  * Ask students to articulate how the Caesar cipher works to you. Be sure to nudge them into offering a precise answer. (Answer: The Caesar cipher uses a letter shift substitution. The shift is determined by the key value.)
  
  * Ask one student to share their message and key with you. Then decode the message live. It's a simple way to create a bit of fun from the stage.

### 4. Instructor Do: Caesar Cipher… In Code (Overview)  (0:05)

* Next, take a few moments to introduce students to their coming challenge: implementing the Caesar cipher in code. Let students know that they will be taking this challenge on in smaller steps. 

![image-20180708234513952](assets/03-Crypto.png)

### 5. Students Do: Planning Caesar's Attack   (0:07)

* When prompted have students take a few moments to pseudocode their plan of attack in implementing the Caesar cipher. Encourage students to keep it simple -* specifying no more than 3-5 of the most critical steps in the process.

*  Then send them the following (also specified on the slide) 

  * **Instructions:**

    * Take the next few moments to pseudocode an approach to building Caesar.py with your neighbor.
    * Specifically, try to break down the problem into 3-5 steps. 
    * Be thinking of concepts you’ve used in Python (for-loops, functions, variables) in selecting your steps.
    * Be prepared to share!

### 6. Instructor Do: Review Planning Caesar's Attack  (0:05)

* Provide students a few moments to share their responses. Offer encouragement and nudges for clarification as they do so. Then use the slides provided to offer your own suggested strategy. 

![image-20180708234513952](assets/04-Crypto.png)

### 7. Students Do: Python Vowel Replacer  (0:12)

* Now it's time to switch away from the PowerPoint temporarily and into the code editor.

* Send students the following as a first step in implementing the Caesar cipher.  

  * **Instructions:**

    * XXX

  * **Hints:**

    * XXX

### 8. Instructor Do: Review Python Vowel Replacer (0:10)

* Next, take a few moments to review the solution. As you do, use the below talking points to guide your discussion:
  
  * XXX

  * XXX

  * XXX

### 9. Instructor Do: Python Vowel Replacer with Dicts (0:10)

* Next, show students how their previous code could be re-written using Python dictionaries. 

* Open the solution file provided and use the below talking points to guide your discussion:

  * XXX

  * XXX

  * XXX

* Send students your solution file once you have completed your review.

### 10.  Students Do: Python Letter to Numbers with Dicts  (0:15)

* Next, students will expand the example you provided to map every single letter to its numeric reference.

* Send students the following instructions to guide them on the next step:

  * **Instructions:**

    * XXX

  * **Hints:**

    * XXX

### 11.  Instructor Do: Review Python Letter to Number with Dicts  (0:10)

* Once time is up, review the exercise using the below talking points to guide your discussion:

  * XXX

  * XXX

  * XXX

* Answer any questions that remain, before sharing your solution.

-------

### 12.  BREAK (0:15)

-------

### 13.  Students Do: Python Dynamic Caesar Cipher (0:20)

* This next activity will be the most challenging for many of your students as they will be tasked with  modifying their previous code to handle various cipher key values. The  implementation will require a bit of logic and creative problem solving, but is well within their skill range.

* Send students the following instructions to guide them on the next step:

  * **Instructions:**

    * XXX

  * **Hints:**

    * XXX

### 14.  Instructor Review: Python Dynamic Caesar Cipher (0:10)

* Once time is up, spend the time necessary to review this solution in-depth.

* Open the provided solution and use the below talking points to guide your discussion:

  * XXX

  * XXX

  * XXX

* Answer any questions that remain, before sharing your solution.

### 15.  Instructor Do: Caesar's Vulnerabilities (0:05)

* Now, return back to the PowerPoint to the section titled Caesar's Vulnerabilities. Then use the slides provided to kick-off the coming thought exercise on cracking the Caesar cipher. 

* Don't give away the answer just yet! Give students a chance to figure it out themselves!

![image-20180708234513952](assets/05-Crypto.png)

### 16.  Students Do: The Barbarian's Got Mail (0:15)

* When prompted have students work with their neighbor on the final thought-exercise. 

* Send the following instructions to students (also specified on the slide):

  * **Instructions:**

    * Work with your neighbor to play out each of the following:

      * *Red Team – You Are the Barbarians*:

        * You’ve successfully (and bloodily) secured one of Caesar’s messages. 

        * However, it reads like gibberish. In fact it says: “olhklk av aol ypcly mvy h zvsv chjhf. zll fvb shaly!”. Figure out a way to determine it’s meaning. 

        * Be ready to share your approach with the general.

      * *Blue Team – You Are Caesar*:

        * The Barbarians have successfully obtained Caesar’s most recent (encrypted) message! Outline a series of steps to assess the risk  and prevent future impact.

        * Specifically come up with at least 5 assessment questions to ask and 5 proposals.

        * Be ready to share your approach with Caesar!
 
### 17.  Instructor Do: Review the Barbarian's Got Mail  (0:05)

* Have students share a few of their solutions prior to sharing the solution provided. 

* Use the below talking points in explaining the Red-Team solution:

  * Because of the limited number of shift possibilities (0-25), a persistent intruder can simply try every option. The option that reads like plain text is thus the intended message. Code implementations can further speed this process up by using functions for confirming that words are English -- thus ruling out all of the gibberish options. 

  * Because the cipher key for encryption is the same as for decryption, the intruder who uses brute force is thus able to retrieve the cipher for all future communication interceptions. Later, we'll be talking about various means to improve security against such intrusions. 

  ![image-20180708234513952](assets/06-Crypto.png)

* Use the below talking points in explaining the Blue-Team solution:
  
  * As a Blue Team defender, we don't always have the ability to prevent or avoid interception altogether. Instead, we often need to plan for the worst. In this case, this means considering a reality that messages will frequently be intercepted and either our cipher needs to be more secure or we need to reduce critical communication along the faulty channel.
  
  * Feel encouraged to expand on this answer with stories or cases from your own work experience. 

### 18.  Instructor Do: Prelude Next Class (0:05)

* Finally, use the last slides of the presentation to conclude class. 

* Encourage students to recognize that they've done well if they can articulate a working definitions of cryptography, the mechanism behind the Caesar cipher, and the idea of "cracking" a cipher using brute force.

* Let students know that they will be learning how to strengthen our cipher next time, before dismissing them for the evening.

-------

### Copyright

Trilogy Education Services © 2018. All Rights Reserved.
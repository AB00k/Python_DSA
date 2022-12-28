"""
       despite belonging to ultra conservative socity i'm open to new experienses and i have struggled hard to get
       quality education from multi cultural and mlti ethenic pertegious institute of pakastan to pursue my dreams to
       attain equal rights in the socity for all the members in the socity specilly women comming into an entirly
       different culture was challanging but i realized my petential when i got 3.95 gpa in first semester . it was a
       turing point as i started believin in my potential and in my hard work . i have remaind an active and enrgetic
       student from the very begining i have won many quiz , debates , drama and painting competitions. i have atended
       many exibitions and represented my region. working with university level socities helpesd me to my communications
       and leadership skills . i have developed team work qualities through sports like cricket and football and basketball
       ets.i have also worked as girls sports incharge ans assistant editor for my department megazine 'expressions'
       with the growing power of social media the youth of our region have shown to much interest in political activities
       as a political scintist i want to lead and guide this political activism in the right direction to achive our
       consitutinol rights through our fruitful dialog and discussions . america being a political divrsed and stable
       nation will provide a platform to anlize and identify the reason for a better goveronmental sysstem . it'll
       also give me a chance to interact with students with diverse background to share my culture and nons with them"""
import math

import data as data

""" 
     
      i'm open to new experiences to pursue my dream to become one of the computer scientists who adapt technology to 
      help the human race evolve. I find it intriguing that how fast society has
      been shaped by the influence of Computer Science.  A few years ago if someone were to have 
      claimed that cars would become autonomous, people would have doubted them. Now we are at a stage where nearly 
      anything is possible and this is due to the relentless problem solving of computer scientists.I have been teaching myself python in my spare time
      and have completed online courses in python programming and DS&Algorithms in pyton, 
      which have allowed me to explore the endless possibilities that computer science can bring to the world.I have 
      remained an active and energetic student from the very beginning i have won many quiz competitions and remained 
      CR(class representative) for 6 years of studies at school and college level. I have developed team work qualities
      through sports like cricket and football and basketball etc.
      I am inspired by the fact that computer science has become a fundamental element in the development of a better, 
      smarter future for our world and my goal is to be part of that development process.
      America being an advanced country in computer science and AI will provide me a platform to interact with students 
      with diverse background to share my culture with them and will also give me a chance to adjust my approach to solve
      different computer science problems.
      
      
      
       The latest software
      update released by Tesla motors allows their cars to learn how to drive themselves is an example of 
      artificial intelligence, a sector which I am most interested in.
      .And now 
      i'm currently practicing my problem solving skills on a platform named codechef.com. 
      despite belonging to one of the middle ranked country in the field of computer science 
      and AI, growing power of social media has helped me to find out that how fast society has
      been shaped by the influence of Computer Science."""
from math import log2
total = 14
salaries_less_or_equal_to_50k = 9
salaries_greater_than_50k = 5

p = 9/14
q = 5/14

uncertanity_in_less_or_equal_to_50k = (-p) * (log2(p))
uncertanity_in_greater_than_50k = (-q) * (log2(q))

total_uncertanity = uncertanity_in_greater_than_50k + uncertanity_in_less_or_equal_to_50k
print(total_uncertanity)

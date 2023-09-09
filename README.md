*`Please read the methodology, description, and impact down below. For actual code, the ones I share publicly are in the folders above`* <br/><br/>
**Table of Contents**
- [Entry #1: An Introduction!](#Introduction)
- [Entry #2: Job search and formatting](#Job-search-and-Formatting)
----------------

# Introduction

![alt text](https://www.usatoday.com/gcdn/-mm-/b9d41a62d1b7691cf33c7c9eda7936d6b85f8111/c=0-8-2496-1418/local/-/media/2018/05/28/USATODAY/USATODAY/636631118463537351-FinderScreenSnapz005.png?width=1200&disable=upscale&format=pjpg&auto=webp)

If there is one hobby that I have recently developed, it would have to be automating some of the most tedious yet important parts of my life using the little knowledge I have about computer programming. This first post is the first of a series of projects I intend to undertake in order to improve my own life. The hope I have for myself is through this process, I should be able to improve my computer programming skills through the projects, my writing skills through blog writing, and allow me more time to focus on important tasks that can not be automated. 

Although some of the skills listed on this series can be useful in a professional setting, I want to take a more intimate journaling approach to this series, as it's just more fun than writing in a super-dry 'corporate talk' that can take the fun and joy out of my writing. If you are looking for a more formal portfolio, please check out my Portfolio section! For everybody else (if there is anybody else), whether you are an prospective employer, co-worker, or just someone who is curious about my work, I hope you have as much fun reading this as I do writing.


<p align="center">
  <img src="https://github.com/Seungjoo-Steven-YOU/automate_away/assets/121839521/eae96a45-8eeb-41b6-8fda-bf02a6b2afed" width="220" height="280">
<p/>

Let me introduce you to a guy I know, the guy in the photo above. This photo was taken a hundred days into his military service in Korea. Don't let the happy-go-lucky expression on his deadpan face fool you, this guy was actually recovering from all the head shaving, being yelled at in his estranged mother tongue, crawling in mud, and shooting guns he had to endure for the last 100 days. Here's a fun fact though. At this time, this guy had no coding experience. Sure, he knew how to do some basic econometric analysis with Excel and was beginning to learn how to use the R programming language, but I want to be 100% upfront with you: much of the things this guy learned was through a mixture of self-teaching, 1 full year of rigorous academic training, and completing projects for either himself or his own employers. I'd say this guy can do some neat stuff with python now, but I'm not gonna be making you a mobile app anytime soon, I'm not gonna be hacking computers; what the hell is a bogosort? 

<p align="center">
  <img src="https://cdn.arstechnica.net/wp-content/uploads/2012/03/chimp-laptop-4f50f9b-intro.jpg">
<p/>

What's stopped me for the longest time in making a portfolio/blog like this is a case of imposter syndrome. But I think that's why it matters that I write this journal: it helps me track my progress but most importantly it can inspire people that even with the bit of programming skills a chimp like me has, you can make your life just a little bit easier.

Now that's enough about me, let's get down to brass tacks. I have a few automation ideas that I've completed or I'm working on. In the following list, the items that are in bold are the projects I have started. Items not in bold are just ideas:
- **Job application**: Automatically create customized cover letters and resumes, while simultaneously placing the information on a jobs spreadsheet to track my application progress.
- **Recipe/Grocery planner**: Find three or four meals to prep for the week, listing the ingredients that would be needed to prep the meals. The most inexpensive (albeit tedious) way to do this would be to make an excel spreadsheet with recipes I know, the ingredients that are needed, and recommend a recipe to try from the list. Ideally, the program will also scan flyers to find the most affordable, tasty, and healthy recipes I can try.
- **Financial statement**: ***I will probably omit the details of the project, as it does contain sensitive financial information. However, once it is completed, I may share how it works with either bogus financial data, or just show the completed dashboard (which would also have bogus financial data)***

- File-Organizer: This is probably something that is easily available online. I just hate having to organize my downloads file, and I wish I can have a program that automatically places the files in their correct place at sometime during the day. I also don't like duplicate files, so maybe it can automatically delete things too. This however may be better done using a command line script, so I'm going to hold off on it until I learn some Powershell.
- Bikes-Near-Me: I use the bike share around Toronto. Sometimes, my heart gets broken when I walk outside and I see no bikes from the two stations that are near my house :( I'll have to think of a way to show that there are bikes available near me!
- More ideas to come! 

I have actually already completed my Job application automation project, however I want to be able to tweak it so that it can truly do everything that I want it to do in the shortest amount of time possible. I will try to finalize my code and submit it in the near future!

Until then, cheers everyone!

# Job Search and Formatting
<p align="center">
  <img src="https://legamart.com/articles/wp-content/uploads/2023/04/job-offer-text-page-min.jpg" width="500" height="300">
<p/>

Dear future recruiters/employers. I'm unsure if you will ever take a look at this page, but I still feel the need to put a disclaimer. This is not a cover letter or cv generator that just says whatever the job description calls for. All I have managed to do is create a program that formats a resume and cover letter into using one of two distinct resume templates, moves them into the correct folder, and finally updates a job application spreadsheet I have (let the record show that I used VBA macros for the excel!). **A good resume and cover letter still requires research, additional editing, reviewing, and writing**. I fear if I don't explain this in detail, I would look like I'm sending 100s of shotgun resumes out a day, with no research and no strategy. Just know that I'm always paying my due diligence!!

Currently, my biggest challenge is finding new employment opportunities. Like many of the countless job seekers today, I struggled greatly with tailoring my resume and cover letters. A few months into my application, I realized that having two main catch-all resumes simply does not work when looking for employment. Similarly, having a catch-all cover letter that simply replaces job titles, company name, and date completely lacks sincerety, and recruiters can see right through the BS!

In this project, my goal is to try to update the directories and excel spreadsheet with each application, while also creating a resume that has 'tailored' information, often highlighting the most relevant skills for each job description that I actually have, as well as having a customizable professional summary. I had a simple version of the code which organized files, however the program executed inconveniently, the code was extremely terse, and it was just unappealing.

In the last few days, I have been meaning to upgrade this job search program, potentially making a kivvy app that I can use even when I'm on the subway, giving me the power to create rough drafts for jobs I want while I'm killing tgime. To make my system work efficiently I wanted to work with multithreading, as there was a lot of external inputs that my program would wait for that used time in an inefficient manner. As of today, this program is probably the most sophisticated 'software' that I am working on for my personal use and development. I have done a lot of KPI analytics and data reporting using Jupyter Notebook, however I did not have the patience for large programs (I might be in over my head with the creative 'ideas' I have for my programs).

Feel free to check the code! Information that contains sensitive information has been censored of course. I will be using the version control as a sort of before and after snapshot for what my code looked like before vs now. If there are any updates in the future, I'll be sure to document the changes using version control.

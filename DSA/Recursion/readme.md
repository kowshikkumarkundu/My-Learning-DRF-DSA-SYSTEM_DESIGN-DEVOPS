recursion problem দেখলে সবার আগে "base case কী?" না ভেবে এই ৩টা প্রশ্ন করো:

Step 1 — Problem-টাকে ছোট করলে কী থাকে?

example:
58392
↓
5839

or 

abcde
↓
bcde

Step 2 — ছোট problem-টার answer আমি কীভাবে ব্যবহার করব?
reverse:
last digit + smaller answer

sum:
smaller answer + first character

Step 3 — কখন আর ছোট করা সম্ভব নয়?
সেখানেই base case।
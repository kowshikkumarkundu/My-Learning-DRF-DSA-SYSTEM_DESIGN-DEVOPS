এখন তোমার Practice

একটা Student model ধরে নিজের হাতে Serializer বানাও:

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.IntegerField()

Requirements:

marks negative হতে পারবে না।
age negative হতে পারবে না।
marks > 100 হলে error দিতে হবে।
grade নামে একটা calculated field থাকবে:
marks >= 80 → "A"
marks >= 60 → "B"
marks >= 40 → "C"
এর নিচে → "F"
POST দিয়ে Student create করার API view লিখবে।
Successful response-এ grade অবশ্যই দেখাবে।

আগে নিজে code করো। বিশেষ করে validate_marks(), validate_age(), validate(), SerializerMethodField, এবং POST view—এই পাঁচটা নিজে লিখে দেখো।

Code পাঠালে আমি line-by-line review করব এবং কোথায় DRF-এর actual flow হচ্ছে সেটা দেখিয়ে দেব।
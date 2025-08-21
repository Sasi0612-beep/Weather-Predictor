# x = input()
# k = int(input())
# res = []
# res.append(x[:k].count("1"))
# for i in x:
#     if i==1:
#         x=x.replace(i,"0")
#     elif i==0:
#         x=x.replace(i,"1")
# y=int(input())
# res.append(x[:y].count("1"))
# print(res)
# def count(n):
#     c=0
#     while(n>0):
#         n=n//10
#         c=c+1
#     return c
# lis=list(map(int, input().split(" ")))
# c1=0
# for i in lis:
#     if(count(lis[i])%2==0):
#         c1=c1+1
# print(c1)
from fpdf import FPDF

class JavaPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Java Complete Guide with Interview Questions', ln=True, align='C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = JavaPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

topics = [
    {
        "title": "1. Core Java & OOP Principles",
        "body": "Key Points:\n- JVM, JRE vs JDK\n- Data types, control flow\n- Classes, objects, inheritance, polymorphism...\n\nInterview Questions:\n1. What is the difference between JDK, JRE, and JVM?\n..."
    },
    {
        "title": "2. Collections & Generics",
        "body": "Key Points:\n- List, Set, Map\n- ArrayList vs LinkedList\n...\n\nInterview Questions:\n1. How does HashMap work internally?\n..."
    },
    # Add remaining sections similarly
]

for topic in topics:
    pdf.chapter_title(topic["title"])
    pdf.chapter_body(topic["body"])

pdf.output("Java_Complete_Guide_Interview_Questions.pdf")

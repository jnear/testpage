from jinja2 import Environment, FileSystemLoader
import os
 
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('index.html')

filename = os.path.join(root, 'index.html')

temp = {'title': '',
        'author': '',
        'description': '',
        'badges': [],
        'link': ''}

all_resources = {
    'Blog Series': [
        {'title': 'A friendly, non-technical introduction to differential privacy',
         'author': 'Damien Desfontaines',
         'description': 'A friendly blog post series about differential privacy! It provides simple explanations for the core concepts behind differential privacy. It is meant for a wide, non-technical audience: it doesn\'t assume any prior knowledge, uses as little math as possible, and illustrates everything with simple examples and diagrams.',
         'badges': ['Somewhat Technical', 'Blog Posts'],
         'link': 'https://desfontain.es/privacy/friendly-intro-to-differential-privacy.html'},

        {'title': 'NIST Differential Privacy Blog Series',
         'author': 'Various',
         'description': 'This series is designed to help business process owners and privacy program personnel understand basic concepts about differential privacy and applicable use cases and to help privacy engineers and IT professionals implement the tools. ',
         'badges': ['Somewhat Technical', 'Blog Posts'],
         'link': 'https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/collaboration-space/blog-series/differential-privacy'}
        ],

    'Courses': [

        {'title': 'CS 860 - Algorithms for Private Data Analysis',
         'author': 'Gautam Kamath',
         'description': 'This course is on algorithms for differentially private analysis of data. As necessitated by the nature of differential privacy, this course will be theoretically and mathematically based. References to practice will be provided as relevant, especially towards the end of the course. Prerequisites include an undergraduate understanding of algorithms, comfort with probability, and mathematical maturity.',
         'badges': ['Technical', 'Course Notes', 'Videos'],
         'link': 'http://www.gautamkamath.com/CS860-fa2020.html'},

        {'title': 'Privacy in Statistics and Machine Learning',
         'author': 'Adam Smith, Jonathan Ullman',
         'description': 'How can we learn from a data set of sensitive information while providing meaningful privacy to the individuals whose information it contains? The course explores this question, starting from the problems faced by straightforward solutions and moving on to rigorous state-of-the-art solutions using differential privacy. The class will focus on foundations, but also delve into some applied work and on some of the social, ethical, and legal context for the subject. Students will be required to complete some mathematical assignments, some light programming assignments, and a final course project.',
         'badges': ['Technical', 'Course Notes', 'Videos'],
         'link': 'https://dpcourse.github.io/'},

        {'title': 'CS 208 - Applied Privacy for Data Science',
         'author': 'Salil Vadhan',
         'description': 'The risks to privacy when making human subjects data available for research and how to protect against these risks using the formal framework of differential privacy. Methods for attacking statistical data releases, the mathematics of and software implementations of differential privacy, deployed solutions in industry and government. Assignments will include implementation and experimentation on data science tasks.',
         'badges': ['Technical', 'Course Notes'],
         'link': 'https://opendp.github.io/cs208/'}],
    }

with open(filename, 'w') as fh:
    fh.write(template.render(
        all_resources = all_resources
    ))

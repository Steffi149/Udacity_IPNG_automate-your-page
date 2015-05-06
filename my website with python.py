# -*- coding: utf-8 -*-
def generate_concept_HTML(concept_title, concept_subtitle, concept_description):
    html_text_1 = '''
    <h1>
        ''' + concept_title
    html_text_2 = '''
    </h1>
    <div class="concept">
        <h2>
        ''' + concept_subtitle
    html_text_3 = '''
        </h2>
        <p>
        ''' + concept_description
    html_text_4 = '''
        </p>
    </div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3 + html_text_4
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('SUBTITLE:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_subtitle(concept):
    start_location = concept.find('SUBTITLE:') 
    end_location = concept.find('DESCRIPTION:')
    subtitle = concept[start_location+10 : end_location-1]
    return subtitle

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('END', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

My_website_with_Python = """TITLE: Structured Data 
SUBTITLE: Lists & Loops     
DESCRIPTION: A string is a structured data because it is a sequence of characters that can be operated on subsequences.
Lists are more powerful, because elements don’t need to be necessarily characters. A string can be a sequence of anything. 
The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. 
Important thing about a list is that items in a list need not be of the same type. 
END  
TITLE:Mutation and Aliasing  
SUBTITLE:Difference between the two  
DESCRIPTION: Mutation means changing the value of an object. Lists support mutation. It is called aliasing when there are 2 names that refer to the same object. 
However, strings are immutable. Learning how technology actually works is how you build technological empathy. 
This empathy will help diagnosing and fixing bugs that otherwise would have been a mystery. 
END
TITLE: List Operations
SUBTITLE:  Built-in operations
DESCRIPTION: There are many built-in operations on lists. Here are a few of the most useful ones here:

Append. The append method adds a new element to the end of a list. The append method mutates the list that it is invoked on, it does not create a new list.
Concatenation. The + operator can be used with lists and is very similar to how it is used to concatenate strings. It produces a new list, it does not mutate either of the input lists.
Length. The len operator can be used to find out the length of an object. The len operator works for many things other than lists, it works for any object that is a collection of things including strings. The output from len is the number of elements in its input.
For. For loops are traditionally used when you have a piece of code which you want to repeat n number of times. As an alternative, there is the WhileLoop, however, while is used when a condition is to be met, or if you want a piece of code to repeat forever,
Sum. Sums start and the items of an iterable from left to right and returns the total. start defaults to 0. The iterable‘s items are normally numbers, and the start value is not allowed to be a string. For some use cases, there are good alternatives to sum(). 
ENDE"""


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        subtitle = get_subtitle(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, subtitle, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(My_website_with_Python)


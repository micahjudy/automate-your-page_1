                               # Stage 2 Automate your Page



def html_generator(content_stage, content, title_header, content_description):
    html_stage = ''' 
        <div class="content_stage">
        ''' + content_stage
    html_content = ''' 
            <div class"content">
            ''' + content
    html_title = '''
                <div class"title_header">
                ''' + title_header
    html_description = '''
                </div>
                    <p class="style"
                    ''' + content_description
    html_end = '''
                    </p>
            </div>
        </div> '''

    full_html_page = html_stage + html_content + html_title + html_description + html_end
    return full_html_page

def get_stage(concept):
    start_location = concept.find("STAGE:")
    end_location = concept.find("STRUCTURE:")
    stage = concept[start_location+7 : end_location-1]
    return stage
    
def get_content(concept):
    start_location = concept.find("STRUCTURE:")
    end_location = concept.find("HEADER:")
    content = concept[start_location+11 : end_location-1]
    return content

def get_title(concept):
    start_location = concept.find("HEADER:")
    end_location = concept.find ("DESCRIPTION:")
    title = concept[start_location+8 :end_location-1]
    return title

def get_description(concept):
    start_location = concept.find("DESCRIPTION:")
    description = concept[start_location+13 : ]
    return description
    
def get_concept_by_number(text,concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find("STAGE:")
        next_concept_end = text.find("STAGE:", next_concept_start+1)
        if next_concept_end >= 0:
            concept = text[next_concept_start : next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start :]
        text = text[next_concept_end :]
    return concept


def generate_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept !='':
        stage = get_stage(concept)
        content = get_content(concept)
        title = get_title(concept)
        description = get_description(concept)
        concept_html = html_generator(stage, content, title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number +1
        concept = get_concept_by_number(text,current_concept_number)
    return all_html
    
TEST_TEXT = """
STAGE: Stage 4
STRUCTURE: Content 4
HEADER: Loops
DESCRIPTION: When coding in Python one of the major conccepts <br>
that you use are Loops. A Loop is code that repeats that code <br>
over and over again until the code either becomes False or <br>
you add a Break parameter. This also helps programmers avoid <br>
repetition. Example of Loop Code  <br>
<br>
<br>
<div class="code-block">
    <span>i = 0</span> <br>
    <span class="print">while</span> i &#60; 25: <br>
    <span class="indent"><span class="print"> print</span> i</span> <br>
    <span class="indent"> i = i + 1</span>
</div>"""


print (generate_html(TEST_TEXT))

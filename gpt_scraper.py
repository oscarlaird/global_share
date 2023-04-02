import pyautogui
from time import sleep
from pathlib import Path

subject = 'AP US History (APUSH)'

essay_prompt = f''' Write a 350 word article for the {subject} test. Make the introduction and conclusion very short (at most one sentence) or just skip the introduction and conclusion altogether. Nevertheless have a logical organization to your article -- break it into sections -- don't just spit out a list of facts. Use advanced vocabulary (college level). Include lots of specific examples, names, and dates which help contribute to the main points.

Write your article in html and don't use the newline character between paragraphs of your essay (just use the paragraph tag). Be liberal with quotes (but only if you are sure that they are authentic). Use html bold tags liberally as well , but never use italics or headers or highlighting.

Emphasize things which often come up on the {subject} test, but don't mention the {subject} test in your essay.
'''

flashcard_prompt = f'''
Write 8 terminology flashcards based on the article you just wrote which would be relevant to the {subject} test. They can ask about concepts, people, events, or terminology. They can provide a term and ask for the definition or provide a definition and ask for a term. Do a mix of both. They should be moderately easy but the answer should never be obvious.

I want you to output a csv with the following fields:
topic_id
question
answer

Use '#' as the delimiter.

Example:
54#What U.S. bombing campaign targeted North Vietnam from 1965 to 1968?#Operation Rolling Thunder
(but use the correct topic id of course)

'''

mc_prompt = '''
Write 6 multiple choice questions based on the article you just wrote. Write a csv with the following fields:
topic_id
question
correct_answer
answers (JSON list of 5 answers; answers should not be numbered or lettered; answers should be simple text and not prefixed with a number 1-5 nor letter A-E; the correct answer must always come first in the list. Even if the correct answer is 'all of the above' that would need to come first in the list of five. The correct answer is always first. The next four answers are wrong.)
explanation (one or two sentences elaborating on the correct answer and why it is correct; add new, interesting information about the correct answer. DO NOT rephrase the question.)

The questions should be challenging. Equally difficult as the AP test. Ideally most of the questions can be answered based off reading the article.

Use '#' as the delimiter

Example:
41#Which Progressive Era reform allowed voters to select candidates for office, weakening the power of political bosses?#Direct primary system#["Direct primary system", "Initiative process", "Referendum process", "Recall process", "Secret ballot system"]#The direct primary system enabled voters to choose candidates for public office, thus reducing the influence of political bosses and promoting a more democratic political process.
(but use the correct topic id of course)
'''

def forward_enter_back():
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('shift', 'tab')

def shift_write(text):
    for line in text.splitlines():
        pyautogui.write(line)
        pyautogui.keyDown("shift")
        pyautogui.press("enter")
        pyautogui.keyUp("shift")
        sleep(0.05)

print('please hover over the appropriate window...')
sleep(4)

model = 4
delay = 45 if model==3.5 else 8.1*60
topics = Path('/home/oscar/dolts/dolt_apush/topicslist').read_text().splitlines()
for i, topic in enumerate(topics, start=1):
    if i<=32:
        continue
    # pyautogui.hotkey('ctrl', 's')
    # sleep(2)
    # pyautogui.write('backup'+str(i))
    # sleep(2)
    # pyautogui.hotkey('enter')
    # sleep(2)
    # pyautogui.hotkey('enter')
    # sleep(2)

    shift_write('topic: ' + topic + '\n\n' + essay_prompt + '\n')
    forward_enter_back()
    sleep(delay)

    shift_write(f'topic id: {i}\n' + flashcard_prompt)
    forward_enter_back()
    sleep(delay)

    shift_write(f'topic id: {i}\n' + mc_prompt)
    forward_enter_back()
    sleep(delay)

    shift_write('Write six more multiple choice questions...' + '\n')
    forward_enter_back()
    sleep(delay)






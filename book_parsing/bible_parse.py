import re
from docx import Document
from docx.shared import Inches

folder = "kjv"
filename = "mark"

run = True
chapter_num = 1
chapter_regex = r"\d*(?=:)"
chapter_and_verse_regex = r"[\d*:\d*]"

output_doc = Document()
output_doc.add_heading(filename, 0)


def write_paragraph(output_line):
    f_out.write(output_line + "\n")
    output_doc.add_paragraph(output_line)
    print(output_line)


def write_chapter(num):
    output_line = "\nCHAPTER " + str(chapter_num) + "\n"
    f_out.write(output_line + "\n")
    output_doc.add_heading(output_line, level=1)
    print(output_line)


with open(folder + "/" + filename + ".txt", "r") as f_in:
    with open(folder + "/" + "edited_" + filename + ".txt", "w") as f_out:
        output_line = "CHAPTER " + str(chapter_num) + "\n"
        f_out.write(output_line + "\n")
        output_doc.add_heading(output_line, level=1)
        output_line = ""
        while(run):
            line = f_in.readline()

            if (line == ""):
                # stop and write out the last paragraph
                run = False
                write_paragraph(output_line)
            else:
                # see if this line is a chapter heading
                chap = re.findall(chapter_regex, line)
                chapter_num_curr = int(chap[0]) if len(chap) > 0 else chapter_num
                if(chapter_num_curr > chapter_num):
                    # write paragraph + next chapter
                    write_paragraph(output_line)
                    chapter_num = chapter_num_curr
                    write_chapter(chapter_num)
                    output_line = ""

                # regex messarounds
                edited_line = re.sub(chapter_and_verse_regex,'',line)
                edited_line = re.sub("\n", "", edited_line)
                if edited_line != "":
                    output_line += edited_line + "\n"

# save the word doc too bruh
output_doc.save(folder + '/' + filename + '.docx')














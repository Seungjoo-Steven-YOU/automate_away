import datetime
import os
from docxtpl import DocxTemplate
from Excel_automatic import new_line
import time

path = input("Type A for analyst or B for Business: ")
company_name = input("Enter name of the Company: ")
position_name = input("Enter name of the Position: ")
tailor = input("In 4-5 sentences, describe why you are a good fit at company: ")
location = input("Enter the location: ")
website = input("Enter the job board: ")

today = datetime.datetime.today().strftime('%m/%d/%Y')

cletter_context = {'today': today,
                   'company_name': company_name,
                   'position_name': position_name,
                   'tailor': tailor}


# New cover letter and cv names
cover_letter_name = 'Cover_letter_' + company_name + \
                    '_' + position_name + '.docx'
cv_name = 'YOU_' + company_name + '_' + position_name + '.docx'


def build():
    """Organize the files and output the time"""
    start_time = time.perf_counter()
    if path.upper() == "A":
        tailor = input("Customize resume? For Cookie Cutter, press enter: ")
        if tailor.upper() != "":
            cv = DocxTemplate("Analyst_template.docx")
            skill1 = input("skill1: ")
            skill2 = input("skill2: ")
            tailor_dict = {"summary": tailor,
                           "skill1": skill1,
                           'skill2': skill2}
            ### Start with resume then cover letter
            os.chdir(r'D:\Resume\Tailored\Analyst\cv')
            cv_doc = DocxTemplate("Analyst_template.docx")
            cv_doc.render(tailor_dict)
            # Save the file with personalized filename
            cv_doc.save(cv_name)

        os.chdir(r'D:\Resume\Tailored\Analyst\cover_letter')
        cover_letter_doc = DocxTemplate("Analyst_template.docx")
        cover_letter_doc.render(cletter_context)
        cover_letter_doc.save(cover_letter_name)
    elif path.upper() == "B":
        tailor = input("Customize resume? For Cookie Cutter, press enter: ")
        if tailor.upper() != "":
            cv = DocxTemplate("Analyst_template.docx")
            skill1 = input("skill1: ")
            skill2 = input("skill2: ")
            skill3 = input("skill3: ")
            skill4 = input("skill4: ")
            skill5 = input("skill5: ")
            skill6 = input("skill6: ")
            tailor_dict = {"summary": tailor,
                           "skill1": skill1, 'skill2': skill2, 'skill3': skill3,
                           'skill4': skill4, 'skill5': skill5, 'skill6': skill6}
            os.chdir(r'D:\Resume\Tailored\Business\cv')
            cv_doc = DocxTemplate("Business_template.docx")
            cv_doc.render(tailor_dict)
            # Save the file with personalized filename
            cv_doc.save(cv_name)

        os.chdir(r'D:\Resume\Tailored\Business\cover_letter')
        cover_letter_doc = DocxTemplate("Business_template.docx")
        cover_letter_doc.render(cletter_context)
        cover_letter_doc.save(cover_letter_name)
    else:
        return
    end_time = time.perf_counter()

    # Update Excel file
    os.chdir(r'D:\Resume')
    new_line(company_name, position_name, today, location, website)
    print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')



if __name__ == "__main__":
    build()




# Main function requires these functions to work constantly
import datetime
import threading
import time
import os
from threading import Thread
import pandas as pd

from docxtpl import DocxTemplate
from Excel_automatic import new_line


class Survey:
    """
    Survey object contains stores important information when applying to jobs
    as a singular object.

    Attributes:
    path: Boolean object that is True iff path == "A"
    _data: List containing needed data for each survey
    """

    def __init__(self) -> None:
        def path():
            closed = True
            while closed:
                path = input("Type A for analyst or B for Business: ")
                if path.upper() in ["A", "B"]:
                    closed = False
            if path.upper() == "A":
                self.path = True
            else:
                self.path = False

        def company_position_ass() -> dict[str]:
            company_name = input("Enter name of the Company: ")
            position_name = input("Enter name of the Position: ")
            content = input("In 4-5 sentences, provide an elevator pitch: ")
            today = datetime.datetime.today().strftime('%m/%d/%Y')

            return {"today": today,
                    "position_name": position_name,
                    "company_name": company_name,
                    "content": content}

        def csv_process() -> None:
            """Return a list of strings that are just input values"""
            location = input("Enter the location: ")
            website = input("Enter the job board: ")
            self._data = [location, website]

        def jump_(choice: bool):
            """Basically the function that moves around and organizes the files
            and RETURN a tuple containing the Docx file and the path. Choice is
            a boolean value that is True iff the destination is cover_letter,
            else it is cv
            """
            if choice:
                loc = ["cover_letter", cover_letter_name]
            else:
                loc = ["cv", cv_name]
            name = loc[1]
            if self.path:
                direct = os.path.join("PATHDIRECTORY,
                                      loc[0])
                os.chdir(direct)
                cv_doc = DocxTemplate("Analyst_template.docx")
            else:
                direct = os.path.join("PATHDIRECTORY",
                                      loc[0])
                os.chdir(direct)
                cv_doc = DocxTemplate("Business_template.docx")
            return cv_doc, direct, name

        def dive(choice: bool, *args, **kwargs):
            """Jump, Load the template, and load the data"""
            cv_doc, direct, name = jump_(choice)
            if kwargs:
                cv_doc.render(kwargs)
                cv_doc.save(name)

        def tailor() -> dict[str: str] | None:
            """Return a CV tailor dictionary. You can add as many skills as you
            would like. Otherwise, return None"""
            summary = input(
                "Customize resume? For Cookie Cutter, press enter: ")
            skill = ""
            n = 0
            result = {}
            if summary.upper() != "":
                result["summary"] = summary
                while skill.lower() != "done":
                    skill = input(
                        "To end the process, type 'done'. Else, type a skill: ")
                    n += 1
                    statement = "skill" + str(n)
                    result[statement] = skill
                self._tailor = result

        start_time = time.perf_counter()
        # First
        path()
        cletter = company_position_ass()
        cover_letter_name = 'Cover_letter_' + cletter["company_name"] + \
                            '_' + cletter["position_name"] + '.docx'
        cv_name = 'YOU_' + cletter["company_name"] + '_' + \
                  cletter["position_name"] + '.docx'

        tailor = Thread(target=tailor)
        # dive1 should end with cover_letters completed
        dive1 = Thread(target=dive, args=[True], kwargs=cletter, daemon=True)

        # At this point we have self.path set, and save is a list that it
        # produces
        tailor.start()
        dive1.start()
        tailor.join()
        # Now we have to collect location and website while completing the cv
        cv_info = Thread(target=csv_process)
        dive2 = Thread(target=dive, args=[False],
                       kwargs=self._tailor, daemon=True)

        # By beginning thread3, we are creating and moving cv into the correct
        # directory
        cv_info.start()
        dive2.start()
        cv_info.join()

        # Update Excel file
        today = cletter["today"]
        company_name = cletter["company_name"]
        position_name = cletter["position_name"]
        location = self._data[0]
        website = self._data[1]
        new_line(company_name, position_name, today, location, website)

        end_time = time.perf_counter()
        new_line(company_name, position_name, today, location, website)
        print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')

if __name__ == "__main__":
    while True:
        survey = Survey()
        print('done', survey)

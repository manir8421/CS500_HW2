
# CS500 / Object Oriented Python / Home Work / HW2
# ID: 20099 / Name: MD MANIRUZZAMAN
# Question: Basic Job Application by Object Oriented programming (Python)


from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

class DetailsCollection(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def get_all(self):
        pass

class EmergencyContact:
    def __init__(self, priority: str, name: str, relationship: str, contact_number: int):
        self.__priority = priority
        self.__name = name
        self.__relationship = relationship
        self.__contact_number = contact_number

    @property
    def priority(self):
        return self.__priority
    
    @priority.setter
    def priority(self, new_priority: str):
        self.__priority = new_priority

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def relationship(self):
        return self.__relationship
    
    @relationship.setter
    def relationship(self, new_relationship: str):
        self.__relationship = new_relationship

    @property
    def contact_number(self):
        return self.__contact_number
    
    @contact_number.setter
    def contact_number(self, new_contact_number: int):
        self.__contact_number = new_contact_number

    def __str__(self):
        return f"\n{self.__priority}: Name: {self.__name}, Relationship: {self.__relationship}, Contact Number: {self.__contact_number}"

class EmergencyContactsCollection(DetailsCollection):
    def __init__(self):
        self._contacts = []

    def add(self, contact: EmergencyContact):
        self._contacts.append(contact)

    def get_all(self) -> List[EmergencyContact]:
        return self._contacts
    

class Education:
    def __init__(self, level: str, school_name: str, year_from: str, year_to: str, degree: str):
        self.__level = level
        self.__school_name = school_name
        self.__year_from = year_from
        self.__year_to = year_to
        self.__degree = degree

    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, new_level: str):
        self.__level = new_level

    @property
    def school_name(self):
        return self.__school_name
    
    @school_name.setter
    def school_name(self, new_school_name: str):
        self.__school_name = new_school_name

    @property
    def year_from(self):
        return self.__year_from
    
    @year_from.setter
    def year_from(self, year_from: str):
        self.__year_from = year_from

    @property
    def year_to(self):
        return self.__year_to
    
    @year_to.setter
    def year_to(self, new_year_to: str):
        self.__year_to = new_year_to

    @property
    def degree(self):
        return self.__degree
    
    @degree.setter
    def degree(self, new_degree: str):
        self.__degree = new_degree

    def __str__(self):
        return f"\nLevel: {self.__level}, School Name: {self.__school_name}, Period(year) From-To: {self.__year_from} - {self.__year_to}, Degree: {self.__degree}"

class EducationCollection(DetailsCollection):
    def __init__(self):
        self._educations = []

    def add(self, education: Education):
        self._educations.append(education)

    def get_all(self) -> List[Education]:
        return self._educations
    

class WorkExperience:
    def __init__(self, company_name: str, company_address: str, year_from: str, year_to: str, position: str, reason_of_leaving: str):
        self.__company_name = company_name
        self.__company_address = company_address
        self.__year_from = year_from
        self.__year_to = year_to
        self.__position = position
        self.__reason_of_leaving = reason_of_leaving

    @property
    def company_name(self):
        return self.__company_name
    
    @company_name.setter
    def company_name(self, new_company_name: str):
        self.__company_name = new_company_name

    @property
    def company_address(self):
        return self.__company_address
    
    @company_address.setter
    def company_address(self, new_company_address: str):
        self.__company_address = new_company_address

    @property
    def date_year_from(self):
        return self.__date_year_from
    
    @date_year_from.setter
    def date_year_from(self, new_date_year_from: str):
        self.__date_year_from = new_date_year_from

    @property
    def date_year_to(self):
        return self.__date_year_to
    
    @date_year_to.setter
    def date_year_to(self, new_date_year_to: str):
        self.__date_year_to = new_date_year_to

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, new_position: str):
        self.__position = new_position

    @property
    def reason_of_leaving(self):
        return self.__reason_of_leaving
    
    @reason_of_leaving.setter
    def reason_of_leaving(self, new_reason_of_leaving: str):
        self.__reason_of_leaving = new_reason_of_leaving

    def __str__(self):
        return f"\nCompany Name: {self.__company_name}, Date(year) From-To: {self.__year_from} - {self.__year_to}, Position: {self.__position}, Reason of leaving: {self.__reason_of_leaving}\nCompany Address:{self.__company_address}"

class WorkExperienceCollection(DetailsCollection):
    def __init__(self):
        self._experiences = []

    def add(self, experience: WorkExperience):
        self._experiences.append(experience)

    def get_all(self) -> List[WorkExperience]:
        return self._experiences
    

class Skill:
    def __init__(self, skill_list: str):
        self.skill_list = skill_list.upper()

    def __str__(self):
        return self.skill_list

class SkillsCollection(DetailsCollection):
    def __init__(self):
        self._skills = []

    def add(self, skill_list: Skill):
        self._skills.append(skill_list)

    def get_all(self) -> List[Skill]:
        return self._skills
    
    def clear_skills(self):
        self._skills.clear()

class Person:
    def __init__(self, first_name: str, middle_name: str, last_name: str, email: str):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__email = email

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name: str):
        self.__first_name = new_first_name

    @property
    def middle_name(self):
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, new_middle_name: str):
        self.__middle_name = new_middle_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name: str):
        self.__last_name = new_last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email: str):
        self.__email = new_email

    @property
    def full_name(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"

class Applicant(Person):
    def __init__(self, first_name, middle_name, last_name, email, date_of_birth, position_applying, house_num, street, city, state, zip, telephone, mobile, place_of_birth, citizenship):
        super().__init__(first_name, middle_name, last_name, email)
        self.__date_of_birth = date_of_birth
        self.__position_applying = position_applying
        self.__house_num = house_num
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__telephone = telephone
        self.__mobile = mobile
        self.__place_of_birth = place_of_birth
        self.__citizenship = citizenship
        self.__emergency_contacts = EmergencyContactsCollection()
        self.__educations = EducationCollection()
        self.__work_experiences = WorkExperienceCollection()
        self.__skills = SkillsCollection()


    @property
    def date_of_birth(self):
        return self.__date_of_birth
    
    @date_of_birth.setter
    def date_of_birth(self, value):
        self.__date_of_birth = value

    @property
    def position_applying(self):
        return self.__position_applying
    
    @position_applying.setter
    def position_applying(self, value):
        self.__position_applying = value

    @property
    def house_num(self):
        return self.__house_num
    
    @house_num.setter
    def house_num(self, new_house_num: str):
        self.__house_num = new_house_num

    @property
    def street(self):
        return self.__street
    
    @street.setter
    def street(self, new_street: str):
        self.__street = new_street

    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, new_city: str):
        self.__city = new_city

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, new_state: str):
        self.__state = new_state

    @property
    def zip(self):
        return self.__zip
    
    @zip.setter
    def zip(self, new_zip: int):
        self.__zip = new_zip


    @property
    def telephone(self):
        return self.__telephone
    
    @telephone.setter
    def telephone(self, value):
        self.__telephone = value

    @property
    def mobile(self):
        return self.__mobile
    
    @mobile.setter
    def mobile(self, value):
        self.__mobile = value

    @property
    def place_of_birth(self):
        return self.__place_of_birth
    
    @place_of_birth.setter
    def place_of_birth(self, value):
        self.__place_of_birth = value

    @property
    def citizenship(self):
        return self.__citizenship
    
    @citizenship.setter
    def citizenship(self, value):
        self.__citizenship = value

    @property
    def emergency_contacts(self):
        return self.__emergency_contacts
    
    @emergency_contacts.setter
    def emergency_contacts(self, new_emergency_contacts):
        self.__emergency_contacts = new_emergency_contacts

    def add_emergency_contact(self, contact: EmergencyContact):
        self.__emergency_contacts.add(contact)

    def get_emergency_contacts(self):
        return self.__emergency_contacts.get_all()
    
    def add_education(self, education: Education):
        self.__educations.add(education)

    def get_educations(self):
        return self.__educations.get_all()

    def add_work_experience(self, experience: WorkExperience):
        self.__work_experiences.add(experience)

    def get_work_experiences(self):
        return self.__work_experiences.get_all()
    
    def add_skill(self, skill: Skill):
        self.__skills.add(skill)

    def get_skills(self) -> List[str]:
        return [skill.skill_list for skill in self.__skills.get_all()]
    
    @property
    def work_experiences(self):
        return self.__work_experiences
    
    @work_experiences.setter
    def work_experiences(self, new_work_experiences):
        self.__work_experiences = new_work_experiences

    @property
    def skills(self):
        return self.__skills
    
    @skills.setter
    def skills(self, new_skills):
        self.__skills = new_skills


    def __str__(self):
        details = [
            f"\nCompany Name: XYZ limited\t\t\t\t\tBASIC JOB APPLICATION\nCompany Address:xx mission falls ln, CA 94539\n{'='*85}"
            f"\nPERSONAL INFORMATION:\nNAME: {self.full_name}\tDATE OF BIRTH: {self.__date_of_birth}\tPOSITION APPLYING: {self.__position_applying}"
            f"\nADDRESS: {self.__house_num}, {self.__street}, {self.__city}, {self.__state} {self.zip}"
            f"\nTELEPHONE(Home): {self.__telephone}\tTELEPHONE(Mobile): {self.__mobile}\tEMAIL ADDRESS: {self.email}",
            f"PLACE OF BIRTH: {self.__place_of_birth}\tCITIZENSHIP: {self.__citizenship}",
            "\nIn case of accident, notify:" + "".join(str(contact) for contact in self.get_emergency_contacts()),
            "\nEDUCATION(most recent):" + "".join(str(education) for education in self.__educations.get_all()),
            "\nWORK EXPERIENCE(last 3 latest only):" + "".join(str(work) for work in self.__work_experiences.get_all()),
            "\nMAJOR SKILLS:\n" + " ".join("-" + skill.skill_list for skill in self.__skills.get_all())
        ]
        return "\n".join(details)
    
    
class ApplicationManager:
    def __init__(self):
        self.applicants = []

    def _collect_emergency_contacts(self):
                emergency_contacts = EmergencyContactsCollection()
                print("Enter emergency contact information (Type 'n' to finish):")
                
                while True:
                    if input("Type 'n' to stop or press Enter to continue: ").lower() == "n":
                        break
                    priority = input("Priority(Primary/Secondery): ").title()
                    name = input("Name: ").title()
                    relationship = input("Relationship: ").title()
                    while True:
                        contact_number = input("Enter the contact number: ")
                        try:
                            cont_num = int(contact_number)
                            break
                        except ValueError:
                            print("Invalid contact number! Please enter a valid number.")
                    
                    emergency_contact = EmergencyContact(priority, name, relationship, cont_num)
                    emergency_contacts.add(emergency_contact)
                return emergency_contacts
    

    def _collect_education_details(self):
        educations = EducationCollection()
        print("Enter education details (Type 'n' to finish):")
        while True:
            if input("Type 'n' to stop or press Enter to continue: ").lower() == "n":
                break
            level = input("Study Level: ").title()
            school_name = input("School/University Name: ").title()
            
            while True:
                year_from = input("Enter the date From (mm/dd/yyyy): ")
                try:
                    y_from = datetime.strptime(year_from, "%m/%d/%Y")
                    edu_y_from = y_from.strftime("%m/%d/%Y")
                    break
                except ValueError:
                    print("Invalid format! The date format should be mm/dd/yyyy.")
            
            while True:
                year_to = input("Enter the date To (mm/dd/yyyy): ")
                try:
                    y_to = datetime.strptime(year_to, "%m/%d/%Y")
                    edu_y_to = y_to.strftime("%m/%d/%Y")
                    break
                except ValueError:
                    print("Invalid format! The date format should be mm/dd/yyyy.")
            
            degree = input("Degree: ").upper()
        
            education = Education(level, school_name, edu_y_from, edu_y_to, degree)
            educations.add(education)
        return educations

    def _collect_work_experience_details(self):
        work_experiences = WorkExperienceCollection()
        print("Enter work experience (Type 'n' to finish):")
        
        while True:
            if input("Type 'n' to stop or press Enter to continue: ").lower() == "n":
                break
            company_name = input("Company Name: ").title()
            company_address = input("Company Address: ").title()

            while True:
                wexp_year_from = input("Enter the date From (mm/dd/yyyy): ")
                try:
                    wexp_y_from = datetime.strptime(wexp_year_from, "%m/%d/%Y")
                    we_from = wexp_y_from.strftime("%m/%d/%Y")
                    break
                except ValueError:
                    print("Invalid format! The date format should be mm/dd/yyyy.")
            
            while True:
                wexp_year_to = input("Enter the date To (mm/dd/yyyy): ")
                try:
                    wexp_y_to = datetime.strptime(wexp_year_to, "%m/%d/%Y")
                    we_to = wexp_y_to.strftime("%m/%d/%Y")
                    break
                except ValueError:
                    print("Invalid format! The date format should be mm/dd/yyyy.")
            
            position = input("Position: ").title()
            reason_of_leaving = input("Reason of Leaving: ")
        
            work_experience = WorkExperience(company_name, company_address, we_from, we_to, position, reason_of_leaving)
            work_experiences.add(work_experience)
        return work_experiences

    def _collect_skills_details(self):
        skills_collection = []
        print("Enter skills (Type 'n' to finish):")
        while True:
            skill_input = input("Skill: ").upper()
            if skill_input.lower() == "n":
                break
            f_skill = skill_input
            skill = Skill(f_skill)
            skills_collection.append(skill)
        return skills_collection


    def add_applicant(self):
      
        first_name = input("Enter the first name of the applicant: ").title()
        middle_name = input("Enter the middle name / initial of the applicant: ").title()
        last_name = input("Enter the last name of the applicant: ").title()
        
        while  True:
            date_of_birth = input("Enter the Date of Birth (mm/dd/yyyy): ")
            try:
                dob = datetime.strptime(date_of_birth, "%m/%d/%Y")
                d_o_b = dob.strftime("%m/%d/%Y")
                break
            except ValueError:
                print("Invalid format! The date format should be mm/dd/yyyy.")
        
       
        position_applying = input("Enter the position applying for: ")
        house_num = input("Enter the house number: ").title()
        street = input("Enter the street: ").title()
        city = input("Enter the city: ").title()
        state =  input("Enter the state: ").upper()
        
        while True:
            zip = input("Enter the Zip code: ")
            try:
                zip_code = int(zip)
                break
            except ValueError:
                print("Invalid Zip Code! Please enter a valid zip code")
        
        while True:
            telephone = input("Enter the Telephone(home) number: ")
            try:
                tel1 = int(telephone)
                break
            except ValueError:
                print("Invalid phone number! Please enter a valid number.")
        
        while True:
            mobile = input("Enter the Telephone(mobile) number: ")
            try:
                mob1 = int(mobile)
                break
            except ValueError:
                print("Invalid phone number! Please enter a valid number.")
        
        email = input("Enter the email address: ")
        place_of_birth = input("Enter the place of birth: ").title()
        citizenship = input("Enter country name of the citizenship: ").upper()        
     
        applicant = Applicant(first_name, middle_name, last_name, email, d_o_b, position_applying, house_num, street, city, state, zip_code, tel1, mob1, place_of_birth, citizenship)
        
        emergency_contacts = self._collect_emergency_contacts()
        for contact in emergency_contacts.get_all():
            applicant.add_emergency_contact(contact)

        educations = self._collect_education_details()
        for education in educations.get_all():
            applicant.add_education(education)

        work_experiences = self._collect_work_experience_details()
        for work_experience in work_experiences.get_all():
            applicant.add_work_experience(work_experience)

        skill_list = self._collect_skills_details()
        for skill in skill_list:
            applicant.add_skill(skill)
        

        self.applicants.append(applicant)
        print("Applicant added successfully.")

    def see_all_applicants(self):
        if not self.applicants:
            print("No applicants to display.")
            return
        
        for applicant in self.applicants:
            print(applicant)
            print("-" * 85)


    def search_applicant_by_name(self):
        first_name = input("Enter the first name of the applicant to search: ").title()
        middle_name = input("Enter the middle name / initial of the applicant to search: ").title()
        last_name = input("Enter the last name of the applicant to search: ").title()
        full_name = f"{last_name}, {first_name} {middle_name}"
        
        found = False
        for applicant in self.applicants:
            if applicant.full_name == full_name:
                print("Matching Applicant Found:")
                print(applicant)
                print("-" * 85)
                found = True         
        if not found:
            print("No matching applicant found.")


    def search_applicant_by_skills(self):
        skill_input = input("Enter the skills to search for (separate multiple skills with commas): ").upper().split(',')
        skills_search_set = set(skill.strip() for skill in skill_input)

        found = False
        for applicant in self.applicants:
            applicant_skills_set = set(applicant.get_skills())

            if skills_search_set.issubset(applicant_skills_set):
                if not found:
                    print("Matching Applicants Found:")
                    found = True
                print(applicant)
                print("-" * 85)

        if not found:
            print("No matching applicants found.")

    
    def search_applicant_by_education(self):
        search_level = input("Enter education level to search for (leave blank for no specific level): ").title()
        found = False
        for applicant in self.applicants:
            for education in applicant.get_educations():
                if search_level in education.level.title() or not search_level:
                    if not found:
                        print("Matching Applicants Found:")
                        found = True
                    print(applicant)
                    print("-" * 85)
                    break
        if not found:
            print("No matching applicants found.")


    def modify_applicant_details(self):
        fst_name = input("Enter the first name of the applicant to search: ").title()
        mdl_name = input("Enter the middle name / initial of the applicant to search: ").title()
        lst_name = input("Enter the last name of the applicant to search: ").title()
        name_full = f"{lst_name}, {fst_name} {mdl_name}"
        found = False
        for applicant in self.applicants:
            if applicant.full_name == name_full:
                found = True
                print(f"Modifying details for {applicant.full_name} ; What would you like to update/modify?")
                print("1. Address")
                print("2. Telephone(Phone)")
                print("3. Skills")
                choice = input("Enter your choice: ")
                if choice == "1":
                    new_house_num = input("Enter the new house number: ").title()
                    new_street = input("Enter the new street: ").title()
                    new_city = input("Enter the new city: ").title()
                    new_state =  input("Enter the new state: ").upper()
                    while True:
                        new_zip_code = input("Enter the new Zip code: ")
                        try:
                            zip = int(new_zip_code)
                            break
                        except ValueError:
                            print("Invalid Zip Code! Please enter a valid zip code")
                    
                    applicant.house_num = new_house_num
                    applicant.street = new_street
                    applicant.city = new_city
                    applicant.state = new_state
                    applicant.zip = new_zip_code
                    print("Address updated/modified successfully.")
                
                elif choice == "2":
                    while True:
                        new_mobile = (input("Enter the new Telephone(Phone) number: "))
                        try:
                            new_cont_num = int(new_mobile)
                            break
                        except ValueError:
                            print("Invalid number! Please enter a valid number.")
                    applicant.mobile = new_cont_num
                    print("Telephone(phone) number updated/modified successfully.")
                
                elif choice == "3":
                    new_skills_input = input("Enter the new skills (comma-separated): ").upper().strip()
                    if new_skills_input:
                        new_skills_list = [skill.strip().upper() for skill in new_skills_input.split(',')]
                        new_skills_objects = [Skill(skill) for skill in new_skills_list]
            
                        applicant.skills.clear_skills()
                        for skill_object in new_skills_objects:
                            applicant.add_skill(skill_object)
                
                        print("Skills updated/modified successfully.")
                    else:
                        print("No new skills were provided.")
                else:
                    print("Invalid choice.")
                    return
                break
        if not found:
            print("Applicant not found.")
        

    def remove_applicant(self):
        fst_name = input("Enter the first name of the applicant to search: ").title()
        mdl_name = input("Enter the middle name / initial of the applicant to search: ").title()
        lst_name = input("Enter the last name of the applicant to search: ").title()
        name_full = f"{lst_name}, {fst_name} {mdl_name}"
        found = False
        for i,applicant in enumerate(self.applicants):
            if applicant.full_name == name_full:
                del self.applicants[i]
                print(f"Applicant {applicant.full_name} removed successfully.")
                return
        print("Applicant not found.")

def main():
    manager = ApplicationManager()
    
    while True:
        print("\nWelcome to the Application Manager\n" + "=" * 35)
        print("1. Add a new applicant")
        print("2. See all applicants")
        print("3. Search an applicant by name")
        print("4. Search applicants by skills")
        print("5. Search applicant by education")
        print("6. Modify an existing application")
        print("7. Remove an applicant")
        print("8. Exit")

        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            manager.add_applicant()
        
        elif choice == "2":
            manager.see_all_applicants()
        
        elif choice == "3":
            manager.search_applicant_by_name()
        
        elif choice == "4":
            manager.search_applicant_by_skills()
        
        elif choice == "5":
            manager.search_applicant_by_education()
        
        elif choice == "6":
            manager.modify_applicant_details()
        
        elif choice == "7":
            manager.remove_applicant()
        
        elif choice == "8":
            print("Exiting the Application Management System. Thank you for using our services.")
            break
        
        else:
            print("Invalid choice! Please choose a number between 1 and 8.")


if __name__ == "__main__":
    main()
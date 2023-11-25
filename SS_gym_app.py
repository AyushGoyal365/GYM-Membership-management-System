import base64
import mysql.connector
import datetime
from datetime import date
from datetime import datetime ,timedelta
from dateutil.parser import parse
import streamlit as st
import pandas as pd

db = mysql.connector.connect(host='localhost', username='root', password='ayush123', database='ss')

class Members:

    def __init__(self, Name, Phone_Number, Age, Height, Weight, Any_disease):
        self.Name = Name
        self.Phone_Number = Phone_Number
        self.Age = Age
        self.Height = Height
        self.Weight = Weight
        self.Any_disease = Any_disease
        self.id = self.add_member()

    def add_member(self):
          # Return the existing member's id

        # If not found, insert the new member
        sql = "INSERT INTO members (Name, Phone_Number, Age, Height, Weight, Any_disease) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.Name, self.Phone_Number, self.Age, self.Height, self.Weight, self.Any_disease)
        cursor.execute(sql, val)
        db.commit()
        new_member_id = cursor.lastrowid  
        cursor.close()
        return new_member_id  

class Membership(Members):

    def __init__ (self, joining_date, ending_date, member_id):
        while True:
            try:
                self.joining_date = datetime.strptime((joining_date), '%Y-%m-%d').date() # type: ignore
                self.ending_date = datetime.strptime((ending_date), '%Y-%m-%d').date() # type: ignore
                self.insert_membership(member_id)
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
            
    def insert_membership(self, member_id):
        cursor = db.cursor()
        sql = "UPDATE members SET joining_date = %s, ending_date = %s,Membership_type = %s WHERE id = %s"
        val = (self.joining_date, self.ending_date,membership_type, member_id)
        try:
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
        except Exception as e:
            st.error("Error inserting data into the database: " + str(e))

class Fees(Membership):

    def __init__(self, paid , pending, member_id):
        self.amount_paid = int(paid)
        self.pending_amount = int(pending)
        self.update_fees(member_id)

    def update_fees(self, member_id):
        cursor = db.cursor()
        sql = "UPDATE members SET Fees = %s, pending = %s WHERE id = %s"
        val = (self.amount_paid, self.pending_amount, member_id)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()




st.title(" SS Fitness Membership Application")

page = st.sidebar.selectbox("Options",["Add New Member","Fees Status","Update Info","View Data"])

if page == "Add New Member":
    ending_date = ""
    st.header("Member Details")
    name = st.text_input("Name")
    phone_number = st.text_input("Phone Number")
    age = st.number_input("Age", min_value=1)
    height = st.number_input("Height (in cm)", min_value=1)
    weight = st.number_input("Weight (in kg)", min_value=1)
    any_disease = st.text_input("Any Disease (optional)")

    st.header("Membership Dates")
    joining_date = st.text_input("Joining Date (YYYY-MM-DD)", value=date.today().strftime("%Y-%m-%d"), key="Joining_Date_Input")
    membership_type = st.selectbox("Membership Type ", ["Regular 1 Month", "Regular 3 Month", "Regular 6 Month", "Regular 1 Year","PT 1 Month", "PT 3 Month", "PT 6 Month", "PT 1 Year", "Online PT 1 Month", "Online PT 3 Month", "Online PT 6 Month", "Online PT 1 Year"])
    if membership_type == "Regular 1 Month":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=30)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d")
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")
    elif membership_type == "Regular 3 Month":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=90)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d")
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")     
    elif membership_type == "Regular 6 Month":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=120)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d")
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")  
    elif membership_type == "Regular 1 Year":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=360)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d")
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   
    elif membership_type == "PT 1 Month":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=30)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d")
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   
    elif membership_type == "PT 3 Month":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=90)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d")
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   

    elif membership_type == "PT 6 Month":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=120)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d")
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   
    elif membership_type == "PT 1 Year":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=360)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d") 
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")  

    elif membership_type == "Online PT 1 Month":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=30)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d")
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   
    elif membership_type == "On    line PT 3 Month":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=90)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d")
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   
    elif membership_type == "Online PT 6 Month":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=120)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d") 
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input") 
    elif membership_type == "Online PT 1 Year":
        current_date = datetime.today()
        next_month_date = current_date + timedelta(days=360)

        auto_ending_date = next_month_date.strftime("%Y-%m-%d") 
        ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")                                           
        

    
        
   
    st.header("Fees Details")
    fees_paid = st.number_input("Fees Paid (in Rs)", min_value=0)
    pending_fees = st.number_input("Pending Fees (in Rs)", min_value=0) 
    
    cursor = db.cursor()

       
    check_sql = "SELECT * FROM members WHERE Name = %s AND Phone_Number = %s"
    cursor.execute(check_sql, (name, phone_number))
    existing_member = cursor.fetchone()

    if existing_member:
        st.warning("Member with the same name and phone number already exists.")
        cursor.close()
        


   
    if st.button("Add Member"):
        try:
            
            member = Members(name, phone_number, age, height, weight, any_disease)

            
            membership = Membership( joining_date, ending_date, member.id)

            
            fees = Fees(fees_paid, pending_fees, member.id)

            st.success("Member added successfully!")
        except Exception as e:
            st.error(f"Error adding member: {str(e)}")

elif page =="Fees Status":
    class Notification:
        def __init__(self):
            self.check_over_membership()

        def check_over_membership(self):
            cursor = db.cursor()

            try:
                today = datetime.now().date() # type: ignore

                sql = "SELECT id, name FROM members WHERE ending_date <= %s And Status = 'Active'"
                cursor.execute(sql, (today,))
                membership_ids= cursor.fetchall()

                if membership_ids:
                    st.warning("Memberships Over:")
                
                    for membership_id in membership_ids:
                        st.write(f"Membership ID {membership_id[0]},{membership_id[1]} is over.")
                        recharged = st.radio(f"Do you want to update Membership for ID {membership_id[0]},{membership_id[1]}?", ("Yes", "No"))

                        if recharged == "Yes":
                            membership_type = st.selectbox("Membership Type ", ["Regular 1 Month", "Regular 3 Month", "Regular 6 Month", "Regular 1 Year","PT 1 Month", "PT 3 Month", "PT 6 Month", "PT 1 Year", "Online PT 1 Month", "Online PT 3 Month", "Online PT 6 Month", "Online PT 1 Year"])
                            if membership_type == "Regular 1 Month":
                               current_date = datetime.today() # type: ignore
                               next_month_date = current_date + timedelta(days=30)

                               auto_ending_date = next_month_date.strftime("%Y-%m-%d")
                               new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")
                            elif membership_type == "Regular 3 Month":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=90)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d")
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")     
                            elif membership_type == "Regular 6 Month":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=120)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d")
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")  
                            elif membership_type == "Regular 1 Year":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=360)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d")
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   
                            elif membership_type == "PT 1 Month":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=30)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d")
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   
                            elif membership_type == "PT 3 Month":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=90)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d")
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   

                            elif membership_type == "PT 6 Month":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=120)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d")
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   
                            elif membership_type == "PT 1 Year":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=360)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d") 
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")  

                            elif membership_type == "Online PT 1 Month":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=30)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d")
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   
                            elif membership_type == "On    line PT 3 Month":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=90)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d")
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")   
                            elif membership_type == "Online PT 6 Month":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=120)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d") 
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input") 
                            elif membership_type == "Online PT 1 Year":
                                current_date = datetime.today() # type: ignore
                                next_month_date = current_date + timedelta(days=360)

                                auto_ending_date = next_month_date.strftime("%Y-%m-%d") 
                                new_ending_date = st.text_input("Ending Date (YYYY-MM-DD)",value=auto_ending_date , key="Ending_Date_Input")

                            fees_paid = st.number_input("Fees Paid (in Rs)", min_value=0)
                            pending_fees = st.number_input("Pending Fees (in Rs)", min_value=0)       
                            
                            if st.button("Save"):
                                cursor_update = db.cursor()
                                sql_update = "UPDATE members SET ending_date = %s,Membership_type = %s, Status = 'Active' WHERE id = %s"
                                cursor_update.execute(sql_update, (new_ending_date,membership_type, membership_id[0])) # type: ignore
                                db.commit()
                                st.success(f"Membership for ID {membership_id[0]} updated successfully.")
                                cursor = db.cursor()
                                sql = "UPDATE members SET Fees = Fees + %s, pending = pending + %s WHERE id = %s"
                                val = (fees_paid,pending_fees, membership_id[0])
                                cursor.execute(sql, val) # type: ignore
                                db.commit()
                                cursor.close()

                            else:
                                st.write("Click 'Save' to update the membership.")
                        elif recharged == "No":
                            if st.button(f"Inactive Membership for ID {membership_id[0]}"):
                                cursor_update = db.cursor()
                                Unactive_sql = "UPDATE  members SET Status = 'Inactive'  WHERE id = %s"
                                cursor_update.execute(Unactive_sql, (membership_id[0],)) # type: ignore
                                db.commit()
                                st.success(f"Membership for ID {membership_id[0]} is Inactived.")
                else:
                    st.info("No Memberships over today.")
    
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")


    notification = Notification()

elif page == "Update Info":
    # Create a cursor
    # Create a cursor

  cursor = db.cursor()
# Query to get ID and name of all members
  
  all_ids_query = "SELECT id, name FROM members"
  cursor.execute(all_ids_query)
  all_ids = cursor.fetchall()

# Create a list of tuples with ID and name
  id_name_tuples = [(id, name) for id, name in all_ids]

# Extract the IDs for select box
  all_id_values = [id for id, _ in id_name_tuples]

# Create a select box with ID and name
  selected_id_name = st.selectbox("Select profile ID you want to edit", id_name_tuples)

  if selected_id_name:
    selected_id = selected_id_name[0]  # Extract the selected ID from the tuple

    class Update_info:
        def __init__(self, selected_id):
            self.selected_id = selected_id
            self.update_member_info()

        def update_member_info(self):
            cursor = db.cursor()
            try:
                check_sql = "SELECT * FROM members WHERE id = %s"
                cursor.execute(check_sql, (self.selected_id,))
                member = cursor.fetchone()

                if member:
                    st.write(f"Updating information for Member ID {self.selected_id}:")
                    st.write("Leave a field blank to keep the existing value.")

                    # Get updated member information from the user
                    new_name = st.text_input(f"New Name ({member[1]}): ").strip() or member[1]
                    new_phone = st.number_input(f"New Phone Number ({member[2]}): ") or member[2]
                    new_age = st.number_input(f"New Age ({member[3]}): ") or member[3]
                    new_height = st.number_input(f"New Height ({member[4]}): ") or member[4]
                    new_weight = st.number_input(f"New Weight ({member[5]}): ") or member[5]
                    new_disease = st.text_input(f"New Any Disease ({member[6]}): ").strip() or member[6]
                    pending_update = st.number_input(f"Pending update ({member[10]}): ") or member[10]

                    status_info = st.selectbox(f"status ({member[11]})", ("same", "Active")) or member[10]
                    if status_info == "Active":
                        new_ending_date = st.date_input(f"New ending date for ID {member[0]}")
                        if st.button("change"):
                            cursor_update = db.cursor()
                            sql_update = "UPDATE members SET ending_date = %s, Status = 'Active' WHERE id = %s"
                            cursor_update.execute(sql_update, (new_ending_date, member[0]))  # type: ignore
                            db.commit()
                            st.success(f"Membership for ID {member[0]} updated successfully.")

                    if st.button("Save"):
                        cursor = db.cursor()
                        sql = """UPDATE members 
                        SET  Fees = Fees + pending - %s ,pending  =  %s  Where id = %s"""
                        val = (pending_update, pending_update, self.selected_id)
                        cursor.execute(sql, val)  # type: ignore
                        db.commit()
                        update_sql = "UPDATE members SET Name = %s, Phone_Number = %s, Age = %s, Height = %s, Weight = %s, Any_disease = %s WHERE id = %s"
                        val = (new_name, new_phone, new_age, new_height, new_weight, new_disease, self.selected_id)
                        cursor.execute(update_sql, val)  # type: ignore
                        db.commit()

                        st.success(f"Member ID {self.selected_id} has been updated.")

                else:
                    st.warning(f"Member ID {self.selected_id} does not exist.")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")
            finally:
                cursor.close()

    update = Update_info(selected_id)


elif page == "View Data":
    view_option = st.selectbox("Select which data you want to see", ("Active", "Inactive", "All Data"))

    if view_option == "Active":
        cursor = db.cursor()
        sql = "SELECT * FROM members WHERE status = 'Active'"
        cursor.execute(sql)

        data = cursor.fetchall()

        cursor.close()

        if cursor.description:
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
            st.write(df)
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="members.csv">Download CSV</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("No data found.")


    elif view_option == "Inactive":
        cursor = db.cursor()
        sql = "SELECT * FROM members Where status ='Inactive'"
        cursor.execute(sql)

        data = cursor.fetchall()

        cursor.close()

        if cursor.description:
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
            st.write(df)
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="members.csv">Download CSV</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("No data found.")


    elif view_option == "All Data":
        cursor = db.cursor()
        sql = "SELECT * FROM members"
        cursor.execute(sql)

        data = cursor.fetchall()

        cursor.close()

        if cursor.description:
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
            st.write(df)
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="members.csv">Download CSV</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("No data found.")
       
    else:
        st.warning("No data Found ")


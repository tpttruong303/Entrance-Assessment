import pandas as pd
import json

def is_leave_request(row):
    keywords = ['leave', 'time off', 'day off', 'vacation', 'absence', 'sick', 'out of office']
    
    subject = str(row['subject']).lower()
    body = str(row['body']).lower()

    for keyword in keywords:
        if keyword in subject or keyword in body:
            return True
    return False


def main():
    main_email_path = "emails.csv"
    df = pd.read_csv(main_email_path)
    leave_requests_index = df.apply(is_leave_request, axis=1)
    leave_requests = df[leave_requests_index]

    remain_columns = ['id', 'sender']
    for col in df.columns:
        if col not in remain_columns:
            leave_requests = leave_requests.drop(columns=[col])

    type_leave_requests = ['leave_request'] * len(leave_requests)
    leave_requests['type'] = type_leave_requests

    leave_requests.to_json("leave_request.json", orient="records")

if __name__ == "__main__":
    main()

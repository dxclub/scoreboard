import time, sys, time, os, gspread
from ascii_art import congrats, insta
from time import sleep
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials


def main():
    # Configurations for connecting to the Google Sheets/Drive API 
    scope = ["https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets", 
            "https://www.googleapis.com/auth/drive.file", 
            "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("ENTERGOOGLESHEETSNAMEHERE").sheet1


    type_writer("Solve the [CHALLENGENAMEHERE] challenge!\n", 0.05)
    type_writer("--------------------------------------------------------\n", 0.01)
    type_writer("CHALLENGE ASCII ART HERE FROM ASCII.PY", 0.001)
    type_writer("\n--------------------------------------------------------\n", 0.01)
    type_writer("Scoreboard:\n\n", 0.05)

    # Timer: 600 seconds for 10 mins
    for i in range(1200, 0, -1):
        mins = i // 60
        sec = i % 60
        print(f"Countdown: {mins:02d}:{sec:02d} mins", end = '\r')
        sleep(1)
        data = sheet.get_all_records()

        # Constantly checks google sheets for any of the answers being inputted by a team.
        for i in range(len(data)):

            team = data[i]['Team Name']
            answer = data[i]["Answer"]

            # If answer is found by the competitor
            if("CORRECTANSWERHERE" in answer):
                print(f"\r{team} solved the cipher!\n")
                sheet.update_cell(i+2, 3, "SOLVED_CHALLENGE")

# Continously prints the progress characters to create a download/upload progress bar animation
def progress(process):
    items = list(range(0, 30))
    ls = len(items)
    progress_settings(0, ls, prefix=process, suffix='Complete', length=50)
    for i, item in enumerate(items):
        time.sleep(0.1)
        progress_settings(i + 1, ls, prefix=process, suffix='Complete', length=50)

# Creates the chars for the progress bar in the console
def progress_settings(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', print_end="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=print_end)
    if iteration == total:
        print()

# Type writer animation for the console!
def type_writer(message, speed):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


if __name__ == '__main__':
    main()
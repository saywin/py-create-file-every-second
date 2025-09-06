import time
from datetime import datetime


def main() -> None:
    while True:
        date_time = datetime.now()
        line_file_content = date_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f'app-{date_time.strftime("%H_%M_%S")}.log'
        with open(file_name, "w") as file:
            file.write(line_file_content)
        print(line_file_content, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()

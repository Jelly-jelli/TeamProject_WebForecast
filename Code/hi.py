from datetime import datetime

# Super Group Members
professor = "Brian Courtehoute"
members = [
    "Tanya Chansataporn",
    "Sofiia Piustonen",
    "Karthik Satheesh",
    "Ashok Kumar Pitta",
    "Xinjiang Liu",
    "Neil C Kalapurackal"
]


def main():
    print("Hello Super Group!")
    print("Current Date & Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print("\nProfessor:")
    print("-", professor)

    print("\nMembers:")
    for member in members:
        print("-", member)


if __name__ == "__main__":
    main()
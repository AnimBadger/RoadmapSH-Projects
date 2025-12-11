from github_activity import fetch_github_activity, print_events

def main():
    username = input("Enter GitHub username\n> ").strip()
    events = fetch_github_activity(username)
    print_events(events)


if __name__ == '__main__':
    main()
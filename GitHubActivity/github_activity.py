from typing import Union, Dict, List
import urllib.request
import urllib.error
import json

def fetch_github_activity(username: str) -> Union[List[Dict], Dict[str, str]]:
    '''
    Docstring for fetch_github_activities
    
    :param username: github username
    :type username: str
    :return: Activities of user or error
    :rtype: List[Dict] | Dict[str, str]
    '''

    if not username or not username.strip():
        raise ValueError('Username cannot be empty')
    
    url = f"https://api.github.com/users/{username}/events"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.getcode()

            if status == 404:
                return {'Error': 'User not found'}
            
            raw = response.read().decode()
            data = json.loads(raw)

            if not isinstance(data, list):
                return {'error': 'Unexpected API response'}
            
            return data
        
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"error": "User not found"}
        return {"error": f"HTTP Error {e.code}"}

    except urllib.error.URLError:
        return {"error": "Network connection failed"}

    except json.JSONDecodeError:
        return {"error": "Invalid JSON received"}

    except Exception:
        return {"error": "Unknown error occurred"}


def print_events(events):
    """Make events readable and clean when printed."""
    if isinstance(events, dict) and "error" in events:
        print(f"❌ {events['error']}")
        return

    if not events:
        print("ℹ️ No recent activity found for this user.")
        return

    print("\n=== 🎯 Recent GitHub Activity ===\n")

    for event in events[:10]:  # Limit to latest 10 events
        event_type = event.get("type", "UnknownEvent")
        repo = event.get("repo", {}).get("name", "Unknown Repository")
        created = event.get("created_at", "Unknown Time")

        print(f"• 📌 {event_type.replace('Event', '')} in {repo} at {created}")

    print("\n=================================\n")
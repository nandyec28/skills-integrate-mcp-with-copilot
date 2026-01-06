#!/usr/bin/env python3
"""
Script to create GitHub issues for new features
"""
import subprocess
import json

issues = [
    {
        "title": "Enhance Capacity Management",
        "body": """Improve enforcement of max_participants limits for activities.

## Description
Ensure the system properly validates and prevents signup when an activity has reached maximum capacity.

## Details
- Display clear error messages when activity is full
- Prevent form submission if capacity is reached
- Show capacity status in real-time updates

## Type
Enhancement"""
    },
    {
        "title": "Implement Duplicate Signup Prevention",
        "body": """Add validation to prevent students from signing up twice for the same activity.

## Description
Currently the system checks for duplicate signups, but we should enhance the UX to provide clear feedback before form submission.

## Details
- Validate on form submission that email isn't already registered
- Show helpful error message if student tries to register again
- Consider adding client-side validation for better UX

## Type
Enhancement"""
    },
    {
        "title": "Implement Real-time Spot Calculation Display",
        "body": """Show real-time available spots for each activity in a clear, prominent way.

## Description
Display "X spots left" for each activity based on current participants vs. max capacity.

## Details
- Show spot count in activity cards
- Update display in real-time when participants join/leave
- Highlight when activity is nearly full or completely full
- Handle capacity edge cases gracefully

## Type
Feature"""
    },
    {
        "title": "Display Participant Email Addresses",
        "body": """Show full email addresses of enrolled students in the participants list.

## Description
Make it easy for organizers and students to see who is enrolled in each activity.

## Details
- Display email addresses next to each participant
- Ensure proper formatting and visibility
- Make emails selectable for easy copying
- Consider privacy implications if applicable

## Type
Feature"""
    },
    {
        "title": "Improve Empty State Handling",
        "body": """Add better messaging and UX when activities have no participants.

## Description
Currently shows "No participants yet" but we can enhance the empty state experience.

## Details
- Show friendly "No participants yet" message
- Add visual indication of empty state
- Consider showing a call-to-action for signup
- Ensure consistency across all activities

## Type
Enhancement"""
    }
]

def create_issue(title, body):
    """Create a GitHub issue using curl"""
    cmd = [
        "curl",
        "-X", "POST",
        "https://api.github.com/repos/nandyec28/skills-integrate-mcp-with-copilot/issues",
        "-H", "Accept: application/vnd.github+json",
        "-H", "Content-Type: application/json",
        "-d", json.dumps({"title": title, "body": body})
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            response = json.loads(result.stdout)
            if "number" in response:
                print(f"✓ Created issue #{response['number']}: {title}")
                return True
        else:
            print(f"✗ Failed to create issue: {title}")
            print(f"  Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Error creating issue: {e}")
        return False

if __name__ == "__main__":
    print("Note: Creating issues without authentication will be rate-limited.")
    print("For authenticated requests, set GITHUB_TOKEN environment variable.\n")
    
    success_count = 0
    for issue in issues:
        if create_issue(issue["title"], issue["body"]):
            success_count += 1
    
    print(f"\n✓ Successfully created {success_count}/{len(issues)} issues")

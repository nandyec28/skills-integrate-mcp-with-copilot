# GitHub Issues for New Features

Below are the 5 feature enhancement issues to create in your repository. You can create these manually through the GitHub UI or use the GitHub CLI.

## Issue 1: Enhance Capacity Management
**Title:** Enhance Capacity Management
**Description:** Improve enforcement of max_participants limits for activities.

- Display clear error messages when activity is full
- Prevent form submission if capacity is reached
- Show capacity status in real-time updates

**Type:** Enhancement

---

## Issue 2: Implement Duplicate Signup Prevention
**Title:** Implement Duplicate Signup Prevention
**Description:** Add validation to prevent students from signing up twice for the same activity.

- Validate on form submission that email isn't already registered
- Show helpful error message if student tries to register again
- Consider adding client-side validation for better UX

**Type:** Enhancement

---

## Issue 3: Implement Real-time Spot Calculation Display
**Title:** Implement Real-time Spot Calculation Display
**Description:** Show real-time available spots for each activity in a clear, prominent way.

- Show spot count in activity cards
- Update display in real-time when participants join/leave
- Highlight when activity is nearly full or completely full
- Handle capacity edge cases gracefully

**Type:** Feature

---

## Issue 4: Display Participant Email Addresses
**Title:** Display Participant Email Addresses
**Description:** Show full email addresses of enrolled students in the participants list.

- Display email addresses next to each participant
- Ensure proper formatting and visibility
- Make emails selectable for easy copying
- Consider privacy implications if applicable

**Type:** Feature

---

## Issue 5: Improve Empty State Handling
**Title:** Improve Empty State Handling
**Description:** Add better messaging and UX when activities have no participants.

- Show friendly "No participants yet" message
- Add visual indication of empty state
- Consider showing a call-to-action for signup
- Ensure consistency across all activities

**Type:** Enhancement

---

## How to Create These Issues

### Option 1: Using GitHub CLI (Recommended)
```bash
gh issue create --title "Enhance Capacity Management" --body "Improve enforcement of max_participants limits..."
```

### Option 2: Using GitHub Web UI
1. Go to https://github.com/nandyec28/skills-integrate-mcp-with-copilot/issues
2. Click "New issue"
3. Copy the title and description from above
4. Click "Submit new issue"

### Option 3: Using GitHub API with curl
```bash
curl -X POST https://api.github.com/repos/nandyec28/skills-integrate-mcp-with-copilot/issues \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -d '{"title":"Issue Title","body":"Issue description"}'
```

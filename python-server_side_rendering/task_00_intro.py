import os

def generate_invitations(template, attendees):
    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if the template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process the attendees
    for index, attendee in enumerate(attendees, start=1):
        # Replace the placeholders
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") or "N/A"
            invitation = invitation.replace(f"{{{key}}}", value)

        # Write to a file
        output_filename = f"output_{index}.txt"
        with open(output_filename, "w") as file:
            file.write(invitation)

        print(f"Generated: {output_filename}")




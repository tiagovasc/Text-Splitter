import csv

def parse_transcript_to_csv(transcript, csv_filename):
    # Split the transcript into paragraphs based on timestamps
    paragraphs = transcript.strip().split('\n\n')

    # Parse the paragraphs and timestamps
    data = []
    for paragraph in paragraphs:
        parts = paragraph.split('\n', 1)
        if len(parts) == 2:  # Check if there are two parts
            speaker_info, text = parts[0], parts[1]
            # Combine speaker info and text into a single string
            combined_text = f"{speaker_info} {text.strip()}"
            data.append([combined_text])

    # Create a CSV file
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Text'])
        writer.writerows(data)

# Example usage
transcript = "HERE"

csv_filename = 'podcast_transcript.csv'
parse_transcript_to_csv(transcript, csv_filename)

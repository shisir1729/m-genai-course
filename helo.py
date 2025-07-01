import os
import argparse
from google import genai
from dotenv import load_dotenv
load_dotenv()
def generate_poem(user_prompt):
    """
    Generates a poem on Generative AI applicable to education in Nepal,
    using the provided user prompt as a starting point.
    """
    # Initialize the GenAI client with the API key from environment variables
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # Specify the model to use
    model = "gemini-2.0-flash"

    # Define the content for the model. The 'parts' list now directly contains the text.
    contents = [
        {
            "role": "user",
            "parts": [
                {"text": user_prompt},
            ],
        },
    ]

    # Configure how the content should be generated.
    # The 'system_instruction' also directly contains the text.
    generate_content_config = {
        "response_mime_type": "text/plain",
        "system_instruction": [
            {"text": "Generate a Poem on Generative AI that is applicable to education in Nepal."},
        ],
    }

    print("Generating poem...\n")

    # Stream the content generation and print each chunk
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")
    print("\n") # Add a newline for better formatting after the poem

if __name__ == "__main__":
    # Set up argument parsing for command-line input
    parser = argparse.ArgumentParser(description="Generate a poem about Generative AI and education in Nepal.")
    parser.add_argument("prompt", type=str,
                        help="The starting text or prompt for the poem. Enclose in quotes if it contains spaces.")

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Call the function to generate the poem with the user's prompt
    generate_poem(args.prompt)
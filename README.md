# Play Review Prompts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This tool is designed to load Google Play Store reviews for a given app into a SQLite database. This can be particularly useful for generating prompts for large language models (LLMs) based on real user feedback.

## Getting Started

This project utilizes the `google_play_scraper` Python library to fetch reviews from the Google Play Store, and `sqlite3` to store the results in a local SQLite database.

### Prerequisites

- Python 3
- Python `google_play_scraper` library
- Python `sqlite3` library

You can install the necessary libraries with pip:

```bash
pip install google_play_scraper
```

`sqlite3` is a part of the Python standard library and does not need to be installed separately.

### Usage

To use this tool, you need to modify the `app_id` in the script to match the ID of the app you're interested in:

```python
app_id = 'com.example' # change for your app's id
```

The app's ID is the final part of the URL on its Play Store page. For example, if the URL is `https://play.google.com/store/apps/details?id=com.example`, then the app's ID is `com.example`.

Once you've set the `app_id`, you can run the script. It will create a SQLite database called `reviews.db` and a table called `reviews` if they don't already exist, and then populate the table with reviews for the specified app.

Each review is stored with the following data:

- `reviewId`: The unique identifier for the review
- `userName`: The name of the user who wrote the review
- `userImage`: The URL of the user's profile image
- `content`: The text of the review
- `score`: The rating given by the user (out of 5)
- `thumbsUpCount`: The number of thumbs-up the review received
- `reviewCreatedVersion`: The version of the app when the review was written
- `at`: The time when the review was written
- `replyContent`: The developer's reply to the review, if any
- `repliedAt`: The time when the developer replied, if applicable
- `appVersion`: The current version of the app when the data is retrieved

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

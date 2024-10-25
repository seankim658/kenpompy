"""
The utils module provides utility functions, such as logging in.
"""

import cloudscraper

def login(email, password):

    # Create a Cloudscraper session
    scraper = cloudscraper.create_scraper()

    scraper.get('https://kenpom.com/index.php')

    form_data = {
        'email': email,
        'password': password,
        'submit': 'Login!',
    }

    scraper.post(
        'https://kenpom.com/handlers/login_handler.php',
        data=form_data,
        allow_redirects=True,
    )

    # Check if login was successful
    home_page = scraper.get('https://kenpom.com/')
    if 'Logout' not in home_page.text:
        raise Exception('Logging in failed - check your credentials.')

    return scraper

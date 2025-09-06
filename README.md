# Secunoid Security Consulting SPA

A modern, single-page application (SPA) for Secunoid Security Consulting, providing information about cybersecurity architecture, GRC services, and business continuity solutions.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview
Secunoid Security Consulting SPA is a static website designed to showcase the services, expertise, and contact information for Secunoid. It features a responsive design, interactive elements, and clear calls to action for potential clients.

## Features
- Responsive layout for desktop and mobile
- Navigation bar with smooth scrolling
- Hero section with dynamic typing effect
- About, Services, Industries, and Contact sections
- Social media links
- Animated service and industry cards
- Contact form (simulated submission)
- Scroll progress indicator

## Project Structure
```
secunoid-dot-com-spa/
├── index.html         # Main HTML file
├── assets/            # Images, icons, and other static assets
├── test_links.py      # Selenium test script for link validation
├── README.md          # Project documentation
```

## Setup & Installation
1. **Clone the repository:**
	 ```sh
	 git clone https://github.com/secunoid/secunoid-dot-com-spa.git
	 cd secunoid-dot-com-spa
	 ```
2. **Open `index.html` in your browser:**
	 - Double-click the file or use `file:///` path in your browser.

### Optional: Run Link Tests
- Install Python and Selenium:
	```sh
	pip install selenium
	```
- Download and add `chromedriver` to your PATH.
- Run the test script:
	```sh
	python test_links.py
	```

## Usage
- Browse the site to view services, industries, and contact options.
- Use the navigation bar to jump to sections.
- Click social media icons to visit Secunoid's profiles.
- Use the contact form to simulate a consultation request.

## Testing
- Automated link testing is provided via `test_links.py`.
- The script checks all anchor tags for valid navigation and reports results in the console.

## Deployment
To make the site accessible on the internet:
1. Host the contents on a static web server (e.g., GitHub Pages, Netlify, Vercel, AWS S3).
2. Update asset paths if needed for your hosting environment.
3. For custom domains, configure DNS and SSL as required.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature or fix
3. Submit a pull request with a clear description

## License
This project is licensed under the MIT License. See `LICENSE` for details.
# secunoid-dot-com-spa
Secunoid Single Page Application

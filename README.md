# Resume Website

A modern, responsive personal resume website designed for GitHub Pages deployment.

## Features

- Clean single-page resume layout
- Sections for profile, experience, education, projects, skills, certifications, and contact
- Mobile-friendly responsive design
- Simple static HTML, CSS, and JavaScript
- Easy to customize with your own content

## Project Structure

- `index.html` – page structure and content
- `styles.css` – layout and visual styling
- `script.js` – mobile navigation behavior and footer year

## Local Preview

Run a simple local web server from the project root:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## Deploy to GitHub Pages

1. Push this project to a GitHub repository.
2. Open the repository in GitHub.
3. Go to Settings > Pages.
4. Set the source to the default branch.
5. Select the root folder `/` and save.
6. GitHub will publish the site and provide a URL.

## Customize the Resume

Update the text in `index.html` to reflect your own profile, work history, projects, and contact information.

## Notes

This project is intentionally static and lightweight so it can be hosted affordably and deployed quickly on GitHub Pages.

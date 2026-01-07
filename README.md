# Amrita's Portfolio

An interactive and modern portfolio website showcasing projects, skills, achievements, and certifications.

## Features

- 🎨 **Modern Design** - Clean and professional UI with gradient effects
- ✨ **Dynamic Animations** - Smooth transitions and interactive elements
- 📱 **Fully Responsive** - Works perfectly on all devices
- 🎯 **Interactive Sections**:
  - Home with animated typing effect
  - About Me with education timeline
  - Skills with progress bars
  - Projects showcase
  - Achievements timeline
  - Certifications gallery
  - Contact form
- 🔗 **Social Links** - GitHub, LinkedIn, Codeforces, Email
- 📄 **Resume Download** - Easy access to downloadable resume

## Setup Instructions

### 1. Add Your Profile Image

Replace the placeholder profile image:
- Add your photo as `profile.png` in the root directory
- Recommended: Use a photo with transparent background
- Size: 500x500px or larger for best quality

### 2. Add Project Images

Add images for your projects (6 images needed):
- `project1.jpg` through `project6.jpg`
- Recommended size: 800x600px
- Place them in the root directory

### 3. Customize Content

Edit `index.html` to update:
- Your name and personal information
- Project details and links
- Education information
- Achievement descriptions
- Certificate details
- Contact information
- Social media links

### 4. Add Your Resume

- Add your resume PDF as `Amrita_Resume.pdf`
- Update the download link in `script.js` (line ~270)

### 5. Update Links

Replace placeholder links with your actual profiles:
- GitHub: Update all GitHub links
- LinkedIn: Update LinkedIn profile URL
- Codeforces: Update Codeforces profile URL
- Email: Replace with your email address
- Project links: Add actual GitHub/live demo links

## Customization

### Colors

Edit CSS variables in `styles.css` (lines 12-22):
```css
:root {
    --primary-color: #6c5ce7;
    --secondary-color: #00b894;
    --accent-color: #fd79a8;
    /* ... more colors */
}
```

### Typing Animation

Edit phrases in `script.js` (lines ~50-56):
```javascript
const phrases = [
    'Your Title 1',
    'Your Title 2',
    'Your Title 3'
];
```

### Skills

Update skill items in `index.html` skills section with your actual skills and proficiency levels.

## Running Locally

Simply open `index.html` in your web browser. No build process required!

For development with live reload:
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve
```

Then visit `http://localhost:8000` in your browser.

## Technologies Used

- HTML5
- CSS3 (with CSS Grid and Flexbox)
- Vanilla JavaScript
- Font Awesome Icons
- Google Fonts (Poppins)

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Performance Features

- Lazy loading for images
- Intersection Observer for animations
- Optimized animations
- Minimal dependencies

## Deployment

Deploy to any static hosting service:
- GitHub Pages
- Netlify
- Vercel
- AWS S3
- Firebase Hosting

## Credits

Created with ❤️ and lots of ☕

## License

Feel free to use this template for your own portfolio. Attribution appreciated but not required.

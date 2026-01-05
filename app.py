from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Your email
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Your app password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        # Create email message
        msg = Message(
            subject=f'Portfolio Contact: {subject}',
            recipients=[os.getenv('MAIL_USERNAME')],  # Your email
            reply_to=email
        )
        
        msg.body = f"""
New message from your portfolio website!

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
Sent from your portfolio contact form
        """
        
        msg.html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <h2 style="color: #6c5ce7;">New Portfolio Contact Form Submission</h2>
                <div style="background-color: #f4f4f4; padding: 20px; border-radius: 5px;">
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Email:</strong> <a href="mailto:{email}">{email}</a></p>
                    <p><strong>Subject:</strong> {subject}</p>
                    <hr style="border: 1px solid #ddd;">
                    <p><strong>Message:</strong></p>
                    <p style="background-color: white; padding: 15px; border-left: 4px solid #6c5ce7;">
                        {message}
                    </p>
                </div>
                <p style="color: #888; font-size: 12px; margin-top: 20px;">
                    This email was sent from your portfolio contact form.
                </p>
            </body>
        </html>
        """
        
        mail.send(msg)
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'}), 200
    
    except Exception as e:
        print(f'Error sending email: {str(e)}')
        return jsonify({'success': False, 'message': 'Failed to send message. Please try again.'}), 500

if __name__ == '__main__':
    # Use environment variable for port (important for deployment platforms)
    port = int(os.environ.get('PORT', 5000))
    # Set debug=False for production, True for local development
    app.run(debug=True, host='0.0.0.0', port=port)

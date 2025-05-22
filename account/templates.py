EMAIL_MESSAGE_TO_PROSPECT_TEMPLATE = """
    Hi {name},

    Thank you for reaching out to us and submitting your information. We’ve received your details and resume successfully.
    
    One of our attorneys will review your submission and get in touch with you shortly if any further information is needed.
    
    We appreciate your interest and look forward to speaking with you.
    
    Best regards,  
    The Mohirdev Team

"""


EMAIL_MESSAGE_TO_ATTORNEY_TEMPLATE = """
    A new lead has just been submitted by a prospect.
    
    Here are the details:
    - Name: {first_name} {last_name}
    - Email: {email}
    - Resume/CV: {file_link}
    
    Please review the lead at your earliest convenience and follow up accordingly.
    
    Thank you,  
    Mohirdev Lead Management System
"""
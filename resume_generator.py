#!/usr/bin/env python3
"""
Simple PDF Resume Generator
Creates a professional resume PDF from user input.
Run with: python resume_generator.py
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os
from datetime import datetime

class ResumeGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
    
    def setup_custom_styles(self):
        """Create custom styles for the resume"""
        # Header style for name
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=6,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        ))
        
        # Subtitle style for profession
        self.styles.add(ParagraphStyle(
            name='Subtitle',
            parent=self.styles['Normal'],
            fontSize=14,
            spaceAfter=12,
            alignment=TA_CENTER,
            textColor=colors.grey
        ))
        
        # Section header style
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=6,
            textColor=colors.darkblue,
            borderWidth=1,
            borderColor=colors.darkblue,
            borderPadding=3
        ))

    def get_user_input(self):
        """Collect resume information from user"""
        print("=== PDF Resume Generator ===\n")
        
        # Basic info
        name = input("Full Name: ").strip()
        profession = input("Profession/Title: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone: ").strip()
        location = input("Location (City, State): ").strip()
        
        # Skills
        print("\nEnter your key skills (one per line, press Enter twice when done):")
        skills = []
        while True:
            skill = input("- ").strip()
            if skill:
                skills.append(skill)
            else:
                break
        
        # Experience
        print("\nWork Experience:")
        experience = []
        while True:
            print(f"\nJob #{len(experience) + 1} (press Enter for job title to finish):")
            job_title = input("Job Title: ").strip()
            if not job_title:
                break
            
            company = input("Company: ").strip()
            duration = input("Duration (e.g., '2020-2023'): ").strip()
            
            print("Job responsibilities (one per line, press Enter twice when done):")
            responsibilities = []
            while True:
                resp = input("• ").strip()
                if resp:
                    responsibilities.append(resp)
                else:
                    break
            
            experience.append({
                'title': job_title,
                'company': company,
                'duration': duration,
                'responsibilities': responsibilities
            })
        
        # Education
        print("\nEducation:")
        education = []
        while True:
            print(f"\nEducation #{len(education) + 1} (press Enter for degree to finish):")
            degree = input("Degree: ").strip()
            if not degree:
                break
            
            school = input("School/University: ").strip()
            year = input("Graduation Year: ").strip()
            
            education.append({
                'degree': degree,
                'school': school,
                'year': year
            })
        
        return {
            'name': name,
            'profession': profession,
            'email': email,
            'phone': phone,
            'location': location,
            'skills': skills,
            'experience': experience,
            'education': education
        }

    def create_resume(self, data, filename):
        """Generate the PDF resume"""
        doc = SimpleDocTemplate(filename, pagesize=letter, 
                              rightMargin=0.75*inch, leftMargin=0.75*inch,
                              topMargin=0.75*inch, bottomMargin=0.75*inch)
        
        story = []
        
        # Header with name and profession
        story.append(Paragraph(data['name'], self.styles['CustomTitle']))
        story.append(Paragraph(data['profession'], self.styles['Subtitle']))
        story.append(Spacer(1, 12))
        
        # Contact info
        contact_info = f"{data['email']} | {data['phone']} | {data['location']}"
        story.append(Paragraph(contact_info, self.styles['Normal']))
        story.append(Spacer(1, 24))
        
        # Skills section
        if data['skills']:
            story.append(Paragraph("SKILLS", self.styles['SectionHeader']))
            skills_text = " • ".join(data['skills'])
            story.append(Paragraph(skills_text, self.styles['Normal']))
            story.append(Spacer(1, 18))
        
        # Experience section
        if data['experience']:
            story.append(Paragraph("WORK EXPERIENCE", self.styles['SectionHeader']))
            for job in data['experience']:
                # Job title and company
                job_header = f"<b>{job['title']}</b> - {job['company']} ({job['duration']})"
                story.append(Paragraph(job_header, self.styles['Normal']))
                
                # Responsibilities
                for resp in job['responsibilities']:
                    story.append(Paragraph(f"• {resp}", self.styles['Normal']))
                
                story.append(Spacer(1, 12))
        
        # Education section
        if data['education']:
            story.append(Paragraph("EDUCATION", self.styles['SectionHeader']))
            for edu in data['education']:
                edu_text = f"<b>{edu['degree']}</b> - {edu['school']} ({edu['year']})"
                story.append(Paragraph(edu_text, self.styles['Normal']))
                story.append(Spacer(1, 6))
        
        # Build PDF
        doc.build(story)
        print(f"\nResume saved as: {filename}")

def main():
    try:
        generator = ResumeGenerator()
        
        # Get user input
        resume_data = generator.get_user_input()
        
        # Generate filename
        name_for_file = resume_data['name'].replace(' ', '_').lower()
        timestamp = datetime.now().strftime("%Y%m%d")
        filename = f"{name_for_file}_resume_{timestamp}.pdf"
        
        # Create the resume
        print(f"\nGenerating resume...")
        generator.create_resume(resume_data, filename)
        
        print(f"✅ Resume created successfully!")
        print(f"📄 File: {os.path.abspath(filename)}")
        
    except ImportError:
        print("❌ Error: reportlab library not found!")
        print("Install it with: pip install reportlab")
        
    except Exception as e:
        print(f"❌ Error creating resume: {str(e)}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Simple run script for Natalia's Flashcards application.
This script will install dependencies if needed and start the Flask app.
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required dependencies from requirements.txt"""
    try:
        print("Installing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Error installing dependencies. Please check your Python and pip installation.")
        return False

def run_app():
    """Run the Flask application"""
    try:
        print("Starting Natalia's Flashcards...")
        print("Open your browser and go to: http://localhost:5000")
        print("Press Ctrl+C to stop the server")
        
        # Import and run the app
        from app import app, db
        with app.app_context():
            db.create_all()
        
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except ImportError:
        print("Failed to import the application. Installing dependencies...")
        if install_dependencies():
            print("Dependencies installed. Please run the script again.")
        return False
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        return True
    except Exception as e:
        print(f"Error running the application: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("     Natalia's Flashcards Application")
    print("=" * 50)
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("Error: requirements.txt not found!")
        sys.exit(1)
    
    # Try to run the app, install dependencies if needed
    success = run_app()
    
    if not success:
        print("Failed to start the application.")
        sys.exit(1)
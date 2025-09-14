import os
import json
import requests
import streamlit as st

class FirebaseAuth:
    def __init__(self):
        # Firebase Web API Key - should be provided in environment
        self.api_key = "AIzaSyDN0E7ombncbYj-_iLhcEYxUGHb1FWo-6E"
        self.auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.api_key}"
        
    def authenticate_user(self, email, password):
        """
        Authenticate user with Firebase using email and password
        """
        # Demo credentials for testing - in production, remove these
        demo_users = {
            "demo@cyberwolf.com": "demo123",
            "test@cyberwolf.com": "test123", 
            "user@example.com": "Password123!",
            "agent@cyberwolf.com": "cyberwolf2024"
        }
        
        # Check if this is a demo user first
        if email in demo_users and password == demo_users[email]:
            return {
                "uid": f"demo_{email.split('@')[0]}",
                "email": email,
                "token": "demo_token_" + email.split('@')[0]
            }
        
        try:
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": True
            }
            
            response = requests.post(self.auth_url, json=payload)
            
            if response.status_code == 200:
                user_data = response.json()
                return {
                    "uid": user_data.get("localId"),
                    "email": user_data.get("email"),
                    "token": user_data.get("idToken")
                }
            else:
                error_data = response.json()
                error_message = error_data.get("error", {}).get("message", "Unknown error")
                
                # Handle common Firebase errors
                if "EMAIL_NOT_FOUND" in error_message:
                    return None
                elif "INVALID_PASSWORD" in error_message:
                    return None
                elif "USER_DISABLED" in error_message:
                    raise Exception("User account has been disabled")
                else:
                    raise Exception(f"Authentication error: {error_message}")
                    
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error during authentication: {str(e)}")
        except Exception as e:
            raise Exception(f"Authentication failed: {str(e)}")
    
    def verify_token(self, token):
        """
        Verify Firebase ID token
        """
        try:
            verify_url = f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={self.api_key}"
            payload = {"idToken": token}
            
            response = requests.post(verify_url, json=payload)
            
            if response.status_code == 200:
                return response.json()
            else:
                return None
                
        except Exception as e:
            st.error(f"Token verification failed: {str(e)}")
            return None

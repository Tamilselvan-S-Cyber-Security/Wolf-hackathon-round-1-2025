import json
import os
from datetime import datetime

class Database:
    def __init__(self):
        self.data_file = "user_data.json"
        self._ensure_data_file()
    
    def _ensure_data_file(self):
        """
        Ensure the data file exists
        """
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump({}, f)
    
    def get_user_data(self, email):
        """
        Get user data from the database
        """
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                return data.get(email, None)
        except (FileNotFoundError, json.JSONDecodeError):
            return None
    
    def save_user_data(self, email, health_score, completed_challenges, current_challenge, user_score=0):
        """
        Save user data to the database
        """
        try:
            # Load existing data
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}
            
            # Update user data
            data[email] = {
                'health_score': health_score,
                'completed_challenges': completed_challenges,
                'current_challenge': current_challenge,
                'user_score': user_score,
                'last_updated': datetime.now().isoformat()
            }
            
            # Save updated data
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Error saving user data: {e}")
            return False
    
    def get_leaderboard(self):
        """
        Get leaderboard data (users sorted by health score and completed challenges)
        """
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            
            # Convert to list and sort by completed challenges and health score
            leaderboard = []
            for email, user_data in data.items():
                leaderboard.append({
                    'email': email,
                    'health_score': user_data.get('health_score', 0),
                    'completed_challenges': len(user_data.get('completed_challenges', [])),
                    'current_challenge': user_data.get('current_challenge', 1)
                })
            
            # Sort by completed challenges (desc) then by health score (desc)
            leaderboard.sort(key=lambda x: (x['completed_challenges'], x['health_score']), reverse=True)
            
            return leaderboard
            
        except Exception as e:
            print(f"Error getting leaderboard: {e}")
            return []
    
    def reset_user_progress(self, email):
        """
        Reset user progress (for admin purposes)
        """
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            
            if email in data:
                data[email] = {
                    'health_score': 100,
                    'completed_challenges': [],
                    'current_challenge': 1,
                    'last_updated': datetime.now().isoformat()
                }
                
                with open(self.data_file, 'w') as f:
                    json.dump(data, f, indent=2)
                
                return True
            
            return False
            
        except Exception as e:
            print(f"Error resetting user progress: {e}")
            return False

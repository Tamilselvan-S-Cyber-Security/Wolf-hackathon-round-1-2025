import os
import google.generativeai as genai

class WolfAI:
    def __init__(self):
        # Initialize Gemini client
        self.api_key = os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None
        
    def get_hint(self, challenge, challenge_num):
        """
        Generate a helpful hint for the given challenge using Wolf AI (Gemini)
        """
        try:
            if not self.model:
                raise Exception("Gemini API not configured")
                
            # Create a contextual prompt for the challenge
            prompt = f"""
            You are Wolf AI, an advanced cybersecurity training assistant created by the CYBERWOLF TEAM. 
            You are helping a student with a cybersecurity CTF challenge.
            
            Challenge {challenge_num}: {challenge['title']}
            Difficulty: {challenge['difficulty']}
            Description: {challenge['description']}
            
            Provide a helpful hint that guides the student towards the solution without giving away the complete answer. 
            Be encouraging and maintain the cybersecurity training theme. 
            Keep the hint concise (2-3 sentences) and technically accurate.
            
            Start your response with a wolf-themed greeting and sign off as "Wolf AI - CYBERWOLF TEAM".
            """
            
            response = self.model.generate_content(prompt)
            
            if response.text:
                return response.text
            else:
                return "Wolf AI is currently unavailable. Try thinking about the fundamentals of this cybersecurity concept."
                
        except Exception as e:
            # Fallback hints for each challenge type
            fallback_hints = {
                1: "Remember, Wireshark captures network packets in .pcap format. Make sure you're capturing actual network traffic, not just opening the application.",
                2: "Burp Suite excels at intercepting HTTP requests. Look for interesting headers in both requests and responses - they often reveal security configurations.",
                3: "Secure APIs need proper input validation, authentication, and protection against common attacks like SQL injection. Consider implementing rate limiting too.",
                4: "Look for common vulnerabilities like XSS, CSRF, or authentication bypasses. The devil is in the details.",
                5: "Network security often involves understanding protocols and traffic patterns. What seems normal might hide something suspicious.",
                6: "Cryptography challenges usually involve understanding encoding, encryption, or hashing algorithms. Don't forget about common techniques.",
                7: "Social engineering attacks often exploit human psychology. Think about what information an attacker might try to gather.",
                8: "Binary analysis requires understanding how programs work at a low level. Look for strings, functions, or unusual behavior.",
                9: "Advanced web exploitation might involve modern frameworks or complex attack chains. Stay systematic in your approach.",
                10: "The final challenge combines everything you've learned. Think holistically about all the cybersecurity domains."
            }
            
            return fallback_hints.get(challenge_num, "Wolf AI is thinking... Try approaching this challenge from a different angle.")
    
    def get_challenge_feedback(self, challenge_num, user_solution):
        """
        Provide feedback on a user's solution attempt
        """
        try:
            if not self.model:
                raise Exception("Gemini API not configured")
                
            prompt = f"""
            You are Wolf AI from the CYBERWOLF TEAM, providing feedback on a cybersecurity challenge solution.
            
            Challenge {challenge_num} solution attempt: {user_solution}
            
            Provide constructive feedback on this solution. If it's incorrect, give guidance on what to improve.
            If it's correct, congratulate them and explain why it works.
            
            Keep it brief (2-3 sentences) and maintain the cybersecurity training theme.
            """
            
            response = self.model.generate_content(prompt)
            
            if response.text:
                return response.text
            else:
                return "Wolf AI is analyzing your solution. Keep refining your approach!"
                
        except Exception as e:
            return "Wolf AI is currently processing. Your dedication to learning cybersecurity is commendable!"

import re
import os

class ChallengeManager:
    def __init__(self):
        self.challenges = self._load_challenges()
    
    def _load_challenges(self):
        """
        Load all 10 cybersecurity challenges
        """
        return [
            {
                "title": "Network Traffic Capture",
                "difficulty": "Easy",
                "points": 100,
                "description": "Learn to capture network traffic using Wireshark, a fundamental skill for network analysis and security monitoring.",
                "instructions": """
                1. Download and install Wireshark from the official website
                2. Start a packet capture on your network interface
                3. Generate some network traffic (browse websites, ping servers)
                4. Stop the capture and save it as a .pcap file
                5. Upload the .pcap file to complete this challenge
                
                **Learning Objective:** Understand how network packet capture works and practice using industry-standard tools.
                """
            },
            {
                "title": "Web Application Analysis",
                "difficulty": "Easy",
                "points": 150,
                "description": "Use Burp Suite to analyze web applications and discover security headers and HTTP methods.",
                "instructions": """
                1. Download and set up Burp Suite Community Edition
                2. Configure your browser to use Burp as a proxy
                3. Navigate to a website and capture HTTP requests
                4. Analyze the requests and responses for security headers
                5. Document the HTTP methods available and any interesting headers
                6. Submit your findings including the target URL, methods found, and security headers discovered
                
                **Learning Objective:** Master web application security testing fundamentals.
                """
            },
            {
                "title": "Secure API Development",
                "difficulty": "Medium",
                "points": 200,
                "description": "Design and implement a simple API with proper security measures to prevent common vulnerabilities.",
                "instructions": """
                1. Create a simple REST API with at least 2 endpoints
                2. Implement proper input validation
                3. Add authentication mechanisms
                4. Include protection against SQL injection
                5. Implement rate limiting
                6. Use HTTPS in production
                7. Submit your code and list the security measures you implemented
                
                **Learning Objective:** Understand secure coding practices for API development.
                """
            },
            {
                "title": "SQL Injection Detection",
                "difficulty": "Medium",
                "points": 250,
                "description": "Identify and exploit SQL injection vulnerabilities in a web application.",
                "instructions": """
                1. Find a web application with potential SQL injection vulnerabilities
                2. Test various injection payloads
                3. Document successful injection attempts
                4. Explain how to prevent these vulnerabilities
                5. Submit your findings and prevention recommendations
                
                **Learning Objective:** Understand SQL injection attacks and prevention techniques.
                """
            },
            {
                "title": "Network Forensics",
                "difficulty": "Medium",
                "points": 300,
                "description": "Analyze network traffic to identify suspicious activities and potential security incidents.",
                "instructions": """
                1. Analyze the provided network capture file
                2. Identify any suspicious network activities
                3. Look for signs of malware communication or data exfiltration
                4. Document your findings with timestamps and evidence
                5. Provide recommendations for network security improvements
                
                **Learning Objective:** Develop network forensics and incident response skills.
                """
            },
            {
                "title": "Cryptographic Analysis",
                "difficulty": "Hard",
                "points": 350,
                "description": "Decrypt encrypted messages and analyze cryptographic implementations for weaknesses.",
                "instructions": """
                1. Analyze the provided encrypted message
                2. Identify the encryption algorithm used
                3. Find weaknesses in the implementation
                4. Decrypt the message or explain why it's secure
                5. Recommend improvements to the cryptographic implementation
                
                **Learning Objective:** Understand cryptography and its security implications.
                """
            },
            {
                "title": "Social Engineering Defense",
                "difficulty": "Medium",
                "points": 275,
                "description": "Identify social engineering techniques and develop countermeasures to protect organizations.",
                "instructions": """
                1. Research common social engineering techniques
                2. Create a phishing email detection guide
                3. Develop a social engineering awareness training outline
                4. Design policies to prevent social engineering attacks
                5. Submit your comprehensive defense strategy
                
                **Learning Objective:** Understand human factors in cybersecurity.
                """
            },
            {
                "title": "Binary Analysis & Reverse Engineering",
                "difficulty": "Hard",
                "points": 400,
                "description": "Analyze binary files to understand their functionality and identify potential security issues.",
                "instructions": """
                1. Use tools like strings, objdump, or IDA to analyze the binary
                2. Identify the program's functionality
                3. Look for security vulnerabilities or malicious behavior
                4. Document your analysis methodology
                5. Provide a comprehensive report of your findings
                
                **Learning Objective:** Develop malware analysis and reverse engineering skills.
                """
            },
            {
                "title": "Advanced Web Exploitation",
                "difficulty": "Hard",
                "points": 450,
                "description": "Exploit complex web application vulnerabilities including XSS, CSRF, and authentication bypasses.",
                "instructions": """
                1. Identify multiple vulnerability types in the target application
                2. Develop working exploits for each vulnerability
                3. Chain exploits together for maximum impact
                4. Document the attack chain and potential damage
                5. Provide detailed remediation recommendations
                
                **Learning Objective:** Master advanced web application security testing.
                """
            },
            {
                "title": "Comprehensive Security Assessment",
                "difficulty": "Hard",
                "points": 500,
                "description": "Conduct a full security assessment combining all learned skills to evaluate a complex system.",
                "instructions": """
                1. Perform network reconnaissance and mapping
                2. Identify web application vulnerabilities
                3. Analyze network traffic for threats
                4. Test for social engineering vulnerabilities
                5. Conduct binary analysis if applicable
                6. Compile a comprehensive security report with prioritized recommendations
                
                **Learning Objective:** Integrate all cybersecurity skills into a holistic assessment.
                """
            }
        ]
    
    def get_all_challenges(self):
        """
        Return all challenges
        """
        return self.challenges
    
    def get_challenge(self, challenge_num):
        """
        Get a specific challenge by number
        """
        if 1 <= challenge_num <= len(self.challenges):
            return self.challenges[challenge_num - 1]
        return None
    
    def validate_challenge_1(self, uploaded_file, flag=None):
        """
        Validate Challenge 1: Wireshark packet capture
        """
        # Check for the correct flag first
        if flag and flag.strip() == "WOLF{VGhldGFtaWxzZ_Wx2YW5je_WJlcndvbGY=}":
            return True
        
        # More lenient validation for file upload
        if uploaded_file is None:
            return False
        
        # Accept any file type (more forgiving)
        if not uploaded_file.name:
            return False
        
        # Accept any reasonable file size
        if uploaded_file.size < 100:  # Very small minimum
            return False
        
        # Accept any file as long as it's uploaded
        return True
    
    def validate_challenge_2(self, target_url, request_method, headers_found, flag=None):
        """
        Validate Challenge 2: Burp Suite web analysis
        """
        # Check for the correct flag first
        if flag and flag.strip() == "WOLF{VGhldGFtaWxzZ_Wx2YW5je_WJlcndvbGY=}":
            return True
        
        # More lenient validation - just check if basic fields are filled
        if not target_url or not request_method:
            return False
        
        # Accept any URL format (more forgiving)
        if not target_url.startswith(('http://', 'https://')):
            return False
        
        # Accept any HTTP method
        if request_method not in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS']:
            return False
        
        # If headers are provided, check for any security-related content
        if headers_found and headers_found.strip():
            headers_lower = headers_found.lower()
            # Look for any security-related keywords
            security_keywords = ['header', 'security', 'http', 'content', 'x-', 'cors', 'auth']
            return any(keyword in headers_lower for keyword in security_keywords)
        
        # If no headers provided, still accept if URL and method are valid
        return True
    
    def validate_challenge_3(self, api_code, security_measures, flag=None):
        """
        Validate Challenge 3: Secure API development
        """
        # Check for the correct flag first
        if flag and flag.strip() == "WOLF{VGhldGFtaWxzZ_Wx2YW5je_WJlcndvbGY=}":
            return True
        
        # More lenient validation for API code
        if not api_code or not security_measures:
            return False
        
        # Accept any code that has some content
        if len(api_code.strip()) < 10:
            return False
        
        # Accept any security measures selected (reduced requirement)
        if len(security_measures) < 1:
            return False
        
        # Accept any reasonable code and security measures
        return True
    
    def validate_generic_challenge(self, challenge_num, solution, flag=None):
        """
        Validate other challenges with basic solution checking
        """
        # Check for the correct flag first
        if flag and flag.strip() == "WOLF{VGhldGFtaWxzZ_Wx2YW5je_WJlcndvbGY=}":
            return True
        
        # More lenient validation for generic challenges
        if not solution or len(solution.strip()) < 10:
            return False
        
        # Accept any reasonable solution
        return True

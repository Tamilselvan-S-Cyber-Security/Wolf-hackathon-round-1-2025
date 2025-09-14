import streamlit as st
import json
import os
from datetime import datetime
from firebase_auth import FirebaseAuth
from wolf_ai import WolfAI
from challenges import ChallengeManager
from database import Database
from styles import apply_custom_styles

# Initialize components
def init_components():
    # Reload modules to ensure latest code
    import importlib
    import challenges
    importlib.reload(challenges)
    
    firebase_auth = FirebaseAuth()
    wolf_ai = WolfAI()
    challenge_manager = challenges.ChallengeManager()
    database = Database()
    return firebase_auth, wolf_ai, challenge_manager, database

def main():
    # Clear cache to ensure latest code is loaded
    st.cache_data.clear()
    st.cache_resource.clear()
    
    st.set_page_config(
        page_title="CYBERWOLF - Cybersecurity CTF",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Apply custom styles
    apply_custom_styles()
    
    # Initialize components
    firebase_auth, wolf_ai, challenge_manager, db = init_components()
    
    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user_email' not in st.session_state:
        st.session_state.user_email = None
    if 'health_score' not in st.session_state:
        st.session_state.health_score = 100
    if 'completed_challenges' not in st.session_state:
        st.session_state.completed_challenges = set()
    if 'current_challenge' not in st.session_state:
        st.session_state.current_challenge = 1
    if 'hint_active' not in st.session_state:
        st.session_state.hint_active = False
    if 'current_hint' not in st.session_state:
        st.session_state.current_hint = None
    if 'current_hint_challenge' not in st.session_state:
        st.session_state.current_hint_challenge = None
    if 'user_score' not in st.session_state:
        st.session_state.user_score = 0
    
    # Authentication flow
    if not st.session_state.authenticated:
        show_login_page(firebase_auth, db)
    else:
        show_main_game(wolf_ai, challenge_manager, db)

def show_login_page(firebase_auth, db):
    st.markdown("""
    <div class="login-container">
        <h1 class="neon-title">CYBERWOLF</h1>
        <h3 class="subtitle">CYBERSECURITY CTF TRAINING</h3>
        <p class="description">Enter the cybersecurity training matrix</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        
        email = st.text_input("Email", key="email_input")
        password = st.text_input("Password", type="password", key="password_input")
        
        if st.button("LOGIN TO MATRIX", key="login_btn", type="primary"):
            if email and password:
                try:
                    user = firebase_auth.authenticate_user(email, password)
                    if user:
                        st.session_state.authenticated = True
                        st.session_state.user_email = email
                        
                        # Load user data
                        user_data = db.get_user_data(email)
                        if user_data:
                            st.session_state.health_score = user_data.get('health_score', 100)
                            st.session_state.completed_challenges = set(user_data.get('completed_challenges', []))
                            st.session_state.current_challenge = user_data.get('current_challenge', 1)
                            st.session_state.user_score = user_data.get('user_score', 0)
                        
                        st.success("Welcome to the Matrix, Agent!")
                        st.rerun()
                    else:
                        st.error("Invalid credentials. Access denied.")
                except Exception as e:
                    st.error(f"Authentication failed: {str(e)}")
            else:
                st.warning("Please enter both email and password")
        
        st.markdown('</div>', unsafe_allow_html=True)

def show_main_game(wolf_ai, challenge_manager, db):
    # Header
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"""
        <div class="game-header">
            <h1 class="neon-title">CYBERWOLF</h1>
            <p class="user-info">Agent: {st.session_state.user_email}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="health-score">
            <h3>Health Score</h3>
            <div class="score-display">{st.session_state.health_score}/100</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("LOGOUT", type="secondary"):
            # Save user data before logout
            db.save_user_data(
                st.session_state.user_email,
                st.session_state.health_score,
                list(st.session_state.completed_challenges),
                st.session_state.current_challenge
            )
            
            # Reset session
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Check if all challenges are completed
    completed_count = len(st.session_state.completed_challenges)
    all_challenges_completed = completed_count >= 10
    
    # Show completion popup if all challenges are done
    if all_challenges_completed and 'completion_popup_shown' not in st.session_state:
        st.session_state.completion_popup_shown = True
        
        with st.container():
            st.markdown("---")
            st.markdown("## 🎉 **CONGRATULATIONS! ALL CHALLENGES COMPLETED!** 🎉")
            st.markdown("### 🏆 You have successfully completed all cybersecurity challenges!")
            
            # Show the flag in a special container
            st.markdown("### 🏴 **YOUR REWARD - THE MASTER FLAG:**")
            st.code("WOLF{VGhldGFtaWxzZ_Wx2YW5je_WJlcndvbGY=}", language="text")
            
            st.markdown("### 🎯 **What you've accomplished:**")
            st.markdown("- ✅ Network Traffic Analysis")
            st.markdown("- ✅ Web Application Security")
            st.markdown("- ✅ API Security Implementation")
            st.markdown("- ✅ SQL Injection Detection")
            st.markdown("- ✅ Network Forensics")
            st.markdown("- ✅ Cryptographic Analysis")
            st.markdown("- ✅ Social Engineering Defense")
            st.markdown("- ✅ Binary Analysis & Reverse Engineering")
            st.markdown("- ✅ Advanced Web Exploitation")
            st.markdown("- ✅ Comprehensive Security Assessment")
            
            st.markdown("### 🔐 **You are now a CYBERWOLF Security Expert!**")
            st.balloons()
            
            # Reset button for testing
            if st.button("🔄 Reset All Challenges (For Testing)", key="reset_challenges"):
                st.session_state.completed_challenges = set()
                st.session_state.current_challenge = 1
                st.session_state.completion_popup_shown = False
                st.rerun()
            
            st.markdown("---")
    
    # Security Dashboard
    st.markdown("---")
    st.markdown("## 🔒 SECURITY DASHBOARD")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Security Score", f"{st.session_state.health_score}/100", delta="0")
    
    with col2:
        st.metric("Challenges Completed", f"{completed_count}/10", delta="0")
    
    with col3:
        st.metric("User Score", f"{st.session_state.user_score}/50", delta="0")
    
    with col4:
        st.metric("Security Level", "EXPERT" if all_challenges_completed else "INTERMEDIATE" if completed_count >= 5 else "BEGINNER", delta="0")
    
    with col5:
        st.metric("Threat Level", "LOW" if st.session_state.health_score >= 80 else "MEDIUM", delta="0")
    
    # Progress indicator
    if not all_challenges_completed:
        remaining = 10 - completed_count
        st.markdown(f"### 🎯 **Progress: {completed_count}/10 Challenges Completed**")
        st.markdown(f"**Score:** {st.session_state.user_score}/50 points")
        st.markdown(f"**Remaining:** {remaining} challenges to unlock the master flag!")
        
        # Progress bar
        progress = completed_count / 10
        st.progress(progress)
        
        if completed_count > 0:
            st.info(f"💡 Complete all {remaining} remaining challenges to unlock the master flag!")
    
    st.markdown("---")
    
    # Security Tips Section
    with st.expander("🛡️ SECURITY TIPS & BEST PRACTICES"):
        st.markdown("""
        **🔐 Authentication & Authorization:**
        - Use multi-factor authentication (MFA)
        - Implement proper session management
        - Apply principle of least privilege
        
        **🛡️ Input Validation & Sanitization:**
        - Validate all user inputs
        - Sanitize data before processing
        - Use parameterized queries
        
        **🔒 Encryption & Data Protection:**
        - Encrypt sensitive data at rest and in transit
        - Use strong encryption algorithms
        - Implement proper key management
        
        **📊 Monitoring & Logging:**
        - Enable comprehensive audit logging
        - Monitor for suspicious activities
        - Implement real-time alerting
        """)
    
    # Challenge selection
    st.markdown('<div class="challenges-container">', unsafe_allow_html=True)
    st.markdown("## CYBERSECURITY CHALLENGES")
    
    # Create challenge grid
    challenges = challenge_manager.get_all_challenges()
    
    for i in range(0, len(challenges), 2):
        col1, col2 = st.columns(2)
        
        for j, col in enumerate([col1, col2]):
            if i + j < len(challenges):
                challenge = challenges[i + j]
                challenge_num = i + j + 1
                
                with col:
                    show_challenge_card(challenge, challenge_num, wolf_ai, challenge_manager, db)
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_challenge_card(challenge, challenge_num, wolf_ai, challenge_manager, db):
    is_completed = challenge_num in st.session_state.completed_challenges
    is_locked = challenge_num > st.session_state.current_challenge
    
    # Determine card style based on difficulty
    if challenge['difficulty'] == 'Easy':
        card_class = "challenge-card-easy"
    elif challenge['difficulty'] == 'Medium':
        card_class = "challenge-card-medium"
    else:
        card_class = "challenge-card-hard"
    
    if is_completed:
        card_class += " completed"
    elif is_locked:
        card_class += " locked"
    
    st.markdown(f"""
    <div class="{card_class}">
        <h4>Challenge {challenge_num}: {challenge['title']}</h4>
        <p><strong>Difficulty:</strong> {challenge['difficulty']}</p>
        <p>{challenge['description'][:100]}...</p>
        <div class="challenge-status">
            {'Completed' if is_completed else 'Locked' if is_locked else 'Available'}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if not is_locked:
        if st.button(f"{'Review' if is_completed else 'Start'} Challenge {challenge_num}", 
                    key=f"challenge_{challenge_num}", 
                    disabled=is_locked):
            show_challenge_detail(challenge, challenge_num, wolf_ai, challenge_manager, db)

@st.dialog("Challenge Details")
def show_challenge_detail(challenge, challenge_num, wolf_ai, challenge_manager, db):
    st.markdown(f"# Challenge {challenge_num}: {challenge['title']}")
    st.markdown(f"**Difficulty:** {challenge['difficulty']}")
    st.markdown(f"**Points:** {challenge['points']}")
    
    st.markdown("## Description")
    st.markdown(challenge['description'])
    
    st.markdown("## Instructions")
    st.markdown(challenge['instructions'])
    
    # Flag Information - Only show when all challenges are completed
    all_challenges_completed = len(st.session_state.completed_challenges) >= 10
    
    if all_challenges_completed:
        st.markdown("## 🏴 Flag Submission")
        st.info("💡 **Hint:** All challenges can be solved with the same flag: `WOLF{VGhldGFtaWxzZ_Wx2YW5je_WJlcndvbGY=}`")
        
        # Show completion celebration
        st.balloons()
        st.success("🎉 **CONGRATULATIONS!** You have completed all challenges! The flag is now available.")
    
    
    # Wolf AI Hint System
    st.markdown("## Wolf AI Assistant")
    
    # Create columns for Wolf AI section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if st.button("Get Hint from Wolf AI", key=f"hint_{challenge_num}"):
            if st.session_state.health_score > 10:
                hint = wolf_ai.get_hint(challenge, challenge_num)
                st.session_state.hint_active = True
                st.session_state.current_hint = hint
                st.session_state.current_hint_challenge = challenge_num
                
                # Reduce health score
                st.session_state.health_score -= 10
                st.warning("Health score reduced by 10 points for using hint!")
                
                # Save updated health score
                db.save_user_data(
                    st.session_state.user_email,
                    st.session_state.health_score,
                    list(st.session_state.completed_challenges),
                    st.session_state.current_challenge
                )
                st.rerun()
            else:
                st.error("Insufficient health score for hints!")
    
    # Check if hint is active for a different challenge
    if (st.session_state.hint_active and 
        st.session_state.current_hint_challenge != challenge_num):
        
        st.warning(f"🐺 Wolf AI hint is active for Challenge {st.session_state.current_hint_challenge}")
    
    # Display hint if active and for current challenge
    elif (st.session_state.hint_active and 
          st.session_state.current_hint_challenge == challenge_num):
        
        # Show hint without timer
        st.markdown("---")
        st.markdown("## 🐺 **Wolf AI Hint**")
        
        # Hint content
        st.info(f"**Wolf AI:** {st.session_state.current_hint}")
        
        # Manual close button
        col_close1, col_close2, col_close3 = st.columns([1, 1, 1])
        with col_close2:
            if st.button("❌ Close Hint", key=f"close_hint_{challenge_num}"):
                st.session_state.hint_active = False
                st.session_state.current_hint = None
                st.session_state.current_hint_challenge = None
                st.rerun()
    
    with col2:
        st.markdown(f"""
        <div class="hint-cost">
            <p><strong>Hint Cost:</strong> 10 HP</p>
            <p><strong>Current HP:</strong> {st.session_state.health_score}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Challenge-specific interface
    if challenge_num == 1:
        show_challenge_1_interface(challenge_manager, db)
    elif challenge_num == 2:
        show_challenge_2_interface(challenge_manager, db)
    elif challenge_num == 3:
        show_challenge_3_interface(challenge_manager, db)
    else:
        show_generic_challenge_interface(challenge_num, challenge_manager, db)

def show_challenge_1_interface(challenge_manager, db):
    st.markdown("## Submit your .pcap file")
    
    # Check if challenge is already completed
    if 1 in st.session_state.completed_challenges:
        st.markdown("""
        <div style="background-color: rgba(255, 235, 59, 0.3); padding: 1rem; border-radius: 0; border: 4px solid #000000; margin: 1rem 0; box-shadow: 4px 4px 0px #000000;">
            <h4 style="color: #000000; font-weight: 800; text-transform: uppercase;">SECURITY VIOLATION DETECTED</h4>
            <p>Challenge 1 has already been completed! Attempting to redo completed challenges is prohibited.</p>
            <p><strong>Penalty Applied:</strong> -15 Health Points</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("ACKNOWLEDGE VIOLATION", key="ack_violation_1"):
            # Apply penalty
            st.session_state.health_score = max(0, st.session_state.health_score - 15)
            
            # Save updated data
            db.save_user_data(
                st.session_state.user_email,
                st.session_state.health_score,
                list(st.session_state.completed_challenges),
                st.session_state.current_challenge
            )
            
            st.error(f"Security violation recorded! Health reduced to {st.session_state.health_score}/100")
            st.info("Focus on completing available challenges instead!")
            st.rerun()
        return
    
    uploaded_file = st.file_uploader(
        "Upload Wireshark capture file",
        type=['pcap', 'pcapng'],
        key="challenge1_upload"
    )
    
    # Only show flag input if all challenges are completed
    all_challenges_completed = len(st.session_state.completed_challenges) >= 10
    
    if all_challenges_completed:
        flag_input = st.text_input(
            "Enter Flag (Optional)",
            placeholder="WOLF{...}",
            key="challenge1_flag"
        )
    else:
        flag_input = None
    
    # Create columns for buttons
    col1, col2 = st.columns([1, 1])
    
    if uploaded_file is not None:
        st.success(f"File uploaded: {uploaded_file.name}")
    
    with col1:
        if st.button("Submit Challenge 1", key="submit_challenge_1"):
            is_correct = challenge_manager.validate_challenge_1(uploaded_file, flag_input)
            
            if is_correct:
                st.success("Challenge 1 completed! Great work on capturing network traffic!")
                st.session_state.completed_challenges.add(1)
                st.session_state.current_challenge = max(st.session_state.current_challenge, 2)
                
                # Add 5 points for completing the challenge
                if 1 not in st.session_state.completed_challenges:
                    st.session_state.user_score += 5
                    st.info(f"🎯 +5 points! Total score: {st.session_state.user_score}")
                
                # Save progress
                db.save_user_data(
                    st.session_state.user_email,
                    st.session_state.health_score,
                    list(st.session_state.completed_challenges),
                    st.session_state.current_challenge,
                    st.session_state.user_score
                )
                st.rerun()
            else:
                st.error("Invalid file or incorrect format. Try again!")
    
    with col2:
        if st.button("Submit Problem Report", key="submit_problem_1"):
            st.info("Problem report submitted! Our security team will review it within 24 hours.")

def show_challenge_2_interface(challenge_manager, db):
    st.markdown("## Web Analysis Task")
    
    # Check if challenge is already completed
    if 2 in st.session_state.completed_challenges:
        st.markdown("""
        <div style="background-color: rgba(255, 235, 59, 0.3); padding: 1rem; border-radius: 0; border: 4px solid #000000; margin: 1rem 0; box-shadow: 4px 4px 0px #000000;">
            <h4 style="color: #000000; font-weight: 800; text-transform: uppercase;">SECURITY VIOLATION DETECTED</h4>
            <p>Challenge 2 has already been completed! Attempting to redo completed challenges is prohibited.</p>
            <p><strong>Penalty Applied:</strong> -15 Health Points</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("ACKNOWLEDGE VIOLATION", key="ack_violation_2"):
            # Apply penalty
            st.session_state.health_score = max(0, st.session_state.health_score - 15)
            
            # Save updated data
            db.save_user_data(
                st.session_state.user_email,
                st.session_state.health_score,
                list(st.session_state.completed_challenges),
                st.session_state.current_challenge
            )
            
            st.error(f"Security violation recorded! Health reduced to {st.session_state.health_score}/100")
            st.info("Focus on completing available challenges instead!")
            st.rerun()
        return
    
    target_url = st.text_input("Target Website URL", key="challenge2_url")
    request_method = st.selectbox("HTTP Method", ["GET", "POST", "PUT", "DELETE"], key="challenge2_method")
    headers_found = st.text_area("Headers Discovered", key="challenge2_headers")
    
    # Only show flag input if all challenges are completed
    all_challenges_completed = len(st.session_state.completed_challenges) >= 10
    
    if all_challenges_completed:
        flag_input = st.text_input(
            "Enter Flag (Optional)",
            placeholder="WOLF{...}",
            key="challenge2_flag"
        )
    else:
        flag_input = None
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Submit Challenge 2", key="submit_challenge_2"):
            is_correct = challenge_manager.validate_challenge_2(target_url, request_method, headers_found, flag_input)
            
            if is_correct:
                st.success("Challenge 2 completed! Excellent web analysis skills!")
                st.session_state.completed_challenges.add(2)
                st.session_state.current_challenge = max(st.session_state.current_challenge, 3)
                
                # Add 5 points for completing the challenge
                if 2 not in st.session_state.completed_challenges:
                    st.session_state.user_score += 5
                    st.info(f"🎯 +5 points! Total score: {st.session_state.user_score}")
                
                # Save progress
                db.save_user_data(
                    st.session_state.user_email,
                    st.session_state.health_score,
                    list(st.session_state.completed_challenges),
                    st.session_state.current_challenge,
                    st.session_state.user_score
                )
                st.rerun()
            else:
                st.error("Incorrect analysis. Check your methodology!")
    
    with col2:
        if st.button("Submit Problem Report", key="submit_problem_2"):
            st.info("Problem report submitted! Our security team will review it within 24 hours.")

def show_challenge_3_interface(challenge_manager, db):
    st.markdown("## API Security Implementation")
    
    # Check if challenge is already completed
    if 3 in st.session_state.completed_challenges:
        st.markdown("""
        <div style="background-color: rgba(255, 235, 59, 0.3); padding: 1rem; border-radius: 0; border: 4px solid #000000; margin: 1rem 0; box-shadow: 4px 4px 0px #000000;">
            <h4 style="color: #000000; font-weight: 800; text-transform: uppercase;">SECURITY VIOLATION DETECTED</h4>
            <p>Challenge 3 has already been completed! Attempting to redo completed challenges is prohibited.</p>
            <p><strong>Penalty Applied:</strong> -15 Health Points</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("ACKNOWLEDGE VIOLATION", key="ack_violation_3"):
            # Apply penalty
            st.session_state.health_score = max(0, st.session_state.health_score - 15)
            
            # Save updated data
            db.save_user_data(
                st.session_state.user_email,
                st.session_state.health_score,
                list(st.session_state.completed_challenges),
                st.session_state.current_challenge
            )
            
            st.error(f"Security violation recorded! Health reduced to {st.session_state.health_score}/100")
            st.info("Focus on completing available challenges instead!")
            st.rerun()
        return
    
    api_code = st.text_area(
        "Submit your secure API code",
        height=200,
        key="challenge3_code"
    )
    
    security_measures = st.multiselect(
        "Security measures implemented",
        [
            "Input Validation", "Authentication", "Rate Limiting", "HTTPS", 
            "SQL Injection Prevention", "XSS Protection", "CSRF Protection",
            "Content Security Policy", "Secure Headers", "Data Encryption",
            "Session Management", "Access Control", "Audit Logging",
            "Error Handling", "Input Sanitization", "API Versioning",
            "CORS Configuration", "Security Testing", "Vulnerability Scanning"
        ],
        key="challenge3_security"
    )
    
    # Only show flag input if all challenges are completed
    all_challenges_completed = len(st.session_state.completed_challenges) >= 10
    
    if all_challenges_completed:
        flag_input = st.text_input(
            "Enter Flag (Optional)",
            placeholder="WOLF{...}",
            key="challenge3_flag"
        )
    else:
        flag_input = None
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Submit Challenge 3", key="submit_challenge_3"):
            is_correct = challenge_manager.validate_challenge_3(api_code, security_measures, flag_input)
            
            if is_correct:
                st.success("Challenge 3 completed! Your API security implementation is solid!")
                st.session_state.completed_challenges.add(3)
                st.session_state.current_challenge = max(st.session_state.current_challenge, 4)
                
                # Add 5 points for completing the challenge
                if 3 not in st.session_state.completed_challenges:
                    st.session_state.user_score += 5
                    st.info(f"🎯 +5 points! Total score: {st.session_state.user_score}")
                
                # Save progress
                db.save_user_data(
                    st.session_state.user_email,
                    st.session_state.health_score,
                    list(st.session_state.completed_challenges),
                    st.session_state.current_challenge,
                    st.session_state.user_score
                )
                st.rerun()
            else:
                st.error("Security implementation needs improvement!")
    
    with col2:
        if st.button("Submit Problem Report", key="submit_problem_3"):
            st.info("Problem report submitted! Our security team will review it within 24 hours.")

def show_generic_challenge_interface(challenge_num, challenge_manager, db):
    st.markdown("## Submit Your Solution")
    
    # Check if challenge is already completed
    if challenge_num in st.session_state.completed_challenges:
        st.markdown(f"""
        <div style="background-color: rgba(255, 235, 59, 0.3); padding: 1rem; border-radius: 0; border: 4px solid #000000; margin: 1rem 0; box-shadow: 4px 4px 0px #000000;">
            <h4 style="color: #000000; font-weight: 800; text-transform: uppercase;">SECURITY VIOLATION DETECTED</h4>
            <p>Challenge {challenge_num} has already been completed! Attempting to redo completed challenges is prohibited.</p>
            <p><strong>Penalty Applied:</strong> -15 Health Points</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("ACKNOWLEDGE VIOLATION", key=f"ack_violation_{challenge_num}"):
            # Apply penalty
            st.session_state.health_score = max(0, st.session_state.health_score - 15)
            
            # Save updated data
            db.save_user_data(
                st.session_state.user_email,
                st.session_state.health_score,
                list(st.session_state.completed_challenges),
                st.session_state.current_challenge
            )
            
            st.error(f"Security violation recorded! Health reduced to {st.session_state.health_score}/100")
            st.info("Focus on completing available challenges instead!")
            st.rerun()
        return
    
    solution = st.text_area(
        f"Enter your solution for Challenge {challenge_num}",
        height=150,
        key=f"challenge{challenge_num}_solution"
    )
    
    # Only show flag input if all challenges are completed
    all_challenges_completed = len(st.session_state.completed_challenges) >= 10
    
    if all_challenges_completed:
        flag_input = st.text_input(
            "Enter Flag (Optional)",
            placeholder="WOLF{...}",
            key=f"challenge{challenge_num}_flag"
        )
    else:
        flag_input = None
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button(f"Submit Challenge {challenge_num}", key=f"submit_challenge_{challenge_num}"):
            is_correct = challenge_manager.validate_generic_challenge(challenge_num, solution, flag_input)
            
            if is_correct:
                st.success(f"Challenge {challenge_num} completed!")
                st.session_state.completed_challenges.add(challenge_num)
                st.session_state.current_challenge = max(st.session_state.current_challenge, challenge_num + 1)
                
                # Add 5 points for completing the challenge
                if challenge_num not in st.session_state.completed_challenges:
                    st.session_state.user_score += 5
                    st.info(f"🎯 +5 points! Total score: {st.session_state.user_score}")
                
                # Save progress
                db.save_user_data(
                    st.session_state.user_email,
                    st.session_state.health_score,
                    list(st.session_state.completed_challenges),
                    st.session_state.current_challenge,
                    st.session_state.user_score
                )
                st.rerun()
            else:
                st.error("Incorrect solution. Keep trying!")
    
    with col2:
        if st.button("Submit Problem Report", key=f"submit_problem_{challenge_num}"):
            st.info("Problem report submitted! Our security team will review it within 24 hours.")

if __name__ == "__main__":
    main()

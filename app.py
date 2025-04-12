import streamlit as st

# Initialize session state to store records
if "library_records" not in st.session_state:
    st.session_state.library_records = []

# Page Config
st.set_page_config(page_title="Library Record System", page_icon="📚", layout="centered")

# Title
st.markdown("""
    # 📘 Library Record System
    ### Add and view your book records easily!
""")

# Input Fields
book_name = st.text_input("📖 Enter Book Name:")
author_name = st.text_input("✍️ Enter Author Name:")

# Save Record Button
if st.button("💾 Save Record"):
    if not book_name.strip() or not author_name.strip():
        st.warning("⚠️ Please fill in both the Book Name and Author Name!")
    else:
        # Add the record
        new_record = {"Book": book_name.strip(), "Author": author_name.strip()}
        st.session_state.library_records.append(new_record)
        st.success(f"✅ Record saved: *{book_name}* by *{author_name}*")

# Display Saved Records
if st.session_state.library_records:
    st.markdown("## 📚 Saved Records")
    for idx, record in enumerate(st.session_state.library_records, 1):
        st.write(f"{idx}. **{record['Book']}** by *{record['Author']}*")

# Footer
st.markdown("""
---
📚 Keep your records organized! | **Created by Hanishah**
""")

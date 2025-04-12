import streamlit as st

# Initialize session state to hold book records
if "library" not in st.session_state:
    st.session_state.library = []

# Page Config
st.set_page_config(page_title="Library Manager", page_icon="📚", layout="centered")

# Title
st.markdown("""
    # 📘 Personal Library Manager
    ### Add and view your book collection in one place! 📚✨
""")

# Form for Book Entry
with st.form("add_book_form"):
    title = st.text_input("📖 Book Title")
    author = st.text_input("✍️ Author Name")
    year = st.text_input("📅 Publication Year")
    genre = st.text_input("🏷️ Genre")
    read_status = st.radio("📚 Read Status", ["Read ✅", "Unread ❌"], horizontal=True)
    submitted = st.form_submit_button("💾 Add Book")

    if submitted:
        if not title.strip() or not author.strip() or not year.strip() or not genre.strip():
            st.warning("⚠️ Please fill out all the fields!")
        elif not year.isdigit():
            st.warning("⚠️ Year must be a number!")
        else:
            st.session_state.library.append({
                "title": title.strip(),
                "author": author.strip(),
                "year": int(year),
                "genre": genre.strip(),
                "read": read_status.startswith("Read")
            })
            st.success(f"✅ '{title}' by {author} added to your library!")

# Display Library
if st.session_state.library:
    st.markdown("## 📚 Your Library")
    for idx, book in enumerate(st.session_state.library, 1):
        read_tag = "✅ Read" if book["read"] else "❌ Unread"
        st.markdown(f"""
        {idx}. **{book['title']}** by *{book['author']}* ({book['year']})  
        _Genre_: {book['genre']} | _Status_: **{read_tag}**
        """)

    # Statistics
    st.markdown("---")
    st.markdown("## 📊 Library Stats")
    total = len(st.session_state.library)
    read_count = sum(1 for book in st.session_state.library if book["read"])
    percentage = (read_count / total * 100) if total else 0
    st.info(f"**Total Books:** {total} | **Read:** {read_count} | **Percentage Read:** {percentage:.1f}%")

# Footer
st.markdown("""
---
📘 Keep reading and growing! | **Created by Hanishah**
""")

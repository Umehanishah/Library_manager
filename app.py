import streamlit as st

# Initialize library in session state
if "library" not in st.session_state:
    st.session_state.library = []

# Page Config
st.set_page_config(page_title="Library Manager", page_icon="📚", layout="centered")

# Title
st.markdown("""
    # 📘 Personal Library Manager
    ### Manage your book collection with ease 📚✨
""")

# Menu Selection
menu = st.radio("📋 Select an option:", [
    "➕ Add a Book", 
    "❌ Remove a Book", 
    "🔎 Search for a Book", 
    "📚 Display All Books", 
    "📊 Display Statistics", 
    "🚪 Exit"
])

# ➕ Add a Book
if menu == "➕ Add a Book":
    st.markdown("### 📥 Add Book Details")
    title = st.text_input("📖 Book Title")
    author = st.text_input("✍️ Author Name")
    year = st.text_input("📅 Publication Year")
    genre = st.text_input("🏷️ Genre")
    read_status = st.radio("📘 Read Status", ["Read ✅", "Unread ❌"])

    if st.button("💾 Save Book"):
        if not title or not author or not year or not genre:
            st.warning("⚠️ Please fill all fields!")
        elif not year.isdigit():
            st.warning("⚠️ Year must be a number!")
        else:
            book = {
                "title": title.strip(),
                "author": author.strip(),
                "year": int(year),
                "genre": genre.strip(),
                "read": True if read_status == "Read ✅" else False
            }
            st.session_state.library.append(book)
            st.success(f"✅ '{title}' by {author} added to your library!")

# ❌ Remove a Book
elif menu == "❌ Remove a Book":
    st.markdown("### 🗑️ Remove Book")
    if st.session_state.library:
        titles = [book["title"] for book in st.session_state.library]
        selected_title = st.selectbox("Select a book to remove:", titles)
        if st.button("🗑️ Remove Book"):
            st.session_state.library = [book for book in st.session_state.library if book["title"] != selected_title]
            st.success(f"❌ '{selected_title}' removed successfully!")
    else:
        st.info("📭 No books in your library yet!")

# 🔎 Search for a Book
elif menu == "🔎 Search for a Book":
    st.markdown("### 🔍 Search Library")
    query = st.text_input("🔎 Enter title or author:")
    if st.button("🔎 Search"):
        matches = [
            book for book in st.session_state.library
            if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()
        ]
        if matches:
            st.success(f"🔍 Found {len(matches)} match(es):")
            for book in matches:
                read_tag = "✅ Read" if book["read"] else "❌ Unread"
                st.markdown(f"**{book['title']}** by *{book['author']}* ({book['year']}) - {book['genre']} - {read_tag}")
        else:
            st.warning("⚠️ No matching books found.")

# 📚 Display All Books
elif menu == "📚 Display All Books":
    st.markdown("### 📚 Your Library")
    if st.session_state.library:
        for idx, book in enumerate(st.session_state.library, 1):
            read_tag = "✅ Read" if book["read"] else "❌ Unread"
            st.markdown(f"{idx}. **{book['title']}** by *{book['author']}* ({book['year']}) - {book['genre']} - {read_tag}")
    else:
        st.info("📭 No books to display yet.")

# 📊 Display Statistics
elif menu == "📊 Display Statistics":
    st.markdown("### 📊 Library Statistics")
    total = len(st.session_state.library)
    read_count = sum(1 for book in st.session_state.library if book["read"])
    if total > 0:
        percent_read = (read_count / total) * 100
        st.info(f"📚 Total Books: {total}")
        st.info(f"✅ Read: {read_count} | ❌ Unread: {total - read_count}")
        st.success(f"📈 Percentage Read: {percent_read:.1f}%")
    else:
        st.info("📭 No books in your library yet.")

# 🚪 Exit
elif menu == "🚪 Exit":
    st.markdown("### 👋 Thank you for using the Library Manager!")
    st.balloons()

# Footer
st.markdown("""
---
📘 Happy Reading! | **Created by Hanishah**
""")

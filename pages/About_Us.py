import streamlit as st

st.title("About Us")
st.write("Welcome to our platform! We are dedicated to providing high-quality services and solutions to meet your needs.")

st.header("Our Team")
st.write("We are a team of passionate individuals who strive for excellence in everything we do.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Aldous Jerson Sinen")
    st.image("https://images.unsplash.com/photo-1575936123452-b67c3203c357?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D", width=150)
    st.write("CEO & Founder - Leading the vision and strategy of our company.")

with col2:
    st.subheader("Raymond Bago")
    st.image("https://gratisography.com/wp-content/uploads/2024/11/gratisography-augmented-reality-800x525.jpg", width=150)
    st.write("CTO - Driving technological innovation and development.")

# Mission and values
st.header("Our Mission")
st.write("Our mission is to deliver exceptional value to our customers through innovation, integrity, and commitment.")

st.header("Our Values")
st.markdown("- **Customer First**: We prioritize our customers' needs.")
st.markdown("- **Innovation**: We embrace creativity and technology.")
st.markdown("- **Integrity**: We operate with honesty and transparency.")
st.markdown("- **Collaboration**: We believe in teamwork and mutual growth.")

# Contact information
st.header("Get in Touch")
st.write("Have questions or want to work with us? Reach out!")
st.write("📧 Email: contact@bakawan.com")
st.write("📍 Location: 123 Card MRI Street, San Pablo City")

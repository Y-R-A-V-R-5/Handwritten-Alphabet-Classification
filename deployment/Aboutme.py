import streamlit as st

def about_me_page():
    st.title("About Me")

    st.header("👨‍💻 About the Developer")
    st.write(
        """
        Hi, I'm **Adithya Vardhan Reddy**, the creator of this Handwritten Alphabet Classification App.  
        I'm a passionate engineer with a strong interest in machine learning, computer vision, and web development.
        """
    )

    st.write(
        """
        This project was born out of my curiosity to explore the practical applications of neural networks, 
        particularly in the field of handwritten character recognition. The goal was to build a tool that showcases 
        the power of deep learning while providing an interactive learning experience for users.
        """
    )

    st.divider()

    st.subheader("🚀 Motivation")
    st.write(
        """
        The ability of machines to "see" and "understand" the world fascinates me. Handwriting recognition, 
        despite being a challenging task, presents exciting possibilities for real-world applications. 
        Additionally, I wanted to learn more about Streamlit and its potential for building interactive applications.
        """
    )

    st.divider()

    st.subheader("🎯 Project Goals")
    st.write(
        """
        The primary goals of this project were:
        - 🛠️ Build a robust and accurate handwritten alphabet classification system.
        - 📊 Implement and compare the performance of various neural network architectures.
        - 🌐 Develop an interactive, user-friendly web application using Streamlit.
        - 🎓 Provide a valuable educational resource for those interested in computer vision and neural networks.
        """
    )

    st.divider()

    st.subheader("🧠 Technical Skills")
    st.write(
        """
        This project utilized several key technologies and skills:
        - 🐍 **Programming Languages:** Python
        - 🤖 **Deep Learning Frameworks:** TensorFlow, Keras
        - 🌐 **Web Framework:** Streamlit
        - ⚙️ **Other Libraries:** NumPy, Pandas, PIL (Pillow), Matplotlib
        """
    )

    st.divider()

    st.subheader("🔍 Future Enhancements")
    st.write(
        """
        Potential future improvements for this project include:
        - 🔢 Expanding the character set to include numbers and symbols.
        - ✍️ Integrating real-time handwriting recognition capabilities.
        - ⚡ Enhancing model performance through advanced tuning techniques.
        - 📈 Adding interactive visualizations for better model insights.
        - ☁️ Deploying the app on a cloud platform for wider accessibility.
        """
    )

    st.divider()

    st.subheader("📬 Contact")
    st.write(
        """
        Feel free to reach out to me via the following channels:
        - 📧 **Gmail:** [adithyavardhanreddy2003@gmail.com][Gmail](mailto:adithyavardhanreddy2003@gmail.com)
        - 🐙 **GitHub:** [Y-R-A-V-R-5](https://github.com/Y-R-A-V-R-5)
        - 🔗 **LinkedIn:** [Adithya Vardhan Reddy](https://www.linkedin.com/in/yravr/)
        """
    )

    st.success("Thank you for visiting my app! I hope you find it informative and useful.")

    with st.sidebar:
        st.info("🌟 Explore more pages using the navigation menu!")
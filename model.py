import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to plot data based on the selected columns
def plot_data(df, col1, col2):
    st.subheader("Data Visualization")
    if col1 is not None and col2 is not None:
        # Line Plot
        st.subheader("Line Plot")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.lineplot(x=col1, y=col2, data=df, ax=ax)
        st.pyplot(fig)

        # Bar Plot
        st.subheader("Bar Graph")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=col1, y=col2, data=df, ax=ax)
        st.pyplot(fig)

        # Histogram
        st.subheader("Histogram")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(df[col1], kde=True, ax=ax)
        st.pyplot(fig)

        # Scatter Plot
        st.subheader("Scatter Plot")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.scatterplot(x=col1, y=col2, data=df, ax=ax)
        st.pyplot(fig)

         #Heatmap
        st.subheader("Heatmap")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

        # Box Plot
        st.subheader("Box Plot")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x=col1, y=col2, data=df, ax=ax)
        st.pyplot(fig)
    else:
        st.error("Please select two columns to plot.")

# Main function to run the app
def main():
    st.title("Data Visualization WebcApp")

    # File upload and column selection
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"], key="file_uploader")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Select two columns for plotting
        selected_columns = st.multiselect("Select two columns for visualization", df.columns)
        if len(selected_columns) == 2:
            col1, col2 = selected_columns
            plot_data(df, col1, col2)
        else:
            st.warning("Please select exactly two columns.")

if __name__ == "__main__":
    main()

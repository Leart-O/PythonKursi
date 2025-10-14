import streamlit as st
import requests
import pandas as pd

st.title("Project Management App")

st.header("Add developer")
dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Experience(Years)", min_value=0, max_value=50, step=1)

if st.button("Create Developer"):
    dev_data = {"name": dev_name, "experience": dev_experience}
    response = requests.post("http://localhost:8000/developers/", json=dev_data)
    st.json(response.json())

st.header("Add project")
proj_title = st.text_input("Project Title")
proj_desc = st.text_area("Project Description")
proj_lang = st.text_input("Languages Used (comma separated)")
lead_dev_name = st.text_input("Lead Developer Name")
lead_dev_exp = st.number_input("Lead Developer Experience(Years)", min_value=0, max_value=50, step=1)

if st.button("Create Project"):
    lead_dev_data = {"name": lead_dev_name, "experience": lead_dev_exp}
    proj_data = {
        "title": proj_title,
        "description": proj_desc,
        "languages": proj_langs.split(","),
        "lead_developer": lead_dev_data
    }
    response = requests.post("http://localhost:8000/projects/", json=proj_data)
    st.json(response.json())

st.header("Projects Dashboard")

if st.button("Get Projects"):
    response = requests.get("http://localhost:8000/projects/")
    projects_data = response.json()['projects']

    if projects_data:
        projects_df = pd.DataFrame(projects_data)

        st.subheader("Projects Overview")
        st.dataframe(projects_df)

        st.subheader("Project details")
        for project in projects_data:
            st.markdown(f"### {project['title']}")
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Languages:** {', '.join(project['languages'])}")
            st.markdown(f"**Lead Developer:** {project['lead_developer']['name']} with ({project['lead_developer']['experience']} years)")
            st.markdown("---")
        
    else:
        st.warning("No projects found.")
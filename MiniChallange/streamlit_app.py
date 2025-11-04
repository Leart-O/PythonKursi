import streamlit as st
import requests
from typing import Optional

BASE = "http://localhost:8000"

st.set_page_config(page_title="Students CRUD", layout="wide")
st.title("Students registry")

# --- helpers
def api_get(path: str):
    try:
        r = requests.get(f"{BASE}{path}", timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        st.error(f"API GET error: {e}")
        return None

def api_post(path: str, payload: dict):
    try:
        r = requests.post(f"{BASE}{path}", json=payload, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        st.error(f"API POST error: {e}")
        return None

def api_put(path: str, payload: dict):
    try:
        r = requests.put(f"{BASE}{path}", json=payload, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        st.error(f"API PUT error: {e}")
        return None

def api_delete(path: str):
    try:
        r = requests.delete(f"{BASE}{path}", timeout=5)
        r.raise_for_status()
        return True
    except Exception as e:
        st.error(f"API DELETE error: {e}")
        return False

# --- session state defaults
if "selected_id" not in st.session_state:
    st.session_state.selected_id = None
if "to_delete" not in st.session_state:
    st.session_state.to_delete = None

# load students once per run
students = api_get("/students/") or []
id_map = {f"{s['first_name']} {s['last_name']} (id:{s['id']})": s['id'] for s in students}
labels = ["New student"] + list(id_map.keys())

# Layout: left = form, right = list
left, right = st.columns([1, 2])

with left:
    st.header("Add / Edit student")

    # selector to pick student for edit, or New student
    try:
        sel_index = 0
        if st.session_state.selected_id is not None:
            # find label matching selected_id
            for i, (k, v) in enumerate(id_map.items(), start=1):
                if v == st.session_state.selected_id:
                    sel_index = i
                    break
    except Exception:
        sel_index = 0

    sel_label = st.selectbox("Select student to edit or choose New", labels, index=sel_index)
    selected_id = None if sel_label == "New student" else id_map.get(sel_label)

    # keep selected_id synced with session_state (Edit button sets session_state)
    if st.session_state.selected_id is not None and selected_id != st.session_state.selected_id:
        selected_id = st.session_state.selected_id
        # attempt to set sel_label variable for clarity (doesn't affect selectbox state)
        try:
            sel_label = next(k for k, v in id_map.items() if v == selected_id)
        except StopIteration:
            sel_label = "New student"

    # fetch student data if editing
    student_data = api_get(f"/students/{selected_id}") if selected_id else None

    with st.form("student_form"):
        first_name = st.text_input("First name", value=student_data['first_name'] if student_data else "")
        last_name = st.text_input("Last name", value=student_data['last_name'] if student_data else "")
        grade = st.number_input("Grade (year)", min_value=1, max_value=20, value=student_data['grade'] if student_data else 1, step=1)
        avg_grade_val = student_data['avg_grade'] if student_data and student_data['avg_grade'] is not None else 0.0
        avg_grade = st.number_input("Average grade", min_value=0.0, max_value=10.0, value=avg_grade_val, step=0.1, format="%.1f")
        email = st.text_input("Email", value=student_data['email'] if student_data and student_data['email'] else "")
        behaviour_list = [1, 3, 5]
        try:
            behaviour_index = behaviour_list.index(student_data['behaviour']) if student_data else 2
        except Exception:
            behaviour_index = 2
        behaviour = st.selectbox("Behaviour (1 bad - 5 good)", behaviour_list, index=behaviour_index)

        save = st.form_submit_button("Save")
        delete = st.form_submit_button("Delete")

        if save:
            payload = {
                "first_name": first_name.strip(),
                "last_name": last_name.strip(),
                "grade": int(grade),
                "avg_grade": float(avg_grade) if float(avg_grade) != 0.0 else None,
                "email": email.strip() if email.strip() else None,
                "behaviour": int(behaviour),
            }
            if selected_id is None:
                res = api_post("/students/", payload)
                if res:
                    st.success("Student added.")
                    st.session_state.selected_id = None
            else:
                res = api_put(f"/students/{selected_id}", payload)
                if res:
                    st.success("Student updated.")
                    st.session_state.selected_id = None

        if delete and selected_id:
            # request explicit confirmation before delete
            st.session_state.to_delete = selected_id

with right:
    st.header("All students")
    # top action bar
    cols = st.columns([1,1,6])
    if cols[0].button("Refresh"):
        # toggling a state value forces a rerun because widget changed
        st.session_state._refresh = not st.session_state.get("_refresh", False)
    cols[1].button("New student", on_click=lambda: st.session_state.update({"selected_id": None}))

    if students:
        for s in students:
            with st.container():
                st.markdown(f"**{s['first_name']} {s['last_name']}**  •  Grade {s['grade']}  •  Avg: {s['avg_grade']}  •  Behaviour: {s['behaviour']}")
                c1, c2, _ = st.columns([1,1,6])
                if c1.button("Edit", key=f"edit_{s['id']}"):
                    st.session_state.selected_id = s['id']
                if c2.button("Delete", key=f"del_{s['id']}"):
                    st.session_state.to_delete = s['id']
                st.divider()
    else:
        st.info("No students found.")

# Delete confirmation area (global, shown when to_delete is set)
if st.session_state.to_delete:
    sid = st.session_state.to_delete
    st.warning(f"Confirm delete student id {sid}")
    c_yes, c_no = st.columns([1,1])
    if c_yes.button("Yes, delete"):
        ok = api_delete(f"/students/{sid}")
        if ok:
            st.success("Deleted.")
            st.session_state.to_delete = None
            st.session_state.selected_id = None
    if c_no.button("Cancel"):
        st.session_state.to_delete = None
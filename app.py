import streamlit as st
from router import route_request
from notes_storage import save_note, get_all_notes

st.set_page_config(page_title="NEXUS - Multi-Agent AI", page_icon="🤖", layout="centered")

st.title("🤖 NEXUS")
st.caption("A multi-agent AI system that knows which brain to call")

st.markdown("""
**Agents available:** 📅 Calendar · ✉️ Email · ✅ Task · 🗒️ Notes

Type a request below and NEXUS will automatically route it to the right agent.
""")

if "history" not in st.session_state:
    st.session_state.history = []

user_message = st.text_input("Your request:", placeholder="e.g. Schedule a meeting tomorrow at 3pm")

col1, col2 = st.columns([1, 5])
with col1:
    submit = st.button("Send")
with col2:
    show_notes = st.button("📋 Show My Notes")

if show_notes:
    st.session_state.history.append(("system", "Notes", get_all_notes()))

if submit and user_message.strip():
    with st.spinner("Routing your request..."):
        agent_name, agent = route_request(user_message)

        if agent_name == "notes":
            lower_msg = user_message.lower()
            if "show" in lower_msg or "list" in lower_msg:
                response = get_all_notes()
            else:
                save_note(user_message)
                response = agent.respond(user_message) + "\n\n*(This note has been saved.)*"
        else:
            response = agent.respond(user_message)

    st.session_state.history.append((agent_name, agent.name if agent_name != "notes" or "show" not in user_message.lower() else "Notes", response))

st.divider()

for agent_key, agent_display_name, response in reversed(st.session_state.history):
    st.markdown(f"**[{agent_display_name}]**")
    st.write(response)
    st.markdown("---")
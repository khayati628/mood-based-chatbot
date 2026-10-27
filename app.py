from pathlib import Path

import streamlit as st

from moods import DEFAULT_MODE, MODES, get_model, get_reply

st.set_page_config(page_title="MoodMate AI", page_icon="🤖", layout="centered")

STYLES = (Path(__file__).parent / "styles.css").read_text(encoding="utf-8")
st.markdown(f"<style>{STYLES}</style>", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    return get_model()


def reset_chat():
    st.session_state.messages = []


st.session_state.setdefault("mode", DEFAULT_MODE)
st.session_state.setdefault("messages", [])

with st.sidebar:
    st.markdown("## 🎭 Mood settings")
    st.write("Choose your AI personality.")
    st.radio("Personality", list(MODES), key="mode", on_change=reset_chat)

    st.markdown("---")
    st.markdown(f"### {st.session_state.mode}")
    st.caption(MODES[st.session_state.mode]["description"])

    if st.button("🧹 Clear conversation", use_container_width=True):
        reset_chat()
        st.rerun()

    st.markdown("---")
    st.caption("Powered by LangChain + Mistral AI")

st.markdown(
    """
<div class="hero">
    <h1>🤖 MoodMate AI</h1>
    <p>Your AI friend with three different moods.</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(f"### Chat with {st.session_state.mode} mode")
st.caption("Ask anything. Your AI will respond in its selected personality.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Your AI is thinking..."):
            try:
                answer = get_reply(
                    load_model(), st.session_state.mode, st.session_state.messages
                )
            except Exception as error:
                st.session_state.messages.pop()
                st.error(
                    "Unable to get a response. Check your API key, internet "
                    f"connection, model access and quota.\n\nDetails: {error}"
                )
            else:
                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

st.markdown(
    '<p class="small-note">MoodMate AI • Made with Python 🐍</p>',
    unsafe_allow_html=True,
)

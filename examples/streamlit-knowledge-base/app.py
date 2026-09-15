from __future__ import annotations

import streamlit as st

CONTENT = (
    "This demo page contains synthetic information about leave, reimbursement, "
    "and support contacts."
)
METADATA = {
    "Title": "Example Leave and Reimbursement Policy",
    "Last Updated": "2025-03-24",
    "Author": "Example HR Team",
    "Tags": ["leave", "reimbursement", "support"],
}
SUGGESTED_QUESTIONS = [
    "What is the example leave policy?",
    "How does the example reimbursement process work?",
    "Who is the example support contact?",
]
ANSWERS = {
    SUGGESTED_QUESTIONS[0]: "The synthetic policy provides 20 days of annual leave.",
    SUGGESTED_QUESTIONS[1]: (
        "Submit the required synthetic documents within 30 days. "
        "This is demonstration content, not a real company policy."
    ),
    SUGGESTED_QUESTIONS[2]: "Contact the fictional support team used by this demo.",
}

st.set_page_config(page_title="Knowledge Base Q&A", layout="centered")
st.title("Knowledge Base Q&A")
st.caption("Static local prototype using synthetic data; it does not connect to Confluence.")
st.info(CONTENT)

question = st.selectbox("Choose a suggested question", SUGGESTED_QUESTIONS)
if st.button("Show answer", type="primary", use_container_width=True):
    st.subheader("Answer")
    st.write(ANSWERS[question])

with st.expander("View metadata"):
    st.json(METADATA)
    st.table([{"Tag": tag} for tag in METADATA["Tags"]])

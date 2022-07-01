import streamlit as st

st.info("Note! Pressing the small arrow (>) in the top left corner will show a useful sidebar")
 
wells_dvt_max_score = 9
st.subheader("MVP")
# Check if 'key' already exists in session_state
# If not, then initialize it
if 'wells_dvt_score' not in st.session_state:
    st.session_state['wells_dvt_score'] = 0
 
if 'wells_dvt_q1_score' not in st.session_state:
    st.session_state['wells_dvt_q1_score'] = 0
 
if 'wells_dvt_q1_answer' not in st.session_state:
    st.session_state['wells_dvt_q1_answer'] = "No selection"
 
if 'wells_dvt_q2_score' not in st.session_state:
    st.session_state['wells_dvt_q2_score'] = 0
 
if 'wells_dvt_q2_answer' not in st.session_state:
    st.session_state['wells_dvt_q2_answer'] = "No selection"
 
if 'wells_dvt_q3_score' not in st.session_state:
    st.session_state['wells_dvt_q3_score'] = 0
 
if 'wells_dvt_q3_answer' not in st.session_state:
    st.session_state['wells_dvt_q3_answer'] = "No selection"
 
if 'wells_dvt_q4_score' not in st.session_state:
    st.session_state['wells_dvt_q4_score'] = 0
 
if 'wells_dvt_q4_answer' not in st.session_state:
    st.session_state['wells_dvt_q4_answer'] = "No selection"
 
if 'wells_dvt_q5_score' not in st.session_state:
    st.session_state['wells_dvt_q5_score'] = 0
 
if 'wells_dvt_q5_answer' not in st.session_state:
    st.session_state['wells_dvt_q5_answer'] = "No selection"
 
if 'wells_dvt_q6_score' not in st.session_state:
    st.session_state['wells_dvt_q6_score'] = 0
 
if 'wells_dvt_q6_answer' not in st.session_state:
    st.session_state['wells_dvt_q6_answer'] = "No selection"
 
if 'wells_dvt_q7_score' not in st.session_state:
    st.session_state['wells_dvt_q7_score'] = 0
 
if 'wells_dvt_q7_answer' not in st.session_state:
    st.session_state['wells_dvt_q7_answer'] = "No selection"

if 'wells_dvt_q8_score' not in st.session_state:
    st.session_state['wells_dvt_q8_score'] = 0
 
if 'wells_dvt_q8_answer' not in st.session_state:
    st.session_state['wells_dvt_q8_answer'] = "No selection"

if 'wells_dvt_q9_score' not in st.session_state:
    st.session_state['wells_dvt_q9_score'] = 0
 
if 'wells_dvt_q9_answer' not in st.session_state:
    st.session_state['wells_dvt_q9_answer'] = "No selection"

if 'wells_dvt_q10_score' not in st.session_state:
    st.session_state['wells_dvt_q10_score'] = 0
 
if 'wells_dvt_q10_answer' not in st.session_state:
    st.session_state['wells_dvt_q10_answer'] = "No selection"
 
if 'wells_dvt_no_selection' not in st.session_state:
    st.session_state['wells_dvt_no_selection'] = 0
 
if 'wells_dvt_no' not in st.session_state:
    st.session_state['wells_dvt_no'] = 0
 
if 'wells_dvt_yes' not in st.session_state:
    st.session_state['wells_dvt_yes'] = 0
 
def wells_dvt_count_no_selection():
    no_selection = 0
    for i in range(1,11):
        key = f"wells_dvt_q{i}_answer"
        if st.session_state[key] == "No selection":
            no_selection += 1
    return no_selection
 
def wells_dvt_count_no():
    no = 0
    for i in range(1,11):
        key = f"wells_dvt_q{i}_answer"
        if st.session_state[key] == "No":
            no += 1
    return no
 
def wells_dvt_count_yes():
    yes = 0
    for i in range(1,11):
        key = f"wells_dvt_q{i}_answer"
        if st.session_state[key] == "Yes":
            yes += 1
    return yes
 
   
with st.expander("Wells' Criteria for DVT | Fill out Form"):
    st.markdown("""---""")
    st.markdown("<p style='text-align: center; font-size:30px; \
        '>Wells' Criteria for DVT</p>",\
        unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:20px; \
        '>Fill out Form</p>",\
        unsafe_allow_html=True)
    st.markdown("""---""")
    radio_val = st.radio("Active cancer (+1)",\
        ["No selection", "No", "Yes"], horizontal=True, key="haj")
    if radio_val == "Yes":
        st.session_state['wells_dvt_q1_score'] = 1
    else:
        st.session_state['wells_dvt_q1_score'] = 0
    st.session_state['wells_dvt_q1_answer'] = radio_val
    st.markdown("""---""")
    radio_val2 = st.radio("Bedridden recently >3 days or\
        major surgery within 12 weeks (+1)",\
    ["No selection", "No", "Yes"],\
        horizontal=True)
    if radio_val2 == "Yes":
        st.session_state['wells_dvt_q2_score'] = 1
    else:
        st.session_state['wells_dvt_q2_score'] = 0
    st.session_state['wells_dvt_q2_answer'] = radio_val2
    st.markdown("""---""")
 
    radio_val3 = st.radio("Calf swelling >3 cm compared to the other leg (+1)", \
        ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val3 == "Yes":
        st.session_state['wells_dvt_q3_score'] = 1
    else:
        st.session_state['wells_dvt_q3_score'] = 0
    #st.session_state['wells_dvt_q3_answer'] = radio_val3
    st.markdown("""---""")
 
    radio_val4 = st.radio("Collateral (nonvaricose) superficial\
         veins present (+1)", \
            ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val4 == "Yes":
        st.session_state['wells_dvt_q4_score'] = 1
    else:
        st.session_state['wells_dvt_q4_score'] = 0
    st.session_state['wells_dvt_q4_answer'] = radio_val4
    st.markdown("""---""")
    radio_val5 = st.radio("Entire leg swollen (+1)",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val5 == "Yes":
        st.session_state['wells_dvt_q5_score'] = 1
    else:
        st.session_state['wells_dvt_q5_score'] = 0
    st.session_state['wells_dvt_q5_answer'] = radio_val5
    st.markdown("""---""")
    radio_val6 = st.radio("Localized tenderness along the\
         deep venous system (+1)",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val6 == "Yes":
        st.session_state['wells_dvt_q6_score'] = 1
    else:
        st.session_state['wells_dvt_q6_score'] = 0
    st.session_state['wells_dvt_q6_answer'] = radio_val6
    st.markdown("""---""")
    radio_val7 = st.radio("Pitting edema, confined to symptomatic leg (+1)",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val7 == "Yes":
        st.session_state['wells_dvt_q7_score'] = 1
    else:
        st.session_state['wells_dvt_q7_score'] = 0
    st.session_state['wells_dvt_q7_answer'] = radio_val7
    st.markdown("""---""")
    radio_val8 = st.radio("Paralysis, paresis, or recent plaster\
         immobilization of the lower extremity (+1)",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val8 == "Yes":
        st.session_state['wells_dvt_q8_score'] = 1
    else:
        st.session_state['wells_dvt_q8_score'] = 0
    st.session_state['wells_dvt_q8_answer'] = radio_val8
    st.markdown("""---""")
    radio_val9 = st.radio("Previously documented DVT (+1)",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val9 == "Yes":
        st.session_state['wells_dvt_q9_score'] = 1
    else:
        st.session_state['wells_dvt_q9_score'] = 0
    st.session_state['wells_dvt_q9_answer'] = radio_val9
    st.markdown("""---""")
    radio_val10 = st.radio("Alternative diagnosis to DVT as likely or more likely (-2)",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val10 == "Yes":
        st.session_state['wells_dvt_q10_score'] = -2
    else:
        st.session_state['wells_dvt_q10_score'] = 0
    st.session_state['wells_dvt_q10_answer'] = radio_val10

    
 
st.session_state['wells_dvt_score'] = st.session_state['wells_dvt_q1_score']\
    + st.session_state['wells_dvt_q2_score']\
    + st.session_state['wells_dvt_q3_score']\
    + st.session_state['wells_dvt_q4_score']\
    + st.session_state['wells_dvt_q5_score']\
    + st.session_state['wells_dvt_q6_score']\
    + st.session_state['wells_dvt_q7_score']\
    + st.session_state['wells_dvt_q8_score']\
    + st.session_state['wells_dvt_q9_score']\
    + st.session_state['wells_dvt_q10_score']

 
 
wells_dvt_no_selection = wells_dvt_count_no_selection()
wells_dvt_no = wells_dvt_count_no()
wells_dvt_yes = wells_dvt_count_yes()

if 'text_input_wells_dvt' not in st.session_state:
    st.session_state['text_input_wells_dvt'] = "..."
 
with st.sidebar:
    st.header("Wells' Criteria for DVT")
    with st.expander("Optional user input"):
        agree = st.checkbox("Mark when done")
        st.text_area("Notes:", key="text_input_wells_dvt")
    with st.expander("Summary Stats"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"Null: {wells_dvt_no_selection}")
        with col2:
            st.write(f"No: {wells_dvt_no}")
        with col3:
            st.write(f"Yes: {wells_dvt_yes}")
       
        st.write(f"score:\
            {st.session_state['wells_dvt_score']}/{wells_dvt_max_score}")
 
        if st.session_state['wells_dvt_score'] < 1:
            st.success("0 or Lower | Low Risk Group")
        elif st.session_state['wells_dvt_score'] < 3:
            st.warning("1 or 2 | Medium Risk Group")
        else:
            st.error("3 or more | High Risk Group")
    st.markdown("---")

wells_max_score = 12.5

# Check if 'key' already exists in session_state
# If not, then initialize it
if 'wells_score' not in st.session_state:
    st.session_state['wells_score'] = 0

if 'wells_q1_score' not in st.session_state:
    st.session_state['wells_q1_score'] = 0

if 'wells_q1_answer' not in st.session_state:
    st.session_state['wells_q1_answer'] = "No selection"

if 'wells_q2_score' not in st.session_state:
    st.session_state['wells_q2_score'] = 0

if 'wells_q2_answer' not in st.session_state:
    st.session_state['wells_q2_answer'] = "No selection"

if 'wells_q3_score' not in st.session_state:
    st.session_state['wells_q3_score'] = 0

if 'wells_q3_answer' not in st.session_state:
    st.session_state['wells_q3_answer'] = "No selection"

if 'wells_q4_score' not in st.session_state:
    st.session_state['wells_q4_score'] = 0

if 'wells_q4_answer' not in st.session_state:
    st.session_state['wells_q4_answer'] = "No selection"

if 'wells_q5_score' not in st.session_state:
    st.session_state['wells_q5_score'] = 0

if 'wells_q5_answer' not in st.session_state:
    st.session_state['wells_q5_answer'] = "No selection"

if 'wells_q6_score' not in st.session_state:
    st.session_state['wells_q6_score'] = 0

if 'wells_q6_answer' not in st.session_state:
    st.session_state['wells_q6_answer'] = "No selection"

if 'wells_q7_score' not in st.session_state:
    st.session_state['wells_q7_score'] = 0

if 'wells_q7_answer' not in st.session_state:
    st.session_state['wells_q7_answer'] = "No selection"

if 'wells_no_selection' not in st.session_state:
    st.session_state['wells_no_selection'] = 0

if 'wells_no' not in st.session_state:
    st.session_state['wells_no'] = 0

if 'wells_yes' not in st.session_state:
    st.session_state['wells_yes'] = 0

def wells_count_no_selection():
    no_selection = 0
    for i in range(1,8):
        key = f"wells_q{i}_answer"
        if st.session_state[key] == "No selection":
            no_selection += 1
    return no_selection

def wells_count_no():
    no = 0
    for i in range(1,8):
        key = f"wells_q{i}_answer"
        if st.session_state[key] == "No":
            no += 1
    return no

def wells_count_yes():
    yes = 0
    for i in range(1,8):
        key = f"wells_q{i}_answer"
        if st.session_state[key] == "Yes":
            yes += 1
    return yes

def update_hr_w_to_p():
    st.session_state["perc_q2_answer"] = st.session_state["wells_q3_answer"]

    
with st.expander("Wells' Criteria for PE | Fill out Form"):
    st.markdown("""---""")
    st.markdown("<p style='text-align: center; font-size:30px; \
        '>Wells' Criteria for PE</p>",\
        unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:20px; \
        '>Fill out Form</p>",\
        unsafe_allow_html=True)
    st.markdown("""---""")
    radio_val = st.radio("#Clinical signs and symptoms of DVT (+3 if yes)",\
        ["No selection", "No", "Yes"], horizontal=True)
    if radio_val == "Yes":
        st.session_state['wells_q1_score'] = 3
    else:
        st.session_state['wells_q1_score'] = 0
    st.session_state['wells_q1_answer'] = radio_val
    st.markdown("""---""")
    radio_val2 = st.radio("PE is #1 diagnosis OR equally likely (+3)",\
    ["No selection", "No", "Yes"],\
        horizontal=True)
    if radio_val2 == "Yes":
        st.session_state['wells_q2_score'] = 3
    else:
        st.session_state['wells_q2_score'] = 0
    st.session_state['wells_q2_answer'] = radio_val2
    st.markdown("""---""")

    radio_val3 = st.radio("Heart rate ≥ 100 (+1.5)", \
        ["No selection", "No", "Yes"],\
        horizontal=True, help="...", key="wells_q3_answer", \
            on_change=update_hr_w_to_p)
    if radio_val3 == "Yes":
        st.session_state['wells_q3_score'] = 1.5
    else:
        st.session_state['wells_q3_score'] = 0
    #st.session_state['wells_q3_answer'] = radio_val3
    st.markdown("""---""")

    radio_val4 = st.radio("Immobilization at least 3 days \
        OR surgery in the previous 4 weeks (+1.5)", \
            ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val4 == "Yes":
        st.session_state['wells_q4_score'] = 1.5
    else:
        st.session_state['wells_q4_score'] = 0
    st.session_state['wells_q4_answer'] = radio_val4
    st.markdown("""---""")
    radio_val5 = st.radio("Previous, objectively diagnosed PE or DVT (+1.5)",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val5 == "Yes":
        st.session_state['wells_q5_score'] = 1.5
    else:
        st.session_state['wells_q5_score'] = 0
    st.session_state['wells_q5_answer'] = radio_val5
    st.markdown("""---""")
    radio_val6 = st.radio("Hemoptysis (+1)",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val6 == "Yes":
        st.session_state['wells_q6_score'] = 1
    else:
        st.session_state['wells_q6_score'] = 0
    st.session_state['wells_q6_answer'] = radio_val6
    st.markdown("""---""")
    radio_val7 = st.radio("Malignancy w/ treatment \
        within 6 months or palliative (+1)",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if radio_val7 == "Yes":
        st.session_state['wells_q7_score'] = 1
    else:
        st.session_state['wells_q7_score'] = 0
    st.session_state['wells_q7_answer'] = radio_val7

st.session_state['wells_score'] = st.session_state['wells_q1_score']\
    + st.session_state['wells_q2_score']\
    + st.session_state['wells_q3_score']\
    + st.session_state['wells_q4_score']\
    + st.session_state['wells_q5_score']\
    + st.session_state['wells_q6_score']\
    + st.session_state['wells_q7_score']


wells_no_selection = wells_count_no_selection()
wells_no = wells_count_no()
wells_yes = wells_count_yes()

with st.sidebar:
    st.header("Wells' Criteria for PE")
    with st.expander("Optional user input"):
        agree = st.checkbox("Mark when done", key="v3")
        st.text_area("Notes:", key="text_input_wells_pe")
    with st.expander("Summary Stats"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"Null: {wells_no_selection}")
        with col2:
            st.write(f"No: {wells_no}")
        with col3:
            st.write(f"Yes: {wells_yes}")

        st.write(f"Score:\
            {st.session_state['wells_score']}/{wells_max_score}")


        if st.session_state['wells_score'] < 2:
            st.success("Below 2 | Low Risk Group")
        elif st.session_state['wells_score'] < 6:
            st.warning("Below 6 | Medium Risk Group")
        else:
            st.error("6 or more | High Risk Group")



# Check if 'key' already exists in session_state
# If not, then initialize it
if 'perc_score' not in st.session_state:
    st.session_state['perc_score'] = 0
 
if 'perc_q1_score' not in st.session_state:
    st.session_state['perc_q1_score'] = 0
 
if 'perc_q1_answer' not in st.session_state:
    st.session_state['perc_q1_answer'] = "No selection"
 
if 'perc_q2_score' not in st.session_state:
    st.session_state['perc_q2_score'] = 0
 
if 'perc_q2_answer' not in st.session_state:
    st.session_state['perc_q2_answer'] = st.session_state['wells_q3_answer']
 
if 'perc_q3_score' not in st.session_state:
    st.session_state['perc_q3_score'] = 0
 
if 'perc_q3_answer' not in st.session_state:
    st.session_state['perc_q3_answer'] = "No selection"
 
if 'perc_q4_score' not in st.session_state:
    st.session_state['perc_q4_score'] = 0
 
if 'perc_q4_answer' not in st.session_state:
    st.session_state['perc_q4_answer'] = "No selection"
 
if 'perc_q5_score' not in st.session_state:
    st.session_state['perc_q5_score'] = 0
 
if 'perc_q5_answer' not in st.session_state:
    st.session_state['perc_q5_answer'] = "No selection"
 
if 'perc_q6_score' not in st.session_state:
    st.session_state['perc_q6_score'] = 0
 
if 'perc_q6_answer' not in st.session_state:
    st.session_state['perc_q6_answer'] = "No selection"
 
if 'perc_q7_score' not in st.session_state:
    st.session_state['perc_q7_score'] = 0
 
if 'perc_q7_answer' not in st.session_state:
    st.session_state['perc_q7_answer'] = "No selection"

if 'perc_q8_score' not in st.session_state:
    st.session_state['perc_q8_score'] = 0
 
if 'perc_q8_answer' not in st.session_state:
    st.session_state['perc_q8_answer'] = "No selection"
 
if 'perc_no_selection' not in st.session_state:
    st.session_state['perc_no_selection'] = 0
 
if 'perc_no' not in st.session_state:
    st.session_state['perc_no'] = 0
 
if 'perc_yes' not in st.session_state:
    st.session_state['perc_yes'] = 0
 
def perc_count_no_selection():
    no_selection = 0
    for i in range(1,9):
        key = f"perc_q{i}_answer"
        if st.session_state[key] == "No selection":
            no_selection += 1
    return no_selection
 
def perc_count_no():
    no = 0
    for i in range(1,9):
        key = f"perc_q{i}_answer"
        if st.session_state[key] == "No":
            no += 1
    return no
 
def perc_count_yes():
    yes = 0
    for i in range(1,9):
        key = f"perc_q{i}_answer"
        if st.session_state[key] == "Yes":
            yes += 1
    return yes

def update_hr_p_to_w():
    st.session_state["wells_q3_answer"] = st.session_state["perc_q2_answer"]

with st.expander("PERC Rule for PE | Fill out Form"):
    st.markdown("""---""")
    st.markdown("<p style='text-align: center; font-size:30px; \
        '>PERC Rule for PE</p>",\
        unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:20px; \
        '>Fill out Form</p>",\
        unsafe_allow_html=True)
    st.markdown("""---""")
    perc_radio_val = st.radio("Age ≥50",\
        ["No selection", "No", "Yes"], horizontal=True, help="...")
    if perc_radio_val == "Yes":
        st.session_state['perc_q1_score'] = 3
    else:
        st.session_state['perc_q1_score'] = 0
    st.session_state['perc_q1_answer'] = perc_radio_val
    
    st.markdown("""---""")
    perc_radio_val2 = st.radio("Heart Rate ≥ 100",\
     ["No selection", "No", "Yes"],\
        horizontal=True, help="...", key="perc_q2_answer", 
        on_change=update_hr_p_to_w)
    if perc_radio_val2 == "Yes":
        st.session_state['perc_q2_score'] = 3
    else:
        st.session_state['perc_q2_score'] = 0
    #st.session_state['perc_q2_answer'] = perc_radio_val2

    st.markdown("""---""")
    perc_radio_val3 = st.radio("O₂ sat on room air <95%", \
        ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if perc_radio_val3 == "Yes":
        st.session_state['perc_q3_score'] = 1.5
    else:
        st.session_state['perc_q3_score'] = 0
    st.session_state['perc_q3_answer'] = perc_radio_val3
    st.markdown("""---""")
    perc_radio_val4 = st.radio("Unilateral leg swelling", \
            ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if perc_radio_val4 == "Yes":
        st.session_state['perc_q4_score'] = 1.5
    else:
        st.session_state['perc_q4_score'] = 0
    st.session_state['perc_q4_answer'] = perc_radio_val4
    st.markdown("""---""")
    perc_radio_val5 = st.radio("Hemoptysis",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if perc_radio_val5 == "Yes":
        st.session_state['perc_q5_score'] = 1.5
    else:
        st.session_state['perc_q5_score'] = 0
    st.session_state['perc_q5_answer'] = perc_radio_val5
    st.markdown("""---""")
    perc_radio_val6 = st.radio("Recent surgery or trauma",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="Surgery or trauma ≤4 weeks ago requiring \
            treatment with general anesthesia")
    if perc_radio_val6 == "Yes":
        st.session_state['perc_q6_score'] = 1
    else:
        st.session_state['perc_q6_score'] = 0
    st.session_state['perc_q6_answer'] = perc_radio_val6
    st.markdown("""---""")
    perc_radio_val7 = st.radio("Prior PE or DVT",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if perc_radio_val7 == "Yes":
        st.session_state['perc_q7_score'] = 1
    else:
        st.session_state['perc_q7_score'] = 0
    st.session_state['perc_q7_answer'] = perc_radio_val7
    st.markdown("""---""")
    perc_radio_val8 = st.radio("Hormone use",\
         ["No selection", "No", "Yes"],\
        horizontal=True, help="...")
    if perc_radio_val8 == "Yes":
        st.session_state['perc_q8_score'] = 1
    else:
        st.session_state['perc_q8_score'] = 0
    st.session_state['perc_q8_answer'] = perc_radio_val8
    
st.session_state['perc_score'] = st.session_state['perc_q1_score']\
    + st.session_state['perc_q2_score']\
    + st.session_state['perc_q3_score']\
    + st.session_state['perc_q4_score']\
    + st.session_state['perc_q5_score']\
    + st.session_state['perc_q6_score']\
    + st.session_state['perc_q7_score']\
    + st.session_state['perc_q8_score']


perc_no_selection = perc_count_no_selection()
perc_no = perc_count_no()
perc_yes = perc_count_yes()


with st.sidebar:
    st.markdown("""---""")
    st.header("PERC Rule for PE")
    with st.expander("Optional user input"):
        agree = st.checkbox("Mark when done", key="v4")
        st.text_area("Notes:", key="text_input_wells_perc")
    with st.expander("Summary Stats"):
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"Null: {perc_no_selection}")
        with col2:
            st.write(f"No: {perc_no}")
        with col3:
            st.write(f"Yes: {perc_yes}")
        
        if perc_yes > 0:
            st.error("PERC Rule Broken")
        else:
            st.success("PERC Rule Not Broken")
    
    st.markdown("""---""")


with st.expander("Flowchart"):
    st.image("https://cdn-cashy-static-assets.lucidchart.com/marketing/pages/chart/consideration-ppc-2020/hero-images/flowchart-b.png")

placeholder = st.empty()
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

st.subheader("Under development")

# testing different styles
with st.expander("Testing Different Layouts"):
    st.markdown("<p style='text-align: center; font-size:30px; \
        '>Layout Testing Form</p>",\
        unsafe_allow_html=True)
    st.markdown("""---""")
    col1, col2 = st.columns(2)
    with col1: 
        st.write("")
        st.write("")
        st.write("Question 1")

    with col2:
        test_radio_val = st.radio("",\
            ["No selection", "No", "Yes"], horizontal=True, key="test1")

    st.markdown("""---""")
    col1, col2 = st.columns(2)
    with col1:
        st.write("")
        st.write("")
        st.write("PE is #1 diagnosis OR equally likely (+3)")
    with col2:
        test_radio_val2 = st.radio("",\
        ["No selection", "No", "Yes"],\
            horizontal=True, key="test2")
    st.markdown("""---""")

    col1, col2 = st.columns(2)
    with col1:
        st.write("")
        st.write("")
        st.write("Long text: PE is #1 diagnosis OR equally likely\
        PE is #1 diagnosis OR equally likely\
        PE is #1 diagnosis OR equally likely (+3)")
    with col2:
        test_radio_val3 = st.radio("",\
        ["No selection", "No", "Yes"],\
            horizontal=True, key="test3")



with st.expander("Developers' Notes & Questions"):
    st.info("Q: Is it really worth it to sync forms to be able to prepopulate fields?")
        
    st.write("- To test the functionality: see HR sync between\
        Well's PE form and PERC PE form")
    st.write("- Concern: If we do it for one we should probably\
        do it for all otherwise we're causing confusion.\
        I'm concerned there will be situations where there's unsolvable\
        ambiguity and we lure people into blind assumptions\
        which could over time lead to a breakdown of trust for the product")
    st.write("- Is it a feature that significantly improves the UX?")
    st.write("- Estimated time for update: 5-10 hours")
    st.write("- Confidence to get it done: 80%")
    st.write("- Is it a reasonable priority for a MVP?")
    st.markdown("---")
    st.info("Q: Layout preference for forms? Is it really worth it to deviate from the default?")
    st.write("- Will it significantly improve the UX?")
    st.write("- Estimated time for update: 5-20 hours")
    st.write("- Confidence to get it done: 90%")
    st.write("- Is it a reasonable priority for a MVP?")
    st.markdown("---")
    st.info("Q: Toggle hide/show sidebar. Will it be a problem?")
    st.write("https://discuss.streamlit.io/t/toggle-hide-show-sidebar-from-python/5805/3")
    st.write("- Estimated time for update: 1-5 hours")
    st.write("- Confidence to get it done: 30%")
    st.write("- Is it a reasonable priority for a MVP?")




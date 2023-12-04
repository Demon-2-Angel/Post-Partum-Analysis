import streamlit as st
import pandas as pd
import streamlit.components.v1 as components 
from streamlit_option_menu import option_menu

# We Load the dataset
df = pd.read_csv("post partum data set.csv")

# Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=[
            "Home",
            "Know About Post-Partum Depression",
            "Diagnosis & Treatments",
            "Prevention & Pathology",
            "Research Question-1",
            "Research Question-2", 
            "Contributors"
        ],
        default_index=0,
    )
#title will be seen on Each Page
st.title("Post Partum Depression")


#containers
homie = st.container()
info = st.container()
bond = st.container()
guilt = st.container()
people= st.container() 


# Home Page
if selected == "Home":
    st.header("Welcome to our Application!")
    #dataframe
    st.divider()
    st.subheader("Click to observe Dataset")
    with st.expander("Dataframe"):
            st.text("Here is the dataset that has been used in this Analysis : ")
            st.dataframe(df, height=600, width=1200) 
    st.divider()
    st.image("Unhappy_pic.jpg", width=500)
    st.divider()
    st.header("What is Postpartum Depression Analysis ?")
    st.markdown("""
        Postpartum analysis is the examination of a woman's physical and mental health during the period after childbirth. This analysis is important for identifying and treating any potential complications that may arise from the delivery of the baby.
    """)



# Causes Page
elif selected == "Know About Post-Partum Depression":
    st.divider()
    st.header("What could be the Causes & Symptoms for this ?")
    st.divider()
    st.subheader("Causes of Postpartum Complications")
    st.markdown("""
        - **Hormonal changes:** After childbirth, there is a rapid decline in estrogen and progesterone levels. This can lead to physical and emotional symptoms, including mood swings, depression, and anxiety.

        - **Emotional factors:** Stress, sleep deprivation, and lifestyle adjustments can all contribute to postpartum emotional challenges.

        - **Physical changes:** The body is recovering from the trauma of childbirth, and there may be a number of physical changes, such as pain, bleeding, and fatigue.

        - **Bleeding:** Excessive bleeding is a common complication of childbirth. It can be caused by a number of factors, including retained placenta, uterine atony, and lacerations.

        - **Infection:** Infections can occur in the uterus, urinary tract, or at incision sites. They can be serious and even life-threatening.

        - **Blood clots:** Blood clots can form in the legs, lungs, or abdomen after childbirth. They can be life-threatening.

        - **Mental health problems:** Postpartum mental health problems are common, and they can range from mild to severe. They include baby blues, postpartum depression, and postpartum psychosis.
    """)

    st.divider()

    st.subheader("Symptoms of Postpartum Complications")
    st.markdown("""
        - Excessive bleeding
        - Fever
        - Pain
        - Redness, swelling, or pus
        - Difficulty breastfeeding
        - Baby blues
        - Postpartum depression
        - Postpartum anxiety
        - Postpartum psychosis
    """)



# Diagnosis Page
elif selected == "Diagnosis & Treatments":
    st.divider()
    st.header(" What to do now?")
    st.divider()
    st.subheader("Diagnosis of Postpartum Complications")
    st.markdown(
        body= """
        
        <p>
        <strong>Edinburgh Postnatal Depression Scale (EPDS):</strong> 
        The EPDS is a questionnaire that can be used to screen for postpartum depression.
        </p>

        <ul>
            <li><strong>Blood tests:</strong> Blood tests can be used to check for infection, anemia, and other problems.</li>
            <li><strong>Ultrasound:</strong> Ultrasound can be used to visualize the uterus and other reproductive organs.</li>
            <li><strong>X-ray:</strong> X-rays can be used to check for fractures or other injuries.</li>
        </ul>""", unsafe_allow_html=True)

    st.divider()

    st.subheader("Treatment for Postpartum Complications")
    st.markdown("""
        - **Bed rest:** Bed rest may be recommended for women with excessive bleeding or infection.

        - **Medications:** Antibiotics are used to treat infection, and pain medication is used to relieve pain.

        - **Surgery:** Surgery may be necessary to remove a retained placenta, repair a laceration, or treat a blood clot.

        - **Therapy:** Therapy can be helpful for women with postpartum depression or anxiety.

        - **Medication:** Medication may be prescribed for women with severe postpartum depression or anxiety.
    """)



# Prevention & Pathology
elif selected == "Prevention & Pathology":
    st.divider()
    st.header(" What are the Prevention & Pathology? ")
    st.divider()
    st.subheader("Prevention of Postpartum Complications")
    st.markdown("""
        - Getting regular prenatal care
        - Eating a healthy diet
        - Getting enough rest
        - Talking to a healthcare provider about any concerns
    """)

    st.divider()

    st.subheader("Pathology of Postpartum Mental Health Conditions")
    st.markdown("""
        The development of postpartum mental health conditions is a complex process that involves a number of factors, including hormonal changes, psychological factors, and social factors. The transition from pregnancy to postpartum can be a stressful time for women, and this stress can contribute to the development of mental health problems.
    """)

    

# Analysis - 1
elif selected == "Research Question-1":
    st.divider()
    st.header("How Sleeping affects Bonding & Concentration in Post-Partum Depression ?")
    st.divider()
    # Tableau Public Dashboard
    html_DashBoard1 = """<div class='tableauPlaceholder' id='viz1701200066433' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PostPartumDepression_17008109983390&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PostPartumDepression_17008109983390&#47;Dashboard2' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PostPartumDepression_17008109983390&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1701200066433');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1300px';vizElement.style.height='950px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_DashBoard1, width=1300, height=1000)
    st.divider()
    st.subheader("Obeservations")
    st.markdown("""## Key Details:

### General:
- **Post-Partum Women's Emotions:**
  - Irritation and one-sided connection with the baby are common post-partum issues.
  - Sleep problems lasting two or more days are prevalent.
  - Causes: Attributed to the baby or depression.

- **Age-Related Observations:**
  - Irritation towards the baby and partner increases but decreases after age 45.
  - Suggested reason for the decline: Maturity.

### Age Groups:

#### 25-30:
- **Sleep and Connection with Baby:**
  - Lack of sleep affects the connection with the baby, especially if decision-making is impaired.
  - General association of connection issues and irritation, heightened with less sleep and impaired decision-making.
  - Higher irritation towards baby and partner may be due to the youthfulness of this age group.

#### 30-35:
- **Maturity Impact:**
  - Some maturity observed, as sleep-deprived mothers can still bond with the baby.
  - Impaired decision-making with low sleep leads to irritability.
  - Sleep deprivation is common but does not necessarily impair decision-making.

#### 35-40:
- **Sleep Deprivation and Irritation:**
  - Sleep deprivation in this age group is linked to irritation and connection issues.
  - Sleep is crucial due to the proneness to irritation.
  - Decision impairment is common with lack of sleep.

#### 40-45:
- **Sleep Deprivation and Decision Making:**
  - Sleep deprivation is present, but less decision-making impairment compared to other age groups.
  - Highest irritation towards partner and baby, but they can still connect with the baby.

#### 45-50:
- **Maturity and Decision Making:**
  - High maturity observed; easy decision-making even with no sleep for two days.
  - Minimal to no decision-making impairment.
  - Reduced irritation towards partner and baby.
"""
                  )



# Analysis - 2
elif selected == "Research Question-2":
    st.divider()
    st.header("Does Guilt increases Anxiousness & affect there Diet ?")
    st.divider()
    # Tableau Public Dashboard
    html_DashBoard2 = """<div class='tableauPlaceholder' id='viz1701199925161' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PostPartumDepression_17008109983390&#47;Dashboard3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PostPartumDepression_17008109983390&#47;Dashboard3' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PostPartumDepression_17008109983390&#47;Dashboard3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1701199925161');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1300px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='950px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1300px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='950px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.minWidth='1300px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='950px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    
    components.html(html_DashBoard2, width=1500, height=1000)
    st.divider()
    st.subheader("Obeservations")
    st.markdown("""### Age Group 25-30:

#### 1. Anxiety and Appetite:
- **Finding:** 33.15% of women in this age group are anxious, but it doesn't significantly impact their appetite.
- **Observation:** Anxiety seems to coexist without a direct effect on eating habits.

#### 2. Guilt and Sadness:
- **Finding:** Majority of women feeling guilty don't feel sad.
- **Observation:** Guilt may not directly contribute to sadness.

#### 3. Suicide Attempts:
- **Finding:** Suicide attempts are relatively low.
- **Observation:** Despite anxiety and guilt, effective coping mechanisms may be in place.

### 30-35:

#### 1. Anxiety and Appetite:
- **Finding:** 43.25% of women are not anxious, and it doesn't impact their appetite significantly.
- **Observation:** Anxiety is less prevalent and minimally affects eating habits.

#### 2. Guilt and Sadness:
- **Finding:** Majority of guilty women don't feel sad.
- **Observation:** Similar to the younger age group, guilt may not strongly correlate with sadness.

#### 3. Suicide Attempts:
- **Finding:** Suicide attempts are less frequent.
- **Observation:** Despite some anxiety, women in this age group show resilience against severe outcomes.

### Age Group 35-40:

#### 1. Anxiety and Appetite:
- **Finding:** 40.11% of women experience anxiety, but it doesn't affect appetite significantly.
- **Observation:** Anxiety doesn't strongly influence eating habits.

#### 2. Guilt and Sadness:
- **Finding:** Majority of women feeling guilty don't feel sad.
- **Observation:** Consistent with younger groups, guilt may not directly lead to sadness.

#### 3. Suicide Attempts:
- **Finding:** Higher rates of suicide attempts.
- **Observation:** Increased suicide attempts suggest a need for targeted mental health interventions.

### Age Group 45-50:

#### 1. Anxiety and Appetite:
- **Finding:** 43.68% of women experience anxiety, but it doesn't affect appetite significantly.
- **Observation:** Similar to the 35-40 group, anxiety doesn't strongly correlate with changes in appetite.

#### 2. Guilt and Sadness:
- **Finding:** Majority of guilty women don't feel sad.
- **Observation:** Guilt doesn't significantly contribute to sadness in this age group.

#### 3. Suicide Attempts:
- **Finding:** Higher rates of suicide attempts.
- **Observation:** High prevalence of suicide attempts emphasizes the need for mental health support.

## General Observations:

#### 1. Consistent Trends:
- Across age groups, the majority of women feeling guilty do not report feeling sad.

#### 2. Appetite and Anxiety:
- Anxiety, in general, does not appear to have a profound impact on appetite across age groups.

#### 3. Suicide Attempts:
- Notable suicide attempts in the 35-50 age range highlight a critical need for mental health interventions and support.

#### 4. Individual Coping Strategies:
- Despite anxiety and guilt, some women demonstrate resilience, as indicated by lower suicide attempt rates.

#### 5. Recommendations:
- Develop targeted mental health interventions for women in the 35-50 age range.
- Explore and promote effective coping mechanisms identified in groups with lower suicide attempt rates.

    
    """)


#Contributors Page
elif selected == "Contributors":
    st.title("Postpartum Analysis - Contributors")
    st.subheader("Contributors")
    st.markdown("""
        - 21BAI10012 – RAM NAYAK
        - 21BAI10054 – ANIRUDDHA KUMAR
        - 21BAI10055 – JISHNU CHOWDHURY
        - 21BAI10121 – NYASHA RAI
        - 21BAI10307 – SACHIN DESHWAL 
    """)
    st.divider()
    st.subheader("Link to the Resources")
    st.markdown("""
        - [A Comprehensive Analysis of Post-partum Depression Risk Factors: The Role of Socio-Demographic, Individual, Relational, and Delivery Characteristics](https://pubmed.ncbi.nlm.nih.gov/31709213/)
        
        - [Situational analysis to scale up and sustain postpartum family planning services in Niger](https://www.who.int/publications/m/item/situational-analysis-to-scale-up-and-sustain-postpartum-family-planning-services-in-niger)
        
        - [Postpartum depression and associated factors among mothers who gave birth in the last twelve months in Ankesha district, Awi zone, North West Ethiopia](https://bmcpregnancychildbirth.biomedcentral.com/articles/10.1186/s12884-019-2594-y)
        
        - [Optimizing Postpartum Care](https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2018/05/optimizing-postpartum-care)
""")



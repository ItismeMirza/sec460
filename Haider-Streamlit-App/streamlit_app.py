import streamlit as st
from pages.page_1 import func_page_1
from pages.page_2 import func_page_2
from datetime import datetime

# Function for the clock page
def run_clock_page():
    st.title('Clock')
    clock = st.empty()
    while True:
        time = datetime.now().strftime("%H:%M:%S")
        clock.info(f'**Current time: ** {time}')
        if time == '16:09:50':
            clock.empty()
            st.warning('Alarm!!')
            break

# Main function to handle page selection
def main():
    st.sidebar.subheader('Page selection')
    page_selection = st.sidebar.selectbox('Please select a page', ['Main Page', 'Page 1', 'Page 2', 'Clock Page'])
    
    pages_main = {
        'Main Page': main_page,
        'Page 1': run_page_1,
        'Page 2': run_page_2,
        'Clock Page': run_clock_page  # Added the Clock Page option
    }

    # Run selected page
    pages_main[page_selection]()

# Main page
def main_page():
    st.title('Main Page')


conn = st.connection("snowflake")
df = conn.query("SELECT * FROM mytable;", ttl="10m")

for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")

# Run Page 1
def run_page_1():
    func_page_1()

# Run Page 2
def run_page_2():
    func_page_2()

# Running the Streamlit app
if __name__ == '__main__':
    main()

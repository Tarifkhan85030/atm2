
import streamlit as st

# Set page configuration
st.set_page_config(page_title="ATM Interface", page_icon="🏦", layout="centered")

# CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f8ff; /* Light blue background */
    }
    .stSidebar {
        background-color: #e0f7fa; /* Light teal for sidebar background */
    }
    .stRadio > div {
        margin-bottom: 20px; /* Add space between radio buttons */
    }
    input[type="text"], input[type="password"] {
        background-color: #e8f0fe; /* Light blue for input fields */
        color: #333333;
        padding: 8px;
        border-radius: 5px;
        border: 1px solid #b0bec5;
        width: 280px;
        max-width: 100%;
    }
    </style>
    """, unsafe_allow_html=True
)

# Initialize session state for ATM variables
if "pin" not in st.session_state:
    st.session_state["pin"] = ""
if "balance" not in st.session_state:
    st.session_state["balance"] = 0

class ATM:
    def __init__(self):
        # Sidebar menu for ATM operations
        st.sidebar.title("ATM Menu")
        st.sidebar.markdown("<h4 style='color:#444;'>Select an option:</h4>", unsafe_allow_html=True)
        
        # Sidebar radio button options with spacing
        option = st.sidebar.radio("Options:", ["Generate PIN", "Change PIN", "Balance Inquiry", "Withdraw", "Exit"])

        if option == "Generate PIN":
            self.pin_generator()
        elif option == "Change PIN":
            self.pin_changer()
        elif option == "Balance Inquiry":
            self.balance_inquiry()
        elif option == "Withdraw":
            self.withdraw()
        elif option == "Exit":
            st.write("Thank you for using the ATM!")

    def pin_generator(self):
        st.subheader("Generate PIN")
        
        # Input fields for PIN and initial balance
        new_pin = st.text_input("Enter new PIN:", type="password", key="generate_new_pin")
        initial_balance = st.text_input("Enter initial deposit:", key="generate_initial_balance")

        if st.button("Submit PIN"):
            if new_pin:
                try:
                    st.session_state["pin"] = new_pin
                    st.session_state["balance"] = int(initial_balance)
                    st.success("PIN generated and balance set.")
                except ValueError:
                    st.error("Please enter a valid number for the balance.")
            else:
                st.error("Please enter a PIN.")

    def pin_changer(self):
        st.subheader("Change PIN")
        
        # Input fields for current and new PINs
        old_pin = st.text_input("Enter old PIN:", type="password", key="change_old_pin")
        new_pin = st.text_input("Enter new PIN:", type="password", key="change_new_pin")

        if st.button("Submit New PIN"):
            if old_pin == st.session_state["pin"]:
                if new_pin:
                    st.session_state["pin"] = new_pin
                    st.success("PIN successfully changed.")
                else:
                    st.error("Please enter a new PIN.")
            else:
                st.error("Incorrect old PIN.")

    def balance_inquiry(self):
        st.subheader("Balance Inquiry")
        st.info(f"Your current balance is: {st.session_state['balance']}")

    def withdraw(self):
        st.subheader("Withdraw Money")
        
        # Input fields for PIN verification and withdrawal amount
        entered_pin = st.text_input("Enter PIN:", type="password", key="withdraw_pin")
        amount = st.text_input("Enter amount to withdraw:", key="withdraw_amount")

        if st.button("Submit Withdrawal"):
            if entered_pin == st.session_state["pin"]:
                try:
                    withdrawal_amount = int(amount)
                    if withdrawal_amount <= st.session_state["balance"]:
                        st.session_state["balance"] -= withdrawal_amount
                        st.success(f"Withdrawal successful. New balance: {st.session_state['balance']}")
                    else:
                        st.error("Insufficient balance.")
                except ValueError:
                    st.error("Please enter a valid number for the withdrawal amount.")
            else:
                st.error("Incorrect PIN.")

# Instantiate the ATM application
if __name__ == "__main__":
    atm = ATM()

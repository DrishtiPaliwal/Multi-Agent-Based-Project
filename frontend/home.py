import streamlit as st

def render_home_page():
    """Renders a modern, clean, premium Welcome/Home page for the ShopWise application.
    Navigates to the main application when the user clicks 'Get Started'.
    """
    # Create a layout that centers our home page container
    col_left, col_mid, col_right = st.columns([1, 4, 1])
    
    with col_mid:
        # A container wrapping all welcome elements to apply CSS
        st.markdown(
            '<div class="home-container">'
            '  <div class="home-illustration-wrapper">'
            '    <span style="font-size: 3rem; line-height: 1;">🛍️</span>'
            '  </div>'
            '  <div class="home-title">ShopWise</div>'
            '  <div class="home-subtitle">Compare Smarter with AI</div>'
            '  <div class="home-description">'
            '    Compare products, analyze deals, and get AI-powered shopping recommendations '
            '    across top e-commerce platforms instantly.'
            '  </div>'
            '</div>',
            unsafe_allow_html=True
        )
        
        # Place button in home-button-container
        # We wrap this in a div to target it with CSS for centering and styles
        
        btn_left, btn_mid, btn_right = st.columns([2, 1, 2])

        with btn_mid:
           if st.button("Get Started", key="get_started_btn", use_container_width=True):
                st.session_state.entered_app = True
                st.rerun()

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )
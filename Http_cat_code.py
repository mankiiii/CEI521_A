import streamlit as st
import requests

# Base URL for HTTP Cat API
BASE_URL = "https://http.cat/"

HTTP_STATUS_CODES = {
    200: "OK",
    201: "Created",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout"
}

def get_http_cat_image(status_code):
    """Fetch the cat image from a given HTTP status code."""
    response = requests.get(f"{BASE_URL}{status_code}")
    return response.url if response.status_code == 200 else None

def show_cat_http_details():

    st.markdown("<h1 style='text-align: center;'>HTTP Cat Status Code</h1>", unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
    status_code = st.text_input("Enter an HTTP Status Code (e.g., 200, 404, 500):")

    if status_code:
        try:
            # Convert input to integer and fetch image
            status_code = int(status_code)
            image_url = get_http_cat_image(status_code)

            if image_url:
                st.image(image_url, caption=f"HTTP {status_code}")
            else:
                st.error(f"Error, this status code doesn't exists: {status_code}")
                show_available_status_codes()
        except ValueError:
            st.error("Please enter a valid HTTP status code.")
            show_available_status_codes()

def show_available_status_codes():
    st.subheader("Available HTTP Status Codes:")
    for code, description in HTTP_STATUS_CODES.items():
        st.write(f"{code}: {description}")



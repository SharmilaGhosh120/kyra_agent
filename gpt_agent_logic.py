
def get_gpt_response(query):
    if "internship" in query.lower():
        return "You can explore internships through the AICTE internship portal."
    elif "msme" in query.lower():
        return "MSME schemes can be accessed via the official MSME India website."
    else:
        return "Thanks for your query. A counselor will get back to you shortly."

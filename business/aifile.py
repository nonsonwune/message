import os
import openai
from django.conf import settings
openai.api_key = os.getenv("OPENAI_API_KEY")

def companyDescription(business_name, business_type, country, prod_serv, short_description, years, progress):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generate a Company Description section for a Business Plan for the following business, using the guidelines provided:\nBusiness Name: {}\nBusiness Type: {}\nCountry: {}\nProduct or Service: {}\nShort Business Description: {}\nYears in Operation: {}\nBusiness Progress to Date: {}\n\nGuidelines: Start the company description by lisiting the business name and company structure, if one is provided. Write a detailed business decription form the short description provided in a proffessional tone. Describe the Industry the Business will be operating in and rewrite the business progress to date more elaborately, giving more detail and insights. Finally provide a numbered list of 3 suitable business objective for this business and for each objective, describe how the objective fits the business and how it will benefit the stakeholders in the long run.\n\nCompany Description".format(business_name, business_type, country, prod_serv, short_description, years, progress),
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
        )

    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text'].replace('\n', '<br/>')
            return answer
        else:
            return ''
    else:
        return ''
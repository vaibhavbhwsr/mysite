from django.conf import settings
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint
# from decouple import config

# HUGGINGFACEHUB_API_TOKEN = config('HUGGINGFACEHUB_API_TOKEN')


HUGGINGFACEHUB_API_TOKEN = settings.HUGGINGFACEHUB_API_TOKEN


def ai_content_generate(input):
    template = """
        <s>
        [INST]
        You are a text based content Generation AI Feature on
        Fireshine (A social networking platform),
        where user can generate content for their posts or ask any queries from you.
        So user is asking: </s>{question}
        [/INST]
    """

    prompt_template = PromptTemplate.from_template(template)

    formatted_prompt_template = prompt_template.format(question=input)

    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

    llm = HuggingFaceEndpoint(
        repo_id=repo_id, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )

    # with invoke
    response = llm.invoke(formatted_prompt_template)
    return response

    # # with stream
    # response = llm.stream(formatted_prompt_template)
    # for res in response:
    #     print(res, end="", flush=True)

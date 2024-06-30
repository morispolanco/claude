import streamlit as st
import anthropic

# Inicializa el cliente de Anthropics con la API Key
client = anthropic.Anthropic(api_key="my_api_key")

# Función para llamar a la API y obtener la respuesta mejorada
def improve_prompt(original_prompt, task_description):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""
                        You are an AI assistant specialized in improving prompts for language models. Your task is to analyze an original prompt and a task description, then create an improved version of the prompt that will lead to better results for the given task.

                        Here is the original prompt:
                        <original_prompt>{original_prompt}</original_prompt>

                        And here is the description of the task this prompt is meant to accomplish:
                        <task_description>{task_description}</task_description>

                        First, analyze the original prompt and the task description. Consider the following aspects:
                        1. Clarity: Is the prompt clear and easy to understand?
                        2. Specificity: Does it provide enough detail for the AI to complete the task accurately?
                        3. Relevance: Does it align well with the task description?
                        4. Structure: Is the prompt organized in a logical manner?
                        5. Constraints: Does it set appropriate boundaries or limitations?

                        Next, create an improved version of the prompt. When improving the prompt, follow these guidelines:
                        1. Make the instructions more explicit and detailed where necessary.
                        2. Add any missing context or information that would help the AI better understand and complete the task.
                        3. Remove any irrelevant or potentially confusing information.
                        4. Structure the prompt in a clear, step-by-step format if appropriate.
                        5. Include examples or sample outputs if they would be helpful.
                        6. Add any necessary constraints or guidelines to ensure the AI's response aligns with the task requirements.
                        7. Consider including instructions for the AI to think through its approach before providing a final answer, if the task is complex.

                        Write your improved prompt inside <improved_prompt> tags. After the improved prompt, provide a brief explanation of the changes you made and why you believe they will lead to better results. Write this explanation inside <explanation> tags.

                        Remember to maintain a professional and clear tone throughout the improved prompt. Ensure that the improved prompt is comprehensive yet concise, providing all necessary information without unnecessary verbosity.
                        """
                    }
                ]
            }
        ]
    )
    return message.content

# Interfaz de usuario de Streamlit
st.title("Mejora de Prompts con Anthropics API")
st.write("Ingrese el prompt original y la descripción de la tarea para obtener un prompt mejorado.")

# Entrada de usuario
original_prompt = st.text_area("Prompt Original")
task_description = st.text_area("Descripción de la Tarea")

if st.button("Mejorar Prompt"):
    if original_prompt and task_description:
        improved_prompt = improve_prompt(original_prompt, task_description)
        st.subheader("Prompt Mejorado")
        st.write(improved_prompt)
    else:
        st.error("Por favor, ingrese tanto el prompt original como la descripción de la tarea.")

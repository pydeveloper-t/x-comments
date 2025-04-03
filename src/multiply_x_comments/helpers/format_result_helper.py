from multiply_x_comments.helpers.re_helper import get_enclosed_strings

def format_result(input_list: list, output_list: list) -> list[dict]:
    result = []
    for ind, prompt in enumerate(input_list):
        str_list = get_enclosed_strings(source_text=output_list[ind].raw)
        result.append({"source_text": prompt["topic"], "paraphrased_texts": str_list})
    return result    


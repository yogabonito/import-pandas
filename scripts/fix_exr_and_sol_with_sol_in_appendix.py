import os
import re

# TODO 🚨
# - remove JavaScript for Bootstrap tooltips, because I am simply gonna use buttons instead of the arrow-up link
# - improve DRYness: define YAML headmatter here and put it into every file
#   - if any YAML headmatter is already present, it should be merged with the one defined here (or maybe just overwritten)
#   - put all the solutions into a plain .md file and then automatically generate a nice .qmd file for the solutions chapter automatically from it (with correct order of solutions and horizontal rulers between solutions and a heading for each chapter such that the solution numbers correspond to the exercise numbers)

if __name__ == "__main__":
    print("pre-render!!!")
    # output_dir = os.getenv("QUARTO_PROJECT_OUTPUT_DIR")
    # print(type(output_dir), output_dir)
    input_file = os.getenv("QUARTO_PROJECT_INPUT_FILES")
    assert(isinstance(input_file, str)) # not tested with other types (e.g., list of strings)
    print(type(input_file), input_file if input_file else "(empty string)")
    if "\n" in input_file: # multiple files separated by \n
        print("🚨🚨🚨🚨🚨 Only one file may change at a time")
        exit()
    SOL_CHAPTER_FILE = "appendix-solutions-raw.md"
    ANY_SOL_PATTERN = r":::\s*\{#(sol-[A-Za-z0-9-]+)\}"
    SOL_REFS_IN_SOL_CHAPTER = []

    with open(SOL_CHAPTER_FILE, "r") as sol_f:
        sol_file_content = sol_f.read()
        SOL_REFS_IN_SOL_CHAPTER = [sol_match.group(1) for sol_match in re.finditer(ANY_SOL_PATTERN, sol_file_content)]

    EXERCISE_PATTERN_END = r"[\s\S]*?\n:::(\n|$)"
    EXERCISE_PATTERN = r":::\s*\{#(exr-[A-Za-z0-9-]+)\}" + EXERCISE_PATTERN_END
    # TOOLTIP_SCRIPT = (
    #     "<script>\n" +
    #     'const tooltipElements = document.getElementsByClassName("tt")\n' +
    #     "for (const tooltipElement of tooltipElements) {\n" +
    #     "  new bootstrap.Tooltip(tooltipElement)\n"
    #     "}\n"
    #     "</script>"
    # )
    
    if not os.getenv("QUARTO_PROJECT_RENDER_ALL"):
        print("🚨🚨🚨 starting pre-render script for exercises and solutions 🚨🚨🚨")
        
        if isinstance(input_file, str) and input_file != "":
            with open(input_file, "r") as f:
                file_content = f.read()
            
            exercise_refs = []
            for match in re.finditer(EXERCISE_PATTERN, file_content, flags=re.DOTALL):
                exercise_start_index, exercise_end_index = match.span(0)
                exercise_ref = match.group(1) # without leading # or @
                print(f"✅ found exercise {exercise_ref} at index {exercise_start_index}-{exercise_end_index}:\n{file_content[exercise_start_index:exercise_end_index]}\n---\n")
                exercise_refs.append(exercise_ref)
            # print("📜 found the following exercises:")
            # for exercise_ref in exercise_refs:
            #     print("-", exercise_ref)
            
            SOL_REFS_IN_CURRENT_CHAPTER = [sol_match.group(1) for sol_match in re.finditer(ANY_SOL_PATTERN, file_content)]
            SOL_REFS_TOTAL = set(SOL_REFS_IN_SOL_CHAPTER + SOL_REFS_IN_CURRENT_CHAPTER)

            for exercise_ref in exercise_refs:
                solution_ref = exercise_ref.replace("exr", "sol")
                # If reference to solution is not in exercise, add it
                EXERCISE_PATTERN = r":::\s*\{#" + exercise_ref + r"\}" + EXERCISE_PATTERN_END
                exercise_text = re.search(EXERCISE_PATTERN, file_content).group()
                if exercise_text.endswith("\n"):
                    exercise_text = exercise_text[:-1]
                if solution_ref not in exercise_text:
                    wink_to_solution = f"You can compare your solution to @{solution_ref}.\n"
                    if not exercise_text.endswith("\n\n:::"):
                        wink_to_solution = "\n" + wink_to_solution
                    exercise_text_with_wink_to_solution = exercise_text[:-3] + wink_to_solution + exercise_text[-3:]
                    file_content = file_content.replace(exercise_text, exercise_text_with_wink_to_solution)
                    exercise_text = exercise_text_with_wink_to_solution
                
                # If no solution exists, add it
                # link_to_exercise = "[{{< iconify line-md arrow-up >}}](#" + exercise_ref + ")" + '{class="tt" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Back to exercise"}'
                link_to_exercise = f"(for @{exercise_ref})"
                if solution_ref not in SOL_REFS_TOTAL:
                    print(f"😭 no match found for exercise {exercise_ref}")
                    solution_template_to_fill_out = (
                        "\n" +
                        "::: {#" + solution_ref + "}\n" +
                        "\n" +
                        link_to_exercise + "\n\n"
                        "```{python}\n" +
                        "\n" +
                        "```\n" +
                        ":::\n"
                    )
                    file_content = file_content.replace(exercise_text, exercise_text + solution_template_to_fill_out)
                    exercise_text = exercise_text + solution_template_to_fill_out
                # If solution exists, but does not have a link back to exercise, add it (only works when run while sol is in the same file as exr)
                else:
                    print("🤔🤔", solution_ref)
                    SOLUTION_WHOLE_PATTERN = r":::\s*\{#" + solution_ref + r"\}" + EXERCISE_PATTERN_END
                    solution_match_whole = re.search(SOLUTION_WHOLE_PATTERN, file_content)
                    if solution_match_whole is not None: # we do not check for links if the solution is already placed in the .md file with the raw solutions
                        solution_text_whole = solution_match_whole.group()
                        if solution_text_whole.endswith("\n"):
                            solution_text_whole = solution_text_whole[:-1]
                        solution_whole_start_index = solution_match_whole.start()
                        if link_to_exercise in solution_text_whole:
                            print("👍 link back to exercise already present")
                        else:
                            SOLUTION_START_PATTERN = r":::\s*\{#" + solution_ref + r"\}\s*"
                            solution_match_start = re.search(SOLUTION_START_PATTERN, file_content)
                            solution_text_start = solution_match_start.group()
                            print("🙌 adding the link back to the exercise")
                            link_to_paste_index = solution_whole_start_index+len(solution_text_start)
                            rest_of_file_content = file_content[link_to_paste_index:]
                            if rest_of_file_content.startswith("```"):
                                rest_of_file_content = "\n\n" + rest_of_file_content
                            else:
                                rest_of_file_content = " " + rest_of_file_content
                            file_content = file_content[:link_to_paste_index] + link_to_exercise + rest_of_file_content

            # # If the JavaScript for bootstrap tooltips is not in the file, place it at the end of the file
            # if TOOLTIP_SCRIPT not in file_content:
            #     if file_content[-1] != "\n":
            #         file_content += "\n"
            #     file_content += "\n" + TOOLTIP_SCRIPT

            with open(input_file, "w") as f:
                print("✍️ writing file …")
                f.write(file_content)
        else:
            print("❌ input_file is not a non-empty string")
        print("exit now!")
        exit()

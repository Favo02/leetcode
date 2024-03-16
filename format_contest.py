import os
import re
import yaml

def find(pattern, path):
  for root, _, files in os.walk(path):
    for name in files:
      if re.match(pattern, name):
        return os.path.join(root, name)
  return "ERR"

template = """
<details>
  <summary>
    <b>{}</b>
  </summary>

  - [{}]({})
  - Final standing: **{}<sup>{}</sup> / {}**
  - Score: **{}**, Finish time: **{}**
  - Rating change: **{}** _(now {})_

  | Problem | Solved time + Penalties | Solution |
  |--|--|--|
{}
</details>
"""

solved_template = "  | [{}]({}) | ✅ {} {} | [{}]({}) |"
unsolved_template = "  | [{}]({}) | ❌ {} | - |"

with open("format_contest_template.yml", "r") as file:
  c = yaml.safe_load(file)["contest"]

formatted_problems = []

for p in c["problems"]:

  p_name = p["name"]
  p_camel_name = "".join(map(lambda s: s.capitalize(), p_name.split()))
  p_url = p["url"]
  p_is_solved = p["solved_time"] != -1
  p_solved_time = p["solved_time"]
  p_penalties = f"_({p["penalties"]} penalties)_" if p["penalties"] != 0 else ""
  p_solution = "-" if not p_is_solved else find(r"^[0-9]{1,4}\." + p_camel_name + r"\.[a-z]*$", "./solved")
  p_file = p_solution.split("/")[-1]

  if p_is_solved:
    formatted_problems.append(solved_template.format(p_name, p_url, p_solved_time, p_penalties, p_file, p_solution))
  else:
    formatted_problems.append(unsolved_template.format(p_name, p_url, p_penalties))

name = c["name"]
url = c["url"]
position = c["position"]
th = {1: "st", 2: "nd", 3: "rd"}[position % 10] if position % 10 in [1, 2, 3] else "th"
partecipants = c["partecipants"]
score = c["score"]
finish_time = c["finish_time"]
rating_change = c["rating_change"]
new_rating = c["new_rating"]
problems = "\n".join(formatted_problems)

formatted = template.format(name, name, url, position, th, partecipants, score, finish_time, rating_change, new_rating, problems)

print(formatted)

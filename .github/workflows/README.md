# LeetCode Scaffolding Workflow

## Requirements

- Fully automate problem scaffolding
- Ensure consistent folder structure per study-plan
- Avoid manual errors and save time

---

## How It Works

The workflow triggers on push events modifying files with the path:

```bash
scripts/*.json
```

Workflow:
- Detect all modified JSON files
- Skip any files ending with `details.json`
- Run the `scaffolding.py` script passing the JSON containing alla the leetcode problem names as input
- Generate the folder `problems/<json-name>` containing Python files for each problem
- Create or update the file `scripts/<json-name>-details.json` with leetcode problem details fetched via GraphQL
- Add and commit the changes
- Push automatically via GitHub Actions

# 🐍 Python DSA Practice Repository

A structured, scalable system for practicing Data Structures & Algorithms in Python. Designed for pattern-based learning, version control, and local testing.

## 📁 Recommended Scalable Structure
```text
Python DSA/
├── _templates/
│   ├── solution_template.py      # Pre-loaded class/function stubs
│   └── test_template.py          # pytest-ready boilerplate
├── 01_arrays_hashing/
│   ├── lc_217_contains_duplicate.py
│   ├── lc_217_notes.md
│   └── ...
├── 02_two_pointers/
├── 03_sliding_window/
├── 04_linked_lists/
├── 05_stacks_queues/
├── 06_hash_maps/
├── 07_recursion_backtracking/
├── 08_trees/
├── 09_heaps/
├── 10_graphs/
├── 11_dynamic_programming/
├── 12_advanced/
└── PROGRESS.md                   # Master tracker
```

### 💡 Why this works:
- **Numbered folders** keep topics in roadmap order.
- **One file per problem** → easier to `grep`, open, and review.
- **`_templates/`** prevents boilerplate fatigue.
- **`PROGRESS.md`** replaces filename dates with a clean, searchable log.

## 🏷️ Naming Convention
Dates in filenames make sorting/filtering messy over time. Switch to:
`lc_{problem_id}_{problem_name}_{variant}.py`

**Examples:**
- `lc_217_contains_duplicate_attempt1.py`
- `lc_217_contains_duplicate_optimal.py`
- `lc_217_contains_duplicate_notes.md`

**Rule:** Keep attempts minimal (max 3 versions). After that, consolidate into one file with inline comments:
```python
# LC 217: Contains Duplicate
# Attempt 1 (04/16): Sorting → O(n log n) time
# Attempt 2 (04/17): Hash set → O(n) time/space ✅ Optimal
```

## 🐙 Git Workflow for DSA Practice
```bash
# After each attempt
git add .
git commit -m "LC 217: attempt 1 - brute force sort O(n log n)"
git commit -m "LC 217: attempt 2 - hash set O(n) time/space"

# Tag phase completion
git tag phase1-arrays-hash
git push --tags
```
💡 **Pro tip:** Use `git log --oneline --grep="LC 217"` to quickly review your iteration history.

## 🧪 Local Testing Setup (Python)
Stop relying solely on LeetCode's editor. Test locally with `pytest`:
```bash
pip install pytest
```

**`test_lc_217.py`**
```python
import pytest
from lc_217_contains_duplicate_optimal import Solution

def test_contains_duplicate():
    sol = Solution()
    assert sol.containsDuplicate([1,2,3,1]) == True
    assert sol.containsDuplicate([1,2,3,4]) == False
    assert sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
```
**Run:** `pytest -v` → instant feedback, edge case testing, and faster iteration.
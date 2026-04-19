# 📊 DSA Practice Tracker & Spaced Repetition Log

> **Instructions:** Copy this entire file into `PROGRESS.md` at your repo root. Add one row per problem. Update `Next Review` after each successful recall session.

## 🗂️ Active Problem Log

| Date Solved | LC # | Problem | Phase/Topic | Core Pattern | Time / Space | Status | Next Review | Notes / Trigger |
|:-----------:|:----:|:--------|:------------|:-------------|:-------------|:-------|:-----------:|:----------------|
| 2026-04-17 | 217 | Contains Duplicate | 01 Arrays & Hashing | Hash Set Lookup | O(n) / O(n) | ✅ Opt | 2026-04-24 | R1 passed → consolidated to optimal |
| 2026-04-16 | 217 | Contians Duplicate | 01 Arrays & Hashing | Hash Set Lookup | O(n) / O(n) | 🔵 Solved | 2026-04-18 | Check complement *before* inserting |
| 2026-04-17 | 001 | Two Sum | 01 Arrays & Hashing | Hash Map Complement | O(n) / O(n) | 🔵 Solved ✅ Opt | 2026-04-19 | Check complement *before* inserting |

### 🔑 Status Legend
- `🟡 Review` → Struggled or needed hints
- `🔵 Solved` → Solved independently, but not optimal
- `✅ Opt` → Optimal time/space, clean code, all edge cases handled

---

## 🔄 Spaced Repetition Schedule

| Cycle | Timing | Action | Pass/Fail Rule |
|-------|--------|--------|----------------|
| **R1** | `+2 days` | Retype solution from scratch (no LeetCode, no notes) | ✅ Pass → Push to R2 \| ❌ Fail → Reset to R1 |touch SCHEDULE.md
| **R2** | `+7 days` | Solve under 20 mins + write complexity analysis | ✅ Pass → Push to R3 \| ❌ Fail → Reset to R1 |
| **R3** | `+21 days` | Explain pattern aloud + solve 1 unseen variant | ✅ Pass → Archive \| ❌ Fail → Reset to R2 |

💡 **Manual Date Trick:** Add `+2`, `+7`, `+21` to your `Date Solved` column. Use your phone calendar or a simple `date` command to set reminders.

---

## 📈 Progress Metrics (Update Monthly)

```markdown
- Total Solved: ___ / 150
- Optimization Rate (`✅ Opt`): ___% (Target: ≥65%)
- Most Weak Pattern: __________
- Current Streak: ___ days
- Next Phase to Start: __________
```

## 🛠️ Daily Workflow
1. **Solve** → Log row in table
2. **Commit** → git commit -m "LC ###: solved v1"
3. **Review** → Check Next Review column each morning
4. **Pass** → Move date to next cycle or mark ✅ Archived
5. **Fail** → Reset to R1, add trigger note, retry tomorrow
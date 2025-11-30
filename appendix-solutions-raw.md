<!-- chapter data -->

::: {#sol-examples-for-data-in-tables}

(for @exr-examples-for-data-in-tables)

The activities dataset in @tbl-chapter-1-example-table is basically a collection of events, where each event is a pysical activity of a user. Other events could, for example, be

<details>
<summary>exams at a university</summary>
```{python}
#| echo: false
#| label: tbl-chapter-1-exam-data
#| tbl-cap: Example table with exam data
pd.DataFrame(
    {
        "course_id": ["isp.2025.w", "isp.2025.w", "oop1.2026.s","oop1.2026.s", "…"],
        "date": ["2026-02-02", "2026-02-02", "2026-07-02", "2026-07-02", "…"],
        "time": ["15:00", "15:00", "16:00", "17:00", "…"],
        "room": ["P1", "i13", "P1", "P1", "…"],
        "…": ["…"] * 5
    },
    index=[0, 1, 2, 3, "…"]
)
```
</details>

<details>
<summary>or a doctor's list of appointments with patients</summary>
```{python}
#| echo: false
#| label: tbl-chapter-1-doctor-data
#| tbl-cap: Example table with patient data
pd.DataFrame(
    {
        "Social Security Number": ["409720011984", "183212111997", "007208032005", "183212111997", "…"],
        "Appointment Time": ["2025-10-01 08:00", "2025-10-03 09:00", "2025-10-06 13:00", "2025-10-31 08:30", "…"],
        "Weight": [68, 110, pd.NA, 108, "…"],
        "Blood pressure": ["110-70", "155-100", "129-84", "140-92", "…"],
        "…": ["…"] * 5
    },
    index=[0, 1, 2, 3, "…"]
)
```
</details>

or sensor measurements.

```{python}
#| echo: false
#| label: tbl-chapter-1-sensor-data
#| tbl-cap: Example table with data reported by heart rate and GPS sensors
pd.DataFrame(
    {
        "Activity ID": [1, 1, "…", 101, 101],
        "Time": ["2025-10-02 17:45:00", "2025-10-02 17:45:01", "…", "2025-10-31 18:09:47", "2025-10-31 18:09:48"],
        "Heart Rate": ["62", "63", "…", "134", "134"],
        "Longitude": ["13°53'01.5\"E", "13°53'01.9\"E", "…", pd.NA, pd.NA],
        "Latitude": ["46°36'41.7\"N", "46°36'41.8\"N", "…", pd.NA, pd.NA],
        "…": ["…"] * 5
    },
    index=[0, 1, "…", 359802, 359803]
)
```

Note that some pieces of information may be missing (`<NA>`), as in the _Longitude_ and _Latitude_ columns of @tbl-chapter-1-sensor-data.

<!-- TODO: move the following into a chapter about data types.

Each row contains information on an appointment with a patient who is identified by their social security number. Note that we will want to store such numbers as strings to prevent problems cuased by leading zeros. The column `Appointment Date` contains dates. While we could represent these dates using strings as well, it is recommended to use one of the temporal data types offered by Pandas. We will learn about these data types later. (**TODO: specify when temporal data types are discussed.**)

Most of the time, the doctor measures a patient's weight. Note that one value is missing (`<NA>`), while the other values are integers. Pandas offers an integer data type which is capable of representing missing values.

At each appointment, the doctor measures the patient's blood pressure, which consists of two values. In the table above, both values are stored in the same column only separated by a hyphen? This means that the values are stored as strings rather than integers.  -->

<!--
another example: events at CUAS

```{python}
#| echo: false
#| tbl-cap: Example table with data on events
pd.DataFrame(
    {
        "Event": ["Náboj", "Women in Data Science", "…"],
        "Description": ["international math competition", "data science conference", "…"],
        "Date": ["2026-03-13", pd.NA, "…"],
        "Location": ["Villach", "Villach", "…"],
        "…": ["…"] * 3
    }
)
```
-->

In contrast to the examples above, data can also describe entities that are not events. The following table lists the _users_ who recorded the events in @tbl-chapter-1-example-table.

```{python}
#| echo: false
#| tbl-cap: Example table with data on events
pd.DataFrame(
    {
        "User ID": [1, 22, 42, "…"],
        "Name": ["Carl", "Barbara", "Aleks", "…"],
        "E-mail": ["charlie@example.com", "barbara@example.com", "aleks@example.com", "…"],
        "Registered Since": ["2022-01-01 14:52", "2023-04-23 11:45", "2025-08-04 19:10", "…"]
    },
    index=[0, 1, 2, "…"]
)
```

:::

<!-- chapter sampling -->

::: {#sol-head-tail}

(for @exr-head-tail)

```{python}
#| echo: false
activities_series = pd.Series(
    ["run", "hike", "bike", "run"],
    name="Activity Type"
)
```

```{python}
first_few_elements = activities_series.head(2)
last_few_elements = activities_series.tail(2)
first_few_elements, last_few_elements
```

:::

::: {#sol-random-sample}

(for @exr-random-sample)

```{python}
random_sample = activities_series.sample(2, random_state=123)
random_sample
```

:::

<!-- chapter elementwise operations (map) -->

::: {#sol-map-user-ids-to-names}

(for @exr-map-user-ids-to-names)

```{python}
#| echo: false
user_series = pd.Series(
    [42, 22, 1, 42],
    name="User ID"
)
```

```{python}
def user_id_to_names(user_id):
    if user_id == 1:
        return "Carl"
    if user_id == 22:
        return "Barbara"
    if user_id == 42:
        return "Aleks"

user_series.map(user_id_to_names)
```

Note that there are several other ways to solve this exercise. For example, we could have defined `user_id_to_names` using a dictionary.

```{python}
def user_id_to_names(user_id):
    return {1: "Carl", 22: "Barbara", 42: "Aleks"}[user_id]

user_series.map(user_id_to_names)
```

:::

::: {#sol-map-user-ids-to-names-with-lambda}

(for @exr-map-user-ids-to-names-with-lambda)

```{python}
user_series.map(lambda user_id:
    {1: "Carl", 22: "Barbara", 42: "Aleks"}[user_id]
)
```

:::

::: {#sol-map-user-ids-to-names-with-series}

(for @exr-map-user-ids-to-names-with-series)

```{python}
user_id_to_names_series = pd.Series(
    ["Carl", "Barbara", "Aleks"],
    index=[1, 22, 42]
)
user_series.map(user_id_to_names_series)
```

:::

<!-- chapter elementwise operations (arithmetic) -->

::: {#sol-map-minutes-to-cost-with-operators}

(for @exr-map-minutes-to-cost-with-operators)

```{python}
#| echo: false
durations_series = pd.Series(
    [60, 210, 120, 45],
    name="Duration in Minutes"
)
durations_series
activities_series = pd.Series(
    ["run", "hike", "bike", "run"],
    name="Activity Type"
)
```

```{python}
5 * (durations_series + 15) / 60
```

As we might have expected, `*` and `/` have a higher precedence than `+` and `-` also when series are involved. This is why we use parentheses when adding 15 minutes to the durations.
:::

::: {#sol-add-preparation-time-to-durations-using-plus-operator}

(for @exr-add-preparation-time-to-durations-using-plus-operator)

```{python}
activities_series = pd.Series(
    ["run", "hike", "bike", "run"],
    name="Activity Type"
)

durations_series + activities_series.map({
    "run": 15, "hike": 20, "bike": 20
})
```

In the solution above, we map the activity types to their corresponding preparation durations using a dictionary. The obtained preparation times are then added to the activity durations.
:::

<!-- chapter elementwise operations (relational) -->

::: {#sol-inequality-operation-with-two-series}

(for @exr-inequality-operation-with-two-series)

```{python}
#| echo: false
durations_series = pd.Series(
    [60, 210, 120, 45],
    name="Duration in Minutes"
)
durations_series
activities_series = pd.Series(
    ["run", "hike", "bike", "run"],
    name="Activity Type"
)
```

```{python}
durations_series >= activities_series.map({
    "run": 60, "hike": 180, "bike": 180
})
```

The first two activities (60 minutes of running and three and a half hours of hiking) are long. Hence, the first values in the result are `True`. The other activities (two hours of cycling and 45 minutes of running) don't qualify as long, so the corresponding values in the result are `False`.

If you have trouble understanding the solution, perform an intermediary step as shown in the following. There, we define a series with the correct threshold for each duration in `durations_series`.

```{python}
threshold_series = activities_series.map({
    "run": 60, "hike": 180, "bike": 180
})

threshold_series
```

In the next step, we compare `durations_series` with these thresholds.

```{python}
durations_series >= threshold_series
```

:::

---

::: {#sol-inequality-operation-with-series-and-scalar}

(for @exr-inequality-operation-with-series-and-scalar)

```{python}
#| echo: false
activities_series = pd.Series(
    ["run", "hike", "bike", "run"],
    name="Activity Type"
)
```

```{python}
activities_series != "run"
```

:::

<!-- chapter elementwise operations (logical) -->

::: {#sol-logical-operators}

(for @exr-logical-operators)

```{python}
#| echo: false
activities_series = pd.Series(
    ["run", "hike", "bike", "run"],
    name="Activity Type"
)
durations_series = pd.Series(
    [60, 210, 120, 45],
    name="Duration in Minutes"
)
```

```{python}
(
    (durations_series >= 60) & (activities_series == "run") |
    (durations_series >= 180) & (activities_series == "hike") |
    (durations_series >= 180) & (activities_series == "bike")
)
```

In this solution, we placed parentheses around each comparison to avoid problems with operator precedence. Note that no parentheses around the logical AND operation are required, as the `&` operator binds more strongly than the OR operator `~` anyway. We have, however, enclosed the whole statement in a pair of parenthes, because this way, we can break the statement across multiple lines without needing to write an explicit line continuation marker.
:::

<!-- chapter elementwise operations (.isin() and .isna()) -->

::: {#sol-isin-operator}

(for @exr-isin-operator)

```{python}
(
    (durations_series >= 60) & (activities_series == "run") |
    (durations_series >= 180) & (activities_series.isin(["hike", "bike"]))
)
```

:::

::: {#sol-isna-notna-operators}

(for @exr-isna-notna-operators)

There are two equivalent solutions for this task with the latter being more elegant. The first solution uses `.isna()` and then inverts the result with `~`.

```{python}
~durations_series.isna()
```

Since finding non-missing values is a frequent task when working with data, Pandas offers a distinct method for it: `.notna()`. With this method, there is no need to invert a Boolean series to achieve the desired result.

```{python}
durations_series.notna()
```

:::

<!-- chapter indexing by label -->

::: {#sol-series-loc-filter-with-list}

(for @exr-series-loc-filter-with-list)

```{python}
#| echo: false
row_series = pd.Series(
    [1, 42, "run", 60],
    index=["Activity ID", "User ID", "Activity Type", "Duration in Minutes"]
)
```

```{python}
labels = [
    label for label in row_series.index
    if label.startswith("Activity")
]
row_series.loc[labels]
```

:::

<!-- chapter indexing by position  -->

::: {#sol-series-iloc-replicate-head}

(for @exr-series-iloc-replicate-head)

```{python}
#| echo: false
durations_series = pd.Series(
    [60, 210, 120, 45],
    name="Duration in Minutes"
)
durations_series
```

There are two equivalent solutions for this task with the latter being more elegant. The first solution uses `.isna()` and then inverts the result with `~`.

```{python}
def head(series, number_of_elements_to_show=5):
    return series.iloc[:number_of_elements_to_show]

head(durations_series, 3)
```

<!-- TODO: mention in a section in this chapter that we can omit start number or end number of a slice if we want the slice to start at the beginning or go till the end of the series, respectively -->

:::

<!-- chapter indexing with Boolean series -->

::: {#sol-series-loc-with-Boolean-series-1-same-series}

(for @exr-series-loc-with-Boolean-series-1-same-series)

```{python}
#| echo: false
durations_series = pd.Series(
    [60, 210, 120, 45],
    name="Duration in Minutes"
)
```

```{python}
durations_series.loc[durations_series >= 60]
```

:::

---

::: {#sol-series-loc-with-Boolean-series-2-different-series}

(for @exr-series-loc-with-Boolean-series-2-different-series)

```{python}
#| echo: false
durations_series = pd.Series(
    [60, 210, 120, 45],
    name="Duration in Minutes"
)
activities_series = pd.Series(
    ["run", "hike", "bike", "run"],
    name="Activity Type"
)
```

```{python}
activities_series.loc[
    durations_series > 60
]
```

:::

---

::: {#sol-series-loc-with-Boolean-series-resulting-from-logical-and}

(for @exr-series-loc-with-Boolean-series-resulting-from-logical-and) To define our Boolean series representing the conditions, we can reuse our code from any of the Solutions [-@sol-inequality-operation-with-two-series], [-@sol-logical-operators], or [-@sol-isin-operator].

```{python}
is_long_activity = durations_series >= activities_series.map({
    "run": 60, "hike": 180, "bike": 180
})

activities_series.loc[is_long_activity]
```

:::

<!-- chapter indexing to set values in a series  -->

::: {#sol-series-indexing-setting-single-value}

(for @exr-series-indexing-setting-single-value)

```{python}
#| echo: false
row_series = pd.Series(
    [1, 42, "run", pd.NA],
    index=["Activity ID", "User ID", "Activity Type", "Duration in Minutes"]
)
```

```{python}
row_series.iloc[3] = 60

row_series
```

:::

::: {#sol-series-indexing-setting-multiple-values-using-labels}

(for @exr-series-indexing-setting-multiple-values-using-labels)

```{python}
#| echo: false
durations_series = pd.Series(
    [60, pd.NA, pd.NA, 45],
    name="Duration in Minutes",
    dtype="Int64"
)
```

```{python}
durations_series.loc[[1, 2]] = [210, 120]

durations_series
```

:::

::: {#sol-series-indexing-setting-multiple-values-using-boolean-series}

(for @exr-series-indexing-setting-multiple-values-using-boolean-series)

```{python}
durations_series.loc[durations_series > 180] = 180

durations_series
```

:::

<!-- chapter aggregation -->

::: {#sol-series-advanced-sum-activity-durations-of-user-42}

(for @exr-series-advanced-sum-activity-durations-of-user-42)

```{python}
#| echo: false
users_series = pd.Series(
    [42, 22, 1, 42],
    name="User ID"
)
```

```{python}
user_42_durations_series = durations_series.loc[
    users_series == 42
]

user_42_durations_series.sum()
```

To achieve a more concise solution, we can skip the assignment of the filtered series to a variable and call the `.sum()` method directly.

```{python}
durations_series.loc[
    users_series == 42
].sum()
```

:::

::: {#sol-series-advanced-sum-activity-durations-of-running}

(for @exr-series-advanced-sum-activity-durations-of-running)

```{python}
#| echo: false
activities_series = pd.Series(
    ["run", "hike", "bike", "run"],
    name="Activity Type"
)
```

```{python}
running_durations_series = durations_series.loc[
    activities_series == "run"
]
running_durations_series.sum()
```

To achieve a more concise solution, we can skip the assignment of the filtered series to a variable and call the `.sum()` method directly.

```{python}
durations_series.loc[
    activities_series == "run"
].sum()
```

:::

::: {#sol-series-advanced-mean-running-duration}

(for @exr-series-advanced-mean-running-duration)

```{python}
durations_series.loc[
    activities_series == "run"
].mean()
```

:::

::: {#sol-series-advanced-max-activity-duration}

(for @exr-series-advanced-max-activity-duration)

```{python}
durations_series.max()
```

:::

::: {#sol-series-advanced-aggregation-all}

(for @exr-series-advanced-aggregation-all)

```{python}
(activities_series.loc[durations_series <= 60] == "run").all()
```

:::

<!-- chapter counting values -->

::: {#sol-series-advanced-sum-boolean-run-activities}

(for @exr-series-advanced-sum-boolean-run-activities)

```{python}
is_run_series = activities_series == "run"
is_run_series.sum()
```

To achieve a more concise solution, we can skip the assignment of the Boolean series to a variable and call the `.sum()` method directly.

```{python}
(activities_series == "run").sum()
```

:::

::: {#sol-series-advanced-proportion-boolean-run-activities}

(for @exr-series-advanced-proportion-boolean-run-activities)

```{python}
(activities_series == "run").sum()
```

:::

::: {#sol-series-advanced-count-activities-per-user-value-counts-absolute}

(for @exr-series-advanced-count-activities-per-user-value-counts-absolute)

```{python}
#| echo: false
users_series = pd.Series(
    [42, 22, 1, 42],
    name="User ID"
)
```

```{python}
users_series.value_counts()
```

:::

::: {#sol-series-advanced-count-activities-per-user-value-counts-relative}

(for @exr-series-advanced-count-activities-per-user-value-counts-relative)

```{python}
activities_series.value_counts(normalize=True)
```

:::

<!-- chapter sorting -->

::: {#sol-series-advanced-sort-and-find-top-3}

(for @exr-series-advanced-sort-and-find-top-3)

```{python}
durations_series.sort_values(ascending=False).iloc[:3]
```

:::

::: {#sol-series-advanced-nlargest-to-find-top-3}

(for @exr-series-advanced-nlargest-to-find-top-3)

```{python}
durations_series.nlargest(3)
```

:::

<!-- chapter changing dtypes -->

::: {#sol-series-advanced-change-dtype}

(for @exr-series-advanced-change-dtype)

```{python}
durations_series = durations_series.astype("Int64")

durations_series
```

:::

<!-- chapter string methods -->

::: {#sol-series-advanced-strings-strip-and-endswith}

(for @exr-series-advanced-strings-strip-and-endswith)

```{python}
activities_series.str.strip().str.endswith("ing")
```

The first part of the solution (i.e., `activities_series.str.strip()`) returns a series of strings on which we can apply the `.endswith()` string method.

:::

::: {#sol-series-advanced-strings-lower-and-strip-and-endswith}

(for @exr-series-advanced-strings-lower-and-strip-and-endswith)

```{python}
activities_series.str.lower().str.strip().str.endswith("ing")
```

:::

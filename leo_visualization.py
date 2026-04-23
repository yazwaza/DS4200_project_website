import pandas as pd
import altair as alt

df = pd.read_csv("cleaned_lung_cancer_data.csv")

# features to compare against pulmonary disease
features = [
    "smoking",
    "smoking_family_history",
    "throat_discomfort",
    "breathing_issue",
    "immune_weakness",
    "stress_immune",
    "exposure_to_pollution",
    "family_history",
    "age",
    "gender"]

# correlations with pulmonary disease
correlations = []
for feature in features:
    corr = df[feature].corr(df["pulmonary_disease_num"])
    correlations.append({
        "feature": feature,
        "correlation": corr})

corr_df = pd.DataFrame(correlations)

# cleaner labels for the chart
label_map = {
    "smoking": "Smoking",
    "smoking_family_history": "Smoking Family History",
    "throat_discomfort": "Throat Discomfort",
    "breathing_issue": "Breathing Issues",
    "immune_weakness": "Immune Weakness",
    "stress_immune": "Stress / Immune",
    "exposure_to_pollution": "Exposure to Pollution",
    "family_history": "Family History",
    "age": "Age",
    "gender": "Gender"}

corr_df["feature_label"] = corr_df["feature"].map(label_map)

# grouping for color
corr_df["feature_type"] = corr_df["feature"].apply(
    lambda x: "Demographic" if x in ["age", "gender"]
    else "Lifestyle / Symptom")

# Sort features from strongest to weakest
corr_df = corr_df.sort_values("correlation", ascending=False)

# hover interaction
hover = alt.selection_point(on="mouseover", fields=["feature_label"], empty="none")

# ranked bar chart
bars = alt.Chart(corr_df).mark_bar(
    cornerRadiusTopRight=4,
    cornerRadiusBottomRight=4).encode(
    x=alt.X(
        "correlation:Q",
        title="Correlation with Pulmonary Disease",
        scale=alt.Scale(domain=[-0.05, 0.5])
    ),
    y=alt.Y(
        "feature_label:N",
        sort="-x",
        title="Indicator"
    ),
    color=alt.condition(
        hover,
        alt.Color(
            "feature_type:N",
            scale=alt.Scale(
                domain=["Lifestyle / Symptom", "Demographic"],
                range=["#4C78A8", "#F58518"]
            ),
            legend=alt.Legend(title="Indicator Type")
        ),
        alt.value("#D3D3D3")
    ),
    tooltip=[
        alt.Tooltip("feature_label:N", title="Indicator"),
        alt.Tooltip("feature_type:N", title="Type"),
        alt.Tooltip("correlation:Q", title="Correlation", format=".3f")]).add_params(
    hover)

# text labels at the end of bars
text = alt.Chart(corr_df).mark_text(
    align="left",
    baseline="middle",
    dx=5,
    fontSize=12).encode(
    x="correlation:Q",
    y=alt.Y("feature_label:N", sort="-x"),
    text=alt.Text("correlation:Q", format=".2f"))

# zero reference line
rule = alt.Chart(pd.DataFrame({"x": [0]})).mark_rule(
    color="black",
    strokeDash=[4, 4]).encode(
    x="x:Q")

# combine chart pieces
chart = (rule + bars + text).properties(
    width=700,
    height=420,
    title={
        "text": "Indicators Most Associated with Pulmonary Disease",
        "subtitle": [
            "Smoking and symptom-related factors show stronger relationships than age or gender"]})

# style chart
chart = chart.configure_axis(
    labelFontSize=12,
    titleFontSize=13).configure_title(
    fontSize=18,
    subtitleFontSize=12,
    anchor="start").configure_view(
    stroke=None)

# save chart as html for website embedding
chart.save("top_indicators_chart.html")
print("Chart saved as top_indicators_chart.html")

chart
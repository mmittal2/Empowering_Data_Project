# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util


# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell175.csv")


# Provide context

# Population
print("Nepal (South Asia), Rwanda (East Africa), Timor-Leste (Southeast Asia), and Maldives (South Asia) are four countries with a combined population of 46,872,890 people (~ 46.9 million people).")
print("Of this population, 22,781,934 people (~ 22.8 million people) - which equals 48.6 percent of the population - are women.\n")
# Education laws
print("These countries have education laws to ensure that all children receive proper educaiton. The education laws for each country are listed below:")
print("\t - Nepal: 8 years of free basic education for all children")
print("\t - Rwanda: free education for all children until 12th grade")
print("\t - Timor-Leste: free primary school education for women")
print("\t - Maldives: children between 4 to 16 years of age are required to attend school\n")
# Education reality (average years of schooling)
print("Surprisingly, though, many women fail to receive proper education. Below is the average number of years of schooling for women in each of these four countries (as of 2021):")
print("\t - Nepal: 4.161 years")
print("\t - Rwanda: 4.031 years")
print("\t - Timor-Leste: 4.742 years")
print("\t - Maldives: 7.120 years\n")
# Connection to health care
print("Unfortunately, this lack of proper education is impacting women's decision making power when it comes to health care.\n\n")


input("Press enter to continue.\n\n")


# Findings from graph
print("The \"Well-being of Women in 52 Countries\" dataset shows a strong positive correlation between female average/median years of schooling and percentage of women who have the final say on their health care in these four countries (Nepal, Rwanda, Timor-Leste, and Maldives). This shows that increasing the years of schooling women receive causes an increase in the number of women who have the power to make decisions about their health care.")


# Ask the research question
print("Since health care is a very important part of women's lives, this is a critical issue that needs to be addressed.\n")
print("Therefore, I want to pose the following research question:")
print("What are the most important reasons why the number of years of schooling women receive affects their final say on health care and what measures can be taken to increase women’s access to education so that they gain more power to make decisions about their health care?")


# Display the graph

# function to get data for one country
def get_country_data(country_name):
  country_boolean_list = lwd["country_name"] == country_name
  country_data = lwd.loc[country_boolean_list]
  return country_data

# specify country one
country_one = "Nepal"
country_one_data = get_country_data(country_one)

# specify country two
country_two = "Rwanda"
country_two_data = get_country_data(country_two)

# specifiy country three
country_three = "Timor-Leste"
country_three_data = get_country_data(country_three)

# specifiy country four
country_four = "Maldives"
country_four_data = get_country_data(country_four)

# plot the data using scatterplots
plt.scatter(x="ED_educ_years_mean",
            y="DP_decide_health_p",
            data=country_one_data,
            color="red")
plt.scatter(x="ED_educ_years_mean",
            y="DP_decide_health_p",
            data=country_two_data,
            color="orange")
plt.scatter(x="ED_educ_years_mean",
            y="DP_decide_health_p",
            data=country_three_data,
            color="yellow")
plt.scatter(x="ED_educ_years_mean",
            y="DP_decide_health_p",
            data=country_four_data,
            color="magenta")

plt.xlabel("Female average/median years of schooling")
plt.ylabel("Women who have the final say on their health care (%)")
plt.title("Education's Effect on Health Care Decision Power")

plt.legend([country_one, country_two, country_three, country_four])

plt.show()

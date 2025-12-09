#Complete Data Analysis Project: student performance and create a full analysis with at least 2 different types of charts and written insights
import matplotlib.pyplot as plt
import pandas as pd
data={
    "Students": ["Ram","Sita","Gita","Rani","Sweta","Arena","Joy","Reshu","Ayuu","rahul","Sonu","titu","Sweety"],
    "physics": [56, 55, 47, 34, 59, 60, 23, 98, 76, 56, 88, 67, 71],
    "Chemistry":[82, 80, 58, 87, 60, 90, 70, 92, 66, 90, 77, 42, 34],
    "Maths":[45, 23, 49, 75, 89, 65, 85, 62, 91, 78, 94, 90, 55]
}
df= pd.DataFrame(data)
print("Student Performance Data")
print(df,"\n")

#Calculate Total
df["total"]= df["physics"] + df["Chemistry"] + df["Maths"]
print("Students have Gain \n ",df["total"])
#Calculate Average
subject_avg= df[["physics","Chemistry","Maths"]].mean()
print("Mean of the subjects \n ", subject_avg)

#bar chart for Avg subjects 
plt.bar(subject_avg.index, subject_avg.values, color="yellow")
plt.title("Average of Subjects gain by Students")
plt.xlabel("Subject")
plt.ylabel("Average")
plt.grid()
plt.show()

#Line chart for Total marks of students 
plt.plot(df["Students"], df["total"], marker= "o" , color= "blue")
plt.grid()
plt.title("Total Marks of the Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.show()

#print Insights
print("\nINSIGHTS:")
print("1. Best subject:", subject_avg.idxmax())
print("2. Weakest subject:", subject_avg.idxmin())
print("3. Highest scoring student:", df.loc[df['total'].idxmax(), 'Students'])
print("4. Lowest scoring student:", df.loc[df['total'].idxmin(), 'Students'])


# ACME Excercise
Solution to the problem raised by the Ioet company
<h1>Solution Description</h1>

<p>
  <ul>
    <li>It started by reading the file containing the company data</li>
    <li>The data was organized in such a way that it is ordered in dictionaries using the keys: employee, day_entry and day_departure</li>
    <li>Organized information was saved in a list</li>
    <li>To get to the solution:</li>
    <ol value="1">
      <li>The comparison was made to ensure that the days match</li>
      <li>Coincided that the entry time of the first employee is less than the exit time of the second employee and the entry time of the second employee is less than               the exit time of the first employee</li>
      <li>When the coincidences were fulfilled, the number of coincidences is carried out</li>
    </ol>
    <li>Finally, the solution is presented as required.</li>
    </ul>
</p>

<h1>Architecture Explained</h1>
<p>
  To carry out the program, a structured design architecture was used, with the purpose of facilitating the resolution of the problem.
  issue. The problem was divided into 4 modules:
  <li>Reading the data file</li>
  <li>Treatment and organization of data</li>
  <li>Calculation and resolution of the problem</li>
  <li>Sample results</li>
</p>

<h1>Explanation of the approach and methodology</h1>
<h3>Approach</h3>
<p>
  To solve the problem posed, a porototyping approach was taken into account to be able to evaluate the behavior of the solution in several stages.
</p>
<img src="/image/PrototypeModel.jpg">
<h3>Methodology</h3>
<p>
  The Kanban methodology was taken as a basis. The development was divided into small daily tasks. Tests were carried out to validate the completion of the stage and     to be able to continue with the next task.
</p>
<h1>Instructions for running the program locally</h1>
<p>
  <ol>
    <li>You must have <code>Python 3.9.X</code> installed</li>
    <li>You need to clone or download the project from <a href=https://github.com/jeffersoncaicedo/acme_exercise>GitHub</a></li>
    <li>You can open the EmployeesCoincidence.py file from your preferred IDE or run it from the console</li>
    <ul>
      <li>Execute the following command to run the program: <code>python EmployeesCoincidence.py data\data1.txt</code></li>
    <ul>
  </ol>
      <p><b>Note</b>: If you need to use other data you can modify the <code>data1.txt</code> file or change it to a <code>.txt</code> file of your choice</p>
</p>
  

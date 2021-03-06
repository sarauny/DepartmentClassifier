# Department Classifier

### The project work out was done in jupyter notebook (.ipynb). Detailed steps are given along the notebook.

### 1) How did you approach the problem  

> I have decided to simply match each normalized and stemmed words within job titles with ones from the departmental job scopes. For example, a job title called "senior manager operations" becomes "op" after pre-processing steps above. Since "op" could be found on the table of keywords under "Management" department, this job title belongs to "Management". With this approach alone, a sensitivity of ~73% was achieved - 61393 of 84577 job titles were successfully assigned with at least 1 department.

> To achieve higher capture rate (sensitivity), a new keywords table is created based on the existing matching result. Each keyword in a job title was assignment with all departments previously assigned to the job title. For example, a job title called "senior analyst" becomes "analyst" after the previous pre-processing steps. However, analyst itself doesn't allow assignment of any department, although his/her job scope can be quite general and able to work in many departments. For instance, job titles as "financial analyst" and "operation analyst" may get assigned with "Finance" and "Management" departments, respectively. By leveraging the existing departmental assignment (previous Step 1 output as current input - a cascading approach), the new keywords table combines both "Finance" and "Management" departments for the job title keyword of "analyst". To avoid unspecific departmental assignment to unrelevant job titles, only those job titles without any departmental assignment from Step 1 and those job titles with only single keyword left after the pre-processing steps are further processed with following Step 2.

> From this cascading approach, we now have 70581 of 84577 (83%) job titles successfully assigned with at least 1 department.

### 2) Why did you choose this method/algorithms. Please describe about your epochs,activation function and other metrics if used

> Simple keyword matching approach with some NLTK tools seems to work the best because of the small number of words within the job title data (Author's perspective). I adopted cascading approach by using the outputs of the previous steps as the inputs for the rematching jobs to increase the sensitivity.

### 3) What is your accuracy, how did you calculated and what are the future works needs to be done to improve it.
> A total of 100 samples were sampled randomly from the results (attached 'Results_randomSampling100.xls'). Of the 100 samples/job titles, 84 (84%) job titles were successfully assigned with at least 1 department. The accuracy was evaluated in high stringency - if there is at least one department assigned inappropriately, the assignment job will be considered wrong. The accuracy calculated on the 84 samples was 49%.

> Future works to be done could be:-  
    - There are other data cleaning or pre-processing can be attempted to improve performance. For example (based on the 'Results_randomSampling100.xls'), there are many abbreviations/shortform used in the job titles, eg. UX, UI, HR, R&D and IT that can be replaced with proper phrase (user experience, user interface, Human Resources, Research & Development, and Information Technology, respectively) as part of the preprocessing job. Obvious junk, eg. "gfjgkjfg", can also be removed.  
    - To increase specificity/accuracy (but lower sensivity/capture rate), we can adopt and compare less stringent stemming method, eg. SnowballStemmer or PorterStemmer. For example, the word of "operation" can be stemmed with different levels - "op" with LancasterStemmer in this study and "operat" with SnowballStemmer. If computation resources allow, we may combine less stringent and stringent approach to list the more specific results by SnowballStemmer, followed by less specific results by LancasterStemmer.

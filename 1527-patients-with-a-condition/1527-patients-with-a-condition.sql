# Write your MySQL query statement below
Select patient_id, patient_name, conditions
From Patients
Where conditions Like 'DIAB1%' Or conditions Like '% DIAB1%';
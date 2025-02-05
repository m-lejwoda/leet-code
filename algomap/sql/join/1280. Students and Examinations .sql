# Write your MySQL query statement below
Select s.student_id, s.student_name, sb.subject_name, ifnull(count(e.student_id),0) as attended_exams
from Students s cross join Subjects sb
left join examinations e
on e.student_id = s.student_id and e.subject_name = sb.subject_name
group by student_id, student_name, subject_name
order by student_id, subject_name
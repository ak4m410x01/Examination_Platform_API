# Examination System:

## Analysis Requirements document:

1. The system has a number of administrators each administrator has id, name(first name, second name, third name, fourth name),email, phones, gender, birth of date, age, location(country, city, address), image, joined_at.
2. The system has a number of instructors each instructor has id, name(first name, second name, third name, fourth name), email, phones, gender, birth of date, age, location(country, city, address), specialized_in, image, joined_at.
3. The system has a number of students each student has id, name(first name, second name, third name, fourth name), email, phones, gender, birth of date, age, location(country, city, address), image, joined_at.
4. The system has a number of levels each level has id.
5. The system has a number of courses each course has id, code, title, description, duration.
6. The system has a number of exams each exam has id, start at, end at, score.
7. The system has a number of questions each question has id, description.
8. The system has a number of choices each choice has id, description.
9. The system has a number of scores each score has id, score.
10. The system has a number of departments each department has id, name.
11. The system has a number of containers each container has id, identifier, ssh_port, ip_address, status.
12. The system has a number of logins each login has id, username, password, last_login, is_active.

---

12. Each instructor teach many course but course is teached by one instructor.
13. Each instructor set many exams but exam set by only one instructor.
14. Each student take many course and course is taken by many students.
15. Each student belong only one level and each level may be contain many students.
16. Each level contain number of courses but each course belong one level.
17. Each level belong one department but department may be contain many levels.
18. Each course contain number of exams but each exam belong one course.
19. Each exams contain number of questions and each question may belong zero or more exam.
20. Each question contain number of chioces and only one of them is true and each chioce may be any number of questions.

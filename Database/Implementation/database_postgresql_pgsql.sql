-- Active: 1703545083230@@127.0.0.1@5432@postgres@public
-- Administrators
-- administrator entity
CREATE TABLE IF NOT EXISTS "administrators" (
    "id" SERIAL PRIMARY KEY NOT NULL,
    "first_name" VARCHAR(30) NOT NULL,
    "second_name" VARCHAR(30) NOT NULL,
    "third_name" VARCHAR(30) NOT NULL,
    "fourth_name" VARCHAR(30) NOT NULL,
    "date_of_birth" DATE NOT NULL,
    "gender" CHAR(1) NOT NULL CHECK(gender IN ('M', 'F')),
    "country" VARCHAR(30) NOT NULL,
    "city" VARCHAR(30) NOT NULL,
    "address" VARCHAR(40),
    "email" VARCHAR(50),
    "image" VARCHAR,
    "joined_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- multivalued_attribute
CREATE TABLE IF NOT EXISTS "administrators_phones" (
    -- (administrator_id, phone_number) => Composite Primary Key
    "administrator_id" INTEGER NOT NULL,
    "phone_number" VARCHAR(20) NOT NULL,
    PRIMARY KEY ("administrator_id", "phone_number")
);

-- one-to-one relationship [logins]
CREATE TABLE IF NOT EXISTS "administrators_logins" (
    "administrator_id" INTEGER PRIMARY KEY NOT NULL,
    "login_id" INTEGER NOT NULL
);

-- ========================================================
-- Students
CREATE TABLE IF NOT EXISTS "students" (
    "id" SERIAL PRIMARY KEY NOT NULL,
    "first_name" VARCHAR(30) NOT NULL,
    "second_name" VARCHAR(30) NOT NULL,
    "third_name" VARCHAR(30) NOT NULL,
    "fourth_name" VARCHAR(30) NOT NULL,
    "date_of_birth" DATE NOT NULL,
    "gender" CHAR(1) NOT NULL CHECK(gender IN ('M', 'F')),
    "country" VARCHAR(30) NOT NULL,
    "city" VARCHAR(30) NOT NULL,
    "address" VARCHAR(40) NOT NULL,
    "email" VARCHAR(50) NOT NULL,
    "image" VARCHAR NOT NULL,
    "joined_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- one-to-many relationship [levels]
    "level_id" INTEGER NOT NULL,
    "grade" DECIMAL(1, 2) NOT NULL,
    -- one-to-many relationship [departments]
    "department_id" INTEGER NOT NULL
);

-- multivalued_attribute
CREATE TABLE IF NOT EXISTS "students_phones" (
    --  (student_id, phone_number) => Composite Key
    "student_id" INTEGER NOT NULL,
    "phone_number" VARCHAR(20) NOT NULL,
    PRIMARY KEY ("student_id", "phone_number")
);

--  one-to-one relationship [logins]
CREATE TABLE IF NOT EXISTS "students_logins" (
    "student_id" INTEGER PRIMARY KEY NOT NULL,
    "login_id" INTEGER NOT NULL
);

--  many-to-many relationship [courses]
CREATE TABLE IF NOT EXISTS "students_courses" (
    --  (student_id, course_id) => Composite Key
    "student_id" INTEGER NOT NULL,
    "course_id" INTEGER NOT NULL,
    PRIMARY KEY ("student_id", "course_id")
);

--  many-to-many relationship [exams]
CREATE TABLE IF NOT EXISTS "students_exams" (
    --  (student_id, exam_id) => Composite Key
    "student_id" INTEGER NOT NULL,
    "exam_id" INTEGER NOT NULL,
    "score" INTEGER NOT NULL,
    PRIMARY KEY ("student_id", "exam_id")
);

--  ========================================================
--  Instructors
--  instructor entity
CREATE TABLE IF NOT EXISTS "instructors" (
    "id" SERIAL PRIMARY KEY NOT NULL,
    "first_name" VARCHAR(30) NOT NULL,
    "second_name" VARCHAR(30) NOT NULL,
    "third_name" VARCHAR(30) NOT NULL,
    "fourth_name" VARCHAR(30) NOT NULL,
    "date_of_birth" DATE NOT NULL,
    "gender" CHAR(1) NOT NULL CHECK(gender IN ('M', 'F')),
    "country" VARCHAR(30) NOT NULL,
    "city" VARCHAR(30) NOT NULL,
    "address" VARCHAR(40) NOT NULL,
    "email" VARCHAR(50) NOT NULL,
    "image" VARCHAR NOT NULL,
    "joined_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "specialized_in" VARCHAR(50) NOT NULL
);

--  multivalued-attribute
CREATE TABLE IF NOT EXISTS "instructors_phones" (
    --  (instructor_id, phone_number) => Composite Key
    "instructor_id" INTEGER NOT NULL,
    "phone_number" VARCHAR(20) NOT NULL,
    PRIMARY KEY ("instructor_id", "phone_number")
);

--  one-to-one relationship [logins]
CREATE TABLE IF NOT EXISTS "instructors_logins" (
    "instructor_id" INTEGER PRIMARY KEY NOT NULL,
    "login_id" INTEGER NOT NULL
);

--  ========================================================
--  Levels
--  level entity
CREATE TABLE IF NOT EXISTS "levels" (
    "id" INTEGER PRIMARY KEY NOT NULL,
    --  one-to-many relationship [departments]
    "department_id" INTEGER NOT NULL
);

--  ========================================================
--  Departments
--  department entity
CREATE TABLE IF NOT EXISTS "departments" (
    "id" SERIAL PRIMARY KEY NOT NULL,
    "name" VARCHAR(30) NOT NULL
);

--  ========================================================
--  Courses
--  course entity
CREATE TABLE IF NOT EXISTS "courses" (
    "id" SERIAL PRIMARY KEY NOT NULL,
    "code" VARCHAR(10) NOT NULL,
    "title" VARCHAR(30) NOT NULL,
    "description" VARCHAR(30000) NOT NULL,
    "duration" INTEGER NOT NULL,
    --  one-to-many relationship [instructors]
    "instructor_id" INTEGER NOT NULL,
    --  one-to-many relationship [levels]
    "level_id" INTEGER NOT NULL
);

--  ========================================================
--  Exams
--  exam entity
CREATE TABLE IF NOT EXISTS "exams" (
    "id" SERIAL PRIMARY KEY NOT NULL,
    "start_at" TIMESTAMP NOT NULL,
    "end_at" TIMESTAMP NOT NULL,
    "score" INTEGER NOT NULL,
    --  one-to-many relationship [courses]
    "course_id" INTEGER NOT NULL
);

--  many-to-many relationship [questions]
CREATE TABLE IF NOT EXISTS "exams_quuestions" (
    --  (exam_id, question_id) => Composite Key
    "exam_id" INTEGER NOT NULL,
    "question_id" INTEGER NOT NULL,
    PRIMARY KEY ("exam_id", "question_id")
);

--  ========================================================
--  Questions
--  question entity
CREATE TABLE IF NOT EXISTS "questions" (
    "id" SERIAL PRIMARY KEY NOT NULL,
    "description" VARCHAR(10000)
);

--  many-to-many relationship [choices]
CREATE TABLE IF NOT EXISTS "questions_choices" (
    --  (question_id, choice_id) => Composite Key
    "question_id" INTEGER NOT NULL,
    "choice_id" INTEGER NOT NULL,
    "is_right" BOOLEAN NOT NULL,
    PRIMARY KEY ("question_id", "choice_id")
);

-- ========================================================
-- Choices
--  choice entity
CREATE TABLE IF NOT EXISTS "choices" (
    "id" SERIAL PRIMARY KEY NOT NULL,
    "description" VARCHAR(10000) NOT NULL
);

-- ========================================================
-- Containers
--  container entity
CREATE TABLE IF NOT EXISTS "containers" (
    "id" SERIAL PRIMARY KEY NOT NULL,
    "identifier" VARCHAR(30) NOT NULL,
    "ip_address" VARCHAR(16) NOT NULL,
    "ssh_port" INTEGER NOT NULL,
    "status" VARCHAR(10) NOT NULL
);

--  one-to-one relationship [logins]
CREATE TABLE IF NOT EXISTS "containers_logins" (
    "container_id" INTEGER PRIMARY KEY NOT NULL,
    "login_id" INTEGER NOT NULL
);

-- ========================================================
-- Logins
--  login entity
CREATE TABLE IF NOT EXISTS "logins" (
    "id" SERIAL PRIMARY KEY NOT NULL,
    "username" VARCHAR(1000) UNIQUE NOT NULL,
    "password" VARCHAR(100) NOT NULL,
    "last_login" TIMESTAMP NULL,
    "is_active" BOOLEAN NOT NULL
);

ALTER TABLE
    "administrators_phones"
ADD
    FOREIGN KEY ("administrator_id") REFERENCES "administrators" ("id");

ALTER TABLE
    "administrators_logins"
ADD
    FOREIGN KEY ("administrator_id") REFERENCES "administrators" ("id");

ALTER TABLE
    "administrators_logins"
ADD
    FOREIGN KEY ("login_id") REFERENCES "logins" ("id");

ALTER TABLE
    "students"
ADD
    FOREIGN KEY ("level_id") REFERENCES "levels" ("id");

ALTER TABLE
    "students"
ADD
    FOREIGN KEY ("department_id") REFERENCES "departments" ("id");

ALTER TABLE
    "students_phones"
ADD
    FOREIGN KEY ("student_id") REFERENCES "students" ("id");

ALTER TABLE
    "students_logins"
ADD
    FOREIGN KEY ("student_id") REFERENCES "students" ("id");

ALTER TABLE
    "students_logins"
ADD
    FOREIGN KEY ("login_id") REFERENCES "logins" ("id");

ALTER TABLE
    "students_courses"
ADD
    FOREIGN KEY ("student_id") REFERENCES "students" ("id");

ALTER TABLE
    "students_courses"
ADD
    FOREIGN KEY ("course_id") REFERENCES "courses" ("id");

ALTER TABLE
    "students_exams"
ADD
    FOREIGN KEY ("student_id") REFERENCES "students" ("id");

ALTER TABLE
    "students_exams"
ADD
    FOREIGN KEY ("exam_id") REFERENCES "exams" ("id");

ALTER TABLE
    "instructors_phones"
ADD
    FOREIGN KEY ("instructor_id") REFERENCES "instructors" ("id");

ALTER TABLE
    "instructors_logins"
ADD
    FOREIGN KEY ("instructor_id") REFERENCES "instructors" ("id");

ALTER TABLE
    "instructors_logins"
ADD
    FOREIGN KEY ("login_id") REFERENCES "logins" ("id");

ALTER TABLE
    "levels"
ADD
    FOREIGN KEY ("department_id") REFERENCES "departments" ("id");

ALTER TABLE
    "courses"
ADD
    FOREIGN KEY ("instructor_id") REFERENCES "instructors" ("id");

ALTER TABLE
    "courses"
ADD
    FOREIGN KEY ("level_id") REFERENCES "levels" ("id");

ALTER TABLE
    "exams"
ADD
    FOREIGN KEY ("course_id") REFERENCES "courses" ("id");

ALTER TABLE
    "exams_quuestions"
ADD
    FOREIGN KEY ("exam_id") REFERENCES "exams" ("id");

ALTER TABLE
    "exams_quuestions"
ADD
    FOREIGN KEY ("question_id") REFERENCES "questions" ("id");

ALTER TABLE
    "questions_choices"
ADD
    FOREIGN KEY ("question_id") REFERENCES "questions" ("id");

ALTER TABLE
    "questions_choices"
ADD
    FOREIGN KEY ("choice_id") REFERENCES "choices" ("id");

ALTER TABLE
    "containers_logins"
ADD
    FOREIGN KEY ("container_id") REFERENCES "containers" ("id");

ALTER TABLE
    "containers_logins"
ADD
    FOREIGN KEY ("login_id") REFERENCES "logins" ("id");
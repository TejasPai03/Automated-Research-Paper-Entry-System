USE phd_papers;

/* Table containing the department names and their associated department Numbers, which is unique for each dept */
CREATE TABLE department(
	dname VARCHAR(30),
	dno INT PRIMARY KEY
);

/* Table containing the details of the students, who have a unique University Serial Number (USN) */
CREATE TABLE student (
    name VARCHAR(20),
    usn VARCHAR(12) PRIMARY KEY,
    email VARCHAR(30),
    phone VARCHAR(20),
    gender CHAR,
    dno INT,
    FOREIGN KEY(dno) REFERENCES department(dno)
);

CREATE TABLE is_captain(
	usn VARCHAR(12),
    dno INT,
    FOREIGN KEY(dno) REFERENCES department(dno),
    FOREIGN KEY(usn) REFERENCES student(usn)
);

CREATE TABLE research_papers(
	usn VARCHAR(12),
	paper_id INT PRIMARY KEY,
	title VARCHAR(50),
	author VARCHAR(30),
	conference VARCHAR(30),
	journal VARCHAR(30),
    date DATE,
	doi VARCHAR(30),
	FOREIGN KEY(usn) REFERENCES student(usn)
);

CREATE TABLE writes(
	usn VARCHAR(12),
    paper_id INT,
    FOREIGN KEY(usn) REFERENCES student(usn),
    FOREIGN KEY(paper_id) REFERENCES research_papers(paper_id) ON DELETE CASCADE
);

/* Inserting sample values */

INSERT INTO department VALUES('CCE', 1);
INSERT INTO department VALUES('CSE', 2);
INSERT INTO department VALUES('ISE', 3);
INSERT INTO department VALUES('AIML', 4);
INSERT INTO department VALUES('ECE', 5);
INSERT INTO department VALUES('EEE', 6);

INSERT INTO student VALUES('ram', '4nm21cm001', 'ram@nmamit.in', '9988776655', 'M', 1);
INSERT INTO student VALUES('john', '4nm21cm002', 'john@nmamit.in', '8877996655', 'M', 1);
INSERT INTO student VALUES('geeta', '4nm21cs001', 'geeta@nmamit.in', '7799227766', 'F', 2);
INSERT INTO student VALUES('bashir', '4nm21cs002', 'bashir@nmamit.in', '9900776655', 'M', 2);
INSERT INTO student VALUES('joseph', '4nm21is001', 'joseph@nmamit.in', '8877661139', 'M', 3);
INSERT INTO student VALUES('jacob', '4nm21is002', 'jacob@nmamit.in', '7766990164', 'M', 3);
INSERT INTO student VALUES('rajesh', '4nm21ai001', 'rajesh@nmamit.in', '9483729087', 'M', 4);
INSERT INTO student VALUES('dinesh', '4nm21ai002', 'dinesh@nmamit.in', '8790578943', 'M', 4);
INSERT INTO student VALUES('uwais', '4nm21ec001', 'uwais@nmamit.in', '7789678203', 'M', 5);
INSERT INTO student VALUES('anthony', '4nm21ec002', 'anthony@nmamit.in', '6361879076', 'M', 5);
INSERT INTO student VALUES('ashok', '4nm21ee001', 'ashok@nmamit.in', '8890278364', 'M', 6);
INSERT INTO student VALUES('harish', '4nm21ee002', 'harish@nmamit.in', '8790678456', 'M', 6);

INSERT INTO is_captain VALUES('4nm21cm001', 1);
INSERT INTO is_captain VALUES('4nm21cs002', 2);
INSERT INTO is_captain VALUES('4nm21is002', 3);
INSERT INTO is_captain VALUES('4nm21ai001', 4);
INSERT INTO is_captain VALUES('4nm21ec001', 5);
INSERT INTO is_captain VALUES('4nm21ee001', 6);

SELECT * FROM research_papers
WHERE usn = '4nm21cm001';

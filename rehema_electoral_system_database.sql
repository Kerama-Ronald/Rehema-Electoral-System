-- Create Tables
CREATE TABLE students (
    admission_number TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    grade TEXT,
    FOREIGN KEY (grade) REFERENCES grades (grade)
);

CREATE TABLE contestants (
    contestant_id INTEGER PRIMARY KEY,
    admission_number TEXT,
    position TEXT,
    FOREIGN KEY (admission_number) REFERENCES students (admission_number)
);

CREATE TABLE fees (
    admission_number TEXT PRIMARY KEY,
    balance REAL,
    FOREIGN KEY (admission_number) REFERENCES students (admission_number)
);

CREATE TABLE grades (
    grade TEXT PRIMARY KEY
);

CREATE TABLE posts (
    post_id INTEGER PRIMARY KEY,
    post_name TEXT
);

CREATE TABLE votes_cast (
    vote_id INTEGER PRIMARY KEY,
    admission_number TEXT,
    post_id INTEGER,
    vote_status TEXT,
    FOREIGN KEY (admission_number) REFERENCES students (admission_number),
    FOREIGN KEY (post_id) REFERENCES posts (post_id)
);

CREATE TABLE results (
    result_id INTEGER PRIMARY KEY,
    post_id INTEGER,
    contestant_id INTEGER,
    votes_received INTEGER,
    FOREIGN KEY (post_id) REFERENCES posts (post_id),
    FOREIGN KEY (contestant_id) REFERENCES contestants (contestant_id)
);

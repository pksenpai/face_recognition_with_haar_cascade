/* create database */
CREATE DATABASE face_recognition;

/* connect to database */
\c face_recognition;

/* create table */
CREATE TABLE faces (
    id SERIAL PRIMARY KEY,
    face_name VARCHAR(100) NOT NULL,
    face_path text NOT NULL UNIQUE,
    register_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

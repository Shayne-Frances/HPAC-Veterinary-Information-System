CREATE DATABASE hpacdb;




CREATE TABLE stafftb (
	Name VARCHAR(50),
	Position VARCHAR(50),
	Staff_ID INT AUTO_INCREMENT PRIMARY KEY,
	PRC_LN VARCHAR(20),
	Contact_Number VARCHAR(11), 
	Date_Hired DATE, Status VARCHAR(20)
);

SELECT* FROM stafftb;

ALTER TABLE stafftb
	RENAME COLUMN `Name` TO `First_Name`;
	
ALTER TABLE stafftb
	ADD COLUMN Last_Name VARCHAR (50) AFTER First_Name;

ALTER TABLE stafftb 
	MODIFY COLUMN PRC_LN VARCHAR(20) AFTER Position; 
	
ALTER TABLE stafftb
	MODIFY COLUMN Staff_ID VARCHAR(15) PRIMARY KEY;

DESC stafftb;

ALTER TABLE stafftb
DROP PRIMARY KEY;

DELETE FROM stafftb WHERE Staff_ID = "ST-0001";



CREATE TABLE clientb (
	Name VARCHAR(50),
	Client_ID INT AUTO_INCREMENT PRIMARY KEY,
	Contact_Number VARCHAR(11),
	Address VARCHAR(50),
	Patients VARCHAR(100) 
);

ALTER TABLE clientb
	RENAME COLUMN `Name` TO `First_Name`;
	
ALTER TABLE clientb
	ADD COLUMN Last_Name VARCHAR (50) AFTER First_Name;

ALTER TABLE clientb
	ADD COLUMN Status VARCHAR (20);
	
ALTER TABLE clientb
	DROP COLUMN Patients;
	
ALTER TABLE clientb
	MODIFY COLUMN Address VARCHAR(100);

ALTER TABLE clientb
	MODIFY COLUMN Client_ID VARCHAR(15);

DELETE FROM clientb WHERE Client_ID = 'ST-0002';
	
SELECT* FROM clientb;

DESC clientb;



CREATE TABLE patienttb (
	Name VARCHAR(50),
	Patient_ID INT AUTO_INCREMENT PRIMARY KEY,
	OWNER VARCHAR (50),
	Species VARCHAR(100),
	Breed VARCHAR(100),
	Birthdate DATE
);

SELECT* FROM patienttb;

ALTER TABLE patienttb 
	ADD COLUMN Status VARCHAR (20);
	
ALTER TABLE patienttb
	RENAME COLUMN `NAME` TO `Name`,
	RENAME COLUMN `OWNER` TO `Owner`;

ALTER TABLE patienttb
	RENAME COLUMN `NAME` TO `Name`,
	RENAME COLUMN `OWNER` TO `Owner`;

ALTER TABLE patienttb
	ADD COLUMN Sex VARCHAR (15) AFTER Birthdate;

ALTER TABLE patienttb
	MODIFY COLUMN Patient_ID VARCHAR(15);

ALTER TABLE patienttb
	MODIFY COLUMN Patient_ID VARCHAR (15) AFTER OWNER;
	
ALTER TABLE patienttb
	MODIFY COLUMN Breed VARCHAR (30);

DELETE FROM patienttb WHERE Patient_ID = 'ST-0001';

ALTER TABLE patienttb
	RENAME COLUMN `Birthdate` TO `Birthdate (yyyy-MM-dd)`;

ALTER TABLE patienttb
	RENAME COLUMN `Birthdate (yyyy-MM-dd)` TO `Birthdate`;

DESC patienttb;

SELECT * FROM patienttb; 



CREATE TABLE inventorytb (
	Name VARCHAR(50),
	TYPE VARCHAR(20),
	Quantity INT,
	Unit VARCHAR(10),
	Stock INT,
	Price INT
);

SELECT* FROM inventorytb;

ALTER TABLE inventorytb
	RENAME COLUMN `NAME` TO `Name`;

ALTER TABLE inventorytb
	RENAME COLUMN `TYPE` TO `Type`;

ALTER TABLE inventorytb
	RENAME COLUMN `Price` TO `Price(₱)`;

ALTER TABLE inventorytb
	MODIFY COLUMN TYPE VARCHAR(20) AFTER Name;

ALTER TABLE inventorytb
	MODIFY COLUMN inventory_id VARCHAR (15);

ALTER TABLE inventorytb
	RENAME COLUMN `Price(₱)` TO `Price(PHP)`;

ALTER TABLE inventorytb
	RENAME COLUMN `inventory_id` TO `Inventory ID`;

ALTER TABLE inventorytb
	RENAME COLUMN `Inventory ID` TO `Inventory_ID`;

DELETE FROM inventorytb WHERE Inventory_ID = "IV-0001";

DESC inventorytb;
	



CREATE TABLE suppliertb (
	Name VARCHAR(50),
	Company VARCHAR(50),
	Contact_Number VARCHAR(11),
	Notes VARCHAR(50)
);

ALTER TABLE suppliertb
	RENAME COLUMN `Name` TO `First_Name`;
	
ALTER TABLE suppliertb
	ADD COLUMN Last_Name VARCHAR (50) AFTER First_Name;

ALTER TABLE suppliertb
	MODIFY COLUMN Supplier_ID VARCHAR (15);
	
SELECT* FROM suppliertb;

DELETE FROM suppliertb WHERE Supplier_ID = "SP-0001";

DESC suppliertb;

ALTER TABLE suppliertb
	MODIFY COLUMN Supplier_ID VARCHAR (15);
	
ALTER TABLE suppliertb
	MODIFY COLUMN Notes TEXT;



INSERT INTO stafftb (Name, Position, Staff_ID, PRC_LN, Contact_Number, Date_Hired, Status)
	VALUES("Susan P. Ocay", "Owner, Secretary", NULL, NULL, "09423638171", "2020-06-12", "Active"), ("Shanine Florence P. Ocay", "Doctor", NULL, NULL, "09423638171", "2020-06-12", "Active");

	



DELETE FROM stafftb WHERE Staff_ID = 4;


SELECT* FROM patienttb;




	
ALTER TABLE inventorytb
	ADD COLUMN Inventory_ID INT AUTO_INCREMENT PRIMARY KEY AFTER Name;

	
SELECT* FROM inventorytb;


ALTER TABLE suppliertb
	ADD COLUMN Supplier_ID INT AUTO_INCREMENT PRIMARY KEY AFTER Name;

	
SELECT* FROM suppliertb;

USE hpacdb;

desc stafftb;

DROP TABLE student_table;

DROP TABLE staff;

SELECT NAME, patient_id, patienttb.owner FROM patienttb JOIN clientb ON clientb.First_Name=patienttb.`Owner`;
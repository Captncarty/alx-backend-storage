-- Creates a function SafeDiv that divides (and returns)
-- the first by the second number or returns 0
-- if the second number is equal to 0.

-- Change the delimiter to $$
DELIMITER $$
-- Create the view need_meeting
CREATE VIEW need_meeting AS
SELECT student_name
FROM students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
$$
-- Reset the delimiter back to ;
DELIMITER ;

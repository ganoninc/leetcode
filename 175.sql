SELECT p.lastName, p.firstName, city, state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;
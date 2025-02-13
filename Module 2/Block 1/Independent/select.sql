USE Students;
GO

SELECT
    lstStud.FullName,
    lstStud.Course,
    specStud.SpecName,
    lstStud.BirthDate
FROM
    lstStud
JOIN
    specStud ON lstStud.SpecID = specStud.SpecID;
-- Create table
CREATE TABLE Movies (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(255) NOT NULL,
    release_date DATE,
    popularity DECIMAL(10,2)
);
GO

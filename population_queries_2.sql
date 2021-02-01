-- This is the first query:

SELECT DISTINCT year from population_years;

-- Add your additional queries below:
select * from population_years;

SELECT * from population_years where country = 'India' and year='2007';
SELECT DISTINCT country from population_years where population < 2;
SELECT DISTINCT country from population_years where population > 100;

ALTER table population_years
ADD density varchar(64);

select * from population_years;

update population_years set density='High' WHERE population > 100;

update population_years set density='Low' where population < 100;

select country,density from population_years GROUP by country order by density DESC;
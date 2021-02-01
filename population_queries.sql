-- How many entries in the database are from Africa?
select count(*) from countries where continent='Africa';

-- What was the total population of Oceania in 2005?
select sum(population) as total_population from population_years where country_id in (select id from countries where continent='Oceania') and year='2005';

-- What is the average population of countries in South America in 2003?
select avg(population) as avg_population from population_years where country_id in (select id from countries where continent='South America') and year='2003';

-- What country had the smallest population in 2007?
select min(population),country_id from population_years where year='2007' and population!='NULL';
select name from countries where id=200; 

-- What is the average population of Poland during the time period covered by this dataset?
select avg(population) as avg_pop_poland from population_years where country_id in (select id from countries where name='Poland');


-- How many countries have the word "The" in their name?
select name from countries where name like '%The%';


-- What was the total population of each continent in 2010?
select continent,sum(population) as total_population from countries,population_years group by continent;

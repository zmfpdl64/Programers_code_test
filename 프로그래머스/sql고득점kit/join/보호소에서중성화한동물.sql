select i.animal_id, i.animal_type, i.name
from animal_ins i
join animal_outs o on o.animal_id = i.animal_id
where i.sex_upon_intake like '%intact%' and o.sex_upon_outcome not like ('%intact%')
order by i.animal_id;
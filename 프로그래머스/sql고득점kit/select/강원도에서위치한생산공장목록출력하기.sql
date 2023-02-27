select factory_id, factory_name, address
from ffod_factory
where address like '강원도%'
order by factory_id
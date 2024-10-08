views_schema = {
    'view_trip_type_by_duration' : '''
        CREATE OR REPLACE VIEW MAIN.ADA.TRIP_TYPE_BY_DURATION AS
            SELECT 
            ROUND((CAST(SUBSTRING(trip_duration, 1, 2) AS INT) * 60) + CAST(SUBSTRING(trip_duration, 4, 2) AS INT) +(CAST(SUBSTRING(trip_duration, 7, 2) AS INT) / 60.0), 2) AS trip_duration_in_minutes,
                includes_walk,
                includes_bicycle,
                includes_subway,
                includes_brt,
                includes_bus,
                includes_unlicensed_service,
                includes_private_charter,
                includes_school_bus,
                includes_car_as_driver,
                includes_car_as_passenger,
                includes_motorcycle_as_driver,
                includes_motorcycle_as_passenger,
                includes_taxi,
                includes_motorbicycle_taxi,
                includes_private_driver,
                includes_other_modes,
                includes_active_transportation,
                includes_individual_transportation,
                includes_collective_transportation      
            FROM MAIN.ADA.DIM_TRIP
            ; 
        ''',

    'view_avg_md_trip_time' : '''
        CREATE OR REPLACE VIEW MAIN.ADA.AVG_MD_TRIP_TIME AS
            SELECT 
                'WALK' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION
            WHERE includes_walk = 1
            
            UNION ALL

            SELECT 
                'BICYCLE' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_bicycle = 1

            UNION ALL
            
            SELECT 
                'SUBWAY' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_subway = 1

            UNION ALL

            SELECT 
                'BRT' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_brt = 1

            UNION ALL

            SELECT 
                'BUS' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_bus = 1

            UNION ALL

            SELECT 
                'UNLICENSED SERVICE' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_unlicensed_service = 1    

            UNION ALL

            SELECT 
                'PRIVATE CHARTER' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_private_charter = 1       

            UNION ALL

            SELECT 
                'SCHOOL BUS' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_school_bus = 1   

            UNION ALL

            SELECT 
                'CAR' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_car_as_driver = 1    
                OR includes_car_as_passenger = 1

            UNION ALL

            SELECT 
                'MOTORCYCLE' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_motorcycle_as_driver = 1    
                OR includes_motorcycle_as_passenger = 1  
                OR includes_motorbicycle_taxi = 1

            UNION ALL

            SELECT 
                'TAXI' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_taxi = 1   

            UNION ALL

            SELECT 
                'PRIVATE DRIVER' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_private_driver = 1       
            
            UNION ALL

            SELECT 
                'OTHER' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_other_modes = 1      
        
            UNION ALL

            SELECT 
                'ACTIVE TRANSPORTATION' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_active_transportation = 1       
        
            UNION ALL

            SELECT 
                'INDIVIDUAL TRANSPORTATION' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_individual_transportation = 1      

            UNION ALL

            SELECT 
                'COLLECTIVE TRANSPORTATION' AS type,
                ROUND(AVG(trip_duration_in_minutes), 2) AS average_value,
                ROUND(MEDIAN(trip_duration_in_minutes), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_DURATION        
            WHERE includes_collective_transportation = 1
            ;
        ''',

    'view_trip_type_by_cost' : '''
        CREATE OR REPLACE VIEW MAIN.ADA.TRIP_TYPE_BY_COST AS
            SELECT 
                s.stage_cost :: FLOAT AS stage_cost,
                t.includes_walk,
                t.includes_bicycle,
                t.includes_subway,
                t.includes_brt,
                t.includes_bus,
                t.includes_unlicensed_service,
                t.includes_private_charter,
                t.includes_school_bus,
                t.includes_car_as_driver,
                t.includes_car_as_passenger,
                t.includes_motorcycle_as_driver,
                t.includes_motorcycle_as_passenger,
                t.includes_taxi,
                t.includes_motorbicycle_taxi,
                t.includes_private_driver,
                t.includes_other_modes,
                t.includes_active_transportation,
                t.includes_individual_transportation,
                t.includes_collective_transportation      
            FROM MAIN.ADA.DIM_TRIP t
            JOIN MAIN.ADA.DIM_STAGE s ON t.trip_id = s.trip_id
            WHERE s.stage_cost IS NOT NULL 
                AND s.stage_cost <> 'not applicable'
            ;   
        ''',

    'view_avg_md_trip_cost' : '''
        CREATE OR REPLACE VIEW MAIN.ADA.AVG_MD_TRIP_COST AS
            SELECT 
                'WALK' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST
            WHERE includes_walk = 1
            
            UNION ALL

            SELECT 
                'BICYCLE' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_bicycle = 1

            UNION ALL
            
            SELECT 
                'SUBWAY' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_subway = 1

            UNION ALL

            SELECT 
                'BRT' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_brt = 1

            UNION ALL

            SELECT 
                'BUS' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_bus = 1

            UNION ALL

            SELECT 
                'UNLICENSED SERVICE' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_unlicensed_service = 1    

            UNION ALL

            SELECT 
                'PRIVATE CHARTER' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_private_charter = 1       

            UNION ALL

            SELECT 
                'SCHOOL BUS' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_school_bus = 1   

            UNION ALL

            SELECT 
                'CAR' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_car_as_driver = 1    
                OR includes_car_as_passenger = 1

            UNION ALL

            SELECT 
                'MOTORCYCLE' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_motorcycle_as_driver = 1    
                OR includes_motorcycle_as_passenger = 1  
                OR includes_motorbicycle_taxi = 1

            UNION ALL

            SELECT 
                'TAXI' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_taxi = 1   

            UNION ALL

            SELECT 
                'PRIVATE DRIVER' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_private_driver = 1       
            
            UNION ALL

            SELECT 
                'OTHER' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_other_modes = 1      
        
            UNION ALL

            SELECT 
                'ACTIVE TRANSPORTATION' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_active_transportation = 1       
        
            UNION ALL

            SELECT 
                'INDIVIDUAL TRANSPORTATION' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_individual_transportation = 1      

            UNION ALL

            SELECT 
                'COLLECTIVE TRANSPORTATION' AS type,
                ROUND(AVG(stage_cost), 2) AS average_value,
                ROUND(MEDIAN(stage_cost), 2) AS median_value
            FROM MAIN.ADA.TRIP_TYPE_BY_COST        
            WHERE includes_collective_transportation = 1
            ;
        ''',

    'view_trip_type_by_person' : '''
        CREATE OR REPLACE VIEW MAIN.ADA.TRIP_TYPE_BY_PERSON AS
        SELECT DISTINCT 
            p.age, 
            p.gender,
            p.education_level,
            h.income,
            CASE t.mode_type
                WHEN 'IT_private' THEN 'Individual Transport Private'
                WHEN 'CT_public' THEN 'Collective Transport Public'
                WHEN 'CT_private' THEN 'Collective Transport Private'
                WHEN 'AM_walk' THEN 'Active Mobility Walk'
                WHEN 'Other' THEN 'Other'
                WHEN 'AM_bicycle' THEN 'Active Mobility Bicycle'
                WHEN 'IT_public' THEN 'Individual Transport Public'
                WHEN 'Combined' THEN 'Combined'
                ELSE ''
            END AS mode_type,
            COUNT(t.trip_id) AS total_count
        FROM MAIN.ADA.DIM_TRIP t
        JOIN MAIN.ADA.DIM_PERSON p ON p.person_id = t.person_id
        JOIN MAIN.ADA.DIM_HOUSEHOLD h ON h.household_id = t.household_id
        GROUP BY 1,2,3,4,5
        ;
        ''',
    'view_avg_family_income' : '''
        CREATE OR REPLACE VIEW MAIN.ADA.AVG_FAMILY_INCOME AS
        WITH income_separation AS (
            SELECT 
                household_id,
                vehicles,
                income,
                CASE 
                    WHEN income ILIKE '%Has no income%' THEN NULL
                    ELSE TO_NUMBER(REPLACE(REGEXP_SUBSTR(income, '[0-9,.]+'), ',', '')) 
                END AS min_income,
                CASE 
                    WHEN income ILIKE '%Has no income%' THEN NULL
                    WHEN income ILIKE 'More than%' AND income ILIKE '%and less than%' THEN TO_NUMBER(REPLACE(REGEXP_SUBSTR(income, '[0-9,.]+', 1, 2), ',', ''))
                    WHEN income ILIKE '%or less%' THEN TO_NUMBER(REPLACE(REGEXP_SUBSTR(income, '[0-9,.]+'), ',', ''))
                    ELSE TO_NUMBER(REPLACE(REGEXP_SUBSTR(income, '[0-9,.]+', 1, 2), ',', ''))
                END AS max_income
            FROM MAIN.ADA.DIM_HOUSEHOLD
        )
        SELECT 
            p.person_id,
            p.household_id,
            i.vehicles,
            ROUND((i.min_income + i.max_income) / 2, 2) AS AVG_INCOME
        FROM MAIN.ADA.DIM_PERSON p
        JOIN income_separation i ON i.household_id = p.household_id
        ;
    '''
}
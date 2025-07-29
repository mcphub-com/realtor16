import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/s.mahmoud97/api/realtor16'

mcp = FastMCP('realtor16')

@mcp.tool()
def search_forsale(location: Annotated[str, Field(description='Search by address, neighborhood, city or ZIP code')],
                   page: Annotated[Union[str, None], Field(description='')] = None,
                   sort: Annotated[Union[str, None], Field(description='Available types: relevant: Sorts listings by their relevance. Default newest_listing: Sorts listings by the listing date in descending order. highest_price: Sorts listings by the list price in descending order. lowest_price: Sorts listings by the list price in ascending order. open_house_date: Sorts listings by the open house date in ascending order. recently_reduced: Sorts listings by the date when the price was last reduced in descending order. largest_sqft: Sorts listings by the square footage in descending order. lot_size: Sorts listings by the lot size in descending order. For multiple selections, use comma-separated values (e.g., relevant,newest_listing)')] = None,
                   type: Annotated[Union[str, None], Field(description='If empty, all available types will be included. Available types: single_family: Refers to standalone residential properties designed to house a single family. condos: Refers to condominium units. townhomes: Refers specifically to townhouses. duplex_triplex: Refers to properties that have two (duplex) or three (triplex) separate living units. multi_family: Refers to properties designed to house multiple families, such as apartment buildings or complexes. mobile: Refers to mobile homes or manufactured homes. farm: Refers to agricultural properties, including farms. land: Refers to undeveloped land or plots available for sale. For multiple selections, use comma-separated values (e.g., single_family,condo).')] = None,
                   beds_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   beds_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   baths_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   baths_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   limit: Annotated[Union[str, None], Field(description='The number of results. Maximum 200, **default **50')] = None,
                   search_radius: Annotated[Literal['0', '1', '5', '10', '25', '50', None], Field(description="Change search radius (not in miles, it's categorized) **default ** 0")] = None,
                   sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   lot_sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   lot_sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   new_construction: Annotated[Union[bool, None], Field(description='')] = None,
                   hoa_fee_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   hoa_fee_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   foreclosure: Annotated[Union[bool, None], Field(description='The foreclosure parameter controls the visibility of foreclosure listings: false: Hides listings that are foreclosures. true: Shows only listings that are foreclosures. If the parameter is not included, both foreclosure and non-foreclosure listings will be shown.')] = None,
                   has_tour: Annotated[Union[bool, None], Field(description='')] = None,
                   has_3d_tour: Annotated[Union[bool, None], Field(description='')] = None,
                   open_house_min: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                   open_house_max: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                   list_price_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   list_price_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   price_reduced_date_min: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                   pending: Annotated[Union[bool, None], Field(description='The pending_contingent parameter controls the visibility of listings with pending contingencies: false: Hides listings that have pending contingencies. true: Shows only listings with pending contingencies. If the parameter is not included, both listings with and without pending contingencies will be shown.')] = None,
                   tags: Annotated[Union[str, None], Field(description='basement, fireplace, central_air, central_heat, forced_air, den_or_office, spa_or_hot_tub, dining_room, swimming_pool, disability_features, family_room, laundry_room, hardwood_floors, rv_or_boat_parking, tennis_court, game_room, horse_facilities, lease_option, energy_efficient_home, garage_1_or_more, garage_2_or_more, garage_3_or_more, carport, single_story, two_or_more_stories, recreation_facilities, community_swimming_pool, community_clubhouse, community_tennis_court, community_golf, community_spa_or_hot_tub, community_security_features, community_boat_facilities, community_horse_facilities, community_park, senior_community, corner_lot, waterfront, cul_de_sac, water_view, view, hill_or_mountain_view, lake_view, river_view, golf_course_view, city_view, ocean_view, golf_course_lot_or_frontage, washer_dryer, community_doorman, pets_allowed, elevator, community_elevator, community_outdoor_space, furniture, furnished, dishwasher, community_no_fee, community_gym, recreation_facility For multiple selections, use comma-separated values (e.g., community_gym,recreation_facility)')] = None,
                   keywords: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for sale listings by address, neighbourhood, city or ZIP'''
    url = 'https://realtor16.p.rapidapi.com/search/forsale'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'page': page,
        'sort': sort,
        'type': type,
        'beds-min': beds_min,
        'beds-max': beds_max,
        'baths-min': baths_min,
        'baths-max': baths_max,
        'limit': limit,
        'search_radius': search_radius,
        'sqft-min': sqft_min,
        'sqft-max': sqft_max,
        'lot_sqft-min': lot_sqft_min,
        'lot_sqft-max': lot_sqft_max,
        'new_construction': new_construction,
        'hoa_fee-min': hoa_fee_min,
        'hoa_fee-max': hoa_fee_max,
        'foreclosure': foreclosure,
        'has_tour': has_tour,
        'has_3d_tour': has_3d_tour,
        'open_house-min': open_house_min,
        'open_house-max': open_house_max,
        'list_price-min': list_price_min,
        'list_price-max': list_price_max,
        'price_reduced_date-min': price_reduced_date_min,
        'pending': pending,
        'tags': tags,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def forsale_coordinates(latitude: Annotated[Union[int, float], Field(description='The latitude of the center point. Default: 29.270521')],
                        longitude: Annotated[Union[int, float], Field(description='The longitude of the center point. Default: -95.74991')],
                        radius: Annotated[Union[int, float], Field(description='The radius of the search area in kilometers. Default: 30')],
                        page: Annotated[Union[str, None], Field(description='')] = None,
                        sort: Annotated[Union[str, None], Field(description='Available types: relevant: Sorts listings by their relevance. Default newest_listing: Sorts listings by the listing date in descending order. highest_price: Sorts listings by the list price in descending order. lowest_price: Sorts listings by the list price in ascending order. open_house_date: Sorts listings by the open house date in ascending order. recently_reduced: Sorts listings by the date when the price was last reduced in descending order. largest_sqft: Sorts listings by the square footage in descending order. lot_size: Sorts listings by the lot size in descending order. For multiple selections, use comma-separated values (e.g., relevant,newest_listing)')] = None,
                        type: Annotated[Union[str, None], Field(description='If empty, all available types will be included. Available types: single_family: Refers to standalone residential properties designed to house a single family. condos: Refers to condominium units. townhomes: Refers specifically to townhouses. duplex_triplex: Refers to properties that have two (duplex) or three (triplex) separate living units. multi_family: Refers to properties designed to house multiple families, such as apartment buildings or complexes. mobile: Refers to mobile homes or manufactured homes. farm: Refers to agricultural properties, including farms. land: Refers to undeveloped land or plots available for sale. For multiple selections, use comma-separated values (e.g., single_family,condo).')] = None,
                        beds_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        beds_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        baths_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        baths_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        limit: Annotated[Union[str, None], Field(description='The number of results. Maximum 200, **default **50')] = None,
                        sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        lot_sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        lot_sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        new_construction: Annotated[Union[bool, None], Field(description='')] = None,
                        hoa_fee_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        hoa_fee_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        foreclosure: Annotated[Union[bool, None], Field(description='The foreclosure parameter controls the visibility of foreclosure listings: false: Hides listings that are foreclosures. true: Shows only listings that are foreclosures. If the parameter is not included, both foreclosure and non-foreclosure listings will be shown.')] = None,
                        has_tour: Annotated[Union[bool, None], Field(description='')] = None,
                        has_3d_tour: Annotated[Union[bool, None], Field(description='')] = None,
                        open_house_min: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                        open_house_max: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                        list_price_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        list_price_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        price_reduced_date_min: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                        pending: Annotated[Union[bool, None], Field(description='The pending_contingent parameter controls the visibility of listings with pending contingencies: false: Hides listings that have pending contingencies. true: Shows only listings with pending contingencies. If the parameter is not included, both listings with and without pending contingencies will be shown.')] = None,
                        tags: Annotated[Union[str, None], Field(description='basement, fireplace, central_air, central_heat, forced_air, den_or_office, spa_or_hot_tub, dining_room, swimming_pool, disability_features, family_room, laundry_room, hardwood_floors, rv_or_boat_parking, tennis_court, game_room, horse_facilities, lease_option, energy_efficient_home, garage_1_or_more, garage_2_or_more, garage_3_or_more, carport, single_story, two_or_more_stories, recreation_facilities, community_swimming_pool, community_clubhouse, community_tennis_court, community_golf, community_spa_or_hot_tub, community_security_features, community_boat_facilities, community_horse_facilities, community_park, senior_community, corner_lot, waterfront, cul_de_sac, water_view, view, hill_or_mountain_view, lake_view, river_view, golf_course_view, city_view, ocean_view, golf_course_lot_or_frontage, washer_dryer, community_doorman, pets_allowed, elevator, community_elevator, community_outdoor_space, furniture, furnished, dishwasher, community_no_fee, community_gym, recreation_facility For multiple selections, use comma-separated values (e.g., community_gym,recreation_facility)')] = None,
                        keywords: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for sale listings by circle (using latitude, longitude, and radius) or polygon (using a set of coordinates to define a specific area).'''
    url = 'https://realtor16.p.rapidapi.com/search/forsale/coordinates'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'radius': radius,
        'page': page,
        'sort': sort,
        'type': type,
        'beds-min': beds_min,
        'beds-max': beds_max,
        'baths-min': baths_min,
        'baths-max': baths_max,
        'limit': limit,
        'sqft-min': sqft_min,
        'sqft-max': sqft_max,
        'lot_sqft-min': lot_sqft_min,
        'lot_sqft-max': lot_sqft_max,
        'new_construction': new_construction,
        'hoa_fee-min': hoa_fee_min,
        'hoa_fee-max': hoa_fee_max,
        'foreclosure': foreclosure,
        'has_tour': has_tour,
        'has_3d_tour': has_3d_tour,
        'open_house-min': open_house_min,
        'open_house-max': open_house_max,
        'list_price-min': list_price_min,
        'list_price-max': list_price_max,
        'price_reduced_date-min': price_reduced_date_min,
        'pending': pending,
        'tags': tags,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_forrent(location: Annotated[str, Field(description='')],
                   page: Annotated[Union[str, None], Field(description='')] = None,
                   sort: Annotated[Union[str, None], Field(description='Available types: relevant: Sorts listings by their relevance. Default recently_added: Sorts listings by the listing date in descending order. highest_price: Sorts listings by the list price in descending order. lowest_price: Sorts listings by the list price in ascending order. For multiple selections, use comma-separated values (e.g., relevant,newest_listing)')] = None,
                   type: Annotated[Union[str, None], Field(description='If empty, all available types will be included. Available types: single_family: Refers to standalone residential properties designed to house a single family. condos: Refers to condominium units. apartment: Refers to apartment units. townhomes: Refers specifically to townhouses. duplex_triplex: Refers to properties that have two (duplex) or three (triplex) separate living units. multi_family: Refers to properties designed to house multiple families, such as apartment buildings or complexes. other: Refers to other type of properties available for rent. For multiple selections, use comma-separated values (e.g., single_family,condos).')] = None,
                   beds_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   beds_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   baths_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   baths_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   limit: Annotated[Union[str, None], Field(description='The number of results. Maximum 200, **default **50')] = None,
                   search_radius: Annotated[Literal['0', '1', '5', '10', '25', '50', None], Field(description="Change search radius (not in miles, it's categorized) **default ** 0")] = None,
                   sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   has_3d_tour: Annotated[Union[bool, None], Field(description='')] = None,
                   list_price_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   list_price_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   availability_date_max: Annotated[Union[str, datetime, None], Field(description='Shows listings available by this date')] = None,
                   cats: Annotated[Union[bool, None], Field(description='')] = None,
                   dogs: Annotated[Union[bool, None], Field(description='')] = None,
                   noFees: Annotated[Union[bool, None], Field(description='')] = None,
                   pending: Annotated[Union[bool, None], Field(description='')] = None,
                   tags: Annotated[Union[str, None], Field(description='basement, fireplace, central_air, central_heat, forced_air, den_or_office, spa_or_hot_tub, dining_room, swimming_pool, disability_features, family_room, laundry_room, hardwood_floors, rv_or_boat_parking, tennis_court, game_room, horse_facilities, lease_option, energy_efficient_home, garage_1_or_more, garage_2_or_more, garage_3_or_more, carport, single_story, two_or_more_stories, recreation_facilities, community_swimming_pool, community_clubhouse, community_tennis_court, community_golf, community_spa_or_hot_tub, community_security_features, community_boat_facilities, community_horse_facilities, community_park, senior_community, corner_lot, waterfront, cul_de_sac, water_view, view, hill_or_mountain_view, lake_view, river_view, golf_course_view, city_view, ocean_view, golf_course_lot_or_frontage, washer_dryer, community_doorman, pets_allowed, elevator, community_elevator, community_outdoor_space, furniture, furnished, dishwasher, community_no_fee, community_gym, recreation_facility, For multiple selections, use comma-separated values (e.g., community_gym,recreation_facility)')] = None,
                   keywords: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for rent listings by address, neighbourhood, city or ZIP'''
    url = 'https://realtor16.p.rapidapi.com/search/forrent'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'page': page,
        'sort': sort,
        'type': type,
        'beds-min': beds_min,
        'beds-max': beds_max,
        'baths-min': baths_min,
        'baths-max': baths_max,
        'limit': limit,
        'search_radius': search_radius,
        'sqft-min': sqft_min,
        'sqft-max': sqft_max,
        'has_3d_tour': has_3d_tour,
        'list_price-min': list_price_min,
        'list_price-max': list_price_max,
        'availability_date-max': availability_date_max,
        'cats': cats,
        'dogs': dogs,
        'noFees': noFees,
        'pending': pending,
        'tags': tags,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def forrent_coordinates(latitude: Annotated[Union[int, float], Field(description='The latitude of the center point. Default: 29.27052')],
                        longitude: Annotated[Union[int, float], Field(description='The longitude of the center point. Default: -95.74991')],
                        radius: Annotated[Union[int, float], Field(description='The radius of the search area in kilometers. Default: 30')],
                        page: Annotated[Union[str, None], Field(description='')] = None,
                        sort: Annotated[Union[str, None], Field(description='Available types: relevant: Sorts listings by their relevance. Default recently_added: Sorts listings by the listing date in descending order. highest_price: Sorts listings by the list price in descending order. lowest_price: Sorts listings by the list price in ascending order. For multiple selections, use comma-separated values (e.g., relevant,newest_listing)')] = None,
                        type: Annotated[Union[str, None], Field(description='If empty, all available types will be included. Available types: single_family: Refers to standalone residential properties designed to house a single family. condos: Refers to condominium units. apartment: Refers to apartment units. townhomes: Refers specifically to townhouses. duplex_triplex: Refers to properties that have two (duplex) or three (triplex) separate living units. multi_family: Refers to properties designed to house multiple families, such as apartment buildings or complexes. other: Refers to other type of properties available for rent. For multiple selections, use comma-separated values (e.g., single_family,condos).')] = None,
                        beds_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        baths_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        baths_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        limit: Annotated[Union[str, None], Field(description='The number of results. Maximum 200, **default **50')] = None,
                        sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        has_3d_tour: Annotated[Union[bool, None], Field(description='')] = None,
                        list_price_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        list_price_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        availability_date_max: Annotated[Union[str, datetime, None], Field(description='Shows listings available by this date')] = None,
                        cats: Annotated[Union[bool, None], Field(description='')] = None,
                        dogs: Annotated[Union[bool, None], Field(description='')] = None,
                        noFees: Annotated[Union[bool, None], Field(description='')] = None,
                        pending: Annotated[Union[bool, None], Field(description='')] = None,
                        tags: Annotated[Union[str, None], Field(description='basement, fireplace, central_air, central_heat, forced_air, den_or_office, spa_or_hot_tub, dining_room, swimming_pool, disability_features, family_room, laundry_room, hardwood_floors, rv_or_boat_parking, tennis_court, game_room, horse_facilities, lease_option, energy_efficient_home, garage_1_or_more, garage_2_or_more, garage_3_or_more, carport, single_story, two_or_more_stories, recreation_facilities, community_swimming_pool, community_clubhouse, community_tennis_court, community_golf, community_spa_or_hot_tub, community_security_features, community_boat_facilities, community_horse_facilities, community_park, senior_community, corner_lot, waterfront, cul_de_sac, water_view, view, hill_or_mountain_view, lake_view, river_view, golf_course_view, city_view, ocean_view, golf_course_lot_or_frontage, washer_dryer, community_doorman, pets_allowed, elevator, community_elevator, community_outdoor_space, furniture, furnished, dishwasher, community_no_fee, community_gym, recreation_facility, For multiple selections, use comma-separated values (e.g., community_gym,recreation_facility)')] = None,
                        keywords: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for rent listings by circle (using latitude, longitude, and radius) or polygon (using a set of coordinates to define a specific area).'''
    url = 'https://realtor16.p.rapidapi.com/search/forrent/coordinates'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'radius': radius,
        'page': page,
        'sort': sort,
        'type': type,
        'beds-max': beds_max,
        'baths-min': baths_min,
        'baths-max': baths_max,
        'limit': limit,
        'sqft-min': sqft_min,
        'sqft-max': sqft_max,
        'has_3d_tour': has_3d_tour,
        'list_price-min': list_price_min,
        'list_price-max': list_price_max,
        'availability_date-max': availability_date_max,
        'cats': cats,
        'dogs': dogs,
        'noFees': noFees,
        'pending': pending,
        'tags': tags,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_forsold(location: Annotated[str, Field(description='')],
                   page: Annotated[Union[str, None], Field(description='')] = None,
                   sort: Annotated[Union[str, datetime, None], Field(description='Enum Available types: sold_date: Sorts listings by their sold date in descending order. Default highest_price: Sorts listings by the list price in descending order. lowest_price: Sorts listings by the list price in ascending order. largest_sqft: Sorts listings by the square footage in descending order. lot_size: Sorts listings by the lot size in descending order. photo_count : Sorts listings by there phot count in descending order.')] = None,
                   type: Annotated[Union[str, None], Field(description='If empty, all available types will be included. Available types: single_family: Refers to standalone residential properties designed to house a single family. condos: Refers to condominium units. townhomes: Refers specifically to townhouses. duplex_triplex: Refers to properties that have two (duplex) or three (triplex) separate living units. multi_family: Refers to properties designed to house multiple families, such as apartment buildings or complexes. mobile: Refers to mobile homes or manufactured homes. farm: Refers to agricultural properties, including farms. land: Refers to undeveloped land or plots available for sale. For multiple selections, use comma-separated values (e.g., single_family,condo).')] = None,
                   beds_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   beds_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   baths_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   baths_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   limit: Annotated[Union[str, None], Field(description='The number of results. Maximum 200, **default **50')] = None,
                   sold_date_min: Annotated[Union[str, datetime, None], Field(description='The **sold_date_min **parameter allows you to filter listings based on their minimum sold date. This parameter is used to include only those listings that were sold on or after the specified date. If the parameter is not included, there will be no restriction on the minimum sold date, and all sold listings will be shown.')] = None,
                   sold_price_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   sold_price_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   search_radius: Annotated[Literal['0', '1', '5', '10', '25', '50', None], Field(description="Change search radius (not in miles, it's categorized) **default ** 0")] = None,
                   sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   lot_sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   lot_sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   hoa_fee_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   hoa_fee_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                   foreclosure: Annotated[Union[bool, None], Field(description='The foreclosure parameter controls the visibility of foreclosure listings: false: Hides listings that are foreclosures. true: Shows only listings that are foreclosures. If the parameter is not included, both foreclosure and non-foreclosure listings will be shown.')] = None,
                   has_tour: Annotated[Union[bool, None], Field(description='')] = None,
                   has_3d_tour: Annotated[Union[bool, None], Field(description='')] = None,
                   price_reduced_date_min: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                   tags: Annotated[Union[str, None], Field(description='basement, fireplace, central_air, central_heat, forced_air, den_or_office, spa_or_hot_tub, dining_room, swimming_pool, disability_features, family_room, laundry_room, hardwood_floors, rv_or_boat_parking, tennis_court, game_room, horse_facilities, lease_option, energy_efficient_home, garage_1_or_more, garage_2_or_more, garage_3_or_more, carport, single_story, two_or_more_stories, recreation_facilities, community_swimming_pool, community_clubhouse, community_tennis_court, community_golf, community_spa_or_hot_tub, community_security_features, community_boat_facilities, community_horse_facilities, community_park, senior_community, corner_lot, waterfront, cul_de_sac, water_view, view, hill_or_mountain_view, lake_view, river_view, golf_course_view, city_view, ocean_view, golf_course_lot_or_frontage, washer_dryer, community_doorman, pets_allowed, elevator, community_elevator, community_outdoor_space, furniture, furnished, dishwasher, community_no_fee, community_gym, recreation_facility, For multiple selections, use comma-separated values (e.g., community_gym,recreation_facility)')] = None,
                   keywords: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for sold listings by address, neighbourhood, city or ZIP'''
    url = 'https://realtor16.p.rapidapi.com/search/forsold'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'page': page,
        'sort': sort,
        'type': type,
        'beds-min': beds_min,
        'beds-max': beds_max,
        'baths-min': baths_min,
        'baths-max': baths_max,
        'limit': limit,
        'sold_date-min': sold_date_min,
        'sold_price-min': sold_price_min,
        'sold_price-max': sold_price_max,
        'search_radius': search_radius,
        'sqft-min': sqft_min,
        'sqft-max': sqft_max,
        'lot_sqft-min': lot_sqft_min,
        'lot_sqft-max': lot_sqft_max,
        'hoa_fee-min': hoa_fee_min,
        'hoa_fee-max': hoa_fee_max,
        'foreclosure': foreclosure,
        'has_tour': has_tour,
        'has_3d_tour': has_3d_tour,
        'price_reduced_date-min': price_reduced_date_min,
        'tags': tags,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def forsold_coordinates(latitude: Annotated[Union[int, float], Field(description='Default: 29.27052')],
                        longitude: Annotated[Union[int, float, None], Field(description='The longitude of the center point. Default: -95.74991')] = None,
                        radius: Annotated[Union[int, float, None], Field(description='The radius of the search area in kilometers. Default: 30')] = None,
                        page: Annotated[Union[str, None], Field(description='')] = None,
                        sort: Annotated[Union[str, datetime, None], Field(description='Enum Available types: sold_date: Sorts listings by their sold date in descending order. Default highest_price: Sorts listings by the list price in descending order. lowest_price: Sorts listings by the list price in ascending order. largest_sqft: Sorts listings by the square footage in descending order. lot_size: Sorts listings by the lot size in descending order. photo_count : Sorts listings by there phot count in descending order.')] = None,
                        type: Annotated[Union[str, None], Field(description='If empty, all available types will be included. Available types: single_family: Refers to standalone residential properties designed to house a single family. condos: Refers to condominium units. townhomes: Refers specifically to townhouses. duplex_triplex: Refers to properties that have two (duplex) or three (triplex) separate living units. multi_family: Refers to properties designed to house multiple families, such as apartment buildings or complexes. mobile: Refers to mobile homes or manufactured homes. farm: Refers to agricultural properties, including farms. land: Refers to undeveloped land or plots available for sale. For multiple selections, use comma-separated values (e.g., single_family,condo).')] = None,
                        beds_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        beds_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        baths_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        baths_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        sold_date_min: Annotated[Union[str, datetime, None], Field(description='The **sold_date_min **parameter allows you to filter listings based on their minimum sold date. This parameter is used to include only those listings that were sold on or after the specified date. If the parameter is not included, there will be no restriction on the minimum sold date, and all sold listings will be shown.')] = None,
                        sold_price_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        sold_price_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        lot_sqft_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        lot_sqft_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        hoa_fee_min: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        hoa_fee_max: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                        foreclosure: Annotated[Union[bool, None], Field(description='The foreclosure parameter controls the visibility of foreclosure listings: false: Hides listings that are foreclosures. true: Shows only listings that are foreclosures. If the parameter is not included, both foreclosure and non-foreclosure listings will be shown.')] = None,
                        has_tour: Annotated[Union[bool, None], Field(description='')] = None,
                        has_3d_tour: Annotated[Union[bool, None], Field(description='')] = None,
                        price_reduced_date_min: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                        tags: Annotated[Union[str, None], Field(description='basement, fireplace, central_air, central_heat, forced_air, den_or_office, spa_or_hot_tub, dining_room, swimming_pool, disability_features, family_room, laundry_room, hardwood_floors, rv_or_boat_parking, tennis_court, game_room, horse_facilities, lease_option, energy_efficient_home, garage_1_or_more, garage_2_or_more, garage_3_or_more, carport, single_story, two_or_more_stories, recreation_facilities, community_swimming_pool, community_clubhouse, community_tennis_court, community_golf, community_spa_or_hot_tub, community_security_features, community_boat_facilities, community_horse_facilities, community_park, senior_community, corner_lot, waterfront, cul_de_sac, water_view, view, hill_or_mountain_view, lake_view, river_view, golf_course_view, city_view, ocean_view, golf_course_lot_or_frontage, washer_dryer, community_doorman, pets_allowed, elevator, community_elevator, community_outdoor_space, furniture, furnished, dishwasher, community_no_fee, community_gym, recreation_facility, For multiple selections, use comma-separated values (e.g., community_gym,recreation_facility)')] = None,
                        keywords: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Search for sold listings by circle (using latitude, longitude, and radius) or polygon (using a set of coordinates to define a specific area).'''
    url = 'https://realtor16.p.rapidapi.com/search/forsold/coordinates'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'radius': radius,
        'page': page,
        'sort': sort,
        'type': type,
        'beds-min': beds_min,
        'beds-max': beds_max,
        'baths-min': baths_min,
        'baths-max': baths_max,
        'sold_date-min': sold_date_min,
        'sold_price-min': sold_price_min,
        'sold_price-max': sold_price_max,
        'sqft-min': sqft_min,
        'sqft-max': sqft_max,
        'lot_sqft-min': lot_sqft_min,
        'lot_sqft-max': lot_sqft_max,
        'hoa_fee-min': hoa_fee_min,
        'hoa_fee-max': hoa_fee_max,
        'foreclosure': foreclosure,
        'has_tour': has_tour,
        'has_3d_tour': has_3d_tour,
        'price_reduced_date-min': price_reduced_date_min,
        'tags': tags,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_details(property_id: Annotated[Union[str, None], Field(description='')] = None,
                     url: Annotated[Union[str, None], Field(description='eg : https://www.realtor.com/realestateandhomes-detail/2011-Laurel-Hill-Dr_Kingwood_TX_77339_M84616-73077')] = None) -> dict: 
    '''Get a property's details by `property_id` or `url`'''
    url = 'https://realtor16.p.rapidapi.com/property/details'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_photos(property_id: Annotated[Union[str, None], Field(description='')] = None,
                    url: Annotated[Union[str, None], Field(description='eg : https://www.realtor.com/realestateandhomes-detail/2011-Laurel-Hill-Dr_Kingwood_TX_77339_M84616-73077')] = None) -> dict: 
    '''Get a property's photos by `property_id` or `url`'''
    url = 'https://realtor16.p.rapidapi.com/property/photos'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_estimates(historical_years_min: Annotated[Union[str, datetime], Field(description='The start date for historical value estimates, in YYYY-MM-DD format. Specifies the earliest date for historical data.')],
                       historical_years_max: Annotated[Union[str, datetime], Field(description='The end date for historical value estimates, in YYYY-MM-DD format. Specifies the latest date for historical data.')],
                       forecasted_months_max: Annotated[Union[str, datetime], Field(description='The end date for forecasted value estimates, in YYYY-MM-DD format. Specifies the maximum date for forecasted data.')],
                       property_id: Annotated[Union[str, None], Field(description='')] = None,
                       url: Annotated[Union[str, None], Field(description='eg : https://www.realtor.com/realestateandhomes-detail/2011-Laurel-Hill-Dr_Kingwood_TX_77339_M84616-73077')] = None) -> dict: 
    '''Get historical and forecasted value estimates for a property using the `property_id` or `url`.'''
    url = 'https://realtor16.p.rapidapi.com/property/estimates'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'historical_years_min': historical_years_min,
        'historical_years_max': historical_years_max,
        'forecasted_months_max': forecasted_months_max,
        'property_id': property_id,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_amenities_score(property_id: Annotated[Union[str, None], Field(description='')] = None,
                             url: Annotated[Union[str, None], Field(description='eg : https://www.realtor.com/realestateandhomes-detail/2011-Laurel-Hill-Dr_Kingwood_TX_77339_M84616-73077')] = None) -> dict: 
    '''Get nearby amenities and location scores for a property using the `property_id` or `url`'''
    url = 'https://realtor16.p.rapidapi.com/property/amenities_score'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_similar_homes(status: Annotated[Literal['for_sale', 'for_rent', 'sold'], Field(description='')],
                           property_id: Annotated[Union[str, None], Field(description='')] = None,
                           url: Annotated[Union[str, None], Field(description='eg : https://www.realtor.com/realestateandhomes-detail/2011-Laurel-Hill-Dr_Kingwood_TX_77339_M84616-73077')] = None) -> dict: 
    '''Get similar homes for a property by using the `property_id`.'''
    url = 'https://realtor16.p.rapidapi.com/property/similar_homes'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'status': status,
        'property_id': property_id,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_new_construction_similar_homes(status: Annotated[Literal['for_sale', 'for_rent', 'sold'], Field(description='')],
                                            property_id: Annotated[Union[str, None], Field(description='')] = None,
                                            url: Annotated[Union[str, None], Field(description='eg : https://www.realtor.com/realestateandhomes-detail/2011-Laurel-Hill-Dr_Kingwood_TX_77339_M84616-73077')] = None) -> dict: 
    '''Get new construction similar homes for a property using the `property_id` or `url`.'''
    url = 'https://realtor16.p.rapidapi.com/property/new_construction_similar_homes'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'status': status,
        'property_id': property_id,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_history(property_id: Annotated[Union[str, None], Field(description='')] = None,
                     url: Annotated[Union[str, None], Field(description='eg : https://www.realtor.com/realestateandhomes-detail/2011-Laurel-Hill-Dr_Kingwood_TX_77339_M84616-73077')] = None) -> dict: 
    '''Get property history and tax history data for a property using the `property_id` or `url`'''
    url = 'https://realtor16.p.rapidapi.com/property/history'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_environment_risk(property_id: Annotated[Union[str, None], Field(description='')] = None,
                              url: Annotated[Union[str, None], Field(description='eg : https://www.realtor.com/realestateandhomes-detail/2011-Laurel-Hill-Dr_Kingwood_TX_77339_M84616-73077')] = None) -> dict: 
    '''Get a property's environmental risks by `property_id` or `url`. (flood, wildfire, etc)'''
    url = 'https://realtor16.p.rapidapi.com/property/environment_risk'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_schools(property_id: Annotated[Union[str, None], Field(description='')] = None,
                     url: Annotated[Union[str, None], Field(description='eg : https://www.realtor.com/realestateandhomes-detail/2011-Laurel-Hill-Dr_Kingwood_TX_77339_M84616-73077')] = None) -> dict: 
    '''Get a property's nearby schools using the `property_id` or `url`'''
    url = 'https://realtor16.p.rapidapi.com/property/schools'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_market_trends(property_id: Annotated[Union[str, None], Field(description='')] = None,
                           url: Annotated[Union[str, None], Field(description='eg : https://www.realtor.com/realestateandhomes-detail/2011-Laurel-Hill-Dr_Kingwood_TX_77339_M84616-73077')] = None) -> dict: 
    '''Get a property's market trends using the `property_id` or `url`'''
    url = 'https://realtor16.p.rapidapi.com/property/market_trends'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agent_search(location: Annotated[Union[str, None], Field(description='')] = None,
                 name: Annotated[Union[str, None], Field(description='The name of the agent to search for')] = None,
                 page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                 limit: Annotated[Union[str, None], Field(description="The number of results to return. Default is '20'. Max is '50'")] = None,
                 sort: Annotated[Literal['recent_activity_high', 'agent_rating_high', 'recommendations_count_high', 'for_sale_count_high', 'recently_sold_high', None], Field(description='**Possible values: ** recent_activity_high: Sorts by the most recent activity. Default agent_rating_high: Sorts by the highest agent rating. recommendations_count_high: Sorts by the highest number of recommendations. for_sale_count_high: Sorts by the highest number of properties for sale. recently_sold_high: Sorts by the most properties recently sold.')] = None,
                 types: Annotated[Literal['agent', 'team', 'office', None], Field(description='Specifies the type of result, default is agent Possible values: - agent - team - office')] = None,
                 far_opt_out: Annotated[Union[bool, None], Field(description='Set to false to include agents who have opted out of FAR (Federal Acquisition Regulation).')] = None,
                 recommendations_count_min: Annotated[Union[int, float, None], Field(description='Minimum number of recommendations the agent should have')] = None,
                 agent_rating_min: Annotated[Union[int, float, None], Field(description='Minimum rating required for agents to be included in the search results')] = None,
                 languages: Annotated[Union[str, None], Field(description='Languages spoken by the agent eg : French')] = None,
                 agent_type: Annotated[Union[str, None], Field(description='Specifies the type of agent. Possible values : buyer seller If the param is not included, the results will include both types')] = None,
                 price_min: Annotated[Union[int, float, None], Field(description='Minimum price of properties handled by the agent')] = None,
                 price_max: Annotated[Union[int, float, None], Field(description='Maximum price of properties handled by the agent')] = None,
                 photo: Annotated[Union[bool, None], Field(description='Set to true to exclude agents without a photo')] = None) -> dict: 
    '''Search for agents/teams/offices by `location` (city or ZIP code) or `name`.'''
    url = 'https://realtor16.p.rapidapi.com/agent/search'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'name': name,
        'page': page,
        'limit': limit,
        'sort': sort,
        'types': types,
        'far_opt_out': far_opt_out,
        'recommendations_count_min': recommendations_count_min,
        'agent_rating_min': agent_rating_min,
        'languages': languages,
        'agent_type': agent_type,
        'price_min': price_min,
        'price_max': price_max,
        'photo': photo,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agent_profile(advertiser_id: Annotated[str, Field(description='')],
                  nrds_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get an agent's profile by `advertiser_id` and/or `nrds_id`'''
    url = 'https://realtor16.p.rapidapi.com/agent/profile'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'advertiser_id': advertiser_id,
        'nrds_id': nrds_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agent_reviews(advertiser_id: Annotated[str, Field(description='')]) -> dict: 
    '''Get an agent's reviews by `advertiser_id`'''
    url = 'https://realtor16.p.rapidapi.com/agent/reviews'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'advertiser_id': advertiser_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agent_listings(advertiser_id: Annotated[str, Field(description='')],
                   type: Annotated[Literal['all', 'forsale', 'forrent', 'forsold', 'openhouses', None], Field(description='')] = None,
                   page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Get an agent's listings by `advertiser_id`'''
    url = 'https://realtor16.p.rapidapi.com/agent/listings'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'advertiser_id': advertiser_id,
        'type': type,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agent_recommendations(advertiser_id: Annotated[str, Field(description='')]) -> dict: 
    '''Get an agent's recommendations by `advertiser_id`'''
    url = 'https://realtor16.p.rapidapi.com/agent/recommendations'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'advertiser_id': advertiser_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def suggestion(location: Annotated[str, Field(description='')]) -> dict: 
    '''Suggests locations based on keyword'''
    url = 'https://realtor16.p.rapidapi.com/suggestion'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def housing_market_details(location: Annotated[Union[str, None], Field(description='')] = None,
                           slug_id: Annotated[Union[str, None], Field(description="A location's id found in the results of /suggestion endpoint")] = None) -> dict: 
    '''Get detailed housing market statistics for a specific location, including median prices, market temperature, and rankings.'''
    url = 'https://realtor16.p.rapidapi.com/housing_market_details'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'slug_id': slug_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def noise(lat: Annotated[Union[int, float], Field(description='Default: 34.0567')],
          lon: Annotated[Union[int, float], Field(description='Default: -118.2456')]) -> dict: 
    '''Get noise level information by coordinates (lat, lon)'''
    url = 'https://realtor16.p.rapidapi.com/noise'
    headers = {'x-rapidapi-host': 'realtor16.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'lon': lon,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")

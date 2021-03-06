# Сервис по отслеживанию местоположений

Необходимо написать сервис для отслеживания местоположений курьеров. Состоит из 3 компонентов: REST API для получения данных от устройств, API для получения данных о местоположениях курьеров и небольшая админка (страница с картой, на которой отмечены последние координаты курьеров). 
Также необходимо покрыть API и админку авторизацией.

## Стэк:
Django
Python
PostgreSQL 

### Предполагаемая структура данных

```jsx
// Compaies - курьеры привязываются к организации
{
	id: 
	company_token: String
	created_at: Date
	updated_at: Date
}

// Devices -  регистрация каждого устройства (курьера)
{
	id:
	company_id:
	device_id: String
	device_model: String
	created_at: Date
	updated_at: Date
	app: String // Приложение с которого регистрацию прошли
	version: String
}

// Locations - координаты приходящие с устройств

{
	id:
	latitude:
	longitude:
	created_at: Date
	updated_at: Date
	company_id:
	device_id:
	data: json // Данные из устройств
}
```
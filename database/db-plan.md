# Restaurant Management App - Database Schema

## 1. Restaurants
Each restaurant can have multiple tables, menus, and orders.

| Column      | Type       | Notes          |
|------------|-----------|----------------|
| id         | UUID / INT | Primary key    |
| name       | VARCHAR    | Restaurant name|
| address    | VARCHAR    | Optional       |
| phone      | VARCHAR    | Optional       |
| created_at | TIMESTAMP  | Auto           |
| updated_at | TIMESTAMP  | Auto           |

---

## 2. Tables
Represents physical tables in a restaurant.

| Column        | Type       | Notes                          |
|---------------|-----------|--------------------------------|
| id            | UUID / INT | Primary key                    |
| restaurant_id | UUID / INT | FK → Restaurants.id           |
| table_number  | INT        | Unique per restaurant          |
| qr_code       | VARCHAR    | Link to menu/order page        |
| created_at    | TIMESTAMP  | Auto                           |
| updated_at    | TIMESTAMP  | Auto                           |

---

## 3. Menu Categories
Optional, for grouping menu items (Starters, Main Course, Drinks, etc.)

| Column        | Type       | Notes                |
|---------------|-----------|--------------------|
| id            | UUID / INT | Primary key        |
| restaurant_id | UUID / INT | FK → Restaurants.id|
| name          | VARCHAR    | Category name      |
| created_at    | TIMESTAMP  | Auto               |
| updated_at    | TIMESTAMP  | Auto               |

---

## 4. Menu Items

| Column        | Type       | Notes                 |
|---------------|-----------|---------------------|
| id            | UUID / INT | Primary key         |
| restaurant_id | UUID / INT | FK → Restaurants.id |
| category_id   | UUID / INT | FK → MenuCategories.id |
| name          | VARCHAR    | Item name           |
| description   | TEXT       | Optional            |
| price         | DECIMAL    | e.g., 12.99         |
| image_url     | VARCHAR    | Optional            |
| available     | BOOLEAN    | Default TRUE        |
| created_at    | TIMESTAMP  | Auto                |
| updated_at    | TIMESTAMP  | Auto                |

---

## 5. Orders
Each order corresponds to a table placing one or multiple items.

| Column        | Type       | Notes                              |
|---------------|-----------|-----------------------------------|
| id            | UUID / INT | Primary key                       |
| restaurant_id | UUID / INT | FK → Restaurants.id               |
| table_id      | UUID / INT | FK → Tables.id                     |
| status        | ENUM       | e.g., pending, preparing, served, paid |
| total_price   | DECIMAL    | Computed total                     |
| created_at    | TIMESTAMP  | Auto                               |
| updated_at    | TIMESTAMP  | Auto                               |

---

## 6. Order Items
Links an order to the menu items.

| Column        | Type       | Notes                   |
|---------------|-----------|------------------------|
| id            | UUID / INT | Primary key            |
| order_id      | UUID / INT | FK → Orders.id         |
| menu_item_id  | UUID / INT | FK → MenuItems.id      |
| quantity      | INT        | Default 1             |
| price         | DECIMAL    | Snapshot of price     |
| created_at    | TIMESTAMP  | Auto                  |
| updated_at    | TIMESTAMP  | Auto                  |

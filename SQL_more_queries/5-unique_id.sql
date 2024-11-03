-- Création de la table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

-- Insertion d'une entrée
INSERT INTO unique_id (id, name) VALUES (89, "Best School");

-- Autres insertions...


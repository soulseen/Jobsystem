CREATE TABLE `db`.`company` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `com_name` VARCHAR(45) NOT NULL,
  `url` VARCHAR(45) NOT NULL,
  `natural` VARCHAR(45) NULL,
  `scale` VARCHAR(45) NULL,
  `address` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `url_UNIQUE` (`url` ASC));
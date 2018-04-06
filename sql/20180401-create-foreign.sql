ALTER TABLE `db`.`python`
ADD CONSTRAINT `com_id_comid`
  FOREIGN KEY (`com_id`)
  REFERENCES `db`.`company` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
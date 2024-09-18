SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`tecnico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tecnico` (
  `idtecnico` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtecnico`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Sítio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Sítio` (
  `idSítio` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `CEP` VARCHAR(45) NOT NULL,
  `cidade` VARCHAR(45) NOT NULL,
  `endereço` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idSítio`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Foto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Foto` (
  `idFoto` INT NOT NULL AUTO_INCREMENT,
  `data_foto` DATE NOT NULL,
  `server_url` MEDIUMTEXT NOT NULL,
  `metadados` JSON NOT NULL,
  PRIMARY KEY (`idFotos`),
  INDEX `fk_Foto_Sítio1_idx` (`Sítio_idSítio` ASC) VISIBLE,
  CONSTRAINT `fk_Foto_Sítio1`
    FOREIGN KEY (`Sítio_idSítio`)
    REFERENCES `mydb`.`Sítio` (`idSítio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`administrador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`administrador` (
  `idautor` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idautor`))
ENGINE = InnoDB;

-- ----------------------------------------------------
-- Table `mydb`.`Empresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Empresa` (
  `idEmpresa` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idEmpresa`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`template`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`template` (
  `idtemplate` INT NOT NULL AUTO_INCREMENT,
  `pedidos_fotos` JSON NOT NULL,
  `administrador_idautor` INT NOT NULL,
  `Empresa_idEmpresa` INT NOT NULL,
  PRIMARY KEY (`idtemplate`),
  INDEX `fk_template_relatorio_administrador1_idx` (`administrador_idautor` ASC) VISIBLE,
  INDEX `fk_template_relatorio_Empresa1_idx` (`Empresa_idEmpresa` ASC) VISIBLE,
  CONSTRAINT `fk_template_relatorio_administrador1`
    FOREIGN KEY (`administrador_idautor`)
    REFERENCES `mydb`.`administrador` (`idautor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_template_relatorio_Empresa1`
    FOREIGN KEY (`Empresa_idEmpresa`)
    REFERENCES `mydb`.`Empresa` (`idEmpresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- ----------------------------------------------------
-- Table `mydb`.`relatorio_final`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`relatorio_final` (
  `idRelatório` INT NOT NULL AUTO_INCREMENT,
  `endereco_server` VARCHAR(90) NOT NULL,
  `tecnico_idtecnico` INT NOT NULL,
  `descricao` TEXT NOT NULL,
  `data_visita` DATE NOT NULL,
  `Foto_idFotos` INT NOT NULL,
  `Sítio_idSítio` INT NOT NULL,
  `template_idtemplate` INT NOT NULL,
  PRIMARY KEY (`idRelatório`),
  INDEX `fk_relatorio_tecnico1_idx` (`tecnico_idtecnico` ASC) VISIBLE,
  INDEX `fk_relatorio_final_Foto1_idx` (`Foto_idFotos` ASC) VISIBLE,
  INDEX `fk_relatorio_final_Sítio1_idx` (`Sítio_idSítio` ASC) VISIBLE,
  INDEX `fk_relatorio_final_template_relatorio1_idx` (`template_idtemplate` ASC) VISIBLE,
  CONSTRAINT `fk_relatorio_tecnico1`
    FOREIGN KEY (`tecnico_idtecnico`)
    REFERENCES `mydb`.`tecnico` (`idtecnico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_relatorio_final_Foto1`
    FOREIGN KEY (`Foto_idFotos`)
    REFERENCES `mydb`.`Foto` (`idFotos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_relatorio_final_Sítio1`
    FOREIGN KEY (`Sítio_idSítio`)
    REFERENCES `mydb`.`Sítio` (`idSítio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_relatorio_final_template_relatorio1`
    FOREIGN KEY (`template_idtemplate`)
    REFERENCES `mydb`.`template` (`idtemplate`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`n adminstram m tecnimos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`n adminstram m tecnimos` (
  `administrador_idautor` INT NOT NULL AUTO_INCREMENT,
  `tecnico_idtecnico` INT NOT NULL,
  PRIMARY KEY (`administrador_idautor`, `tecnico_idtecnico`),
  INDEX `fk_administrador_has_tecnico_tecnico1_idx` (`tecnico_idtecnico` ASC) VISIBLE,
  INDEX `fk_administrador_has_tecnico_administrador1_idx` (`administrador_idautor` ASC) VISIBLE,
  CONSTRAINT `fk_administrador_has_tecnico_administrador1`
    FOREIGN KEY (`administrador_idautor`)
    REFERENCES `mydb`.`administrador` (`idautor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_administrador_has_tecnico_tecnico1`
    FOREIGN KEY (`tecnico_idtecnico`)
    REFERENCES `mydb`.`tecnico` (`idtecnico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

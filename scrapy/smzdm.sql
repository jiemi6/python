CREATE TABLE `NewTable` (
`id`  varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
`title`  varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
`price`  varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
`link`  varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
`zhide`  varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
`buzhi`  varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
`collectNum`  varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
`commentNum`  varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
`publishTime`  varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
`store`  varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL ,
`timesort`  bigint(20) NOT NULL ,
`timeStr`  timestamp NULL DEFAULT NULL ,
PRIMARY KEY (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4 COLLATE=utf8mb4_general_ci
ROW_FORMAT=DYNAMIC
;


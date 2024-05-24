template_4obj_cc = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03, "PNG_FILE") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04, "PNG_FILE") { SPRITE04 }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_elev, "PNG_FILE") { SPRITE_elev01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02_elev, "PNG_FILE") { SPRITE_elev02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03_elev, "PNG_FILE") { SPRITE_elev03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04_elev, "PNG_FILE") { SPRITE_elev04 }

spritelayout NAME_OF_OBJECT_VAR01_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR01_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR01, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR01_3;
            1: NAME_OF_OBJECT_VAR01_4;
            2: NAME_OF_OBJECT_VAR01_8;
            3: NAME_OF_OBJECT_VAR01_2;
            4: NAME_OF_OBJECT_VAR01_6;
            5: NAME_OF_OBJECT_VAR01_5;
            6: NAME_OF_OBJECT_VAR01_7;
            7: NAME_OF_OBJECT_VAR01_1;
            8: NAME_OF_OBJECT_VAR01_3;
            9: NAME_OF_OBJECT_VAR01_4;
            10: NAME_OF_OBJECT_VAR01_8;
            11: NAME_OF_OBJECT_VAR01_2;
            12: NAME_OF_OBJECT_VAR01_6;
            13: NAME_OF_OBJECT_VAR01_5;
            14: NAME_OF_OBJECT_VAR01_7;
        NAME_OF_OBJECT_VAR01_9;
}

spritelayout NAME_OF_OBJECT_VAR02_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR02_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR02, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR02_3;
            1: NAME_OF_OBJECT_VAR02_4;
            2: NAME_OF_OBJECT_VAR02_8;
            3: NAME_OF_OBJECT_VAR02_2;
            4: NAME_OF_OBJECT_VAR02_6;
            5: NAME_OF_OBJECT_VAR02_5;
            6: NAME_OF_OBJECT_VAR02_7;
            7: NAME_OF_OBJECT_VAR02_1;
            8: NAME_OF_OBJECT_VAR02_3;
            9: NAME_OF_OBJECT_VAR02_4;
            10: NAME_OF_OBJECT_VAR02_8;
            11: NAME_OF_OBJECT_VAR02_2;
            12: NAME_OF_OBJECT_VAR02_6;
            13: NAME_OF_OBJECT_VAR02_5;
            14: NAME_OF_OBJECT_VAR02_7;
        NAME_OF_OBJECT_VAR02_9;
}

spritelayout NAME_OF_OBJECT_VAR03_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR03_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR03, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR03_3;
            1: NAME_OF_OBJECT_VAR03_4;
            2: NAME_OF_OBJECT_VAR03_8;
            3: NAME_OF_OBJECT_VAR03_2;
            4: NAME_OF_OBJECT_VAR03_6;
            5: NAME_OF_OBJECT_VAR03_5;
            6: NAME_OF_OBJECT_VAR03_7;
            7: NAME_OF_OBJECT_VAR03_1;
            8: NAME_OF_OBJECT_VAR03_3;
            9: NAME_OF_OBJECT_VAR03_4;
            10: NAME_OF_OBJECT_VAR03_8;
            11: NAME_OF_OBJECT_VAR03_2;
            12: NAME_OF_OBJECT_VAR03_6;
            13: NAME_OF_OBJECT_VAR03_5;
            14: NAME_OF_OBJECT_VAR03_7;
        NAME_OF_OBJECT_VAR03_9;
}

spritelayout NAME_OF_OBJECT_VAR04_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR04_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR04, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR04_3;
            1: NAME_OF_OBJECT_VAR04_4;
            2: NAME_OF_OBJECT_VAR04_8;
            3: NAME_OF_OBJECT_VAR04_2;
            4: NAME_OF_OBJECT_VAR04_6;
            5: NAME_OF_OBJECT_VAR04_5;
            6: NAME_OF_OBJECT_VAR04_7;
            7: NAME_OF_OBJECT_VAR04_1;
            8: NAME_OF_OBJECT_VAR04_3;
            9: NAME_OF_OBJECT_VAR04_4;
            10: NAME_OF_OBJECT_VAR04_8;
            11: NAME_OF_OBJECT_VAR04_2;
            12: NAME_OF_OBJECT_VAR04_6;
            13: NAME_OF_OBJECT_VAR04_5;
            14: NAME_OF_OBJECT_VAR04_7;
        NAME_OF_OBJECT_VAR04_9;
}

switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT, view) {
            0: NAME_OF_OBJECT_VAR01;
            1: NAME_OF_OBJECT_VAR02;
            2: NAME_OF_OBJECT_VAR03;
            3: NAME_OF_OBJECT_VAR04;
}
switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_menu, view) {
            0: NAME_OF_OBJECT_VAR01_menu;
            1: NAME_OF_OBJECT_VAR02_menu;
            2: NAME_OF_OBJECT_VAR03_menu;
            3: NAME_OF_OBJECT_VAR04_menu;
}

item (FEAT_OBJECTS, NAME_OF_OBJECT, NUMERO) {
    property {
        class:                  "CATEGORY";
        classname:              NAME_OF_CAT;
        name:                   NAME_IN_MENU;
        climates_available:     ALL_CLIMATES;
        size:                   SIZE;
        build_cost_multiplier:  1;
        remove_cost_multiplier: 1;
        introduction_date:      0x00000000;
        end_of_life_date:       0xFFFFFFFF;
        object_flags:           (param_scenario_editor==1 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) :
                                ( (param_scenario_editor==1 && param_irremovable==0) ? bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) :
                                    ((param_scenario_editor==0 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) : bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE)));
        height:                 2;
        num_views:              4;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT;
        purchase:               switch_NAME_OF_OBJECT_menu;
    }
}

"""

template_4obj = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03, "PNG_FILE") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04, "PNG_FILE") { SPRITE04 }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_elev, "PNG_FILE") { SPRITE_elev01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02_elev, "PNG_FILE") { SPRITE_elev02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03_elev, "PNG_FILE") { SPRITE_elev03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04_elev, "PNG_FILE") { SPRITE_elev04 }

spritelayout NAME_OF_OBJECT_VAR01_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR01_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR01, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR01_3;
            1: NAME_OF_OBJECT_VAR01_4;
            2: NAME_OF_OBJECT_VAR01_8;
            3: NAME_OF_OBJECT_VAR01_2;
            4: NAME_OF_OBJECT_VAR01_6;
            5: NAME_OF_OBJECT_VAR01_5;
            6: NAME_OF_OBJECT_VAR01_7;
            7: NAME_OF_OBJECT_VAR01_1;
            8: NAME_OF_OBJECT_VAR01_3;
            9: NAME_OF_OBJECT_VAR01_4;
            10: NAME_OF_OBJECT_VAR01_8;
            11: NAME_OF_OBJECT_VAR01_2;
            12: NAME_OF_OBJECT_VAR01_6;
            13: NAME_OF_OBJECT_VAR01_5;
            14: NAME_OF_OBJECT_VAR01_7;
        NAME_OF_OBJECT_VAR01_9;
}

spritelayout NAME_OF_OBJECT_VAR02_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR02_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02(0);
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR02, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR02_3;
            1: NAME_OF_OBJECT_VAR02_4;
            2: NAME_OF_OBJECT_VAR02_8;
            3: NAME_OF_OBJECT_VAR02_2;
            4: NAME_OF_OBJECT_VAR02_6;
            5: NAME_OF_OBJECT_VAR02_5;
            6: NAME_OF_OBJECT_VAR02_7;
            7: NAME_OF_OBJECT_VAR02_1;
            8: NAME_OF_OBJECT_VAR02_3;
            9: NAME_OF_OBJECT_VAR02_4;
            10: NAME_OF_OBJECT_VAR02_8;
            11: NAME_OF_OBJECT_VAR02_2;
            12: NAME_OF_OBJECT_VAR02_6;
            13: NAME_OF_OBJECT_VAR02_5;
            14: NAME_OF_OBJECT_VAR02_7;
        NAME_OF_OBJECT_VAR02_9;
}

spritelayout NAME_OF_OBJECT_VAR03_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR03_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03(0);
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR03, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR03_3;
            1: NAME_OF_OBJECT_VAR03_4;
            2: NAME_OF_OBJECT_VAR03_8;
            3: NAME_OF_OBJECT_VAR03_2;
            4: NAME_OF_OBJECT_VAR03_6;
            5: NAME_OF_OBJECT_VAR03_5;
            6: NAME_OF_OBJECT_VAR03_7;
            7: NAME_OF_OBJECT_VAR03_1;
            8: NAME_OF_OBJECT_VAR03_3;
            9: NAME_OF_OBJECT_VAR03_4;
            10: NAME_OF_OBJECT_VAR03_8;
            11: NAME_OF_OBJECT_VAR03_2;
            12: NAME_OF_OBJECT_VAR03_6;
            13: NAME_OF_OBJECT_VAR03_5;
            14: NAME_OF_OBJECT_VAR03_7;
        NAME_OF_OBJECT_VAR03_9;
}

spritelayout NAME_OF_OBJECT_VAR04_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR04_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_GRN_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04(0);
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR04, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR04_3;
            1: NAME_OF_OBJECT_VAR04_4;
            2: NAME_OF_OBJECT_VAR04_8;
            3: NAME_OF_OBJECT_VAR04_2;
            4: NAME_OF_OBJECT_VAR04_6;
            5: NAME_OF_OBJECT_VAR04_5;
            6: NAME_OF_OBJECT_VAR04_7;
            7: NAME_OF_OBJECT_VAR04_1;
            8: NAME_OF_OBJECT_VAR04_3;
            9: NAME_OF_OBJECT_VAR04_4;
            10: NAME_OF_OBJECT_VAR04_8;
            11: NAME_OF_OBJECT_VAR04_2;
            12: NAME_OF_OBJECT_VAR04_6;
            13: NAME_OF_OBJECT_VAR04_5;
            14: NAME_OF_OBJECT_VAR04_7;
        NAME_OF_OBJECT_VAR04_9;
}

switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT, view) {
            0: NAME_OF_OBJECT_VAR01;
            1: NAME_OF_OBJECT_VAR02;
            2: NAME_OF_OBJECT_VAR03;
            3: NAME_OF_OBJECT_VAR04;
}
switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_menu, view) {
            0: NAME_OF_OBJECT_VAR01_menu;
            1: NAME_OF_OBJECT_VAR02_menu;
            2: NAME_OF_OBJECT_VAR03_menu;
            3: NAME_OF_OBJECT_VAR04_menu;
}

item (FEAT_OBJECTS, NAME_OF_OBJECT, NUMERO) {
    property {
        class:                  "CATEGORY";
        classname:              NAME_OF_CAT;
        name:                   NAME_IN_MENU;
        climates_available:     ALL_CLIMATES;
        size:                   SIZE;
        build_cost_multiplier:  1;
        remove_cost_multiplier: 1;
        introduction_date:      0x00000000;
        end_of_life_date:       0xFFFFFFFF;
        object_flags:           (param_scenario_editor==1 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) :
                                ( (param_scenario_editor==1 && param_irremovable==0) ? bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) :
                                    ((param_scenario_editor==0 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) : bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE)));
        height:                 2;
        num_views:              4;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT;
        purchase:               switch_NAME_OF_OBJECT_menu;
    }
}

"""

template_Transition_tiles = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01_OFGX, "gfx/ground_transition_type2.png") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02_OFGX, "gfx/ground_transition_type2.png") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03_OFGX, "gfx/ground_transition_type2.png") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04_OFGX, "gfx/ground_transition_type2.png") { SPRITE04 }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_TYPE1, "gfx/ground_transition_type1.png") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02_TYPE1, "gfx/ground_transition_type1.png") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03_TYPE1, "gfx/ground_transition_type1.png") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04_TYPE1, "gfx/ground_transition_type1.png") { SPRITE04 }

spritelayout layout_NAME_OF_OBJECT_VAR01 {
    ground { sprite: spriteset_GRN_EMPTY; }
    childsprite   { sprite: LOAD_TEMP(1); }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01_OFGX;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01_TYPE1;
               hide_sprite: param_ground;
               always_draw: 0; } }
spritelayout layout_NAME_OF_OBJECT_VAR02 {
    ground { sprite: spriteset_GRN_EMPTY; }
    childsprite   { sprite: LOAD_TEMP(1); }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02_OFGX;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02_TYPE1;
               hide_sprite: param_ground;
               always_draw: 0; } }
spritelayout layout_NAME_OF_OBJECT_VAR03 {
    ground { sprite: spriteset_GRN_EMPTY; }
    childsprite   { sprite: LOAD_TEMP(1); }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR03_OFGX;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR03_TYPE1;
               hide_sprite: param_ground;
               always_draw: 0; } }
spritelayout layout_NAME_OF_OBJECT_VAR04 {
    ground { sprite: spriteset_GRN_EMPTY; }
    childsprite   { sprite: LOAD_TEMP(1); }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR04_OFGX;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR04_TYPE1;
               hide_sprite: param_ground;
               always_draw: 0; } }

spritelayout layout_NAME_OF_OBJECT_VAR01_menu {
    ground { sprite: GROUNDSPRITE_NORMAL; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01_OFGX;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01_TYPE1;
               hide_sprite: param_ground;
               always_draw: 0; } }
spritelayout layout_NAME_OF_OBJECT_VAR02_menu {
    ground { sprite: GROUNDSPRITE_NORMAL; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02_OFGX;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02_TYPE1;
               hide_sprite: param_ground;
               always_draw: 0; } }
spritelayout layout_NAME_OF_OBJECT_VAR03_menu {
    ground { sprite: GROUNDSPRITE_NORMAL; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR03_OFGX;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR03_TYPE1;
               hide_sprite: param_ground;
               always_draw: 0; } }
spritelayout layout_NAME_OF_OBJECT_VAR04_menu {
    ground { sprite: GROUNDSPRITE_NORMAL; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR04_OFGX;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR04_TYPE1;
               hide_sprite: param_ground;
               always_draw: 0; } }

switch (FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_VAR_view, view) {
    0: layout_NAME_OF_OBJECT_VAR01;
    1: layout_NAME_OF_OBJECT_VAR02;
    2: layout_NAME_OF_OBJECT_VAR03;
    3: layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS, SELF, switch_TERRAIN_NAME_OF_OBJECT, [
    STORE_TEMP( (nearby_tile_terrain_type(0,0) == TILETYPE_DESERT) * GROUNDSPRITE_DESERT, 1),
    STORE_TEMP( LOAD_TEMP(1) + (LOAD_TEMP(1) == 0) * 4512 * (nearby_tile_terrain_type( 1, 0) == TILETYPE_DESERT), 1),
    STORE_TEMP( LOAD_TEMP(1) + (LOAD_TEMP(1) == 0) * 4512 * (nearby_tile_terrain_type(-1, 0) == TILETYPE_DESERT), 1),
    STORE_TEMP( LOAD_TEMP(1) + (LOAD_TEMP(1) == 0) * 4512 * (nearby_tile_terrain_type( 0, 1) == TILETYPE_DESERT), 1),
    STORE_TEMP( LOAD_TEMP(1) + (LOAD_TEMP(1) == 0) * 4512 * (nearby_tile_terrain_type( 0,-1) == TILETYPE_DESERT), 1),
    STORE_TEMP( LOAD_TEMP(1) + (LOAD_TEMP(1) == 0) * GROUNDSPRITE_NORMAL, 1),
    STORE_TEMP(terrain_type == TILETYPE_SNOW   ? GROUNDSPRITE_SNOW : LOAD_TEMP(1), 1),
    STORE_TEMP(snowline_height == 0xFF ? 0xFF : nearby_tile_height(0,0) - snowline_height, 127),
    STORE_TEMP((LOAD_TEMP(127) == -1) ? GROUNDSPRITE_SNOW_1_4 : LOAD_TEMP(1), 1),
    STORE_TEMP((LOAD_TEMP(127) ==  0) ? GROUNDSPRITE_SNOW_2_4 : LOAD_TEMP(1), 1),
    STORE_TEMP((LOAD_TEMP(127) ==  1) ? GROUNDSPRITE_SNOW_3_4 : LOAD_TEMP(1), 1) ])
    { switch_NAME_OF_OBJECT_VAR_view; }
switch (FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_VAR_menu, view) {
    0: layout_NAME_OF_OBJECT_VAR01_menu;
    1: layout_NAME_OF_OBJECT_VAR02_menu;
    2: layout_NAME_OF_OBJECT_VAR03_menu;
    3: layout_NAME_OF_OBJECT_VAR04_menu; }

item (FEAT_OBJECTS, NAME_OF_OBJECT, NUMERO) {
    property {
        class:                  "CATEGORY";
        classname:              NAME_OF_CAT;
        name:                   NAME_IN_MENU;
        climates_available:     ALL_CLIMATES;
        size:                   SIZE;
        build_cost_multiplier:  1;
        remove_cost_multiplier: 1;
        introduction_date:      0x00000000;
        end_of_life_date:       0xFFFFFFFF;
        object_flags:           (param_scenario_editor==1 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) :
                                ( (param_scenario_editor==1 && param_irremovable==0) ? bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) :
                                    ((param_scenario_editor==0 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) : bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE)));
        height:                 2;
        num_views:              4;
    }
    graphics {
        default:                switch_TERRAIN_NAME_OF_OBJECT;
        purchase:               switch_NAME_OF_OBJECT_VAR_menu;
    }
}

"""

template_Water_based_tiles = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03, "PNG_FILE") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04, "PNG_FILE") { SPRITE04 }

spritelayout layout_NAME_OF_OBJECT_VAR01 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: spriteset_SPRITE01_GROUND_TYPE2;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_SPRITE01_GROUND_TYPE1;
               hide_sprite: param_ground; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01;
               always_draw: 1; } }
spritelayout layout_NAME_OF_OBJECT_VAR02 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: spriteset_SPRITE02_GROUND_TYPE2;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_SPRITE02_GROUND_TYPE1;
               hide_sprite: param_ground; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02;
               always_draw: 1; } }
spritelayout layout_NAME_OF_OBJECT_VAR03 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: spriteset_SPRITE03_GROUND_TYPE2;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_SPRITE03_GROUND_TYPE1;
               hide_sprite: param_ground; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR03;
               always_draw: 1; } }
spritelayout layout_NAME_OF_OBJECT_VAR04 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: spriteset_SPRITE04_GROUND_TYPE2;
               hide_sprite: (1 - param_ground);
               always_draw: 0; }
    building { sprite: spriteset_SPRITE04_GROUND_TYPE1;
               hide_sprite: param_ground; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR04;
               always_draw: 1; } }
switch (FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_VAR_view, view) {
    0: layout_NAME_OF_OBJECT_VAR01;
    1: layout_NAME_OF_OBJECT_VAR02;
    2: layout_NAME_OF_OBJECT_VAR03;
    3: layout_NAME_OF_OBJECT_VAR04; }

item (FEAT_OBJECTS, NAME_OF_OBJECT, NUMERO) {
    property {
        class:                  "CATEGORY";
        classname:              NAME_OF_CAT;
        name:                   NAME_IN_MENU;
        climates_available:     ALL_CLIMATES;
        size:                   SIZE;
        build_cost_multiplier:  1;
        remove_cost_multiplier: 1;
        introduction_date:      0x00000000;
        end_of_life_date:       0xFFFFFFFF;
        object_flags:           (param_scenario_editor==1 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) :
                                ( (param_scenario_editor==1 && param_irremovable==0) ? bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) :
                                    ((param_scenario_editor==0 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) : bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE)));
        height:                 2;
        num_views:              4;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT_VAR_view;
        purchase:               switch_NAME_OF_OBJECT_VAR_view;
    }
}

"""

template_Dock_overlapping_tiles = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03, "PNG_FILE") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04, "PNG_FILE") { SPRITE04 }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_elev, "PNG_FILE") { SPRITE_elev01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02_elev, "PNG_FILE") { SPRITE_elev02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03_elev, "PNG_FILE") { SPRITE_elev03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04_elev, "PNG_FILE") { SPRITE_elev04 }

spritelayout NAME_OF_OBJECT_VAR01_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR01_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR01, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR01_3;
            1: NAME_OF_OBJECT_VAR01_4;
            2: NAME_OF_OBJECT_VAR01_8;
            3: NAME_OF_OBJECT_VAR01_2;
            4: NAME_OF_OBJECT_VAR01_6;
            5: NAME_OF_OBJECT_VAR01_5;
            6: NAME_OF_OBJECT_VAR01_7;
            7: NAME_OF_OBJECT_VAR01_1;
            8: NAME_OF_OBJECT_VAR01_3;
            9: NAME_OF_OBJECT_VAR01_4;
            10: NAME_OF_OBJECT_VAR01_8;
            11: NAME_OF_OBJECT_VAR01_2;
            12: NAME_OF_OBJECT_VAR01_6;
            13: NAME_OF_OBJECT_VAR01_5;
            14: NAME_OF_OBJECT_VAR01_7;
        NAME_OF_OBJECT_VAR01_9;
}

spritelayout NAME_OF_OBJECT_VAR02_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR02_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02(0);
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR02, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR02_3;
            1: NAME_OF_OBJECT_VAR02_4;
            2: NAME_OF_OBJECT_VAR02_8;
            3: NAME_OF_OBJECT_VAR02_2;
            4: NAME_OF_OBJECT_VAR02_6;
            5: NAME_OF_OBJECT_VAR02_5;
            6: NAME_OF_OBJECT_VAR02_7;
            7: NAME_OF_OBJECT_VAR02_1;
            8: NAME_OF_OBJECT_VAR02_3;
            9: NAME_OF_OBJECT_VAR02_4;
            10: NAME_OF_OBJECT_VAR02_8;
            11: NAME_OF_OBJECT_VAR02_2;
            12: NAME_OF_OBJECT_VAR02_6;
            13: NAME_OF_OBJECT_VAR02_5;
            14: NAME_OF_OBJECT_VAR02_7;
        NAME_OF_OBJECT_VAR02_9;
}

spritelayout NAME_OF_OBJECT_VAR03_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR03_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03(0);
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR03, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR03_3;
            1: NAME_OF_OBJECT_VAR03_4;
            2: NAME_OF_OBJECT_VAR03_8;
            3: NAME_OF_OBJECT_VAR03_2;
            4: NAME_OF_OBJECT_VAR03_6;
            5: NAME_OF_OBJECT_VAR03_5;
            6: NAME_OF_OBJECT_VAR03_7;
            7: NAME_OF_OBJECT_VAR03_1;
            8: NAME_OF_OBJECT_VAR03_3;
            9: NAME_OF_OBJECT_VAR03_4;
            10: NAME_OF_OBJECT_VAR03_8;
            11: NAME_OF_OBJECT_VAR03_2;
            12: NAME_OF_OBJECT_VAR03_6;
            13: NAME_OF_OBJECT_VAR03_5;
            14: NAME_OF_OBJECT_VAR03_7;
        NAME_OF_OBJECT_VAR03_9;
}

spritelayout NAME_OF_OBJECT_VAR04_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR04_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04(0);
                always_draw: 0;
                hide_sprite: 0; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR04, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR04_3;
            1: NAME_OF_OBJECT_VAR04_4;
            2: NAME_OF_OBJECT_VAR04_8;
            3: NAME_OF_OBJECT_VAR04_2;
            4: NAME_OF_OBJECT_VAR04_6;
            5: NAME_OF_OBJECT_VAR04_5;
            6: NAME_OF_OBJECT_VAR04_7;
            7: NAME_OF_OBJECT_VAR04_1;
            8: NAME_OF_OBJECT_VAR04_3;
            9: NAME_OF_OBJECT_VAR04_4;
            10: NAME_OF_OBJECT_VAR04_8;
            11: NAME_OF_OBJECT_VAR04_2;
            12: NAME_OF_OBJECT_VAR04_6;
            13: NAME_OF_OBJECT_VAR04_5;
            14: NAME_OF_OBJECT_VAR04_7;
        NAME_OF_OBJECT_VAR04_9;
}

switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT, view) {
            0: NAME_OF_OBJECT_VAR01;
            1: NAME_OF_OBJECT_VAR02;
            2: NAME_OF_OBJECT_VAR03;
            3: NAME_OF_OBJECT_VAR04;
}
switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_menu, view) {
            0: NAME_OF_OBJECT_VAR01_menu;
            1: NAME_OF_OBJECT_VAR02_menu;
            2: NAME_OF_OBJECT_VAR03_menu;
            3: NAME_OF_OBJECT_VAR04_menu;
}

item (FEAT_OBJECTS, NAME_OF_OBJECT, NUMERO) {
    property {
        class:                  "CATEGORY";
        classname:              NAME_OF_CAT;
        name:                   NAME_IN_MENU;
        climates_available:     ALL_CLIMATES;
        size:                   SIZE;
        build_cost_multiplier:  1;
        remove_cost_multiplier: 1;
        introduction_date:      0x00000000;
        end_of_life_date:       0xFFFFFFFF;
        object_flags:           (param_scenario_editor==1 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) :
                                ( (param_scenario_editor==1 && param_irremovable==0) ? bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) :
                                    ((param_scenario_editor==0 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) : bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE)));
        height:                 2;
        num_views:              4;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT;
        purchase:               switch_NAME_OF_OBJECT_menu;
    }
}

"""

template_Dock_overlapping_tiles_water = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03, "PNG_FILE") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04, "PNG_FILE") { SPRITE04 }

spritelayout layout_NAME_OF_OBJECT_VAR01 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: GROUNDSPRITE_WATER;
               yoffset: -16; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01; } }
spritelayout layout_NAME_OF_OBJECT_VAR02 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: GROUNDSPRITE_WATER;
               xoffset: -16; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02; } }
spritelayout layout_NAME_OF_OBJECT_VAR03 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: GROUNDSPRITE_WATER;
               yoffset: -16;  }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR03; } }
spritelayout layout_NAME_OF_OBJECT_VAR04 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: GROUNDSPRITE_WATER;
               xoffset: -16; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR04; } }

switch (FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_VAR_view, view) {
    0: layout_NAME_OF_OBJECT_VAR01;
    1: layout_NAME_OF_OBJECT_VAR02;
    2: layout_NAME_OF_OBJECT_VAR03;
    3: layout_NAME_OF_OBJECT_VAR04; }

item (FEAT_OBJECTS, NAME_OF_OBJECT, NUMERO) {
    property {
        class:                  "CATEGORY";
        classname:              NAME_OF_CAT;
        name:                   NAME_IN_MENU;
        climates_available:     ALL_CLIMATES;
        size:                   SIZE;
        build_cost_multiplier:  1;
        remove_cost_multiplier: 1;
        introduction_date:      0x00000000;
        end_of_life_date:       0xFFFFFFFF;
        object_flags:           (param_scenario_editor==1 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) :
                                ( (param_scenario_editor==1 && param_irremovable==0) ? bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) :
                                    ((param_scenario_editor==0 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) : bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE)));
        height:                 2;
        num_views:              4;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT_VAR_view;
        purchase:               switch_NAME_OF_OBJECT_VAR_view;
    }
}

"""

template_Dock_overlapping_tiles_cc = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03, "PNG_FILE") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04, "PNG_FILE") { SPRITE04 }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_elev, "PNG_FILE") { SPRITE_elev01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02_elev, "PNG_FILE") { SPRITE_elev02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03_elev, "PNG_FILE") { SPRITE_elev03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04_elev, "PNG_FILE") { SPRITE_elev04 }

spritelayout NAME_OF_OBJECT_VAR01_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
}
spritelayout NAME_OF_OBJECT_VAR01_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR01_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR01_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR01_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR01_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR01_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR01_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE01_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR01, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR01_3;
            1: NAME_OF_OBJECT_VAR01_4;
            2: NAME_OF_OBJECT_VAR01_8;
            3: NAME_OF_OBJECT_VAR01_2;
            4: NAME_OF_OBJECT_VAR01_6;
            5: NAME_OF_OBJECT_VAR01_5;
            6: NAME_OF_OBJECT_VAR01_7;
            7: NAME_OF_OBJECT_VAR01_1;
            8: NAME_OF_OBJECT_VAR01_3;
            9: NAME_OF_OBJECT_VAR01_4;
            10: NAME_OF_OBJECT_VAR01_8;
            11: NAME_OF_OBJECT_VAR01_2;
            12: NAME_OF_OBJECT_VAR01_6;
            13: NAME_OF_OBJECT_VAR01_5;
            14: NAME_OF_OBJECT_VAR01_7;
        NAME_OF_OBJECT_VAR01_9;
}

spritelayout NAME_OF_OBJECT_VAR02_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
}
spritelayout NAME_OF_OBJECT_VAR02_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR02_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR02_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR02_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR02_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR02_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR02_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE02_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR02, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR02_3;
            1: NAME_OF_OBJECT_VAR02_4;
            2: NAME_OF_OBJECT_VAR02_8;
            3: NAME_OF_OBJECT_VAR02_2;
            4: NAME_OF_OBJECT_VAR02_6;
            5: NAME_OF_OBJECT_VAR02_5;
            6: NAME_OF_OBJECT_VAR02_7;
            7: NAME_OF_OBJECT_VAR02_1;
            8: NAME_OF_OBJECT_VAR02_3;
            9: NAME_OF_OBJECT_VAR02_4;
            10: NAME_OF_OBJECT_VAR02_8;
            11: NAME_OF_OBJECT_VAR02_2;
            12: NAME_OF_OBJECT_VAR02_6;
            13: NAME_OF_OBJECT_VAR02_5;
            14: NAME_OF_OBJECT_VAR02_7;
        NAME_OF_OBJECT_VAR02_9;
}

spritelayout NAME_OF_OBJECT_VAR03_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
}
spritelayout NAME_OF_OBJECT_VAR03_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR03_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR03_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR03_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR03_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR03_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR03_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE03_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR03, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR03_3;
            1: NAME_OF_OBJECT_VAR03_4;
            2: NAME_OF_OBJECT_VAR03_8;
            3: NAME_OF_OBJECT_VAR03_2;
            4: NAME_OF_OBJECT_VAR03_6;
            5: NAME_OF_OBJECT_VAR03_5;
            6: NAME_OF_OBJECT_VAR03_7;
            7: NAME_OF_OBJECT_VAR03_1;
            8: NAME_OF_OBJECT_VAR03_3;
            9: NAME_OF_OBJECT_VAR03_4;
            10: NAME_OF_OBJECT_VAR03_8;
            11: NAME_OF_OBJECT_VAR03_2;
            12: NAME_OF_OBJECT_VAR03_6;
            13: NAME_OF_OBJECT_VAR03_5;
            14: NAME_OF_OBJECT_VAR03_7;
        NAME_OF_OBJECT_VAR03_9;
}

spritelayout NAME_OF_OBJECT_VAR04_1 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
}
spritelayout NAME_OF_OBJECT_VAR04_2 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR04_3 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_4 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_5 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR04_6 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04_7 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR04_8 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04_elev(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR04_9 {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
    }
spritelayout NAME_OF_OBJECT_VAR04_menu {
            ground { sprite: spriteset_GRN_EMPTY; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE1(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_SPRITE04_GROUND_TYPE2(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04(0);
                always_draw: 0;
                hide_sprite: 0;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR04, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR04_3;
            1: NAME_OF_OBJECT_VAR04_4;
            2: NAME_OF_OBJECT_VAR04_8;
            3: NAME_OF_OBJECT_VAR04_2;
            4: NAME_OF_OBJECT_VAR04_6;
            5: NAME_OF_OBJECT_VAR04_5;
            6: NAME_OF_OBJECT_VAR04_7;
            7: NAME_OF_OBJECT_VAR04_1;
            8: NAME_OF_OBJECT_VAR04_3;
            9: NAME_OF_OBJECT_VAR04_4;
            10: NAME_OF_OBJECT_VAR04_8;
            11: NAME_OF_OBJECT_VAR04_2;
            12: NAME_OF_OBJECT_VAR04_6;
            13: NAME_OF_OBJECT_VAR04_5;
            14: NAME_OF_OBJECT_VAR04_7;
        NAME_OF_OBJECT_VAR04_9;
}

switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT, view) {
            0: NAME_OF_OBJECT_VAR01;
            1: NAME_OF_OBJECT_VAR02;
            2: NAME_OF_OBJECT_VAR03;
            3: NAME_OF_OBJECT_VAR04;
}
switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_menu, view) {
            0: NAME_OF_OBJECT_VAR01_menu;
            1: NAME_OF_OBJECT_VAR02_menu;
            2: NAME_OF_OBJECT_VAR03_menu;
            3: NAME_OF_OBJECT_VAR04_menu;
}

item (FEAT_OBJECTS, NAME_OF_OBJECT, NUMERO) {
    property {
        class:                  "CATEGORY";
        classname:              NAME_OF_CAT;
        name:                   NAME_IN_MENU;
        climates_available:     ALL_CLIMATES;
        size:                   SIZE;
        build_cost_multiplier:  1;
        remove_cost_multiplier: 1;
        introduction_date:      0x00000000;
        end_of_life_date:       0xFFFFFFFF;
        object_flags:           (param_scenario_editor==1 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) :
                                ( (param_scenario_editor==1 && param_irremovable==0) ? bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) :
                                    ((param_scenario_editor==0 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE) : bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_NO_FOUNDATIONS,OBJ_FLAG_ALLOW_BRIDGE)));
        height:                 2;
        num_views:              4;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT;
        purchase:               switch_NAME_OF_OBJECT_menu;
    }
}

"""

template_Ships = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03, "PNG_FILE") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04, "PNG_FILE") { SPRITE04 }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_WATER, "PNG_FILE") { SPRITE_WATER01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02_WATER, "PNG_FILE") { SPRITE_WATER02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03_WATER, "PNG_FILE") { SPRITE_WATER03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04_WATER, "PNG_FILE") { SPRITE_WATER04 }

spritelayout layout_NAME_OF_OBJECT_VAR01 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01;
                recolour_mode: RECOLOUR_REMAP;
                palette: LOAD_TEMP(3); }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01_WATER;
               always_draw: 0; } }
spritelayout layout_NAME_OF_OBJECT_VAR02 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02;
                recolour_mode: RECOLOUR_REMAP;
                palette: LOAD_TEMP(3); }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02_WATER;
               always_draw: 0; } }
spritelayout layout_NAME_OF_OBJECT_VAR03 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR03;
                recolour_mode: RECOLOUR_REMAP;
                palette: LOAD_TEMP(3); }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR03_WATER;
               always_draw: 0; } }
spritelayout layout_NAME_OF_OBJECT_VAR04 {
    ground { sprite: GROUNDSPRITE_WATER; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR04;
                recolour_mode: RECOLOUR_REMAP;
                palette: LOAD_TEMP(3); }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR04_WATER;
               always_draw: 0; } }

switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_1, [STORE_TEMP(775, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_2, [STORE_TEMP(776, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_3, [STORE_TEMP(777, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_4, [STORE_TEMP(778, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_5, [STORE_TEMP(779, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_6, [STORE_TEMP(780, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_7, [STORE_TEMP(781, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_8, [STORE_TEMP(782, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_9, [STORE_TEMP(783, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_10,[STORE_TEMP(784, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_11,[STORE_TEMP(785, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_12,[STORE_TEMP(786, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_13,[STORE_TEMP(787, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_14,[STORE_TEMP(788, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_15,[STORE_TEMP(789, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR01_16,[STORE_TEMP(790, 3)]) { layout_NAME_OF_OBJECT_VAR01; }
random_switch (FEAT_OBJECTS, SELF, colour_NAME_OF_OBJECT_VAR01) {
      1: NAME_OF_OBJECT_VAR01_1;           // dark blue
      1: NAME_OF_OBJECT_VAR01_2;           // pale green
      1: NAME_OF_OBJECT_VAR01_3;           // pink
      1: NAME_OF_OBJECT_VAR01_4;           // yellow
      1: NAME_OF_OBJECT_VAR01_5;           // red
      1: NAME_OF_OBJECT_VAR01_6;           // light blue
      1: NAME_OF_OBJECT_VAR01_7;           // green
      1: NAME_OF_OBJECT_VAR01_8;           // dark green
      1: NAME_OF_OBJECT_VAR01_9;           // blue
      1: NAME_OF_OBJECT_VAR01_10;          // cream
      1: NAME_OF_OBJECT_VAR01_11;          // mauve
      1: NAME_OF_OBJECT_VAR01_12;          // purple
      1: NAME_OF_OBJECT_VAR01_13;          // orange
      1: NAME_OF_OBJECT_VAR01_14;          // brown
      1: NAME_OF_OBJECT_VAR01_15;          // grey
      1: NAME_OF_OBJECT_VAR01_16;  }           // white

switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_1, [STORE_TEMP(775, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_2, [STORE_TEMP(776, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_3, [STORE_TEMP(777, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_4, [STORE_TEMP(778, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_5, [STORE_TEMP(779, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_6, [STORE_TEMP(780, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_7, [STORE_TEMP(781, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_8, [STORE_TEMP(782, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_9, [STORE_TEMP(783, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_10,[STORE_TEMP(784, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_11,[STORE_TEMP(785, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_12,[STORE_TEMP(786, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_13,[STORE_TEMP(787, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_14,[STORE_TEMP(788, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_15,[STORE_TEMP(789, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR02_16,[STORE_TEMP(790, 3)]) { layout_NAME_OF_OBJECT_VAR02; }
random_switch (FEAT_OBJECTS, SELF, colour_NAME_OF_OBJECT_VAR02) {
      1: NAME_OF_OBJECT_VAR02_1;           // dark blue
      1: NAME_OF_OBJECT_VAR02_2;           // pale green
      1: NAME_OF_OBJECT_VAR02_3;           // pink
      1: NAME_OF_OBJECT_VAR02_4;           // yellow
      1: NAME_OF_OBJECT_VAR02_5;           // red
      1: NAME_OF_OBJECT_VAR02_6;           // light blue
      1: NAME_OF_OBJECT_VAR02_7;           // green
      1: NAME_OF_OBJECT_VAR02_8;           // dark green
      1: NAME_OF_OBJECT_VAR02_9;           // blue
      1: NAME_OF_OBJECT_VAR02_10;          // cream
      1: NAME_OF_OBJECT_VAR02_11;          // mauve
      1: NAME_OF_OBJECT_VAR02_12;          // purple
      1: NAME_OF_OBJECT_VAR02_13;          // orange
      1: NAME_OF_OBJECT_VAR02_14;          // brown
      1: NAME_OF_OBJECT_VAR02_15;          // grey
      1: NAME_OF_OBJECT_VAR02_16;  }           // white

switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_1, [STORE_TEMP(775, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_2, [STORE_TEMP(776, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_3, [STORE_TEMP(777, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_4, [STORE_TEMP(778, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_5, [STORE_TEMP(779, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_6, [STORE_TEMP(780, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_7, [STORE_TEMP(781, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_8, [STORE_TEMP(782, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_9, [STORE_TEMP(783, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_10,[STORE_TEMP(784, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_11,[STORE_TEMP(785, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_12,[STORE_TEMP(786, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_13,[STORE_TEMP(787, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_14,[STORE_TEMP(788, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_15,[STORE_TEMP(789, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR03_16,[STORE_TEMP(790, 3)]) { layout_NAME_OF_OBJECT_VAR03; }
random_switch (FEAT_OBJECTS, SELF, colour_NAME_OF_OBJECT_VAR03) {
      1: NAME_OF_OBJECT_VAR03_1;           // dark blue
      1: NAME_OF_OBJECT_VAR03_2;           // pale green
      1: NAME_OF_OBJECT_VAR03_3;           // pink
      1: NAME_OF_OBJECT_VAR03_4;           // yellow
      1: NAME_OF_OBJECT_VAR03_5;           // red
      1: NAME_OF_OBJECT_VAR03_6;           // light blue
      1: NAME_OF_OBJECT_VAR03_7;           // green
      1: NAME_OF_OBJECT_VAR03_8;           // dark green
      1: NAME_OF_OBJECT_VAR03_9;           // blue
      1: NAME_OF_OBJECT_VAR03_10;          // cream
      1: NAME_OF_OBJECT_VAR03_11;          // mauve
      1: NAME_OF_OBJECT_VAR03_12;          // purple
      1: NAME_OF_OBJECT_VAR03_13;          // orange
      1: NAME_OF_OBJECT_VAR03_14;          // brown
      1: NAME_OF_OBJECT_VAR03_15;          // grey
      1: NAME_OF_OBJECT_VAR03_16;  }           // white

switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_1, [STORE_TEMP(775, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_2, [STORE_TEMP(776, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_3, [STORE_TEMP(777, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_4, [STORE_TEMP(778, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_5, [STORE_TEMP(779, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_6, [STORE_TEMP(780, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_7, [STORE_TEMP(781, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_8, [STORE_TEMP(782, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_9, [STORE_TEMP(783, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_10,[STORE_TEMP(784, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_11,[STORE_TEMP(785, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_12,[STORE_TEMP(786, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_13,[STORE_TEMP(787, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_14,[STORE_TEMP(788, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_15,[STORE_TEMP(789, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
switch (FEAT_OBJECTS,SELF, NAME_OF_OBJECT_VAR04_16,[STORE_TEMP(790, 3)]) { layout_NAME_OF_OBJECT_VAR04; }
random_switch (FEAT_OBJECTS, SELF, colour_NAME_OF_OBJECT_VAR04) {
      1: NAME_OF_OBJECT_VAR04_1;           // dark blue
      1: NAME_OF_OBJECT_VAR04_2;           // pale green
      1: NAME_OF_OBJECT_VAR04_3;           // pink
      1: NAME_OF_OBJECT_VAR04_4;           // yellow
      1: NAME_OF_OBJECT_VAR04_5;           // red
      1: NAME_OF_OBJECT_VAR04_6;           // light blue
      1: NAME_OF_OBJECT_VAR04_7;           // green
      1: NAME_OF_OBJECT_VAR04_8;           // dark green
      1: NAME_OF_OBJECT_VAR04_9;           // blue
      1: NAME_OF_OBJECT_VAR04_10;          // cream
      1: NAME_OF_OBJECT_VAR04_11;          // mauve
      1: NAME_OF_OBJECT_VAR04_12;          // purple
      1: NAME_OF_OBJECT_VAR04_13;          // orange
      1: NAME_OF_OBJECT_VAR04_14;          // brown
      1: NAME_OF_OBJECT_VAR04_15;          // grey
      1: NAME_OF_OBJECT_VAR04_16;  }           // white

switch (FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_VAR_view, view) {
    0: colour_NAME_OF_OBJECT_VAR01;
    1: colour_NAME_OF_OBJECT_VAR02;
    2: colour_NAME_OF_OBJECT_VAR03;
    3: colour_NAME_OF_OBJECT_VAR04; }

item (FEAT_OBJECTS, NAME_OF_OBJECT, NUMERO) {
    property {
        class:                  "CATEGORY";
        classname:              NAME_OF_CAT;
        name:                   NAME_IN_MENU;
        climates_available:     ALL_CLIMATES;
        size:                   SIZE;
        build_cost_multiplier:  1;
        remove_cost_multiplier: 1;
        introduction_date:      0x00000000;
        end_of_life_date:       0xFFFFFFFF;
        object_flags:           (param_scenario_editor==1 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE,OBJ_FLAG_2CC) :
                                ( (param_scenario_editor==1 && param_irremovable==0) ? bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE,OBJ_FLAG_2CC) :
                                    ((param_scenario_editor==0 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE,OBJ_FLAG_2CC) : bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE,OBJ_FLAG_2CC)));
        height:                 2;
        num_views:              4;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT_VAR_view;
        purchase:               switch_NAME_OF_OBJECT_VAR_view;
    }
}

"""
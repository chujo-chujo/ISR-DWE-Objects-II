template_2obj_cc = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_elev, "PNG_FILE") { SPRITE_elev01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02_elev, "PNG_FILE") { SPRITE_elev02 }

spritelayout NAME_OF_OBJECT_VAR01_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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

switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT, view) {
            0: NAME_OF_OBJECT_VAR01;
            1: NAME_OF_OBJECT_VAR02;
}
switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_menu, view) {
            0: NAME_OF_OBJECT_VAR01_menu;
            1: NAME_OF_OBJECT_VAR02_menu;
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
        num_views:              2;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT;
        purchase:               switch_NAME_OF_OBJECT_menu;
    }
}

"""

template_1obj_cc = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_elev, "PNG_FILE") { SPRITE_elev01 }

spritelayout NAME_OF_OBJECT_VAR01_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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

switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT, view) {
            0: NAME_OF_OBJECT_VAR01;
}
switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_menu, view) {
            0: NAME_OF_OBJECT_VAR01_menu;
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
        num_views:              1;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT;
        purchase:               switch_NAME_OF_OBJECT_menu;
    }
}

"""

template_2obj = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_elev, "PNG_FILE") { SPRITE_elev01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02_elev, "PNG_FILE") { SPRITE_elev02 }

spritelayout NAME_OF_OBJECT_VAR01_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR01_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_3 {
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_6 {
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_8 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR02_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_3 {
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_6 {
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_8 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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

switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT, view) {
            0: NAME_OF_OBJECT_VAR01;
            1: NAME_OF_OBJECT_VAR02;
}
switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_menu, view) {
            0: NAME_OF_OBJECT_VAR01_menu;
            1: NAME_OF_OBJECT_VAR02_menu;
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
        num_views:              2;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT;
        purchase:               switch_NAME_OF_OBJECT_menu;
    }
}

"""

template_1obj = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_elev, "PNG_FILE") { SPRITE_elev01 }

spritelayout NAME_OF_OBJECT_VAR01_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR01_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_3 {
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_6 {
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_8 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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

switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT, view) {
            0: NAME_OF_OBJECT_VAR01;
}
switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_menu, view) {
            0: NAME_OF_OBJECT_VAR01_menu;
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
        num_views:              1;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT;
        purchase:               switch_NAME_OF_OBJECT_menu;
    }
}

"""

template_4obj_cc_2x = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01a, "PNG_FILE") { SPRITE01a }
spriteset(spriteset_NAME_OF_OBJECT_VAR01b, "PNG_FILE") { SPRITE01b }
spriteset(spriteset_NAME_OF_OBJECT_VAR02a, "PNG_FILE") { SPRITE02a }
spriteset(spriteset_NAME_OF_OBJECT_VAR02b, "PNG_FILE") { SPRITE02b }
spriteset(spriteset_NAME_OF_OBJECT_VAR03a, "PNG_FILE") { SPRITE03a }
spriteset(spriteset_NAME_OF_OBJECT_VAR03b, "PNG_FILE") { SPRITE03b }
spriteset(spriteset_NAME_OF_OBJECT_VAR04a, "PNG_FILE") { SPRITE04a }
spriteset(spriteset_NAME_OF_OBJECT_VAR04b, "PNG_FILE") { SPRITE04b }
spriteset(spriteset_NAME_OF_OBJECT_VAR01a_elev, "PNG_FILE") { SPRITE_elev01a }
spriteset(spriteset_NAME_OF_OBJECT_VAR01b_elev, "PNG_FILE") { SPRITE_elev01b }
spriteset(spriteset_NAME_OF_OBJECT_VAR02a_elev, "PNG_FILE") { SPRITE_elev02a }
spriteset(spriteset_NAME_OF_OBJECT_VAR02b_elev, "PNG_FILE") { SPRITE_elev02b }
spriteset(spriteset_NAME_OF_OBJECT_VAR03a_elev, "PNG_FILE") { SPRITE_elev03a }
spriteset(spriteset_NAME_OF_OBJECT_VAR03b_elev, "PNG_FILE") { SPRITE_elev03b }
spriteset(spriteset_NAME_OF_OBJECT_VAR04a_elev, "PNG_FILE") { SPRITE_elev04a }
spriteset(spriteset_NAME_OF_OBJECT_VAR04b_elev, "PNG_FILE") { SPRITE_elev04b }
spriteset(spriteset_NAME_OF_OBJECT_VAR01a_menu, "PNG_FILE") { SPRITE_purchase1L }
spriteset(spriteset_NAME_OF_OBJECT_VAR01b_menu, "PNG_FILE") { SPRITE_purchase1R }
spriteset(spriteset_NAME_OF_OBJECT_VAR02a_menu, "PNG_FILE") { SPRITE_purchase2L }
spriteset(spriteset_NAME_OF_OBJECT_VAR02b_menu, "PNG_FILE") { SPRITE_purchase2R }
spriteset(spriteset_NAME_OF_OBJECT_VAR03a_menu, "PNG_FILE") { SPRITE_purchase3L }
spriteset(spriteset_NAME_OF_OBJECT_VAR03b_menu, "PNG_FILE") { SPRITE_purchase3R }
spriteset(spriteset_NAME_OF_OBJECT_VAR04a_menu, "PNG_FILE") { SPRITE_purchase4L }
spriteset(spriteset_NAME_OF_OBJECT_VAR04b_menu, "PNG_FILE") { SPRITE_purchase4R }

spritelayout NAME_OF_OBJECT_VAR01a_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR01a_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01a_3 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR01a_4 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR01a_5 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01a_6 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR01a_7 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01a_8 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01a_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01a(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR01a, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR01a_3;
            1: NAME_OF_OBJECT_VAR01a_4;
            2: NAME_OF_OBJECT_VAR01a_8;
            3: NAME_OF_OBJECT_VAR01a_2;
            4: NAME_OF_OBJECT_VAR01a_6;
            5: NAME_OF_OBJECT_VAR01a_5;
            6: NAME_OF_OBJECT_VAR01a_7;
            7: NAME_OF_OBJECT_VAR01a_1;
            8: NAME_OF_OBJECT_VAR01a_3;
            9: NAME_OF_OBJECT_VAR01a_4;
            10: NAME_OF_OBJECT_VAR01a_8;
            11: NAME_OF_OBJECT_VAR01a_2;
            12: NAME_OF_OBJECT_VAR01a_6;
            13: NAME_OF_OBJECT_VAR01a_5;
            14: NAME_OF_OBJECT_VAR01a_7;
        NAME_OF_OBJECT_VAR01a_9;
}

spritelayout NAME_OF_OBJECT_VAR01b_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR01b_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01b_3 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR01b_4 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR01b_5 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01b_6 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR01b_7 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01b_8 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01b_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01b(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01a_menu(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01b_menu(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR01b, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR01b_3;
            1: NAME_OF_OBJECT_VAR01b_4;
            2: NAME_OF_OBJECT_VAR01b_8;
            3: NAME_OF_OBJECT_VAR01b_2;
            4: NAME_OF_OBJECT_VAR01b_6;
            5: NAME_OF_OBJECT_VAR01b_5;
            6: NAME_OF_OBJECT_VAR01b_7;
            7: NAME_OF_OBJECT_VAR01b_1;
            8: NAME_OF_OBJECT_VAR01b_3;
            9: NAME_OF_OBJECT_VAR01b_4;
            10: NAME_OF_OBJECT_VAR01b_8;
            11: NAME_OF_OBJECT_VAR01b_2;
            12: NAME_OF_OBJECT_VAR01b_6;
            13: NAME_OF_OBJECT_VAR01b_5;
            14: NAME_OF_OBJECT_VAR01b_7;
        NAME_OF_OBJECT_VAR01b_9;
}

spritelayout NAME_OF_OBJECT_VAR02a_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR02a_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02a_3 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR02a_4 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR02a_5 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02a_6 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR02a_7 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02a_8 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02a_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02a(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR02a, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR02a_3;
            1: NAME_OF_OBJECT_VAR02a_4;
            2: NAME_OF_OBJECT_VAR02a_8;
            3: NAME_OF_OBJECT_VAR02a_2;
            4: NAME_OF_OBJECT_VAR02a_6;
            5: NAME_OF_OBJECT_VAR02a_5;
            6: NAME_OF_OBJECT_VAR02a_7;
            7: NAME_OF_OBJECT_VAR02a_1;
            8: NAME_OF_OBJECT_VAR02a_3;
            9: NAME_OF_OBJECT_VAR02a_4;
            10: NAME_OF_OBJECT_VAR02a_8;
            11: NAME_OF_OBJECT_VAR02a_2;
            12: NAME_OF_OBJECT_VAR02a_6;
            13: NAME_OF_OBJECT_VAR02a_5;
            14: NAME_OF_OBJECT_VAR02a_7;
        NAME_OF_OBJECT_VAR02a_9;
}

spritelayout NAME_OF_OBJECT_VAR02b_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR02b_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02b_3 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR02b_4 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR02b_5 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02b_6 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR02b_7 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02b_8 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02b_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02b(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02a_menu(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02b_menu(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR02b, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR02b_3;
            1: NAME_OF_OBJECT_VAR02b_4;
            2: NAME_OF_OBJECT_VAR02b_8;
            3: NAME_OF_OBJECT_VAR02b_2;
            4: NAME_OF_OBJECT_VAR02b_6;
            5: NAME_OF_OBJECT_VAR02b_5;
            6: NAME_OF_OBJECT_VAR02b_7;
            7: NAME_OF_OBJECT_VAR02b_1;
            8: NAME_OF_OBJECT_VAR02b_3;
            9: NAME_OF_OBJECT_VAR02b_4;
            10: NAME_OF_OBJECT_VAR02b_8;
            11: NAME_OF_OBJECT_VAR02b_2;
            12: NAME_OF_OBJECT_VAR02b_6;
            13: NAME_OF_OBJECT_VAR02b_5;
            14: NAME_OF_OBJECT_VAR02b_7;
        NAME_OF_OBJECT_VAR02b_9;
}

spritelayout NAME_OF_OBJECT_VAR03a_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR03a_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03a_3 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR03a_4 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR03a_5 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03a_6 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR03a_7 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03a_8 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03a_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03a(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR03a, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR03a_3;
            1: NAME_OF_OBJECT_VAR03a_4;
            2: NAME_OF_OBJECT_VAR03a_8;
            3: NAME_OF_OBJECT_VAR03a_2;
            4: NAME_OF_OBJECT_VAR03a_6;
            5: NAME_OF_OBJECT_VAR03a_5;
            6: NAME_OF_OBJECT_VAR03a_7;
            7: NAME_OF_OBJECT_VAR03a_1;
            8: NAME_OF_OBJECT_VAR03a_3;
            9: NAME_OF_OBJECT_VAR03a_4;
            10: NAME_OF_OBJECT_VAR03a_8;
            11: NAME_OF_OBJECT_VAR03a_2;
            12: NAME_OF_OBJECT_VAR03a_6;
            13: NAME_OF_OBJECT_VAR03a_5;
            14: NAME_OF_OBJECT_VAR03a_7;
        NAME_OF_OBJECT_VAR03a_9;
}

spritelayout NAME_OF_OBJECT_VAR03b_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR03b_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03b_3 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR03b_4 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR03b_5 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03b_6 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR03b_7 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03b_8 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03b_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03b(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03a_menu(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03b_menu(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR03b, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR03b_3;
            1: NAME_OF_OBJECT_VAR03b_4;
            2: NAME_OF_OBJECT_VAR03b_8;
            3: NAME_OF_OBJECT_VAR03b_2;
            4: NAME_OF_OBJECT_VAR03b_6;
            5: NAME_OF_OBJECT_VAR03b_5;
            6: NAME_OF_OBJECT_VAR03b_7;
            7: NAME_OF_OBJECT_VAR03b_1;
            8: NAME_OF_OBJECT_VAR03b_3;
            9: NAME_OF_OBJECT_VAR03b_4;
            10: NAME_OF_OBJECT_VAR03b_8;
            11: NAME_OF_OBJECT_VAR03b_2;
            12: NAME_OF_OBJECT_VAR03b_6;
            13: NAME_OF_OBJECT_VAR03b_5;
            14: NAME_OF_OBJECT_VAR03b_7;
        NAME_OF_OBJECT_VAR03b_9;
}

spritelayout NAME_OF_OBJECT_VAR04a_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR04a_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04a_3 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR04a_4 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR04a_5 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04a_6 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR04a_7 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04a_8 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04a_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR04a, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR04a_3;
            1: NAME_OF_OBJECT_VAR04a_4;
            2: NAME_OF_OBJECT_VAR04a_8;
            3: NAME_OF_OBJECT_VAR04a_2;
            4: NAME_OF_OBJECT_VAR04a_6;
            5: NAME_OF_OBJECT_VAR04a_5;
            6: NAME_OF_OBJECT_VAR04a_7;
            7: NAME_OF_OBJECT_VAR04a_1;
            8: NAME_OF_OBJECT_VAR04a_3;
            9: NAME_OF_OBJECT_VAR04a_4;
            10: NAME_OF_OBJECT_VAR04a_8;
            11: NAME_OF_OBJECT_VAR04a_2;
            12: NAME_OF_OBJECT_VAR04a_6;
            13: NAME_OF_OBJECT_VAR04a_5;
            14: NAME_OF_OBJECT_VAR04a_7;
        NAME_OF_OBJECT_VAR04a_9;
}

spritelayout NAME_OF_OBJECT_VAR04b_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR04b_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04b_3 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR04b_4 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR04b_5 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04b_6 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR04b_7 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04b_8 {
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
                sprite: spriteset_GRN_CHIPS_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04b_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT;
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_menu(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT; }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_menu(0);
                recolour_mode: RECOLOUR_REMAP;
                palette: PALETTE_USE_DEFAULT; }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR04b, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR04b_3;
            1: NAME_OF_OBJECT_VAR04b_4;
            2: NAME_OF_OBJECT_VAR04b_8;
            3: NAME_OF_OBJECT_VAR04b_2;
            4: NAME_OF_OBJECT_VAR04b_6;
            5: NAME_OF_OBJECT_VAR04b_5;
            6: NAME_OF_OBJECT_VAR04b_7;
            7: NAME_OF_OBJECT_VAR04b_1;
            8: NAME_OF_OBJECT_VAR04b_3;
            9: NAME_OF_OBJECT_VAR04b_4;
            10: NAME_OF_OBJECT_VAR04b_8;
            11: NAME_OF_OBJECT_VAR04b_2;
            12: NAME_OF_OBJECT_VAR04b_6;
            13: NAME_OF_OBJECT_VAR04b_5;
            14: NAME_OF_OBJECT_VAR04b_7;
        NAME_OF_OBJECT_VAR04b_9;
}

random_switch(FEAT_OBJECTS, SELF, random_NAME_OF_OBJECT_VAR01) {
    1: NAME_OF_OBJECT_VAR01a;
    1: NAME_OF_OBJECT_VAR01b;
}
random_switch(FEAT_OBJECTS, SELF, random_NAME_OF_OBJECT_VAR02) {
    1: NAME_OF_OBJECT_VAR02a;
    1: NAME_OF_OBJECT_VAR02b;
}
random_switch(FEAT_OBJECTS, SELF, random_NAME_OF_OBJECT_VAR03) {
    1: NAME_OF_OBJECT_VAR03a;
    1: NAME_OF_OBJECT_VAR03b;
}
random_switch(FEAT_OBJECTS, SELF, random_NAME_OF_OBJECT_VAR04) {
    1: NAME_OF_OBJECT_VAR04a;
    1: NAME_OF_OBJECT_VAR04b;
}
switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT, view) {
            0: random_NAME_OF_OBJECT_VAR01;
            1: random_NAME_OF_OBJECT_VAR02;
            2: random_NAME_OF_OBJECT_VAR03;
            3: random_NAME_OF_OBJECT_VAR04;
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

template_Road_overlapping_tiles = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03, "PNG_FILE") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04, "PNG_FILE") { SPRITE04 }

spritelayout layout_NAME_OF_OBJECT_VAR01 {
    ground { sprite: GROUNDSPRITE_CLEARED; }
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground); }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
spritelayout layout_NAME_OF_OBJECT_VAR02 {
    ground { sprite: GROUNDSPRITE_CLEARED; }
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground); }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
spritelayout layout_NAME_OF_OBJECT_VAR03 {
    ground { sprite: GROUNDSPRITE_CLEARED; }
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground); }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR03;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
spritelayout layout_NAME_OF_OBJECT_VAR04 {
    ground { sprite: GROUNDSPRITE_CLEARED; }
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground); }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR04;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
spritelayout layout_NAME_OF_OBJECT_VAR01_menu {
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground);
               zoffset: 10; }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground;
               zoffset: 10; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01;
               zoffset: 10;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
spritelayout layout_NAME_OF_OBJECT_VAR02_menu {
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground);
               zoffset: 10; }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground;
               zoffset: 10; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02;
               zoffset: 10;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
spritelayout layout_NAME_OF_OBJECT_VAR03_menu {
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground);
               zoffset: 10; }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground;
               zoffset: 10; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR03;
               zoffset: 10;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
spritelayout layout_NAME_OF_OBJECT_VAR04_menu {
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground);
               zoffset: 10; }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground;
               zoffset: 10; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR04;
               zoffset: 10;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
switch (FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_VAR_view, view) {
    0: layout_NAME_OF_OBJECT_VAR01;
    1: layout_NAME_OF_OBJECT_VAR02;
    2: layout_NAME_OF_OBJECT_VAR03;
    3: layout_NAME_OF_OBJECT_VAR04; }
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
        default:                switch_NAME_OF_OBJECT_VAR_view;
        purchase:               switch_NAME_OF_OBJECT_VAR_menu;
    }
}

"""

template_Drive_through_tiles_2obj = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }

spritelayout layout_NAME_OF_OBJECT_VAR01 {
    ground { sprite: GROUNDSPRITE_CLEARED; }
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground); }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
spritelayout layout_NAME_OF_OBJECT_VAR02 {
    ground { sprite: GROUNDSPRITE_CLEARED; }
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground); }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
spritelayout layout_NAME_OF_OBJECT_VAR01_menu {
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground);
               zoffset: 10; }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground;
               zoffset: 10; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR01;
               zoffset: 10;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
spritelayout layout_NAME_OF_OBJECT_VAR02_menu {
    building { sprite: spriteset_SPRITE_GROUND_OGFX;
               hide_sprite: (1 - param_ground);
               zoffset: 10; }
    building { sprite: spriteset_SPRITE_GROUND_CHIPS;
               hide_sprite: param_ground;
               zoffset: 10; }
    building { sprite: spriteset_NAME_OF_OBJECT_VAR02;
               zoffset: 10;
               recolour_mode: RECOLOUR_REMAP;
               palette: PALETTE_USE_DEFAULT; } }
switch (FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_VAR_view, view) {
    0: layout_NAME_OF_OBJECT_VAR01;
    1: layout_NAME_OF_OBJECT_VAR02; }
switch (FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT_VAR_menu, view) {
    0: layout_NAME_OF_OBJECT_VAR01_menu;
    1: layout_NAME_OF_OBJECT_VAR02_menu; }

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
        num_views:              2;
    }
    graphics {
        default:                switch_NAME_OF_OBJECT_VAR_view;
        purchase:               switch_NAME_OF_OBJECT_VAR_menu;
    }
}

"""

template_ISR_DWE_roads_10 = """

/////////////////////////////////////////////////////////////////////
// NAME_OF_OBJECT
/////////////////////////////////////////////////////////////////////

spriteset(spriteset_NAME_OF_OBJECT_VAR01, "PNG_FILE") { SPRITE01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02, "PNG_FILE") { SPRITE02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03, "PNG_FILE") { SPRITE03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04a, "PNG_FILE") { SPRITE04a }
spriteset(spriteset_NAME_OF_OBJECT_VAR04b, "PNG_FILE") { SPRITE04b }
spriteset(spriteset_NAME_OF_OBJECT_VAR01_elev, "PNG_FILE") { SPRITE_elev01 }
spriteset(spriteset_NAME_OF_OBJECT_VAR02_elev, "PNG_FILE") { SPRITE_elev02 }
spriteset(spriteset_NAME_OF_OBJECT_VAR03_elev, "PNG_FILE") { SPRITE_elev03 }
spriteset(spriteset_NAME_OF_OBJECT_VAR04a_elev, "PNG_FILE") { SPRITE_elev04a }
spriteset(spriteset_NAME_OF_OBJECT_VAR04b_elev, "PNG_FILE") { SPRITE_elev04b }

spritelayout NAME_OF_OBJECT_VAR01_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR01_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_3 {
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_6 {
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_8 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR01(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR01_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR02_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_3 {
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_6 {
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_8 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR02(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR02_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR03_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_3 {
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_6 {
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
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
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_8 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR03(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR03_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
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

spritelayout NAME_OF_OBJECT_VAR04a_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR04a_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04a_3 {
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR04a_4 {
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04a_5 {
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04a_6 {
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04a_7 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04a_8 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04a_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR04a, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR04a_3;
            1: NAME_OF_OBJECT_VAR04a_4;
            2: NAME_OF_OBJECT_VAR04a_8;
            3: NAME_OF_OBJECT_VAR04a_2;
            4: NAME_OF_OBJECT_VAR04a_6;
            5: NAME_OF_OBJECT_VAR04a_5;
            6: NAME_OF_OBJECT_VAR04a_7;
            7: NAME_OF_OBJECT_VAR04a_1;
            8: NAME_OF_OBJECT_VAR04a_3;
            9: NAME_OF_OBJECT_VAR04a_4;
            10: NAME_OF_OBJECT_VAR04a_8;
            11: NAME_OF_OBJECT_VAR04a_2;
            12: NAME_OF_OBJECT_VAR04a_6;
            13: NAME_OF_OBJECT_VAR04a_5;
            14: NAME_OF_OBJECT_VAR04a_7;
        NAME_OF_OBJECT_VAR04a_9;
}

spritelayout NAME_OF_OBJECT_VAR04b_1 {
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
}
spritelayout NAME_OF_OBJECT_VAR04b_2 {
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04b_3 {
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
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
spritelayout NAME_OF_OBJECT_VAR04b_4 {
            building {
                sprite: spriteset_jetty_ne_sw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_ne_sw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(0,1) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04b_5 {
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_nw_se(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04b_6 {
            building {
                sprite: spriteset_jetty_slope_ne_sw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) == WATER_CLASS_NONE); }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_se_nw_no_water(0);
                always_draw: 0;
                hide_sprite: (nearby_tile_water_class(1,0) != WATER_CLASS_NONE); }
    }
spritelayout NAME_OF_OBJECT_VAR04b_7 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04b_8 {
            building {
                sprite: spriteset_jetty_slope_se_nw(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_jetty_slope_sw_ne(0);
                always_draw: 0;
                hide_sprite: 0; }
            building {
                sprite: spriteset_GRN_CHIPS_elev(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX_elev(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b_elev(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04b_9 {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                always_draw: 0;
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                always_draw: 0;
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04b(0);
                always_draw: 0;
                hide_sprite: 0; }
    }
spritelayout NAME_OF_OBJECT_VAR04_menu {
            building {
                sprite: spriteset_GRN_CHIPS(0);
                hide_sprite: param_ground; }
            building {
                sprite: spriteset_GRN_OGFX(0);
                hide_sprite: (1 - param_ground); }
            building {
                sprite: spriteset_NAME_OF_OBJECT_VAR04a(0); }
            building {
                sprite: spriteset_MULTI_2x(0); }
}
switch(FEAT_OBJECTS, SELF, NAME_OF_OBJECT_VAR04b, nearby_tile_slope(0,0) + ((nearby_tile_water_class(0,0) == WATER_CLASS_NONE && nearby_tile_slope(0,0) == 0)*100)) {
            0: NAME_OF_OBJECT_VAR04b_3;
            1: NAME_OF_OBJECT_VAR04b_4;
            2: NAME_OF_OBJECT_VAR04b_8;
            3: NAME_OF_OBJECT_VAR04b_2;
            4: NAME_OF_OBJECT_VAR04b_6;
            5: NAME_OF_OBJECT_VAR04b_5;
            6: NAME_OF_OBJECT_VAR04b_7;
            7: NAME_OF_OBJECT_VAR04b_1;
            8: NAME_OF_OBJECT_VAR04b_3;
            9: NAME_OF_OBJECT_VAR04b_4;
            10: NAME_OF_OBJECT_VAR04b_8;
            11: NAME_OF_OBJECT_VAR04b_2;
            12: NAME_OF_OBJECT_VAR04b_6;
            13: NAME_OF_OBJECT_VAR04b_5;
            14: NAME_OF_OBJECT_VAR04b_7;
        NAME_OF_OBJECT_VAR04b_9;
}

random_switch(FEAT_OBJECTS, SELF, random_NAME_OF_OBJECT_VAR04) {
    1: NAME_OF_OBJECT_VAR04a;
    1: NAME_OF_OBJECT_VAR04b;
}
switch(FEAT_OBJECTS, SELF, switch_NAME_OF_OBJECT, view) {
            0: NAME_OF_OBJECT_VAR01;
            1: NAME_OF_OBJECT_VAR02;
            2: NAME_OF_OBJECT_VAR03;
            3: random_NAME_OF_OBJECT_VAR04;
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
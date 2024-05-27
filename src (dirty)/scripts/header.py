header = """grf {
 grfid: "CH\\0F\\01";
 name: string(STR_GRF_NAME);
 desc: string(STR_GRF_DESCRIPTION);
 url:  string(STR_GRF_URL);
 version: 1;
 min_compatible_version: 1;

 param 0 {
        param_ground {
                name:       string(STR_PAR_ground_NAME);
                desc:       string(STR_PAR_ground_DESC);
                type:       int;
                min_value:  0;
                max_value:  1;
                def_value:  0;
                names: {    0: string(STR_PAR_ground_TYPE1);
                            1: string(STR_PAR_ground_TYPE2); };
                }
        }
 param 1 {
        param_scenario_editor {
                name:       string(STR_PAR01_NAME);
                desc:       string(STR_PAR01_DESC);
                type:       bool;
                def_value:  0;
                }
        }
 param 2 {
        param_irremovable {
                name:       string(STR_PAR02_NAME);
                desc:       string(STR_PAR02_DESC);
                type:       bool;
                def_value:  0;
                }
        }
 }

//check OpenTTD version - parameterized spritelayout is only supported since OpenTTD 1.2.0 r22723
if (version_openttd(1,2,0,22723) > openttd_version) {
        error(FATAL, REQUIRES_OPENTTD, string(STR_OPENTTD_VERSION));
}

// [(left_x, upper_y, width, height, )offset_x, offset_y(, flags)(, filename)(, mask)]
template template_standard(x, y)      { [x, y, 64, 100, -31, -69, ANIM] }
template template_standard_elev(x, y) { [x, y, 64, 100, -31, -77, ANIM] }
template template_water_tiles(x, y)   { [x, y, 64, 100, -31, -68, ANIM] }

template template_ships(x,y)          { [x, y, 104, 71, -51, -24, ANIM] }

template template_106px(x, y)         { [x, y, 106,100, -52, -69, ANIM] }
template template_106px_elev(x, y)    { [x, y, 106,100, -52, -77, ANIM] }
template template_102px_1x2(x, y)     { [x, y, 102,100, -69, -69, ANIM] }
template template_102px_2x1(x, y)     { [x, y, 102,100, -27, -69, ANIM] }
template template_102px_1x2_elev(x, y)     { [x, y, 102,100, -69, -77, ANIM] }
template template_102px_2x1_elev(x, y)     { [x, y, 102,100, -27, -77, ANIM] }
template template_96px(x, y)          { [x, y, 96, 100, -47, -69, ANIM] }
template template_96px_elev(x, y)     { [x, y, 96, 100, -47, -77, ANIM] }
template template_70px(x, y)          { [x, y, 70, 100, -34, -69, ANIM] }
template template_70px_elev(x, y)     { [x, y, 70, 100, -34, -77, ANIM] }
template template_68px(x, y)          { [x, y, 68, 100, -33, -69, ANIM] }
template template_68px_elev(x, y)     { [x, y, 68, 100, -33, -77, ANIM] }
template template_66px(x, y)          { [x, y, 66, 100, -32, -69, ANIM] }
template template_66px_elev(x, y)     { [x, y, 66, 100, -32, -77, ANIM] }

template template_1x2(x, y)           { [x, y, 96, 100, -63, -69, ANIM] }
template template_1x2_elev(x, y)      { [x, y, 96, 100, -63, -77, ANIM] }
template template_2x1(x, y)           { [x, y, 96, 100, -31, -69, ANIM] }
template template_2x1_elev(x, y)      { [x, y, 96, 100, -31, -77, ANIM] }
template template_1x2_overlap(x, y)   { [x, y, 96, 100, -31, -53, ANIM] }
template template_2x1_overlap(x, y)   { [x, y, 96, 100, -63, -53, ANIM] }
template template_1x2_overlap_shifted_up(x, y)    { [x, y, 96, 100, -63, -69, ANIM] }
template template_2x1_overlap_shifted_up(x, y)    { [x, y, 96, 100, -31, -69, ANIM] }
template template_2x1_overlap_shifted_right(x, y) { [x, y, 96, 100, -31, -53, ANIM] }
template template_1x2_overlap_elev(x, y)   { [x, y, 96, 100, -31, -61, ANIM] }
template template_2x1_overlap_elev(x, y)   { [x, y, 96, 100, -63, -61, ANIM] }
template template_1x2_overlap_shifted_up_elev(x, y)    { [x, y, 96, 100, -63, -77, ANIM] }
template template_2x1_overlap_shifted_up_elev(x, y)    { [x, y, 96, 100, -31, -77, ANIM] }
template template_2x1_overlap_shifted_right_elev(x, y) { [x, y, 96, 100, -31, -61, ANIM] }
template template_1x2_overlap_menu(x, y) { [x, y, 96, 100, -31, -77, ANIM] }
template template_2x1_overlap_menu(x, y) { [x, y, 96, 100, -63, -77, ANIM] }

template template_menu_L(x, y)        { [x, y, 64, 100, -56, -69, ANIM] }
template template_menu_R(x, y)        { [x, y, 64, 100, -6,  -69, ANIM] }

// spritesets for ground
spriteset(spriteset_GRN_EMPTY,      "gfx/ground_empty.png") { template_standard(0,0) }

spriteset(spriteset_GRN_TYPE2,      "gfx/ground_type2.png") { template_standard(0,0) }
spriteset(spriteset_GRN_TYPE2_elev, "gfx/ground_type2.png") { template_standard_elev(0,0) }
spriteset(spriteset_GRN_TYPE1,      "gfx/ground_type1.png") { template_standard(0,0) }
spriteset(spriteset_GRN_TYPE1_elev, "gfx/ground_type1.png") { template_standard_elev(0,0) }

spriteset(spriteset_GRN_1x2_TYPE2,          "gfx/ground_1x2_type2.png") { template_1x2(0,0) }
spriteset(spriteset_GRN_2x1_TYPE2,          "gfx/ground_2x1_type2.png") { template_2x1(0,0) }
spriteset(spriteset_GRN_1x2_TYPE2_elev,     "gfx/ground_1x2_type2.png") { template_1x2_elev(0,0) }
spriteset(spriteset_GRN_2x1_TYPE2_elev,     "gfx/ground_2x1_type2.png") { template_2x1_elev(0,0) }
spriteset(spriteset_GRN_1x2_overlap_TYPE2,  "gfx/ground_1x2_type2.png") { template_1x2_overlap(0,0) }
spriteset(spriteset_GRN_2x1_overlap_TYPE2,  "gfx/ground_2x1_type2.png") { template_2x1_overlap(0,0) }
spriteset(spriteset_GRN_1x2_overlap_shifted_up_TYPE2,  "gfx/ground_1x2_type2.png") { template_1x2_overlap_shifted_up(0,0) }
spriteset(spriteset_GRN_2x1_overlap_shifted_up_TYPE2,  "gfx/ground_2x1_type2.png") { template_2x1_overlap_shifted_up(0,0) }
spriteset(spriteset_GRN_1x2_overlap_TYPE2_elev,  "gfx/ground_1x2_type2.png") { template_1x2_overlap_elev(0,0) }
spriteset(spriteset_GRN_2x1_overlap_TYPE2_elev,  "gfx/ground_2x1_type2.png") { template_2x1_overlap_elev(0,0) }
spriteset(spriteset_GRN_1x2_overlap_shifted_up_TYPE2_elev,  "gfx/ground_1x2_type2.png") { template_1x2_overlap_shifted_up_elev(0,0) }
spriteset(spriteset_GRN_2x1_overlap_shifted_up_TYPE2_elev,  "gfx/ground_2x1_type2.png") { template_2x1_overlap_shifted_up_elev(0,0) }

spriteset(spriteset_GRN_1x2_TYPE1,         "gfx/ground_1x2_type1.png") { template_1x2(0,0) }
spriteset(spriteset_GRN_2x1_TYPE1,         "gfx/ground_2x1_type1.png") { template_2x1(0,0) }
spriteset(spriteset_GRN_1x2_TYPE1_elev,    "gfx/ground_1x2_type1.png") { template_1x2_elev(0,0) }
spriteset(spriteset_GRN_2x1_TYPE1_elev,    "gfx/ground_2x1_type1.png") { template_2x1_elev(0,0) }
spriteset(spriteset_GRN_1x2_overlap_TYPE1, "gfx/ground_1x2_type1.png") { template_1x2_overlap(0,0) }
spriteset(spriteset_GRN_2x1_overlap_TYPE1, "gfx/ground_2x1_type1.png") { template_2x1_overlap(0,0) }
spriteset(spriteset_GRN_1x2_overlap_shifted_up_TYPE1, "gfx/ground_1x2_type1.png") { template_1x2_overlap_shifted_up(0,0) }
spriteset(spriteset_GRN_2x1_overlap_shifted_up_TYPE1, "gfx/ground_2x1_type1.png") { template_2x1_overlap_shifted_up(0,0) }
spriteset(spriteset_GRN_1x2_overlap_TYPE1_elev, "gfx/ground_1x2_type1.png") { template_1x2_overlap_elev(0,0) }
spriteset(spriteset_GRN_2x1_overlap_TYPE1_elev, "gfx/ground_2x1_type1.png") { template_2x1_overlap_elev(0,0) }
spriteset(spriteset_GRN_1x2_overlap_shifted_up_TYPE1_elev, "gfx/ground_1x2_type1.png") { template_1x2_overlap_shifted_up_elev(0,0) }
spriteset(spriteset_GRN_2x1_overlap_shifted_up_TYPE1_elev, "gfx/ground_2x1_type1.png") { template_2x1_overlap_shifted_up_elev(0,0) }

spriteset(spriteset_ROUND_GRN_NE_TYPE1, "gfx/ground_round_type1.png") { [0  , 0, 64, 100, -31, -76, ANIM] }
spriteset(spriteset_ROUND_GRN_NW_TYPE1, "gfx/ground_round_type1.png") { [80 , 0, 64, 100, -31, -76, ANIM] }
spriteset(spriteset_ROUND_GRN_SW_TYPE1, "gfx/ground_round_type1.png") { [160, 0, 64, 100, -31, -81, ANIM] }
spriteset(spriteset_ROUND_GRN_SE_TYPE1, "gfx/ground_round_type1.png") { [240, 0, 64, 100, -31, -81, ANIM] }
spriteset(spriteset_ROUND_GRN_NE_TYPE2, "gfx/ground_round_type2.png") { [0  , 0, 64, 100, -31, -76, ANIM] }
spriteset(spriteset_ROUND_GRN_NW_TYPE2, "gfx/ground_round_type2.png") { [80 , 0, 64, 100, -31, -76, ANIM] }
spriteset(spriteset_ROUND_GRN_SW_TYPE2, "gfx/ground_round_type2.png") { [160, 0, 64, 100, -31, -81, ANIM] }
spriteset(spriteset_ROUND_GRN_SE_TYPE2, "gfx/ground_round_type2.png") { [240, 0, 64, 100, -31, -81, ANIM] }

spriteset(spriteset_DIAG_GRN_S_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(0  ,0) }
spriteset(spriteset_DIAG_GRN_N_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(80 ,0) }
spriteset(spriteset_DIAG_GRN_E_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(160,0) }
spriteset(spriteset_DIAG_GRN_W_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(240,0) }
spriteset(spriteset_DIAG_GRN_S_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(0  ,0) }
spriteset(spriteset_DIAG_GRN_N_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(80 ,0) }
spriteset(spriteset_DIAG_GRN_E_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(160,0) }
spriteset(spriteset_DIAG_GRN_W_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(240,0) }

spriteset(spriteset_CORNER_GRN_S_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(0  ,110) }
spriteset(spriteset_CORNER_GRN_N_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(80 ,110) }
spriteset(spriteset_CORNER_GRN_E_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(160,110) }
spriteset(spriteset_CORNER_GRN_W_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(240,110) }
spriteset(spriteset_CORNER_GRN_S_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(0  ,110) }
spriteset(spriteset_CORNER_GRN_N_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(80 ,110) }
spriteset(spriteset_CORNER_GRN_E_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(160,110) }
spriteset(spriteset_CORNER_GRN_W_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(240,110) }

spriteset(spriteset_WATER_L1_GRN_S_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(0  ,220) }
spriteset(spriteset_WATER_L1_GRN_N_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(80 ,220) }
spriteset(spriteset_WATER_L1_GRN_E_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(160,220) }
spriteset(spriteset_WATER_L1_GRN_W_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(240,220) }
spriteset(spriteset_WATER_L1_GRN_S_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(0  ,220) }
spriteset(spriteset_WATER_L1_GRN_N_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(80 ,220) }
spriteset(spriteset_WATER_L1_GRN_E_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(160,220) }
spriteset(spriteset_WATER_L1_GRN_W_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(240,220) }

spriteset(spriteset_WATER_R1_GRN_S_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(320,220) }
spriteset(spriteset_WATER_R1_GRN_N_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(400,220) }
spriteset(spriteset_WATER_R1_GRN_E_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(480,220) }
spriteset(spriteset_WATER_R1_GRN_W_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(560,220) }
spriteset(spriteset_WATER_R1_GRN_S_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(320,220) }
spriteset(spriteset_WATER_R1_GRN_N_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(400,220) }
spriteset(spriteset_WATER_R1_GRN_E_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(480,220) }
spriteset(spriteset_WATER_R1_GRN_W_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(560,220) }

spriteset(spriteset_WATER_L2_GRN_S_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(0  ,330) }
spriteset(spriteset_WATER_L2_GRN_N_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(80 ,330) }
spriteset(spriteset_WATER_L2_GRN_E_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(160,330) }
spriteset(spriteset_WATER_L2_GRN_W_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(240,330) }
spriteset(spriteset_WATER_L2_GRN_S_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(0  ,330) }
spriteset(spriteset_WATER_L2_GRN_N_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(80 ,330) }
spriteset(spriteset_WATER_L2_GRN_E_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(160,330) }
spriteset(spriteset_WATER_L2_GRN_W_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(240,330) }

spriteset(spriteset_WATER_R2_GRN_S_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(320,330) }
spriteset(spriteset_WATER_R2_GRN_N_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(400,330) }
spriteset(spriteset_WATER_R2_GRN_E_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(480,330) }
spriteset(spriteset_WATER_R2_GRN_W_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(560,330) }
spriteset(spriteset_WATER_R2_GRN_S_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(320,330) }
spriteset(spriteset_WATER_R2_GRN_N_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(400,330) }
spriteset(spriteset_WATER_R2_GRN_E_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(480,330) }
spriteset(spriteset_WATER_R2_GRN_W_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(560,330) }

spriteset(spriteset_WATER_3_GRN_S_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(0  ,440) }
spriteset(spriteset_WATER_3_GRN_N_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(80 ,440) }
spriteset(spriteset_WATER_3_GRN_E_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(160,440) }
spriteset(spriteset_WATER_3_GRN_W_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(240,440) }
spriteset(spriteset_WATER_3_GRN_S_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(0  ,440) }
spriteset(spriteset_WATER_3_GRN_N_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(80 ,440) }
spriteset(spriteset_WATER_3_GRN_E_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(160,440) }
spriteset(spriteset_WATER_3_GRN_W_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(240,440) }

spriteset(spriteset_WATER_4_GRN_S_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(320,440) }
spriteset(spriteset_WATER_4_GRN_N_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(400,440) }
spriteset(spriteset_WATER_4_GRN_E_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(480,440) }
spriteset(spriteset_WATER_4_GRN_W_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(560,440) }
spriteset(spriteset_WATER_4_GRN_S_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(320,440) }
spriteset(spriteset_WATER_4_GRN_N_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(400,440) }
spriteset(spriteset_WATER_4_GRN_E_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(480,440) }
spriteset(spriteset_WATER_4_GRN_W_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(560,440) }

spriteset(spriteset_WATER_5_GRN_S_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(640,440) }
spriteset(spriteset_WATER_5_GRN_N_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(720,440) }
spriteset(spriteset_WATER_5_GRN_E_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(800,440) }
spriteset(spriteset_WATER_5_GRN_W_TYPE1, "gfx/ground_water_based_type1.png") { template_water_tiles(880,440) }
spriteset(spriteset_WATER_5_GRN_S_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(640,440) }
spriteset(spriteset_WATER_5_GRN_N_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(720,440) }
spriteset(spriteset_WATER_5_GRN_E_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(800,440) }
spriteset(spriteset_WATER_5_GRN_W_TYPE2, "gfx/ground_water_based_type2.png")  { template_water_tiles(880,440) }

spriteset(spriteset_WATER_ONLY_TYPE1, "gfx/ground_water_based_type1.png") { [0, 0, 64, 10, -31, -9, ANIM] }
spriteset(spriteset_WATER_ONLY_TYPE2,  "gfx/ground_water_based_type2.png")  { [0, 0, 64, 10, -31, -9, ANIM] }

// spritesets for foundations (stolen from Brickblocks1's 'CHIPS style dock objects')
spriteset (spriteset_jetty_se_nw,       "gfx/ground_tiles.png") { [10, 50, 64, 39, -31, -7, ANIM] }
spriteset (spriteset_jetty_ne_sw,       "gfx/ground_tiles.png") { [80, 50, 64, 39, -31, -7, ANIM] }
spriteset (spriteset_jetty_slope_nw_se, "gfx/ground_tiles.png") { [150, 50, 64, 39, -31, -7, ANIM] }
spriteset (spriteset_jetty_slope_ne_sw, "gfx/ground_tiles.png") { [220, 50, 64, 39, -31, -7, ANIM] }
spriteset (spriteset_jetty_slope_se_nw, "gfx/ground_tiles.png") { [290, 50, 64, 39, -31, -7, ANIM] }
spriteset (spriteset_jetty_slope_sw_ne, "gfx/ground_tiles.png") { [360, 50, 64, 39, -31, -7, ANIM] }

spriteset (spriteset_jetty_se_nw_no_water, "gfx/ground_tiles.png") { [10, 90, 64, 39, -31, -7, ANIM] }
spriteset (spriteset_jetty_ne_sw_no_water, "gfx/ground_tiles.png") { [80, 90, 64, 39, -31, -7, ANIM] }

spriteset (spriteset_empty_elevated, "gfx/ground_tiles.png") { [290, 10, 64, 31, -31, -8, ANIM] }
spriteset (spriteset_empty, "gfx/ground_tiles.png") { [290, 10, 64, 31, -31, 0, ANIM] }

// SEPARATOR IN PURCHASE MENU
spritelayout layout_menu_separator {
    ground { sprite: GROUNDSPRITE_CLEARED; }
    building { sprite: spriteset_GRN_TYPE2;
               hide_sprite: (1 - param_ground); }
    building { sprite: spriteset_GRN_TYPE1;
               hide_sprite: param_ground; }
}
item (FEAT_OBJECTS, menu_separator, 000) {
    property {
        class:                  "I200";
        classname:              string(STR_Separator);
        name:                   string(STR_Separator_menu);
        climates_available:     ALL_CLIMATES;
        size:                   [1,1];
        build_cost_multiplier:  1;
        remove_cost_multiplier: 1;
        introduction_date:      0x00000000;
        end_of_life_date:       0xFFFFFFFF;
        object_flags:           (param_scenario_editor==1 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) :
                                ( (param_scenario_editor==1 && param_irremovable==0) ? bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ONLY_SE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) :
                                    ((param_scenario_editor==0 && param_irremovable==1) ? bitmask(OBJ_FLAG_IRREMOVABLE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE) : bitmask(OBJ_FLAG_ANYTHING_REMOVE,OBJ_FLAG_ON_WATER,OBJ_FLAG_DRAW_WATER,OBJ_FLAG_ALLOW_BRIDGE)));
        height:                 2;
        num_views:              1;
    }
    graphics {
        default:                layout_menu_separator;
    }
}

"""
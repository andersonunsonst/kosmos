
class StylesCss:
    # Class Method :
    def writecode():
        # Class of Attribute : Public
        v_strucs = """@charset utf-8;
        
/* reset css */
* { margin: 0; padding: 0; border: 0; } 
body { font-family: 'Catamaran', sans-serif; font-size: 16px; } 
img, embed, object, video { max-width: 100%; }

/* 
.title-1  { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.title-2 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.title-3 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.title-4 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.title-5 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.title-6 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }

.subtitle-1  { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.subtitle-2 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.subtitle-3 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.subtitle-4 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.subtitle-5 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.subtitle-6 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }

.paragraph-1  { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.paragraph-2 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.paragraph-3 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }

.link-1  { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.link-2 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }
.link-3 { margin-top:  0px; margin-left: 0px; font-size: 0px; color: 000; }

.grid-media {}
.grid-roller {}
.grid-product {}
.grid-service {}
.grid-desc {}

.block-center {}
.block-left {}
.block-right {}

.block-1 {}
.block-2 {}
.block-3 {}
.block-4 {}
.block-5 {}
.block-6 {}
*/

 /* 
    SMARTPHONE RESPONSIVE 
 */
 @media screen and (min-width: 240px) and (max-width: 319px) {}
 @media screen and (min-width: 320px) and (max-width: 479px) {}
 @media screen and (min-width: 480px) and (max-width: 568px) {

    /* Aplica estilos na navbar : */
    .navbar-1 { background-color: #FFF ! important; box-shadow: none; border-bottom: 1px solid #e0e0e0;  } .menu-1 { display: block ! important; }
        .title-1 { margin-top:  15px; margin-left: 20px; font-size: 20px; color: 000; } .right { margin-right: 20px; }

    .grid-media-1 { height: auto; background-color: transparent; }
        .block-1 { height: 400px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; text-align: center; } 
            .subtitle-1  { font-size: 45px; color: 000; }
            .paragraph-1  { font-size: 35px; color: 000; }

    .grid-roller-1 { height: auto; background-color: transparent; }
        .block-2 { height: auto ! important; height: 200px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; text-align: center;  }
            .subtitle-2  { color: 000; font-size: 35px; }
            .paragraph-2  { color: 000; font-size: 25px; }  

    .grid-desc-1 { height: auto; background-color: transparent; display: flex; flex-direction: column-reverse; }
        .block-left-1 { height: 400px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; } 
            .subtitle-3  { color: 000; font-size: 35px; text-align: center; margin-right: 0px; }
            .paragraph-3  { color: 000; font-size: 25px; text-align: center; margin-left: 0px; margin-right: 0px; }
        .block-right-1 { height: 400px; display: flex; flex-direction: column; justify-content: center;  }

    .grid-media-2 { height: auto; background-color: transparent; }
        .block-3 { height: 400px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; }

    .grid-desc-2 { height: auto; background-color: transparent; }
        .block-left-2 { height: 400px; display: flex; flex-direction: column; justify-content: center; } 
        .block-right-2 { height: 400px; background-color: transparent; display: flex; flex-direction: column; justify-content: center;  }
            .subtitle-4  { color: 000; font-size: 35px; text-align: center; margin-left: 0px; }
            .paragraph-4  { color: 000; font-size: 25px; text-align: center; margin-left: 0px; margin-right: 0px; }

    .grid-catalog-1 { height: auto; background-color: transparent; }
        .block-4 { height: auto ! important; height: 400px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; text-align: center;  }
            .subtitle-5  { color: 000; font-size: 35px; }
            .paragraph-5  { color: 000; font-size: 25px; }

}


 /* 
    IPAD, TABLET RESPONSIVE LAYOUT 
*/
@media screen and (min-width: 569px) and (max-width: 664px) {}
@media screen and (min-width: 665px) and (max-width: 767px) {}
@media screen and (min-width: 768px) and (max-width: 1023px) {

    /* Aplica estilos na navbar : */
    .navbar-1 { background-color: #FFF ! important; box-shadow: none; border-bottom: 1px solid #e0e0e0;  } .menu-1 { display: block ! important; }
        .title-1 { margin-top:  15px; margin-left: 20px; font-size: 20px; color: 000; } .right { margin-right: 20px; }

    .grid-media-1 { height: auto; background-color: transparent; }
        .block-1 { height: 600px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; text-align: center; } 
            .subtitle-1  { font-size: 50px; color: 000; }
            .paragraph-1  { font-size: 40px; color: 000; }

    .grid-roller-1 { height: auto; background-color: transparent; }
        .block-2 { height: auto ! important; height: 200px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; text-align: center;  }
            .subtitle-2  { color: 000; font-size: 40px; }
            .paragraph-2  { color: 000; font-size: 30px; }  

    .grid-desc-1 { height: auto; background-color: transparent; display: flex; flex-direction: column-reverse; }
        .block-left-1 { height: 400px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; } 
            .subtitle-3  { color: 000; font-size: 40px; text-align: center; margin-right: 0px; }
            .paragraph-3  { color: 000; font-size: 30px; text-align: center; margin-left: 0px; margin-right: 0px; }
        .block-right-1 { height: 400px; display: flex; flex-direction: column; justify-content: center;  }

    .grid-media-2 { height: auto; background-color: transparent; }
        .block-3 { height: 600px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; }

    .grid-desc-2 { height: auto; background-color: transparent; }
        .block-left-2 { height: 400px; display: flex; flex-direction: column; justify-content: center; } 
        .block-right-2 { height: 400px; background-color: transparent; display: flex; flex-direction: column; justify-content: center;  }
            .subtitle-4  { color: 000; font-size: 40px; text-align: center; margin-left: 0px; }
            .paragraph-4  { color: 000; font-size: 30px; text-align: center; margin-left: 0px; margin-right: 0px; }

    .grid-catalog-1 { height: auto; background-color: transparent; }
        .block-4 { height: auto ! important; height: 600px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; text-align: center;  }
            .subtitle-5  { color: 000; font-size: 40px; }
            .paragraph-5  { color: 000; font-size: 30px; }
            
}


 /* 
    DESKTOP PC, NOTEBOOK E NETBOOK RESPONSIVE LAYOUT 
*/
@media screen and (min-width: 1024px) and (max-width: 1278px) {}
@media screen and (min-width: 1280px) and (max-width: 1438px) {}
@media screen and (min-width: 1440px) and (max-width: 1678px) {}
@media screen and (min-width: 1680px) and (max-width: 1920px) {

    /* Aplica estilos na navbar : */
    .navbar-1 { background-color: transparent ! important; box-shadow: none; border-bottom: 0px solid #e0e0e0;  } .menu-1 { display: none ! important; }
        .title-1 { margin-top:  15px; margin-left: 20px; font-size: 30px; color: 000; } .right { margin-right: 20px; }

    .grid-media-1 { height: auto; background-color: transparent; margin-top: -64px; }
        .block-1 { 
                    height: 940px; background-image: url('/assets/util/banmain.svg'); background-repeat: no-repeat;
                    display: flex; flex-direction: column; justify-content: center; text-align: center; 
                }
            .subtitle-1  { font-size: 70px; color: 000; }
            .paragraph-1  { font-size: 60px; color: 000; }

    .grid-roller-1 { height: auto; background-color: transparent; }
        .block-2 { height: 200px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; text-align: center;  }
            .subtitle-2  { color: 000; font-size: 35px; }
            .paragraph-2  { color: 000; font-size: 25px; }  

    .grid-desc-1 { height: auto; background-color: transparent; }
        .block-left-1 { height: 800px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; } 
            .subtitle-3  { color: 000; font-size: 60px; text-align: right; margin-right: 80px; }
            .paragraph-3  { color: 000; font-size: 50px; text-align: right; margin-left: 80px; margin-right: 80px; }
        .block-right-1 { height: 800px; display: flex; flex-direction: column; justify-content: center;  }

    .grid-media-2 { height: auto; background-color: transparent; }
        .block-3 { height: 800px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; }

    .grid-desc-2 { height: auto; background-color: transparent; }
        .block-left-2 { height: 800px; display: flex; flex-direction: column; justify-content: center; } 
        .block-right-2 { height: 800px; background-color: transparent; display: flex; flex-direction: column; justify-content: center;  }
            .util-zoom-1 { margin: 0 auto; max-width: 500px; max-height: 500px; width: 100%; height: 100%; }
            .subtitle-4  { color: 000; font-size: 60px; text-align: left; margin-left: 80px; }
            .paragraph-4  { color: 000; font-size: 30px; text-align: left; margin-left: 80px; margin-right: 80px; }

    .grid-catalog-1 { height: auto; background-color: transparent; }
        .block-4 { height: 800px; background-color: transparent; display: flex; flex-direction: column; justify-content: center; text-align: center;  }
            .subtitle-5  { color: 000; font-size: 60px; }
            .paragraph-5  { color: 000; font-size: 50px; }

}
        """
        return v_strucs
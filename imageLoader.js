var imageLoader = {
    loaded:true,
    loadedImages:0,
    totalImages:0,
    load:function(url){
        this.totalImages++;
        this.loaded = false;
        var image = new Image();
        image.src = url;
        image.onload = function(){
            imageLoader.loadedImages++;
            if(imageLoader.loadedImages === imageLoader.totalImages){
                imageLoader.loaded = true;
            }
        }
        return image;
    }
}
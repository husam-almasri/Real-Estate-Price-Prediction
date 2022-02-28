function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBRValue() {
    var uiBedrooms = document.getElementsByName("uiBedrooms");
    for(var i in uiBedrooms) {
      if(uiBedrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }

  function getBalconiesValue() {
    var uiBalconies = document.getElementsByName("uiBalconies");
    for(var i in uiBalconies) {
      if(uiBalconies[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var total_sqft = document.getElementById("uiSqft");
    var bedrooms = getBRValue();
    var bath = getBathValue();
    var balcony = getBalconiesValue();
    var location = document.getElementById("uiLocations");
    var area_type = document.getElementById("uiAreas");

    var estPrice = document.getElementById("uiEstimatedPrice");
    var url = "http://127.0.0.1:5000/predict_home_price";
  
    $.post(url, {
        bedrooms: bedrooms,
        total_sqft: parseFloat(total_sqft.value),
        bath: bath,
        balcony: balcony,
        area_type: area_type.value,
        location: location.value
      },function(data, status) {
        estPrice.innerHTML = "<h1>" + data.estimated_price.toString() + "</h1>";
      }
    );
  }
  
  function onPageLoad() {
    var url1 = "http://127.0.0.1:5000/get_location_names";
    $.get(url1,function(data, status) {
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
        
        });

        var url2 = "http://127.0.0.1:5000/get_area_names"; 
        $.get(url2,function(data, status) {
            if(data) {
                var areas = data.Area_type;
                var uiAreas = document.getElementById("uiAreas");
                $('#uiAreas').empty();
                for(var i in areas) {
                    var opt = new Option(areas[i]);
                    $('#uiAreas').append(opt);
                }
            }
            
            });
          }
  window.onload = onPageLoad;
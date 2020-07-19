import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:geocoder/geocoder.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:intl/intl.dart';
import 'package:leaf_problem_detection/models/user_model.dart';
import 'package:leaf_problem_detection/models/weather_model.dart';
import 'package:leaf_problem_detection/utils/firebase.dart';
import 'package:leaf_problem_detection/utils/localization.dart';
import 'package:leaf_problem_detection/widgets/card.dart';
import 'package:location/location.dart' as loc;
import 'package:permission_handler/permission_handler.dart';
import 'package:provider/provider.dart';
import 'package:http/http.dart' as http;

final PermissionHandler _permissionHandler = PermissionHandler();

Future<loc.LocationData> getLocation(bool check) async {
  requestLocationPermission();
  loc.Location location = new loc.Location();

  bool _serviceEnabled;
  loc.PermissionStatus _permissionGranted;
  loc.LocationData _locationData;
  _serviceEnabled = await location.serviceEnabled();
  if (!_serviceEnabled) {
    _serviceEnabled = await location.requestService();
    if (!_serviceEnabled) {}
  }

  _permissionGranted = await location.hasPermission();
  if (_permissionGranted == PermissionStatus.denied) {
    _permissionGranted = await location.requestPermission();
    if (_permissionGranted != PermissionStatus.granted) {}
  }

  if (check) await Future.delayed(Duration(seconds: 5));
  _locationData = await location.getLocation();
  return _locationData;
}

Future<bool> requestLocationPermission() async {
  return requestPermission(PermissionGroup.locationWhenInUse);
}

Future<bool> requestPermission(PermissionGroup permission) async {
  var result = await _permissionHandler.requestPermissions([permission]);
  if (result[permission] == PermissionStatus.granted) {
    return true;
  }
  return false;
}

Widget showLocData(BuildContext context) {
  var coords;
  try {
    UserModel user = Provider.of<UserModel>(context, listen: false);
    coords = new Coordinates(user.loc.latitude, user.loc.longitude);
  } catch (Exception) {
    return Row(
      children: [
        Text(
          DemoLocalizations.of(context).vals["FirstPage"]["7"],
          style: TextStyle(
            color: Colors.black54,
            fontWeight: FontWeight.w500,
            fontSize: MediaQuery.of(context).size.height < 600 ? 11.3 : 17,
          ),
          softWrap: true,
        ),
        Text(
          " NA",
          style: TextStyle(
            color: Colors.black54,
            fontSize: MediaQuery.of(context).size.height < 600 ? 11.3 : 17,
          ),
          softWrap: true,
        ),
      ],
    );
  }

  return FutureBuilder<List<Address>>(
    future: Geocoder.local.findAddressesFromCoordinates(coords),
    builder: (context, data) {
      if (data.hasData) {
        return Container(
          child: Wrap(
            children: [
              Text(
                DemoLocalizations.of(context).vals["FirstPage"]["7"],
                style: TextStyle(
                  color: Colors.black54,
                  fontWeight: FontWeight.w500,
                  fontSize:
                      MediaQuery.of(context).size.height < 600 ? 11.3 : 17,
                ),
                softWrap: true,
              ),
              Text(
                data.data[0].addressLine,
                style: TextStyle(
                  color: Colors.black54,
                  fontSize:
                      MediaQuery.of(context).size.height < 600 ? 11.3 : 17,
                ),
                //softWrap: true,
                overflow: TextOverflow.ellipsis,
              ),
            ],
          ),
        );
      } else {
        return Center(child: CircularProgressIndicator());
      }
    },
  );
}

Widget buildWeatherCard(BuildContext context) {
  return card(
    context,
    IntrinsicHeight(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: usingWeatherData(context),
          ),
        ],
      ),
    ),
  );
}

Widget usingWeatherData(BuildContext context) {
  try {
    WeatherModel data = Provider.of<WeatherModel>(context, listen: true);
    print(data.day);
    return Container(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    data.day,
                    style: TextStyle(
                      color: Colors.black54,
                      fontSize:
                          MediaQuery.of(context).size.height < 600 ? 16.5 : 25,
                    ),
                  ),
                  Text(
                    data.temp + "°C",
                    style: TextStyle(
                      color: Colors.black,
                      fontSize:
                          MediaQuery.of(context).size.height < 600 ? 20 : 30,
                    ),
                  ),
                  Text(
                    data.minTemp + "°C/" + data.maxTemp + "°C",
                    style: TextStyle(
                      color: Colors.black38,
                      fontSize:
                          MediaQuery.of(context).size.height < 600 ? 10 : 15,
                    ),
                  ),
                ],
              ),
              Image.network(
                  "http://openweathermap.org/img/wn/" + data.id + "@2x.png",
                  scale: 1.5),
            ],
          ),
          Divider(color: Color.fromRGBO(24, 165, 123, 1)),
          Wrap(
            children: [
              Text(
                DemoLocalizations.of(context).vals["FirstPage"]["1"],
                style: TextStyle(
                  color: Colors.black54,
                  fontWeight: FontWeight.w500,
                  fontSize:
                      MediaQuery.of(context).size.height < 600 ? 11.3 : 17,
                ),
              ),
              Text(
                data.typeWeather,
                style: TextStyle(
                  color: Colors.black54,
                  fontSize:
                      MediaQuery.of(context).size.height < 600 ? 11.3 : 17,
                ),
              ),
            ],
          ),
          Wrap(
            children: [
              Text(
                DemoLocalizations.of(context).vals["FirstPage"]["2"],
                style: TextStyle(
                  color: Colors.black54,
                  fontWeight: FontWeight.w500,
                  fontSize:
                      MediaQuery.of(context).size.height < 600 ? 11.3 : 17,
                ),
              ),
              Text(
                data.humidity + "%",
                style: TextStyle(
                  color: Colors.black54,
                  fontSize:
                      MediaQuery.of(context).size.height < 600 ? 11.3 : 17,
                ),
              ),
            ],
          ),
          showLocData(context),
        ],
      ),
    );
  } catch (e) {
    print("error: " + e.toString());
    return locNotEnabled();
  }
}

class locNotEnabled extends StatefulWidget {
  locNotEnabled();

  @override
  _locNotEnabled createState() => _locNotEnabled();
}

class _locNotEnabled extends State<locNotEnabled> {
  _locNotEnabled();
  bool switchState = false;
  PermissionHandler _permissionHandler = PermissionHandler();
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Center(
          child: Text(
            DemoLocalizations.of(context).vals["FirstPage"]["8"],
            style: TextStyle(fontWeight: FontWeight.w400, fontSize: 17),
          ),
        ),
        ListTile(
          contentPadding: EdgeInsets.zero,
          title: Text("Enable Location Permissions: "),
          trailing: CupertinoSwitch(
            value: switchState,
            activeColor: Color.fromRGBO(24, 165, 123, 1),
            onChanged: (selected) async {
              setState(
                () {
                  switchState = !switchState;
                  getLocation(true).then((value) {
                    Provider.of<UserModel>(context, listen: false).loc =
                        LatLng(value.latitude, value.longitude);
                    setWeatherData(
                        Provider.of<UserModel>(context, listen: false).uid,
                        context,
                        value.latitude.toString(),
                        value.longitude.toString());
                    updateUserWeather(
                        Provider.of<UserModel>(context, listen: false).uid,
                        value);
                  });
                },
              );
            },
          ),
        )
      ],
    );
  }
}

Future<Map> getWeatherData(String uid, String lat, String long) async {
  String apiKey = await rootBundle.loadString("data/keys.json");
  String weatherKey = jsonDecode(apiKey)["weather"];
  String path = 'http://api.openweathermap.org/data/2.5/weather?lat=' +
      lat.toString().trim() +
      '&lon=' +
      long.toString().trim() +
      '&appid=' +
      weatherKey +
      '&units=metric';

  var request = await http.get(path);
  return json.decode(request.body);
}
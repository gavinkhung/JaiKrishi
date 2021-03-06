import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:location/location.dart';
import 'package:provider/provider.dart';
import 'package:flutter/material.dart';

class UserModel extends ChangeNotifier {
  String _phoneNumber;
  String _url;
  String _uid;
  DateTime _seed;
  DateTime _trans;
  String _crop;
  int _type;
  LatLng _loc;
  Map _data;
  String _address;
  String _tutLink;

  String get phoneNumber => _phoneNumber;
  String get url => _url;
  String get uid => _uid;
  DateTime get seed => _seed;
  DateTime get trans => _trans;
  String get crop => _crop;
  int get type => _type;
  LatLng get loc => _loc;
  Map get data => _data;
  String get address => _address;
  String get tutLink => _tutLink;

  set tutLink(String val) {
    _tutLink = val;
  }

  set address(String val) {
    _address = val;
  }

  set loc(LatLng val) {
    _loc = val;
    //notifyListeners();
  }

  set data(Map val) {
    _data = val;
    //notifyListeners();
  }

  set seed(DateTime val) {
    _seed = val;
    //notifyListeners();
  }

  set trans(DateTime val) {
    _trans = val;
    //notifyListeners();
  }

  set crop(String val) {
    _crop = val;
    //notifyListeners();
  }

  set type(int val) {
    _type = val;
    //notifyListeners();
  }

  set phoneNumber(String value) {
    _phoneNumber = value;
    //notifyListeners();
  }

  set uid(String val) {
    _uid = val;
    //notifyListeners();
  }

  set url(String val) {
    _url = val;
    //notifyListeners();
  }
}

import 'package:flutter/material.dart';
import 'package:leaf_problem_detection/utils/firebase.dart';
import 'package:provider/provider.dart';
import 'models/user_model.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(
          create: (context) => UserModel(),
        ),
      ],
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: App(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class App extends StatefulWidget {
  App();
  @override
  _App createState() => _App();
}

class _App extends State<App> {
  Widget build(BuildContext context) {
    return Scaffold(
      body: autoLogin(
        Text("pee"),
        Text("poo"),
      ),
    );
  }
}

import 'package:flutter/material.dart';
import 'main_menu.dart'; // MainMenu sınıfını içe aktar

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Giriş Sayfası',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: LoginPage(), // Giriş sayfasını ayarla
    );
  }
}

class LoginPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Giriş Sayfası'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => MainMenu()), // Ana menüye geçiş
            );
          },
          child: const Text('Giriş Yap'),
        ),
      ),
    );
  }
}
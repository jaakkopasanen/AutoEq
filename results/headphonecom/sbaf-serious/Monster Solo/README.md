# Monster Solo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -8.0; 22 -8.3; 23 -8.5; 25 -8.7; 26 -8.8; 28 -9.1; 30 -9.2; 32 -9.4; 35 -9.7; 37 -9.8; 40 -10.0; 42 -10.2; 45 -10.3; 49 -10.4; 52 -10.5; 56 -10.7; 59 -10.9; 64 -11.3; 68 -11.4; 73 -11.5; 78 -11.5; 83 -11.4; 89 -11.1; 95 -10.7; 102 -10.0; 109 -9.5; 117 -9.9; 125 -10.6; 134 -11.2; 143 -11.5; 153 -11.1; 164 -10.3; 175 -10.0; 188 -9.8; 201 -9.2; 215 -8.3; 230 -7.2; 246 -6.2; 263 -5.1; 282 -4.4; 301 -3.9; 323 -3.3; 345 -2.7; 369 -2.0; 395 -1.3; 423 -0.4; 452 0.2; 484 0.5; 518 0.6; 554 0.8; 593 0.9; 635 0.7; 679 0.3; 726 0.0; 777 -0.1; 832 -0.2; 890 -0.4; 952 -0.2; 1019 0.1; 1090 0.5; 1167 1.0; 1248 1.5; 1336 1.8; 1429 1.9; 1529 2.0; 1636 2.0; 1751 2.1; 1873 2.3; 2004 2.4; 2145 2.4; 2295 2.7; 2455 2.9; 2627 2.8; 2811 3.3; 3008 3.6; 3219 3.5; 3444 3.2; 3685 2.6; 3943 1.9; 4219 0.6; 4514 -0.2; 4830 1.8; 5168 5.4; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Solo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.5  | -7.3 dB |
| Peaking | 75 Hz   | 0.79 | -7.2 dB |
| Peaking | 171 Hz  | 1.26 | -7.8 dB |
| Peaking | 2353 Hz | 0.83 | 3.0 dB  |
| Peaking | 5879 Hz | 4.01 | 6.2 dB  |
| Peaking | 518 Hz  | 1.53 | 4.0 dB  |
| Peaking | 516 Hz  | 0.78 | -2.3 dB |
| Peaking | 4557 Hz | 1.75 | 2.7 dB  |
| Peaking | 4443 Hz | 5.07 | -5.1 dB |
| Peaking | 8325 Hz | 2.38 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Solo/Monster%20Solo.png)
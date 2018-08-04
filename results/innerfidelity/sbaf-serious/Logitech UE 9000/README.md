# Logitech UE 9000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.1; 22 -0.4; 23 -0.5; 25 -0.8; 26 -0.9; 28 -1.1; 30 -1.2; 32 -1.3; 35 -1.4; 37 -1.5; 40 -1.6; 42 -1.6; 45 -1.7; 49 -1.6; 52 -1.6; 56 -1.5; 59 -1.5; 64 -1.4; 68 -1.4; 73 -1.3; 78 -1.3; 83 -1.3; 89 -1.2; 95 -1.3; 102 -1.5; 109 -1.7; 117 -2.5; 125 -3.4; 134 -3.8; 143 -3.5; 153 -3.0; 164 -2.3; 175 -1.7; 188 -2.0; 201 -2.4; 215 -2.2; 230 -1.6; 246 -1.1; 263 -0.7; 282 -0.3; 301 -0.2; 323 0.1; 345 0.5; 369 0.7; 395 1.0; 423 1.2; 452 1.3; 484 1.2; 518 1.3; 554 1.4; 593 1.5; 635 1.4; 679 1.1; 726 0.9; 777 0.9; 832 0.8; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.0; 1336 0.1; 1429 0.1; 1529 0.0; 1636 0.0; 1751 0.6; 1873 1.2; 2004 1.8; 2145 2.5; 2295 3.7; 2455 4.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 4.8; 4219 4.0; 4514 4.0; 4830 3.7; 5168 5.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 9000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.88 | -1.7 dB |
| Peaking | 208 Hz  | 4.61 | -1.9 dB |
| Peaking | 136 Hz  | 2.92 | -3.6 dB |
| Peaking | 3112 Hz | 1.63 | 6.5 dB  |
| Peaking | 5819 Hz | 3.35 | 5.5 dB  |
| Peaking | 551 Hz  | 0.75 | 1.8 dB  |
| Peaking | 1278 Hz | 1.03 | -1.4 dB |
| Peaking | 2502 Hz | 6.79 | 1.4 dB  |
| Peaking | 266 Hz  | 1.41 | -0.8 dB |
| Peaking | 8289 Hz | 4.41 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%209000/Logitech%20UE%209000.png)
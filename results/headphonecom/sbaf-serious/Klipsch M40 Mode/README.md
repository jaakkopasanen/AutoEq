# Klipsch M40 Mode

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.3; 23 -4.5; 25 -4.8; 26 -4.8; 28 -5.0; 30 -5.0; 32 -5.0; 35 -5.0; 37 -5.0; 40 -4.8; 42 -4.8; 45 -4.7; 49 -4.6; 52 -4.4; 56 -4.3; 59 -4.2; 64 -4.0; 68 -3.9; 73 -3.7; 78 -3.5; 83 -3.3; 89 -3.0; 95 -2.8; 102 -2.5; 109 -2.3; 117 -2.0; 125 -2.0; 134 -1.8; 143 -1.6; 153 -1.4; 164 -1.3; 175 -1.1; 188 -1.1; 201 -1.0; 215 -0.7; 230 -0.8; 246 -0.7; 263 -0.6; 282 -0.3; 301 0.1; 323 0.7; 345 0.8; 369 0.7; 395 0.6; 423 0.7; 452 0.7; 484 0.5; 518 0.6; 554 1.0; 593 1.1; 635 1.2; 679 1.1; 726 1.0; 777 1.1; 832 0.9; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.7; 1167 -1.3; 1248 -2.0; 1336 -2.9; 1429 -4.2; 1529 -5.3; 1636 -5.6; 1751 -4.1; 1873 -2.5; 2004 0.1; 2145 2.5; 2295 4.1; 2455 5.8; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch M40 Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.36 | -4.9 dB |
| Peaking | 655 Hz  | 1.84 | 1.1 dB  |
| Peaking | 348 Hz  | 3.89 | 1.0 dB  |
| Peaking | 1609 Hz | 2.14 | -9.7 dB |
| Peaking | 3169 Hz | 0.68 | 7.8 dB  |
| Peaking | 1923 Hz | 6.24 | -0.8 dB |
| Peaking | 2446 Hz | 3.75 | 1.5 dB  |
| Peaking | 3318 Hz | 2.49 | -1.2 dB |
| Peaking | 6224 Hz | 2.14 | 5.6 dB  |
| Peaking | 7447 Hz | 1.45 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20M40%20Mode/Klipsch%20M40%20Mode.png)
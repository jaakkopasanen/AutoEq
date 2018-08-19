# Denon AH-C260R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.3dB
GraphicEQ: 10 -84; 20 -15.1; 22 -15.1; 23 -15.1; 25 -15.0; 26 -15.0; 28 -14.9; 30 -14.8; 32 -14.7; 35 -14.6; 37 -14.5; 40 -14.3; 42 -14.2; 45 -14.1; 49 -13.9; 52 -13.8; 56 -13.7; 59 -13.6; 64 -13.4; 68 -13.3; 73 -13.2; 78 -13.0; 83 -12.9; 89 -12.7; 95 -12.5; 102 -12.2; 109 -11.9; 117 -11.7; 125 -11.4; 134 -11.2; 143 -10.9; 153 -10.7; 164 -10.3; 175 -9.9; 188 -9.6; 201 -9.2; 215 -8.7; 230 -8.3; 246 -7.8; 263 -7.3; 282 -6.9; 301 -6.3; 323 -5.8; 345 -5.2; 369 -4.7; 395 -4.2; 423 -3.7; 452 -3.3; 484 -2.8; 518 -2.4; 554 -1.9; 593 -1.4; 635 -0.9; 679 -0.6; 726 -0.3; 777 -0.0; 832 0.2; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.2; 1429 -1.7; 1529 -2.1; 1636 -2.5; 1751 -2.7; 1873 -2.7; 2004 -2.8; 2145 -2.9; 2295 -2.9; 2455 -2.9; 2627 -3.2; 2811 -3.5; 3008 -3.7; 3219 -2.9; 3444 -1.8; 3685 -1.0; 3943 -1.4; 4219 -2.5; 4514 -3.8; 4830 -4.5; 5168 -5.0; 5530 -5.8; 5917 -6.4; 6331 -5.2; 6775 -3.5; 7249 -2.4; 7756 -1.5; 8299 -1.2; 8880 -1.8; 9502 -3.3; 10167 -3.8; 10879 -1.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.0; 17469 -1.7; 18692 -0.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.2929168449823528dB` and instead set Global volume in the UI for both channels to **-2**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C260R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.19 | -14.8 dB |
| Peaking | 178 Hz   | 0.68 | -4.3 dB  |
| Peaking | 2357 Hz  | 1.55 | -3.0 dB  |
| Peaking | 5756 Hz  | 1.95 | -5.8 dB  |
| Peaking | 17861 Hz | 4.14 | -1.9 dB  |
| Peaking | 837 Hz   | 2.22 | 1.5 dB   |
| Peaking | 1605 Hz  | 4.74 | -1.1 dB  |
| Peaking | 7930 Hz  | 3.59 | 1.1 dB   |
| Peaking | 10010 Hz | 4.06 | -4.6 dB  |
| Peaking | 11271 Hz | 2.5  | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C260R/Denon%20AH-C260R.png)
# Nocs NS400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 10 -84; 20 -12.2; 22 -12.1; 23 -12.0; 25 -12.0; 26 -11.9; 28 -11.9; 30 -11.9; 32 -11.8; 35 -11.7; 37 -11.7; 40 -11.6; 42 -11.5; 45 -11.5; 49 -11.4; 52 -11.4; 56 -11.4; 59 -11.3; 64 -11.2; 68 -11.2; 73 -11.1; 78 -11.1; 83 -11.0; 89 -10.9; 95 -10.8; 102 -10.6; 109 -10.4; 117 -10.2; 125 -10.0; 134 -9.8; 143 -9.6; 153 -9.3; 164 -9.1; 175 -8.7; 188 -8.4; 201 -8.0; 215 -7.6; 230 -7.1; 246 -6.7; 263 -6.3; 282 -5.8; 301 -5.3; 323 -4.8; 345 -4.3; 369 -3.8; 395 -3.3; 423 -2.9; 452 -2.4; 484 -2.0; 518 -1.5; 554 -1.1; 593 -0.7; 635 -0.3; 679 0.1; 726 0.3; 777 0.4; 832 0.5; 890 0.5; 952 0.3; 1019 0.0; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.7; 1529 -2.1; 1636 -2.5; 1751 -2.8; 1873 -3.1; 2004 -3.7; 2145 -4.3; 2295 -4.6; 2455 -4.7; 2627 -4.3; 2811 -3.3; 3008 -1.7; 3219 0.4; 3444 2.3; 3685 3.3; 3943 3.1; 4219 1.9; 4514 0.7; 4830 0.0; 5168 -0.3; 5530 -1.4; 5917 -3.8; 6331 -6.7; 6775 -6.3; 7249 -4.4; 7756 -2.5; 8299 -0.9; 8880 -0.5; 9502 -1.5; 10167 -2.5; 10879 -1.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.1; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.5233439363143395dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.21 | -11.8 dB |
| Peaking | 170 Hz   | 0.73 | -4.3 dB  |
| Peaking | 2438 Hz  | 1.76 | -5.7 dB  |
| Peaking | 3753 Hz  | 2.65 | 5.4 dB   |
| Peaking | 6632 Hz  | 3.78 | -7.3 dB  |
| Peaking | 328 Hz   | 2.05 | -0.8 dB  |
| Peaking | 790 Hz   | 1.52 | 1.6 dB   |
| Peaking | 1561 Hz  | 3.28 | -1.0 dB  |
| Peaking | 9930 Hz  | 1.95 | 1.2 dB   |
| Peaking | 10118 Hz | 5.36 | -3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS400/Nocs%20NS400.png)
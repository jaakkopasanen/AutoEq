# Meze 11 Deco

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -11.6; 22 -11.6; 23 -11.6; 25 -11.6; 26 -11.6; 28 -11.6; 30 -11.6; 32 -11.6; 35 -11.6; 37 -11.5; 40 -11.4; 42 -11.4; 45 -11.3; 49 -11.2; 52 -11.2; 56 -11.1; 59 -11.0; 64 -10.9; 68 -10.9; 73 -10.8; 78 -10.9; 83 -10.9; 89 -11.1; 95 -11.4; 102 -11.6; 109 -11.9; 117 -12.1; 125 -12.5; 134 -12.7; 143 -12.7; 153 -12.6; 164 -12.4; 175 -12.1; 188 -11.7; 201 -11.4; 215 -11.0; 230 -10.5; 246 -10.1; 263 -9.6; 282 -9.1; 301 -8.6; 323 -8.1; 345 -7.5; 369 -7.1; 395 -6.6; 423 -5.9; 452 -5.3; 484 -5.0; 518 -4.4; 554 -3.8; 593 -3.2; 635 -2.2; 679 -1.9; 726 -1.5; 777 -0.5; 832 -0.1; 890 -0.3; 952 -0.2; 1019 0.1; 1090 0.2; 1167 0.3; 1248 0.4; 1336 0.4; 1429 0.1; 1529 -0.5; 1636 -1.9; 1751 -3.5; 1873 -4.4; 2004 -4.1; 2145 -3.2; 2295 -1.9; 2455 0.0; 2627 1.6; 2811 3.4; 3008 5.4; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.9; 4514 4.9; 4830 4.2; 5168 3.8; 5530 2.4; 5917 -1.0; 6331 -6.6; 6775 -6.6; 7249 -2.5; 7756 0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 11 Deco ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.37 | -10.6 dB |
| Peaking | 173 Hz   | 0.46 | -10.9 dB |
| Peaking | 2063 Hz  | 1.74 | -12.8 dB |
| Peaking | 2795 Hz  | 0.58 | 10.1 dB  |
| Peaking | 6544 Hz  | 4.7  | -11.7 dB |
| Peaking | 802 Hz   | 8.73 | 1.0 dB   |
| Peaking | 1761 Hz  | 8.73 | -1.5 dB  |
| Peaking | 2630 Hz  | 7.56 | -1.4 dB  |
| Peaking | 5301 Hz  | 0.48 | 0.8 dB   |
| Peaking | 10222 Hz | 1.06 | -1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2011%20Deco/Meze%2011%20Deco.png)
# Phiaton PS 300 NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.1; 22 -2.0; 23 -2.9; 25 -4.5; 26 -5.1; 28 -6.3; 30 -7.2; 32 -8.0; 35 -8.9; 37 -9.4; 40 -10.0; 42 -10.3; 45 -10.7; 49 -11.2; 52 -11.4; 56 -11.5; 59 -11.5; 64 -11.4; 68 -11.3; 73 -12.1; 78 -13.0; 83 -13.1; 89 -13.1; 95 -13.1; 102 -13.0; 109 -12.8; 117 -12.8; 125 -12.8; 134 -12.7; 143 -12.6; 153 -12.5; 164 -12.4; 175 -12.1; 188 -11.7; 201 -11.2; 215 -11.2; 230 -11.1; 246 -10.9; 263 -10.9; 282 -11.0; 301 -10.9; 323 -11.0; 345 -10.7; 369 -10.3; 395 -9.5; 423 -8.2; 452 -6.4; 484 -3.6; 518 -0.1; 554 3.0; 593 4.6; 635 4.2; 679 3.8; 726 3.2; 777 2.4; 832 1.5; 890 0.8; 952 0.4; 1019 -0.0; 1090 -0.7; 1167 -1.7; 1248 -1.7; 1336 -2.5; 1429 -3.9; 1529 -5.4; 1636 -6.6; 1751 -7.7; 1873 -6.8; 2004 -4.9; 2145 -3.0; 2295 -1.5; 2455 0.0; 2627 1.6; 2811 1.6; 3008 1.8; 3219 4.1; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -0.2; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 300 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 66 Hz   | 0.54 | -11.6 dB |
| Peaking | 174 Hz  | 1.1  | -7.4 dB  |
| Peaking | 336 Hz  | 2.81 | -8.1 dB  |
| Peaking | 1775 Hz | 3.12 | -9.1 dB  |
| Peaking | 4394 Hz | 1.18 | 7.1 dB   |
| Peaking | 1366 Hz | 2.63 | -1.3 dB  |
| Peaking | 444 Hz  | 2.96 | -5.9 dB  |
| Peaking | 597 Hz  | 1.99 | 8.1 dB   |
| Peaking | 6307 Hz | 3.39 | 4.7 dB   |
| Peaking | 7370 Hz | 1.53 | -3.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Phiaton%20PS%20300%20NC/Phiaton%20PS%20300%20NC.png)
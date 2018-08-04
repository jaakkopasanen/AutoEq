# Ultrasone HFI-580

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 3.2; 22 2.1; 23 1.6; 25 0.7; 26 0.2; 28 -0.6; 30 -1.4; 32 -2.1; 35 -3.1; 37 -3.6; 40 -4.3; 42 -4.6; 45 -5.0; 49 -5.4; 52 -5.6; 56 -5.6; 59 -5.5; 64 -5.3; 68 -5.2; 73 -3.9; 78 -2.3; 83 -2.1; 89 -2.4; 95 -2.4; 102 -2.3; 109 -2.1; 117 -1.6; 125 -1.0; 134 -0.3; 143 0.2; 153 0.7; 164 2.1; 175 3.5; 188 3.6; 201 1.0; 215 0.0; 230 0.1; 246 -0.4; 263 -1.0; 282 -1.6; 301 -1.9; 323 -1.9; 345 -1.5; 369 -1.2; 395 -0.9; 423 -0.6; 452 -0.4; 484 -0.4; 518 -0.4; 554 -0.3; 593 -0.0; 635 0.1; 679 0.1; 726 0.1; 777 0.3; 832 0.2; 890 0.1; 952 -0.0; 1019 -0.0; 1090 0.4; 1167 1.1; 1248 0.3; 1336 -0.3; 1429 -0.9; 1529 -1.3; 1636 -2.2; 1751 -3.3; 1873 -4.0; 2004 -4.3; 2145 -4.3; 2295 -4.2; 2455 -3.8; 2627 -4.1; 2811 -4.9; 3008 -5.8; 3219 -7.3; 3444 -7.1; 3685 -6.2; 3943 -4.8; 4219 -3.7; 4514 -2.6; 4830 -0.1; 5168 2.3; 5530 4.3; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.2; 7756 -2.3; 8299 -4.9; 8880 -6.4; 9502 -6.8; 10167 -5.8; 10879 -2.7; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 54 Hz    | 1.44 | -6.1 dB |
| Peaking | 3458 Hz  | 1.78 | -7.7 dB |
| Peaking | 1986 Hz  | 3.4  | -3.2 dB |
| Peaking | 6074 Hz  | 2.48 | 8.7 dB  |
| Peaking | 9081 Hz  | 2.73 | -8.4 dB |
| Peaking | 105 Hz   | 4.36 | -1.2 dB |
| Peaking | 178 Hz   | 4.86 | 4.5 dB  |
| Peaking | 311 Hz   | 2.69 | -2.0 dB |
| Peaking | 1167 Hz  | 5.55 | 1.6 dB  |
| Peaking | 11955 Hz | 6.15 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFI-580/Ultrasone%20HFI-580.png)
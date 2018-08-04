# Ultrasone HFI-450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.8; 40 5.1; 42 4.5; 45 3.6; 49 2.4; 52 1.6; 56 0.8; 59 0.1; 64 -0.9; 68 -1.3; 73 -1.1; 78 -0.4; 83 -0.6; 89 -1.7; 95 -2.6; 102 -3.1; 109 -3.3; 117 -3.2; 125 -2.4; 134 -2.1; 143 -2.0; 153 -1.8; 164 -1.3; 175 -0.6; 188 -0.6; 201 -0.4; 215 -0.3; 230 -0.2; 246 -0.6; 263 -1.5; 282 -2.4; 301 -3.0; 323 -3.5; 345 -3.8; 369 -3.3; 395 -2.7; 423 -3.0; 452 -2.7; 484 -2.0; 518 -1.3; 554 -1.0; 593 -0.7; 635 -0.4; 679 -0.3; 726 -0.3; 777 -0.1; 832 0.0; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.2; 1167 0.3; 1248 0.7; 1336 1.3; 1429 2.3; 1529 2.9; 1636 3.1; 1751 1.7; 1873 0.7; 2004 0.9; 2145 1.5; 2295 2.4; 2455 3.3; 2627 4.5; 2811 5.4; 3008 5.5; 3219 4.8; 3444 3.6; 3685 4.3; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.2; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 1.01 | 6.9 dB  |
| Peaking | 104 Hz  | 1.52 | -3.6 dB |
| Peaking | 367 Hz  | 1.94 | -3.7 dB |
| Peaking | 3192 Hz | 1.1  | 4.4 dB  |
| Peaking | 5414 Hz | 2.33 | 5.0 dB  |
| Peaking | 65 Hz   | 1.36 | 1.2 dB  |
| Peaking | 64 Hz   | 3.52 | -2.8 dB |
| Peaking | 1572 Hz | 4.98 | 2.5 dB  |
| Peaking | 1942 Hz | 4.77 | -1.9 dB |
| Peaking | 8847 Hz | 3.25 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Ultrasone%20HFI-450/Ultrasone%20HFI-450.png)
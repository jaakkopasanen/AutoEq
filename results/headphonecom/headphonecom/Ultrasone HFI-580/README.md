# Ultrasone HFI-580

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.7; 22 1.6; 23 1.1; 25 0.1; 26 -0.3; 28 -1.2; 30 -1.9; 32 -2.7; 35 -3.6; 37 -4.2; 40 -4.9; 42 -5.2; 45 -5.6; 49 -6.0; 52 -6.1; 56 -6.2; 59 -6.0; 64 -5.9; 68 -5.7; 73 -4.5; 78 -2.9; 83 -2.9; 89 -3.2; 95 -3.3; 102 -3.3; 109 -3.2; 117 -2.8; 125 -2.2; 134 -1.6; 143 -1.1; 153 -0.6; 164 0.7; 175 2.1; 188 2.2; 201 -0.4; 215 -1.4; 230 -1.3; 246 -1.7; 263 -2.3; 282 -3.0; 301 -3.2; 323 -3.3; 345 -2.9; 369 -2.6; 395 -2.1; 423 -1.8; 452 -1.4; 484 -1.1; 518 -1.0; 554 -0.8; 593 -0.5; 635 -0.2; 679 0.0; 726 0.1; 777 0.1; 832 0.1; 890 0.1; 952 -0.0; 1019 0.0; 1090 0.5; 1167 1.4; 1248 0.9; 1336 1.1; 1429 1.2; 1529 1.3; 1636 0.9; 1751 -0.3; 1873 -1.1; 2004 -1.4; 2145 -1.3; 2295 -1.1; 2455 -0.9; 2627 -1.1; 2811 -2.0; 3008 -3.3; 3219 -5.0; 3444 -5.0; 3685 -4.2; 3943 -2.5; 4219 -0.1; 4514 2.2; 4830 5.2; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.3; 8299 -3.5; 8880 -4.4; 9502 -4.2; 10167 -2.2; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 55 Hz   | 1.12 | -6.5 dB  |
| Peaking | 325 Hz  | 2.37 | -3.4 dB  |
| Peaking | 3600 Hz | 1.59 | -12.1 dB |
| Peaking | 5353 Hz | 0.84 | 12.4 dB  |
| Peaking | 8647 Hz | 1.93 | -9.8 dB  |
| Peaking | 184 Hz  | 7.9  | 3.4 dB   |
| Peaking | 155 Hz  | 1.36 | -2.3 dB  |
| Peaking | 166 Hz  | 3.34 | 3.2 dB   |
| Peaking | 1525 Hz | 2.12 | 1.6 dB   |
| Peaking | 1920 Hz | 3.8  | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Ultrasone%20HFI-580/Ultrasone%20HFI-580.png)
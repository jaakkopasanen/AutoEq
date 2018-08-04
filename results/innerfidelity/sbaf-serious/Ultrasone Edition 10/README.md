# Ultrasone Edition 10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.4; 35 4.6; 37 4.2; 40 3.6; 42 3.3; 45 3.0; 49 2.7; 52 2.5; 56 2.1; 59 1.8; 64 1.4; 68 1.2; 73 0.9; 78 0.9; 83 0.9; 89 0.5; 95 0.1; 102 -0.2; 109 -0.5; 117 -0.7; 125 -0.9; 134 -1.0; 143 -1.1; 153 -1.0; 164 -0.9; 175 -0.7; 188 -0.6; 201 -0.4; 215 -0.1; 230 0.1; 246 0.3; 263 0.4; 282 0.7; 301 0.7; 323 1.0; 345 1.2; 369 1.3; 395 1.4; 423 1.6; 452 1.7; 484 1.6; 518 1.6; 554 1.6; 593 1.6; 635 1.6; 679 1.5; 726 1.4; 777 1.4; 832 1.0; 890 0.5; 952 0.2; 1019 -0.2; 1090 -0.4; 1167 -1.1; 1248 -1.3; 1336 -1.2; 1429 -0.7; 1529 -0.0; 1636 1.1; 1751 3.4; 1873 6.0; 2004 6.0; 2145 6.0; 2295 5.9; 2455 6.0; 2627 6.0; 2811 5.5; 3008 3.8; 3219 1.2; 3444 -0.8; 3685 -2.8; 3943 -4.1; 4219 -4.2; 4514 -1.9; 4830 1.9; 5168 1.7; 5530 -1.6; 5917 -6.9; 6331 -10.0; 6775 -5.3; 7249 0.5; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -2.0; 14260 -6.2; 15258 -8.4; 16326 -7.0; 17469 -3.1; 18692 -0.3; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 1.03 | 6.4 dB   |
| Peaking | 2400 Hz  | 1.89 | 7.2 dB   |
| Peaking | 3915 Hz  | 5.09 | -6.1 dB  |
| Peaking | 6298 Hz  | 8.3  | -11.1 dB |
| Peaking | 32509 Hz | 2.86 | -9.4 dB  |
| Peaking | 151 Hz   | 1.52 | -1.7 dB  |
| Peaking | 768 Hz   | 0.49 | 2.5 dB   |
| Peaking | 1337 Hz  | 1.16 | -4.4 dB  |
| Peaking | 1865 Hz  | 6.47 | 3.9 dB   |
| Peaking | 9643 Hz  | 1.09 | 0.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Edition%2010/Ultrasone%20Edition%2010.png)
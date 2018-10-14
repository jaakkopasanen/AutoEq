# Koss SportaPro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 4.9; 41 3.6; 45 2.5; 49 1.4; 54 0.3; 60 -0.7; 66 -1.3; 72 -2.2; 79 -2.8; 87 -3.1; 96 -3.6; 106 -3.8; 116 -4.0; 128 -4.2; 141 -4.2; 155 -3.7; 170 -3.4; 187 -3.2; 206 -3.3; 227 -3.2; 249 -2.8; 274 -2.5; 302 -2.2; 332 -1.8; 365 -1.4; 402 -1.2; 442 -0.9; 486 -0.6; 535 -0.4; 588 -0.2; 647 0.1; 712 0.2; 783 0.3; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.6; 1387 -1.3; 1526 -2.3; 1678 -3.0; 1846 -3.6; 2031 -4.4; 2234 -4.7; 2457 -4.0; 2703 -2.3; 2973 -1.1; 3270 -1.1; 3597 -2.8; 3957 -4.6; 4353 -0.8; 4788 -4.7; 5267 -0.9; 5793 1.2; 6373 5.4; 7010 2.5; 7711 0.3; 8482 -3.7; 9330 -8.8; 10263 -2.5; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SportaPro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.8  | 7.4 dB  |
| Peaking | 112 Hz   | 0.56 | -4.9 dB |
| Peaking | 2849 Hz  | 0.7  | -3.4 dB |
| Peaking | 6457 Hz  | 5.16 | 7.4 dB  |
| Peaking | 9310 Hz  | 6.5  | -9.7 dB |
| Peaking | 949 Hz   | 1.25 | 1.4 dB  |
| Peaking | 2167 Hz  | 1.93 | -2.6 dB |
| Peaking | 3174 Hz  | 2.55 | 5.7 dB  |
| Peaking | 3689 Hz  | 2.24 | -3.7 dB |
| Peaking | 11039 Hz | 6.57 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20SportaPro/Koss%20SportaPro.png)
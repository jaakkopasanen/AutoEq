# Woodees iESW100B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 21 -8.5; 23 -8.5; 25 -8.5; 28 -8.5; 31 -8.5; 34 -8.4; 37 -8.4; 41 -8.4; 45 -8.4; 49 -8.4; 54 -8.4; 60 -8.5; 66 -8.5; 72 -8.6; 79 -8.6; 87 -8.6; 96 -8.5; 106 -8.3; 116 -8.2; 128 -8.0; 141 -7.7; 155 -7.5; 170 -7.1; 187 -6.7; 206 -6.2; 227 -5.6; 249 -5.0; 274 -4.4; 302 -3.7; 332 -3.0; 365 -2.2; 402 -1.5; 442 -0.8; 486 -0.2; 535 0.3; 588 0.9; 647 1.3; 712 1.5; 783 1.4; 861 1.1; 947 0.4; 1042 -0.0; 1146 -1.0; 1261 -1.7; 1387 -1.1; 1526 -2.1; 1678 -2.9; 1846 -3.5; 2031 -4.0; 2234 -4.7; 2457 -5.6; 2703 -6.4; 2973 -4.6; 3270 -0.9; 3597 1.8; 3957 1.5; 4353 -0.7; 4788 -2.9; 5267 -4.8; 5793 -8.3; 6373 -6.6; 7010 -2.7; 7711 -1.6; 8482 -4.4; 9330 -7.1; 10263 -2.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.3; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.2dB` and instead set Global volume in the UI for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW100B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.16 | -9.1 dB |
| Peaking | 1217 Hz  | 0.26 | 4.4 dB  |
| Peaking | 2125 Hz  | 1.09 | -8.8 dB |
| Peaking | 6061 Hz  | 2.54 | -8.5 dB |
| Peaking | 21764 Hz | 1.86 | -3.4 dB |
| Peaking | 1194 Hz  | 6.52 | -1.8 dB |
| Peaking | 2798 Hz  | 6.29 | -3.8 dB |
| Peaking | 3699 Hz  | 4.56 | 4.2 dB  |
| Peaking | 7230 Hz  | 5.95 | 2.5 dB  |
| Peaking | 9239 Hz  | 5.57 | -7.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW100B/Woodees%20iESW100B.png)
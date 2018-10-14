# AKG K812 sn002100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 0.0; 23 -0.3; 25 -0.6; 28 -0.9; 31 -1.1; 34 -1.3; 37 -1.5; 41 -1.7; 45 -1.8; 49 -1.9; 54 -2.2; 60 -2.4; 66 -2.5; 72 -2.6; 79 -2.8; 87 -3.3; 96 -3.6; 106 -3.9; 116 -4.2; 128 -4.6; 141 -4.6; 155 -4.8; 170 -4.8; 187 -4.8; 206 -4.9; 227 -4.7; 249 -4.6; 274 -4.5; 302 -4.3; 332 -4.2; 365 -4.0; 402 -3.8; 442 -3.3; 486 -3.2; 535 -2.9; 588 -2.3; 647 -1.9; 712 -1.6; 783 -0.8; 861 -0.3; 947 -0.3; 1042 0.3; 1146 0.8; 1261 1.0; 1387 0.9; 1526 -0.1; 1678 0.6; 1846 1.5; 2031 0.9; 2234 0.9; 2457 2.5; 2703 3.8; 2973 -0.9; 3270 -1.9; 3597 -0.7; 3957 2.7; 4353 4.3; 4788 -0.9; 5267 -5.0; 5793 -8.3; 6373 -5.0; 7010 -0.2; 7711 -1.4; 8482 -2.9; 9330 -2.7; 10263 -0.4; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.6; 20000 -8.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.9dB` and instead set Global volume in the UI for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 sn002100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 186 Hz   | 0.42 | -5.0 dB |
| Peaking | 2818 Hz  | 2.03 | 6.4 dB  |
| Peaking | 3122 Hz  | 3.41 | -7.2 dB |
| Peaking | 4231 Hz  | 6.21 | 6.2 dB  |
| Peaking | 5776 Hz  | 3.93 | -9.2 dB |
| Peaking | 42 Hz    | 2.18 | -0.4 dB |
| Peaking | 1166 Hz  | 3.01 | 1.5 dB  |
| Peaking | 6999 Hz  | 5.7  | 3.9 dB  |
| Peaking | 9227 Hz  | 1.58 | -4.2 dB |
| Peaking | 10644 Hz | 2.33 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812%20sn002100/AKG%20K812%20sn002100.png)
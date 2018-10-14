# Ultrasone PRO 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.4; 37 4.7; 41 4.0; 45 3.7; 49 3.5; 54 3.3; 60 3.6; 66 3.0; 72 1.9; 79 1.2; 87 0.8; 96 0.9; 106 0.8; 116 0.7; 128 0.7; 141 0.9; 155 1.2; 170 1.7; 187 1.8; 206 2.2; 227 2.6; 249 3.0; 274 3.2; 302 2.8; 332 2.4; 365 1.4; 402 0.1; 442 -0.4; 486 1.3; 535 1.8; 588 1.7; 647 2.0; 712 1.6; 783 1.3; 861 0.5; 947 0.1; 1042 -0.2; 1146 -0.2; 1261 -0.3; 1387 -0.9; 1526 -1.6; 1678 -1.8; 1846 -0.2; 2031 2.7; 2234 4.6; 2457 5.0; 2703 0.1; 2973 1.1; 3270 0.0; 3597 -0.6; 3957 -0.8; 4353 1.1; 4788 5.5; 5267 3.0; 5793 2.3; 6373 0.8; 7010 1.9; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -4.9; 16529 -4.4; 18182 -0.5; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.67 | 6.2 dB  |
| Peaking | 267 Hz   | 1.37 | 2.9 dB  |
| Peaking | 4943 Hz  | 4.61 | 5.2 dB  |
| Peaking | 13579 Hz | 2.1  | 2.0 dB  |
| Peaking | 15554 Hz | 2.41 | -6.7 dB |
| Peaking | 429 Hz   | 5.2  | -2.3 dB |
| Peaking | 604 Hz   | 1.94 | 1.8 dB  |
| Peaking | 1584 Hz  | 3.69 | -2.4 dB |
| Peaking | 2313 Hz  | 5.78 | 6.2 dB  |
| Peaking | 3930 Hz  | 5.57 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20650/Ultrasone%20PRO%20650.png)
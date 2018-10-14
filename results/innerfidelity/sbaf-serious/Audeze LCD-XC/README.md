# Audeze LCD-XC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.6; 28 4.8; 31 4.9; 34 4.7; 37 4.3; 41 4.2; 45 4.1; 49 4.0; 54 3.6; 60 2.5; 66 1.7; 72 1.4; 79 1.2; 87 0.9; 96 0.7; 106 0.6; 116 0.5; 128 0.3; 141 0.2; 155 0.4; 170 0.1; 187 0.1; 206 0.3; 227 0.6; 249 0.9; 274 1.4; 302 1.6; 332 1.8; 365 2.1; 402 2.2; 442 2.2; 486 1.9; 535 1.9; 588 2.2; 647 2.2; 712 1.7; 783 1.4; 861 0.7; 947 0.2; 1042 -0.3; 1146 -1.0; 1261 -1.7; 1387 -2.8; 1526 -3.7; 1678 -4.2; 1846 -4.0; 2031 -2.8; 2234 -1.2; 2457 0.6; 2703 1.9; 2973 2.7; 3270 3.1; 3597 2.4; 3957 0.7; 4353 0.1; 4788 0.6; 5267 4.2; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.9; 15026 -1.5; 16529 -1.5; 18182 -3.6; 20000 -4.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.79 | 5.2 dB  |
| Peaking | 536 Hz   | 0.86 | 2.5 dB  |
| Peaking | 1693 Hz  | 1.62 | -5.1 dB |
| Peaking | 3001 Hz  | 2.63 | 4.0 dB  |
| Peaking | 5966 Hz  | 4.19 | 6.8 dB  |
| Peaking | 52 Hz    | 3.37 | 1.4 dB  |
| Peaking | 74 Hz    | 0.52 | -0.5 dB |
| Peaking | 4430 Hz  | 3.95 | -3.1 dB |
| Peaking | 4470 Hz  | 1.85 | 1.7 dB  |
| Peaking | 19444 Hz | 0.98 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-XC/Audeze%20LCD-XC.png)
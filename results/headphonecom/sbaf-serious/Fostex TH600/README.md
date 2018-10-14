# Fostex TH600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.5; 23 -2.0; 25 -2.5; 28 -3.0; 31 -3.4; 34 -3.7; 37 -3.9; 41 -4.1; 45 -4.1; 49 -4.2; 54 -4.6; 60 -5.0; 66 -4.6; 72 -4.4; 79 -5.1; 87 -5.4; 96 -5.5; 106 -5.5; 116 -5.4; 128 -5.3; 141 -5.2; 155 -5.0; 170 -4.5; 187 -4.3; 206 -3.8; 227 -3.3; 249 -2.7; 274 -2.0; 302 -1.0; 332 0.1; 365 1.2; 402 2.0; 442 2.5; 486 3.1; 535 3.3; 588 2.8; 647 2.1; 712 1.2; 783 0.7; 861 1.5; 947 0.2; 1042 0.0; 1146 0.2; 1261 0.2; 1387 0.1; 1526 -0.2; 1678 -0.2; 1846 0.2; 2031 0.5; 2234 1.7; 2457 4.5; 2703 6.0; 2973 6.0; 3270 5.9; 3597 5.3; 3957 3.0; 4353 -0.3; 4788 -2.1; 5267 -2.5; 5793 -3.2; 6373 -3.3; 7010 -3.0; 7711 -2.2; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.4; 18182 -3.6; 20000 -5.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 1.04 | -1.6 dB |
| Peaking | 122 Hz   | 0.38 | -5.5 dB |
| Peaking | 466 Hz   | 1.31 | 5.1 dB  |
| Peaking | 3150 Hz  | 2.07 | 7.7 dB  |
| Peaking | 5710 Hz  | 1.64 | -4.5 dB |
| Peaking | 1920 Hz  | 1.61 | -1.2 dB |
| Peaking | 2561 Hz  | 8.42 | 2.7 dB  |
| Peaking | 9112 Hz  | 5.21 | 1.1 dB  |
| Peaking | 15913 Hz | 1.13 | 2.4 dB  |
| Peaking | 19656 Hz | 0.91 | -6.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Fostex%20TH600/Fostex%20TH600.png)
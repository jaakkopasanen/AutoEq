# Fostex TH900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 -4.7; 23 -4.9; 25 -5.0; 28 -5.2; 31 -5.2; 34 -5.3; 37 -5.3; 41 -5.3; 45 -5.1; 49 -4.6; 54 -4.1; 60 -5.3; 66 -5.8; 72 -5.9; 79 -5.9; 87 -5.8; 96 -5.9; 106 -6.0; 116 -5.9; 128 -6.0; 141 -6.0; 155 -5.7; 170 -5.3; 187 -5.1; 206 -4.7; 227 -4.4; 249 -4.0; 274 -3.4; 302 -2.8; 332 -2.1; 365 -1.3; 402 -0.3; 442 0.9; 486 2.5; 535 4.5; 588 5.0; 647 3.2; 712 2.2; 783 2.2; 861 0.7; 947 0.2; 1042 0.0; 1146 0.0; 1261 0.2; 1387 0.4; 1526 -0.2; 1678 -0.8; 1846 -0.8; 2031 1.5; 2234 3.8; 2457 2.5; 2703 2.3; 2973 1.2; 3270 1.5; 3597 2.1; 3957 2.1; 4353 -0.0; 4788 -1.6; 5267 -2.0; 5793 -3.3; 6373 -2.2; 7010 -2.2; 7711 -1.9; 8482 -0.0; 9330 0.0; 10263 0.0; 11289 -1.8; 12418 -0.1; 13660 0.0; 15026 -0.5; 16529 -2.5; 18182 -2.7; 20000 -9.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.88 | -3.7 dB |
| Peaking | 121 Hz   | 0.38 | -5.9 dB |
| Peaking | 562 Hz   | 2.21 | 6.6 dB  |
| Peaking | 3471 Hz  | 1.08 | 3.5 dB  |
| Peaking | 5610 Hz  | 1.44 | -4.3 dB |
| Peaking | 1821 Hz  | 3.82 | -2.6 dB |
| Peaking | 2203 Hz  | 4.39 | 3.1 dB  |
| Peaking | 3042 Hz  | 7.77 | -1.4 dB |
| Peaking | 8953 Hz  | 5.84 | 1.1 dB  |
| Peaking | 20389 Hz | 1.47 | -9.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Fostex%20TH900/Fostex%20TH900.png)
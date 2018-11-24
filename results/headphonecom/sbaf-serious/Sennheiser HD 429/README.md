# Sennheiser HD 429

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.3; 23 -1.5; 25 -1.6; 28 -1.7; 31 -1.9; 34 -2.0; 37 -2.0; 41 -2.0; 45 -2.1; 49 -2.0; 54 -2.0; 60 -1.9; 66 -1.9; 72 -1.7; 79 -1.2; 87 -0.4; 96 1.2; 106 -0.0; 116 -1.5; 128 -2.1; 141 -2.4; 155 -1.8; 170 -2.1; 187 -2.2; 206 -2.2; 227 -2.1; 249 -1.6; 274 -0.5; 302 0.3; 332 0.7; 365 0.8; 402 0.4; 442 0.2; 486 -0.2; 535 -0.5; 588 -0.6; 647 -0.6; 712 -0.9; 783 -0.7; 861 -0.4; 947 -0.1; 1042 -0.2; 1146 -0.8; 1261 -0.8; 1387 -0.7; 1526 -1.3; 1678 -1.1; 1846 -0.1; 2031 0.9; 2234 2.6; 2457 4.0; 2703 4.0; 2973 4.7; 3270 5.2; 3597 5.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 429 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 429 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 1.12 | -2.0 dB |
| Peaking | 60 Hz   | 2.91 | -1.4 dB |
| Peaking | 179 Hz  | 1.71 | -2.4 dB |
| Peaking | 1523 Hz | 1.9  | -2.4 dB |
| Peaking | 4093 Hz | 0.94 | 6.6 dB  |
| Peaking | 10 Hz   | 1.57 | -0.7 dB |
| Peaking | 347 Hz  | 4.84 | 1.4 dB  |
| Peaking | 2450 Hz | 5.57 | 1.6 dB  |
| Peaking | 6207 Hz | 2.46 | 6.4 dB  |
| Peaking | 6780 Hz | 1.21 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20429/Sennheiser%20HD%20429.png)
# Sennheiser HD 439

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.1; 25 -0.1; 28 -0.4; 31 -0.7; 34 -0.9; 37 -1.0; 41 -1.2; 45 -1.3; 49 -1.5; 54 -1.6; 60 -1.7; 66 -1.7; 72 -1.6; 79 -1.2; 87 -2.0; 96 -1.2; 106 1.3; 116 -0.3; 128 -2.2; 141 -2.7; 155 -2.7; 170 -2.4; 187 -2.4; 206 -2.6; 227 -2.8; 249 -2.5; 274 -2.1; 302 -1.2; 332 -1.3; 365 0.4; 402 0.4; 442 0.6; 486 1.0; 535 1.0; 588 0.7; 647 0.3; 712 0.5; 783 0.2; 861 -0.2; 947 -0.7; 1042 0.2; 1146 0.1; 1261 0.4; 1387 -1.2; 1526 -1.6; 1678 -1.3; 1846 -0.4; 2031 1.1; 2234 3.0; 2457 4.7; 2703 5.3; 2973 5.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 439 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 1.46 | -1.6 dB |
| Peaking | 212 Hz  | 1.05 | -3.0 dB |
| Peaking | 449 Hz  | 1.83 | 1.6 dB  |
| Peaking | 1628 Hz | 2.5  | -3.8 dB |
| Peaking | 3732 Hz | 0.83 | 7.0 dB  |
| Peaking | 108 Hz  | 5.89 | 5.4 dB  |
| Peaking | 110 Hz  | 2.31 | -2.5 dB |
| Peaking | 3942 Hz | 5.01 | -1.0 dB |
| Peaking | 6384 Hz | 2.38 | 5.0 dB  |
| Peaking | 7418 Hz | 1.62 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)
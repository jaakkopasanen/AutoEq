# Sennheiser HD 558
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.7; 34 5.2; 37 4.7; 41 4.0; 45 3.5; 49 3.0; 54 2.4; 60 1.9; 66 1.5; 72 1.3; 79 0.8; 87 1.9; 96 0.7; 106 -0.6; 116 -1.0; 128 -1.3; 141 -1.7; 155 -2.1; 170 -2.2; 187 -2.3; 206 -2.1; 227 -2.2; 249 -2.3; 274 -2.3; 302 -2.2; 332 -1.9; 365 -1.7; 402 -1.6; 442 -1.4; 486 -1.3; 535 -1.0; 588 -0.4; 647 -0.4; 712 -0.5; 783 0.1; 861 0.1; 947 0.1; 1042 -0.2; 1146 -0.0; 1261 -0.2; 1387 -0.4; 1526 -0.4; 1678 -0.2; 1846 -1.0; 2031 -1.8; 2234 -1.9; 2457 -1.5; 2703 -2.8; 2973 -3.2; 3270 -3.7; 3597 -2.3; 3957 -1.3; 4353 -3.6; 4788 -3.2; 5267 -0.8; 5793 1.3; 6373 2.3; 7010 1.1; 7711 0.3; 8482 -0.2; 9330 -1.9; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.9; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 558 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 558 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.5  | 6.2 dB  |
| Peaking | 208 Hz   | 0.71 | -2.8 dB |
| Peaking | 3005 Hz  | 2    | -3.3 dB |
| Peaking | 4636 Hz  | 5.24 | -3.5 dB |
| Peaking | 6218 Hz  | 4.42 | 2.9 dB  |
| Peaking | 89 Hz    | 5.71 | 2.5 dB  |
| Peaking | 89 Hz    | 1.68 | -1.2 dB |
| Peaking | 884 Hz   | 3.04 | 0.6 dB  |
| Peaking | 2092 Hz  | 9.55 | -1.0 dB |
| Peaking | 19363 Hz | 2.36 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20558/Sennheiser%20HD%20558.png)
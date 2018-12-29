# Sennheiser HD 800 S sn01067
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 0.0; 23 4.0; 25 3.6; 28 3.2; 31 2.8; 34 2.5; 37 2.2; 41 1.9; 45 1.6; 49 1.5; 54 1.3; 60 1.1; 66 1.1; 72 0.9; 79 0.3; 87 -0.0; 96 -0.7; 106 -1.2; 116 -1.5; 128 -2.0; 141 -2.1; 155 -2.3; 170 -2.3; 187 -2.5; 206 -2.6; 227 -2.6; 249 -2.7; 274 -2.6; 302 -2.5; 332 -2.4; 365 -2.2; 402 -2.1; 442 -1.8; 486 -1.7; 535 -1.6; 588 -1.1; 647 -1.1; 712 -0.9; 783 -0.5; 861 -0.4; 947 -0.1; 1042 0.3; 1146 0.4; 1261 0.9; 1387 1.2; 1526 1.6; 1678 1.5; 1846 1.3; 2031 1.7; 2234 1.5; 2457 2.1; 2703 2.5; 2973 1.9; 3270 2.3; 3597 0.9; 3957 -0.3; 4353 -0.2; 4788 0.4; 5267 -0.4; 5793 -1.5; 6373 -3.9; 7010 -2.9; 7711 -1.2; 8482 -0.8; 9330 -0.4; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.8; 15026 -1.0; 16529 0.0; 18182 0.0; 20000 -0.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S sn01067 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S sn01067 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.19 | 4.3 dB  |
| Peaking | 221 Hz   | 0.47 | -2.9 dB |
| Peaking | 1535 Hz  | 1.54 | 1.5 dB  |
| Peaking | 2781 Hz  | 2.16 | 2.3 dB  |
| Peaking | 6589 Hz  | 4    | -4.2 dB |
| Peaking | 41 Hz    | 2.59 | -0.6 dB |
| Peaking | 8772 Hz  | 5.16 | -0.2 dB |
| Peaking | 14463 Hz | 5.88 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800%20S%20sn01067/Sennheiser%20HD%20800%20S%20sn01067.png)
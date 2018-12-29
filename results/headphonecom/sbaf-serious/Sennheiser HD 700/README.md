# Sennheiser HD 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 4.1; 25 3.5; 28 2.9; 31 2.3; 34 1.8; 37 1.4; 41 1.0; 45 0.6; 49 0.2; 54 -0.2; 60 -0.6; 66 -1.0; 72 -1.4; 79 -1.6; 87 -2.0; 96 -2.3; 106 -2.5; 116 -2.7; 128 -3.1; 141 -3.2; 155 -3.5; 170 -3.4; 187 -3.6; 206 -3.5; 227 -3.5; 249 -3.5; 274 -3.4; 302 -3.1; 332 -2.8; 365 -2.5; 402 -2.2; 442 -2.0; 486 -1.7; 535 -1.5; 588 -1.2; 647 -0.8; 712 -0.7; 783 -0.5; 861 -0.5; 947 0.0; 1042 0.0; 1146 0.8; 1261 0.9; 1387 1.3; 1526 1.6; 1678 2.4; 1846 3.1; 2031 3.8; 2234 3.2; 2457 4.7; 2703 5.1; 2973 3.6; 3270 4.3; 3597 4.4; 3957 3.0; 4353 -1.9; 4788 -2.7; 5267 -1.9; 5793 0.2; 6373 -5.4; 7010 -3.3; 7711 -0.5; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -3.9; 18182 -7.0; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.67 | 5.8 dB   |
| Peaking | 194 Hz   | 0.41 | -3.7 dB  |
| Peaking | 3613 Hz  | 0.81 | 10.7 dB  |
| Peaking | 4788 Hz  | 1.12 | -10.5 dB |
| Peaking | 19032 Hz | 1.57 | -8.4 dB  |
| Peaking | 3030 Hz  | 7.07 | -3.1 dB  |
| Peaking | 3051 Hz  | 2.98 | 1.7 dB   |
| Peaking | 5834 Hz  | 8.31 | 3.9 dB   |
| Peaking | 6564 Hz  | 8.22 | -6.2 dB  |
| Peaking | 11317 Hz | 1.05 | 0.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)
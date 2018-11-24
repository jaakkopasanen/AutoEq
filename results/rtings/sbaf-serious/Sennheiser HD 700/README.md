# Sennheiser HD 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.1; 28 4.4; 31 3.8; 34 3.3; 37 2.9; 41 2.5; 45 2.0; 49 1.6; 54 1.1; 60 0.6; 66 0.1; 72 -0.2; 79 -0.6; 87 -1.0; 96 -1.4; 106 -1.9; 116 -2.3; 128 -2.7; 141 -3.0; 155 -3.2; 170 -3.2; 187 -3.2; 206 -3.1; 227 -3.0; 249 -2.8; 274 -2.6; 302 -2.3; 332 -2.1; 365 -1.9; 402 -1.7; 442 -1.5; 486 -1.3; 535 -1.1; 588 -1.0; 647 -0.7; 712 -0.5; 783 -0.3; 861 -0.3; 947 -0.2; 1042 0.3; 1146 1.0; 1261 1.7; 1387 2.0; 1526 2.1; 1678 2.4; 1846 3.2; 2031 3.3; 2234 4.0; 2457 3.7; 2703 4.0; 2973 3.9; 3270 4.9; 3597 5.2; 3957 3.2; 4353 1.4; 4788 0.8; 5267 -0.9; 5793 -2.2; 6373 -6.6; 7010 -1.9; 7711 -0.5; 8482 -1.8; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.9; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.39 | 7.4 dB  |
| Peaking | 180 Hz   | 0.5  | -3.4 dB |
| Peaking | 2200 Hz  | 1.11 | 3.7 dB  |
| Peaking | 3511 Hz  | 3.54 | 3.9 dB  |
| Peaking | 6349 Hz  | 5.22 | -6.9 dB |
| Peaking | 1145 Hz  | 1.71 | -0.9 dB |
| Peaking | 1247 Hz  | 3.28 | 1.4 dB  |
| Peaking | 19728 Hz | 2.58 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)
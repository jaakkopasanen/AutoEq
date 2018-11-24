# Sennheiser HD 518

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 5.1; 25 4.5; 28 3.7; 31 2.9; 34 2.2; 37 1.7; 41 1.0; 45 0.5; 49 0.0; 54 -0.6; 60 -1.2; 66 -1.7; 72 -2.1; 79 -2.5; 87 -2.4; 96 -1.6; 106 -2.7; 116 -3.4; 128 -4.0; 141 -4.3; 155 -4.6; 170 -4.3; 187 -4.6; 206 -4.4; 227 -4.4; 249 -4.4; 274 -4.2; 302 -4.0; 332 -3.6; 365 -3.4; 402 -3.0; 442 -2.8; 486 -2.5; 535 -1.9; 588 -1.5; 647 -1.5; 712 -1.6; 783 -0.5; 861 -0.8; 947 -0.2; 1042 0.2; 1146 1.4; 1261 1.9; 1387 3.1; 1526 3.9; 1678 4.9; 1846 4.3; 2031 2.9; 2234 1.9; 2457 2.3; 2703 1.4; 2973 0.3; 3270 -0.3; 3597 1.3; 3957 1.3; 4353 -1.9; 4788 -1.9; 5267 -0.4; 5793 1.6; 6373 3.1; 7010 2.2; 7711 0.3; 8482 -0.9; 9330 -0.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.4; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 518 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 518 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.97 | 6.2 dB  |
| Peaking | 189 Hz   | 0.95 | -1.0 dB |
| Peaking | 203 Hz   | 0.36 | -3.7 dB |
| Peaking | 1667 Hz  | 1.78 | 5.2 dB  |
| Peaking | 19401 Hz | 2.31 | -3.9 dB |
| Peaking | 3881 Hz  | 6.74 | 3.4 dB  |
| Peaking | 4470 Hz  | 2.78 | -3.5 dB |
| Peaking | 6343 Hz  | 3.46 | 3.7 dB  |
| Peaking | 8653 Hz  | 6.79 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20518/Sennheiser%20HD%20518.png)
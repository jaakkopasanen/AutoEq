# Etymotic ER4XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.6; 87 4.9; 96 4.1; 106 3.2; 116 2.4; 128 1.6; 141 0.9; 155 0.3; 170 -0.1; 187 -0.5; 206 -0.8; 227 -1.0; 249 -1.0; 274 -1.0; 302 -0.9; 332 -0.9; 365 -0.8; 402 -0.7; 442 -0.6; 486 -0.4; 535 -0.2; 588 0.1; 647 0.5; 712 0.8; 783 0.9; 861 0.8; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -1.8; 1387 -2.5; 1526 -3.0; 1678 -3.5; 1846 -4.0; 2031 -4.3; 2234 -3.7; 2457 -2.8; 2703 -2.2; 2973 -2.2; 3270 -2.5; 3597 -3.2; 3957 -3.9; 4353 -4.4; 4788 -3.4; 5267 -1.3; 5793 1.2; 6373 2.7; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -2.5; 15026 -7.2; 16529 -1.2; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.59 | 7.0 dB  |
| Peaking | 1897 Hz  | 1.74 | -4.2 dB |
| Peaking | 4353 Hz  | 2.12 | -4.6 dB |
| Peaking | 6393 Hz  | 3.24 | 4.3 dB  |
| Peaking | 15148 Hz | 4.31 | -7.9 dB |
| Peaking | 18 Hz    | 1.13 | 2.7 dB  |
| Peaking | 42 Hz    | 1.04 | -2.0 dB |
| Peaking | 81 Hz    | 1.21 | 2.6 dB  |
| Peaking | 205 Hz   | 0.67 | -1.9 dB |
| Peaking | 776 Hz   | 2.49 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Etymotic%20ER4XR/Etymotic%20ER4XR.png)
# Sennheiser HD 598
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.2; 41 4.4; 45 3.7; 49 3.1; 54 2.4; 60 1.6; 66 0.9; 72 0.3; 79 -0.3; 87 -0.9; 96 -1.5; 106 -2.1; 116 -2.6; 128 -3.0; 141 -3.3; 155 -3.6; 170 -3.6; 187 -3.6; 206 -3.4; 227 -3.1; 249 -2.9; 274 -2.8; 302 -2.6; 332 -2.4; 365 -2.2; 402 -1.9; 442 -1.8; 486 -1.9; 535 -1.6; 588 -0.8; 647 -0.7; 712 -0.5; 783 -0.4; 861 -0.2; 947 -0.0; 1042 0.1; 1146 0.2; 1261 0.1; 1387 -0.1; 1526 0.0; 1678 0.1; 1846 -0.2; 2031 -0.8; 2234 -1.2; 2457 -1.0; 2703 -1.1; 2973 -1.2; 3270 -2.3; 3597 -2.8; 3957 -3.4; 4353 -4.6; 4788 -2.6; 5267 -1.0; 5793 -1.4; 6373 -0.2; 7010 1.5; 7711 0.3; 8482 -2.7; 9330 -3.6; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.0; 18182 -6.3; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.53 | 6.8 dB  |
| Peaking | 93 Hz    | 2.07 | 0.3 dB  |
| Peaking | 150 Hz   | 0.49 | -4.3 dB |
| Peaking | 4118 Hz  | 2.35 | -4.1 dB |
| Peaking | 19258 Hz | 1.85 | -9.3 dB |
| Peaking | 2290 Hz  | 6.19 | -0.7 dB |
| Peaking | 7084 Hz  | 6.19 | 2.4 dB  |
| Peaking | 8983 Hz  | 6.21 | -4.3 dB |
| Peaking | 14781 Hz | 1.68 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)
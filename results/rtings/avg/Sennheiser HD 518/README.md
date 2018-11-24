# Sennheiser HD 518

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.4; 37 4.7; 41 3.8; 45 3.1; 49 2.4; 54 1.8; 60 1.1; 66 0.3; 72 -0.2; 79 -0.8; 87 -1.3; 96 -1.8; 106 -2.5; 116 -3.0; 128 -3.4; 141 -3.6; 155 -3.7; 170 -3.8; 187 -3.7; 206 -3.5; 227 -3.2; 249 -3.0; 274 -2.9; 302 -2.8; 332 -2.6; 365 -2.4; 402 -2.4; 442 -2.2; 486 -2.1; 535 -1.9; 588 -1.6; 647 -1.2; 712 -0.5; 783 -0.5; 861 -0.4; 947 -0.2; 1042 0.3; 1146 0.8; 1261 1.4; 1387 2.2; 1526 3.3; 1678 3.9; 1846 3.5; 2031 3.0; 2234 2.6; 2457 2.4; 2703 2.5; 2973 1.6; 3270 -0.1; 3597 -0.7; 3957 -1.0; 4353 -2.3; 4788 -0.8; 5267 0.6; 5793 1.4; 6373 3.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.2; 18182 -3.9; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 518 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 518 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.51 | 7.4 dB  |
| Peaking | 137 Hz   | 0.31 | -4.5 dB |
| Peaking | 1825 Hz  | 1.29 | 4.0 dB  |
| Peaking | 4250 Hz  | 3.63 | -2.8 dB |
| Peaking | 6519 Hz  | 5.64 | 4.4 dB  |
| Peaking | 276 Hz   | 1.41 | 1.3 dB  |
| Peaking | 284 Hz   | 0.82 | -0.9 dB |
| Peaking | 2810 Hz  | 6.76 | 1.2 dB  |
| Peaking | 3339 Hz  | 7.5  | -1.0 dB |
| Peaking | 19281 Hz | 2.07 | -5.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20518/Sennheiser%20HD%20518.png)
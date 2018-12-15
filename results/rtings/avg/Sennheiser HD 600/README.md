# Sennheiser HD 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.7; 41 5.1; 45 4.5; 49 4.0; 54 3.5; 60 2.8; 66 2.2; 72 1.6; 79 1.0; 87 0.4; 96 -0.1; 106 -0.6; 116 -1.0; 128 -1.4; 141 -1.7; 155 -1.9; 170 -2.0; 187 -2.0; 206 -1.8; 227 -1.6; 249 -1.4; 274 -1.2; 302 -1.1; 332 -1.2; 365 -1.2; 402 -1.1; 442 -1.1; 486 -1.2; 535 -1.1; 588 -1.0; 647 -0.9; 712 -0.7; 783 -0.7; 861 -0.7; 947 -0.4; 1042 -0.3; 1146 -0.9; 1261 -1.4; 1387 -2.1; 1526 -2.6; 1678 -3.0; 1846 -3.4; 2031 -3.8; 2234 -2.8; 2457 -2.6; 2703 -2.5; 2973 -3.2; 3270 -3.9; 3597 -3.8; 3957 -2.9; 4353 -1.5; 4788 -1.5; 5267 -1.5; 5793 -0.7; 6373 -1.1; 7010 -1.2; 7711 -1.4; 8482 -1.8; 9330 -0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -1.1; 15026 -2.9; 16529 -2.3; 18182 -3.7; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.38 | 7.0 dB  |
| Peaking | 120 Hz   | 0.44 | -3.6 dB |
| Peaking | 1829 Hz  | 1.86 | -3.0 dB |
| Peaking | 3462 Hz  | 1.74 | -3.3 dB |
| Peaking | 20376 Hz | 0.95 | -9.0 dB |
| Peaking | 1007 Hz  | 9.77 | 0.7 dB  |
| Peaking | 8008 Hz  | 3.14 | -1.7 dB |
| Peaking | 12335 Hz | 0.98 | 1.4 dB  |
| Peaking | 14957 Hz | 3    | -2.3 dB |
| Peaking | 17725 Hz | 2.98 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)
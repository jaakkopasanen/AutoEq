# Superlux HD 681
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 0.0; 23 -0.2; 25 -0.7; 28 -1.5; 31 -2.1; 34 -2.5; 37 -2.8; 41 -3.0; 45 -3.1; 49 -3.1; 54 -3.0; 60 -2.9; 66 -2.9; 72 -2.8; 79 -2.8; 87 -2.9; 96 -2.9; 106 -3.0; 116 -2.9; 128 -2.7; 141 -2.5; 155 -2.2; 170 -1.7; 187 -1.1; 206 -0.2; 227 -0.6; 249 -0.9; 274 -0.8; 302 -0.7; 332 -0.6; 365 -0.5; 402 -0.5; 442 -0.6; 486 -0.8; 535 -0.3; 588 0.4; 647 0.0; 712 0.1; 783 0.0; 861 0.1; 947 0.0; 1042 -0.0; 1146 -0.0; 1261 -0.1; 1387 -0.2; 1526 -0.8; 1678 -2.0; 1846 -4.1; 2031 -5.3; 2234 -5.4; 2457 -4.3; 2703 -3.0; 2973 -2.9; 3270 -3.1; 3597 -0.8; 3957 2.3; 4353 -1.6; 4788 -6.4; 5267 -7.3; 5793 -4.9; 6373 -4.5; 7010 -4.7; 7711 -7.9; 8482 -10.1; 9330 -10.8; 10263 -10.6; 11289 -8.3; 12418 -5.4; 13660 -5.5; 15026 -5.8; 16529 -4.6; 18182 -5.3; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 68 Hz    | 0.48 | -3.2 dB  |
| Peaking | 2155 Hz  | 2.92 | -5.5 dB  |
| Peaking | 9340 Hz  | 1.04 | -10.1 dB |
| Peaking | 20895 Hz | 0.63 | -8.5 dB  |
| Peaking | 135 Hz   | 4.97 | -0.6 dB  |
| Peaking | 3288 Hz  | 4.83 | -2.2 dB  |
| Peaking | 4001 Hz  | 4.79 | 6.3 dB   |
| Peaking | 4961 Hz  | 4.13 | -5.7 dB  |
| Peaking | 6753 Hz  | 5.11 | 2.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20681/Superlux%20HD%20681.png)
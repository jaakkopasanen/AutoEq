# Grado SR225e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.2; 41 4.3; 45 3.6; 49 2.9; 54 2.3; 60 1.7; 66 1.1; 72 0.7; 79 0.4; 87 0.0; 96 -0.2; 106 -0.4; 116 -0.7; 128 -0.8; 141 -0.9; 155 -0.9; 170 -0.9; 187 -0.8; 206 -0.6; 227 -0.3; 249 -0.3; 274 -1.0; 302 -0.9; 332 -0.6; 365 -0.6; 402 -0.6; 442 -0.7; 486 -0.7; 535 -0.7; 588 -0.6; 647 -0.4; 712 -0.3; 783 -0.1; 861 -0.0; 947 0.0; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -1.0; 1526 -1.6; 1678 -2.6; 1846 -6.1; 2031 -9.1; 2234 -8.7; 2457 -7.0; 2703 -5.2; 2973 -4.1; 3270 -3.6; 3597 -1.8; 3957 -1.1; 4353 -6.4; 4788 -5.3; 5267 -4.6; 5793 -5.3; 6373 -2.9; 7010 -1.5; 7711 -3.7; 8482 -7.1; 9330 -9.8; 10263 -10.9; 11289 -10.4; 12418 -8.6; 13660 -4.9; 15026 -1.0; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.6  | 7.1 dB  |
| Peaking | 83 Hz    | 0.38 | -1.9 dB |
| Peaking | 2217 Hz  | 2.19 | -8.9 dB |
| Peaking | 10017 Hz | 1.31 | -9.2 dB |
| Peaking | 11865 Hz | 3.1  | -3.6 dB |
| Peaking | 1774 Hz  | 1.08 | 1.6 dB  |
| Peaking | 1959 Hz  | 6.52 | -3.1 dB |
| Peaking | 4851 Hz  | 2.75 | -4.0 dB |
| Peaking | 7149 Hz  | 5.93 | 3.7 dB  |
| Peaking | 16114 Hz | 3.06 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR225e/Grado%20SR225e.png)
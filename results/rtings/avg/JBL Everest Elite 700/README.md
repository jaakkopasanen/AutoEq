# JBL Everest Elite 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.9; 23 -1.0; 25 -1.1; 28 -1.2; 31 -1.2; 34 -1.1; 37 -1.0; 41 -0.8; 45 -0.7; 49 -0.6; 54 -0.5; 60 -0.4; 66 -0.3; 72 -0.1; 79 -0.0; 87 -0.0; 96 0.1; 106 0.0; 116 0.0; 128 0.0; 141 0.0; 155 -0.0; 170 -0.1; 187 -0.1; 206 -0.2; 227 -0.2; 249 -0.2; 274 -0.1; 302 0.0; 332 0.2; 365 0.5; 402 0.3; 442 -0.1; 486 -0.4; 535 -0.6; 588 -0.6; 647 -0.3; 712 0.1; 783 0.3; 861 0.2; 947 0.0; 1042 0.1; 1146 0.3; 1261 -1.1; 1387 -2.6; 1526 -2.3; 1678 -1.9; 1846 -2.6; 2031 -2.9; 2234 -2.9; 2457 -2.5; 2703 -2.2; 2973 -2.2; 3270 -2.0; 3597 -1.0; 3957 -0.4; 4353 1.0; 4788 4.9; 5267 5.9; 5793 0.9; 6373 -0.9; 7010 0.2; 7711 0.3; 8482 -2.3; 9330 -5.6; 10263 -7.7; 11289 -9.6; 12418 -8.6; 13660 -3.3; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.82 | -1.2 dB  |
| Peaking | 91 Hz    | 1.82 | 0.3 dB   |
| Peaking | 2244 Hz  | 1.11 | -3.0 dB  |
| Peaking | 5068 Hz  | 4.89 | 7.6 dB   |
| Peaking | 11323 Hz | 2.36 | -10.6 dB |
| Peaking | 1208 Hz  | 2.03 | 1.6 dB   |
| Peaking | 1381 Hz  | 4.73 | -2.6 dB  |
| Peaking | 7761 Hz  | 4.17 | 4.7 dB   |
| Peaking | 8128 Hz  | 1.73 | -2.6 dB  |
| Peaking | 14916 Hz | 3.96 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Everest%20Elite%20700/JBL%20Everest%20Elite%20700.png)
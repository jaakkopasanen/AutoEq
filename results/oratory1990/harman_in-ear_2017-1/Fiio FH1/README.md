# Fiio FH1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.2; 23 -7.9; 25 -8.1; 28 -7.9; 31 -7.7; 34 -7.7; 37 -7.7; 41 -7.7; 45 -7.7; 49 -7.6; 54 -7.9; 60 -8.0; 66 -8.3; 72 -8.3; 79 -8.4; 87 -8.5; 96 -8.0; 106 -8.3; 116 -7.9; 128 -7.9; 141 -7.6; 155 -7.3; 170 -7.1; 187 -6.9; 206 -6.5; 227 -6.0; 249 -5.7; 274 -5.2; 302 -4.6; 332 -4.1; 365 -3.5; 402 -2.9; 442 -2.5; 486 -1.9; 535 -1.4; 588 -0.9; 647 -0.5; 712 0.0; 783 0.4; 861 0.6; 947 0.4; 1042 -0.4; 1146 -1.4; 1261 -2.2; 1387 -2.7; 1526 -3.0; 1678 -3.0; 1846 -3.0; 2031 -2.4; 2234 -1.1; 2457 0.8; 2703 2.4; 2973 3.4; 3270 3.7; 3597 4.4; 3957 6.0; 4353 5.9; 4788 3.1; 5267 5.1; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.1; 8482 -4.1; 9330 -3.8; 10263 -1.2; 11289 0.0; 12418 -0.1; 13660 -5.2; 15026 -13.4; 16529 -18.2; 18182 -18.2; 20000 -16.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.23 | -8.7 dB  |
| Peaking | 5093 Hz  | 0.68 | 12.8 dB  |
| Peaking | 8828 Hz  | 3.45 | -6.6 dB  |
| Peaking | 12445 Hz | 0.61 | 23.3 dB  |
| Peaking | 16172 Hz | 0.28 | -33.7 dB |
| Peaking | 845 Hz   | 0.74 | 8.3 dB   |
| Peaking | 1430 Hz  | 0.31 | -7.2 dB  |
| Peaking | 2747 Hz  | 2.35 | 4.1 dB   |
| Peaking | 4626 Hz  | 1.24 | 6.2 dB   |
| Peaking | 4862 Hz  | 5    | -6.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Fiio%20FH1/Fiio%20FH1.png)
# Fiio FH3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.0; 23 -3.7; 25 -4.1; 28 -4.1; 31 -4.2; 34 -4.4; 37 -4.5; 41 -4.7; 45 -4.7; 49 -4.9; 54 -5.3; 60 -5.5; 66 -5.9; 72 -5.9; 79 -6.4; 87 -6.3; 96 -6.1; 106 -6.4; 116 -6.2; 128 -6.4; 141 -6.1; 155 -6.0; 170 -5.8; 187 -5.7; 206 -5.5; 227 -5.2; 249 -4.8; 274 -4.4; 302 -4.0; 332 -3.4; 365 -2.9; 402 -2.5; 442 -2.1; 486 -1.6; 535 -1.2; 588 -0.8; 647 -0.5; 712 -0.2; 783 0.1; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.1; 1387 -1.2; 1526 -0.9; 1678 -0.2; 1846 0.7; 2031 2.1; 2234 3.8; 2457 5.4; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.8; 5793 3.9; 6373 0.6; 7010 -0.8; 7711 -2.5; 8482 -3.1; 9330 -0.2; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -9.2; 15026 -18.0; 16529 -19.0; 18182 -17.2; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.35 | -3.6 dB  |
| Peaking | 161 Hz   | 0.48 | -4.6 dB  |
| Peaking | 3883 Hz  | 0.95 | 7.5 dB   |
| Peaking | 17224 Hz | 1.14 | -21.2 dB |
| Peaking | 1504 Hz  | 2.7  | -2.4 dB  |
| Peaking | 2527 Hz  | 5    | 2.3 dB   |
| Peaking | 7900 Hz  | 3.32 | -4.4 dB  |
| Peaking | 12497 Hz | 1.55 | 9.1 dB   |
| Peaking | 14649 Hz | 2.75 | -11.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Fiio%20FH3/Fiio%20FH3.png)
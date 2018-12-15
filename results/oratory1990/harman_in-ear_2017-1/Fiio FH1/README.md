# Fiio FH1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.6; 28 1.8; 31 1.9; 34 1.8; 37 1.7; 41 1.5; 45 1.2; 49 0.9; 54 0.2; 60 -0.4; 66 -1.2; 72 -1.7; 79 -2.4; 87 -3.0; 96 -3.1; 106 -4.0; 116 -4.2; 128 -4.8; 141 -5.0; 155 -5.3; 170 -5.6; 187 -5.9; 206 -5.9; 227 -5.8; 249 -5.6; 274 -5.2; 302 -4.6; 332 -4.1; 365 -3.5; 402 -2.9; 442 -2.5; 486 -1.9; 535 -1.4; 588 -0.9; 647 -0.5; 712 0.0; 783 0.4; 861 0.6; 947 0.4; 1042 -0.4; 1146 -1.4; 1261 -2.2; 1387 -2.7; 1526 -3.0; 1678 -3.0; 1846 -3.0; 2031 -2.4; 2234 -1.1; 2457 0.8; 2703 2.4; 2973 3.4; 3270 3.7; 3597 4.4; 3957 6.0; 4353 5.9; 4788 3.1; 5267 5.1; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.1; 8482 -4.1; 9330 -3.8; 10263 -1.2; 11289 0.0; 12418 -0.1; 13660 -5.2; 15026 -13.4; 16529 -18.2; 18182 -18.2; 20000 -16.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 189 Hz   | 0.8  | -6.2 dB  |
| Peaking | 5055 Hz  | 0.66 | 13.1 dB  |
| Peaking | 8826 Hz  | 3.5  | -6.5 dB  |
| Peaking | 12468 Hz | 0.59 | 24.1 dB  |
| Peaking | 16129 Hz | 0.26 | -34.6 dB |
| Peaking | 30 Hz    | 1.28 | 2.5 dB   |
| Peaking | 870 Hz   | 2.01 | 2.9 dB   |
| Peaking | 1941 Hz  | 1.04 | -5.6 dB  |
| Peaking | 2649 Hz  | 0.94 | 4.6 dB   |
| Peaking | 4840 Hz  | 8.3  | -4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Fiio%20FH1/Fiio%20FH1.png)
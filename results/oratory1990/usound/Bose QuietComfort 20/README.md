# Bose QuietComfort 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 21 -0.6; 23 -1.8; 25 -2.7; 28 -3.6; 31 -4.1; 34 -4.3; 37 -4.3; 41 -4.2; 45 -4.1; 49 -4.0; 54 -3.9; 60 -3.9; 66 -4.0; 72 -4.2; 79 -4.6; 87 -5.0; 96 -5.4; 106 -5.6; 116 -5.7; 128 -5.5; 141 -5.2; 155 -4.9; 170 -4.7; 187 -4.7; 206 -4.7; 227 -4.7; 249 -4.7; 274 -4.7; 302 -4.7; 332 -4.7; 365 -4.7; 402 -4.8; 442 -4.9; 486 -4.7; 535 -3.9; 588 -2.6; 647 -1.5; 712 -0.9; 783 -0.1; 861 0.7; 947 0.5; 1042 -0.5; 1146 -1.6; 1261 -2.7; 1387 -3.5; 1526 -6.1; 1678 -8.2; 1846 -8.2; 2031 -6.9; 2234 -5.8; 2457 -5.5; 2703 -5.1; 2973 -4.9; 3270 -4.8; 3597 -5.3; 3957 -6.4; 4353 -6.0; 4788 -3.3; 5267 0.5; 5793 2.6; 6373 1.7; 7010 -4.7; 7711 -8.0; 8482 -3.9; 9330 -0.5; 10263 -0.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-28**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 99 Hz    | 0.33 | -5.3 dB  |
| Peaking | 411 Hz   | 1.96 | -3.1 dB  |
| Peaking | 1801 Hz  | 2.58 | -7.8 dB  |
| Peaking | 3600 Hz  | 1.45 | -5.4 dB  |
| Peaking | 21436 Hz | 2.19 | -4.7 dB  |
| Peaking | 35 Hz    | 3.44 | -1.5 dB  |
| Peaking | 886 Hz   | 4.07 | 2.5 dB   |
| Peaking | 4402 Hz  | 4.71 | -3.4 dB  |
| Peaking | 5998 Hz  | 2.33 | 6.7 dB   |
| Peaking | 7519 Hz  | 4.14 | -10.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)
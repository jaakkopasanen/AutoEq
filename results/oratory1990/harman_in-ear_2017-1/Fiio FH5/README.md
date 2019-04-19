# Fiio FH5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.7; 25 -12.5; 28 -12.3; 31 -12.2; 34 -12.0; 37 -11.8; 41 -11.6; 45 -11.4; 49 -11.2; 54 -11.1; 60 -11.0; 66 -10.9; 72 -10.9; 79 -10.9; 87 -10.9; 96 -10.9; 106 -10.8; 116 -10.8; 128 -10.7; 141 -10.6; 155 -10.4; 170 -10.2; 187 -10.0; 206 -9.7; 227 -9.4; 249 -9.2; 274 -8.9; 302 -8.7; 332 -8.3; 365 -8.1; 402 -8.0; 442 -7.9; 486 -7.7; 535 -7.6; 588 -7.5; 647 -7.5; 712 -7.4; 783 -7.4; 861 -7.5; 947 -7.8; 1042 -8.4; 1146 -8.8; 1261 -8.8; 1387 -8.2; 1526 -7.5; 1678 -7.0; 1846 -6.7; 2031 -6.3; 2234 -5.4; 2457 -3.9; 2703 -2.3; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.7; 5793 -2.5; 6373 -4.3; 7010 -6.7; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.3; 15026 -23.3; 16529 -28.2; 18182 -28.1; 20000 -19.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.52 | -5.6 dB  |
| Peaking | 125 Hz   | 0.4  | -3.7 dB  |
| Peaking | 1438 Hz  | 0.84 | -7.0 dB  |
| Peaking | 8369 Hz  | 0.18 | 14.7 dB  |
| Peaking | 17142 Hz | 0.42 | -33.8 dB |
| Peaking | 2223 Hz  | 3.08 | -2.4 dB  |
| Peaking | 3067 Hz  | 0.9  | 1.7 dB   |
| Peaking | 7268 Hz  | 2.76 | -3.9 dB  |
| Peaking | 12487 Hz | 2.42 | 6.6 dB   |
| Peaking | 14925 Hz | 2.76 | -5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -25.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Fiio%20FH5/Fiio%20FH5.png)
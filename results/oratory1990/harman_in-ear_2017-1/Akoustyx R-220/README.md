# Akoustyx R-220
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.7; 41 -0.8; 45 -1.0; 49 -1.2; 54 -1.4; 60 -1.7; 66 -2.1; 72 -2.4; 79 -2.8; 87 -3.2; 96 -3.7; 106 -4.2; 116 -4.6; 128 -4.9; 141 -5.1; 155 -5.7; 170 -6.0; 187 -6.2; 206 -6.9; 227 -7.6; 249 -7.7; 274 -7.5; 302 -7.3; 332 -7.2; 365 -7.1; 402 -7.1; 442 -7.0; 486 -6.9; 535 -6.7; 588 -6.6; 647 -6.6; 712 -6.5; 783 -6.3; 861 -6.3; 947 -6.7; 1042 -7.3; 1146 -8.0; 1261 -8.3; 1387 -8.2; 1526 -7.8; 1678 -7.4; 1846 -7.0; 2031 -6.4; 2234 -6.1; 2457 -6.1; 2703 -6.4; 2973 -6.4; 3270 -5.8; 3597 -5.0; 3957 -4.2; 4353 -3.6; 4788 -3.4; 5267 -3.4; 5793 -3.9; 6373 -5.0; 7010 -6.5; 7711 -8.2; 8482 -10.3; 9330 -11.5; 10263 -9.8; 11289 -7.1; 12418 -9.0; 13660 -15.5; 15026 -20.5; 16529 -23.0; 18182 -24.3; 20000 -23.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Akoustyx R-220 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Akoustyx R-220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.51 | 6.4 dB   |
| Peaking | 1320 Hz  | 2.5  | -2.0 dB  |
| Peaking | 4939 Hz  | 1.92 | 4.2 dB   |
| Peaking | 16096 Hz | 1.62 | -8.3 dB  |
| Peaking | 19205 Hz | 0.59 | -17.5 dB |
| Peaking | 262 Hz   | 1.91 | -1.6 dB  |
| Peaking | 6324 Hz  | 4.2  | 1.1 dB   |
| Peaking | 9358 Hz  | 2.53 | -4.4 dB  |
| Peaking | 11734 Hz | 2.45 | 5.6 dB   |
| Peaking | 14282 Hz | 3.68 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.6 dB   |
| Peaking | 125 Hz   | 1.41 | 1.2 dB   |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -21.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Akoustyx%20R-220/Akoustyx%20R-220.png)
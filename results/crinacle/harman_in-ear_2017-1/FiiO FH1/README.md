# FiiO FH1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.1; 25 -11.2; 28 -11.2; 31 -11.3; 34 -11.3; 37 -11.4; 41 -11.4; 45 -11.5; 49 -11.5; 54 -11.6; 60 -11.7; 66 -11.8; 72 -12.0; 79 -12.1; 87 -12.2; 96 -12.4; 106 -12.5; 116 -12.6; 128 -12.5; 141 -12.5; 155 -12.4; 170 -12.2; 187 -11.9; 206 -11.5; 227 -11.1; 249 -10.7; 274 -10.3; 302 -9.7; 332 -9.1; 365 -8.5; 402 -8.1; 442 -7.6; 486 -7.0; 535 -6.5; 588 -6.0; 647 -5.6; 712 -5.1; 783 -4.7; 861 -4.6; 947 -4.9; 1042 -5.7; 1146 -6.7; 1261 -7.6; 1387 -8.1; 1526 -8.3; 1678 -8.4; 1846 -8.3; 2031 -7.7; 2234 -6.3; 2457 -4.3; 2703 -2.7; 2973 -1.8; 3270 -1.4; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -2.0; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.2; 9330 -8.6; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -10.4; 15026 -18.6; 16529 -23.4; 18182 -23.4; 20000 -21.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO FH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO FH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.28 | -4.8 dB  |
| Peaking | 165 Hz   | 0.83 | -3.9 dB  |
| Peaking | 5142 Hz  | 0.88 | 11.5 dB  |
| Peaking | 12511 Hz | 1.33 | 14.4 dB  |
| Peaking | 16903 Hz | 0.28 | -20.7 dB |
| Peaking | 888 Hz   | 0.94 | 7.3 dB   |
| Peaking | 1569 Hz  | 0.44 | -7.5 dB  |
| Peaking | 2980 Hz  | 1.24 | 6.5 dB   |
| Peaking | 4817 Hz  | 8.45 | -2.2 dB  |
| Peaking | 6356 Hz  | 5.37 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 16000 Hz | 1.41 | -18.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FiiO%20FH1/FiiO%20FH1.png)
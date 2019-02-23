# Fiio FH1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -13.0; 25 -13.2; 28 -13.0; 31 -12.8; 34 -12.8; 37 -12.8; 41 -12.8; 45 -12.8; 49 -12.7; 54 -13.0; 60 -13.1; 66 -13.4; 72 -13.4; 79 -13.5; 87 -13.6; 96 -13.1; 106 -13.4; 116 -13.0; 128 -13.0; 141 -12.7; 155 -12.4; 170 -12.3; 187 -12.0; 206 -11.6; 227 -11.2; 249 -10.8; 274 -10.3; 302 -9.7; 332 -9.2; 365 -8.6; 402 -8.0; 442 -7.6; 486 -7.0; 535 -6.5; 588 -6.0; 647 -5.6; 712 -5.1; 783 -4.7; 861 -4.5; 947 -4.7; 1042 -5.5; 1146 -6.5; 1261 -7.3; 1387 -7.8; 1526 -8.1; 1678 -8.1; 1846 -8.1; 2031 -7.5; 2234 -6.2; 2457 -4.3; 2703 -2.7; 2973 -1.8; 3270 -1.4; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -2.0; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.2; 9330 -8.9; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -10.4; 15026 -18.6; 16529 -23.3; 18182 -23.3; 20000 -22.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.27 | -7.3 dB  |
| Peaking | 4915 Hz  | 0.65 | 12.4 dB  |
| Peaking | 8726 Hz  | 3.67 | -4.7 dB  |
| Peaking | 12707 Hz | 0.62 | 21.3 dB  |
| Peaking | 16074 Hz | 0.26 | -30.1 dB |
| Peaking | 23 Hz    | 2.88 | -1.1 dB  |
| Peaking | 832 Hz   | 1.53 | 3.4 dB   |
| Peaking | 1982 Hz  | 1.05 | -5.3 dB  |
| Peaking | 2687 Hz  | 1.25 | 4.6 dB   |
| Peaking | 4776 Hz  | 8.47 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.2 dB  |
| Peaking | 62 Hz    | 1.41 | -5.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -18.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Fiio%20FH1/Fiio%20FH1.png)
# Stax SR-404
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.1; 49 -2.7; 54 -4.6; 60 -7.2; 66 -9.7; 72 -11.0; 79 -11.1; 87 -10.2; 96 -9.1; 106 -8.3; 116 -7.8; 128 -7.4; 141 -7.1; 155 -6.8; 170 -6.7; 187 -6.6; 206 -6.5; 227 -6.4; 249 -6.1; 274 -6.2; 302 -6.2; 332 -5.9; 365 -5.8; 402 -5.8; 442 -5.8; 486 -5.8; 535 -5.8; 588 -5.9; 647 -6.1; 712 -6.3; 783 -6.7; 861 -7.3; 947 -7.9; 1042 -8.6; 1146 -9.3; 1261 -10.2; 1387 -11.0; 1526 -11.2; 1678 -10.3; 1846 -10.2; 2031 -9.4; 2234 -7.8; 2457 -6.8; 2703 -6.3; 2973 -6.7; 3270 -7.0; 3597 -6.0; 3957 -4.8; 4353 -2.9; 4788 -2.8; 5267 -5.0; 5793 -8.5; 6373 -6.9; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.1; 11289 -10.1; 12418 -7.5; 13660 -6.8; 15026 -9.6; 16529 -13.0; 18182 -16.9; 20000 -22.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-404 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-404 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.4  | 16.6 dB  |
| Peaking | 72 Hz    | 0.77 | -19.1 dB |
| Peaking | 1495 Hz  | 1.79 | -5.0 dB  |
| Peaking | 4534 Hz  | 4.16 | 4.6 dB   |
| Peaking | 19637 Hz | 0.73 | -15.2 dB |
| Peaking | 6012 Hz  | 5.58 | -5.3 dB  |
| Peaking | 6524 Hz  | 2.56 | 3.4 dB   |
| Peaking | 11139 Hz | 5.39 | -3.6 dB  |
| Peaking | 13453 Hz | 2.34 | 2.7 dB   |
| Peaking | 16934 Hz | 1.81 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 9.4 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -7.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Stax%20SR-404/Stax%20SR-404.png)
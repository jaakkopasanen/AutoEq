# Massdrop x Fostex T-X0
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.4; 34 -2.1; 37 -2.7; 41 -3.2; 45 -3.6; 49 -4.1; 54 -4.8; 60 -5.3; 66 -5.6; 72 -5.7; 79 -6.3; 87 -7.1; 96 -7.8; 106 -8.7; 116 -9.4; 128 -10.0; 141 -10.6; 155 -11.1; 170 -11.5; 187 -11.8; 206 -11.9; 227 -11.9; 249 -11.9; 274 -11.8; 302 -11.0; 332 -9.1; 365 -8.1; 402 -7.3; 442 -6.5; 486 -5.6; 535 -4.8; 588 -2.7; 647 -2.1; 712 -2.8; 783 -5.8; 861 -6.9; 947 -7.3; 1042 -8.0; 1146 -7.3; 1261 -5.9; 1387 -5.1; 1526 -4.2; 1678 -2.9; 1846 -2.1; 2031 -1.4; 2234 -1.8; 2457 -3.3; 2703 -4.1; 2973 -4.3; 3270 -4.8; 3597 -5.1; 3957 -3.8; 4353 -3.5; 4788 -5.1; 5267 -6.3; 5793 -7.3; 6373 -4.5; 7010 -4.8; 7711 -8.3; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.0; 20000 -11.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex T-X0 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex T-X0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.56 | 6.2 dB  |
| Peaking | 202 Hz  | 0.81 | -6.1 dB |
| Peaking | 615 Hz  | 3.19 | 5.6 dB  |
| Peaking | 2049 Hz | 2.26 | 5.4 dB  |
| Peaking | 4179 Hz | 4.29 | 2.9 dB  |
| Peaking | 288 Hz  | 3.94 | -2.1 dB |
| Peaking | 348 Hz  | 1.55 | 1.4 dB  |
| Peaking | 1032 Hz | 4.29 | -2.2 dB |
| Peaking | 6730 Hz | 9.54 | 3.1 dB  |
| Peaking | 7959 Hz | 6.89 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Fostex%20T-X0/Massdrop%20x%20Fostex%20T-X0.png)
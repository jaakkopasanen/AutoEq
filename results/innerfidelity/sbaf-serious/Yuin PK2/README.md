# Yuin PK2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.6; 170 -0.8; 187 -1.2; 206 -1.3; 227 -1.4; 249 -1.7; 274 -1.5; 302 -1.6; 332 -1.6; 365 -1.9; 402 -2.5; 442 -3.7; 486 -2.9; 535 -4.1; 588 -4.0; 647 -4.3; 712 -4.8; 783 -5.1; 861 -5.7; 947 -6.4; 1042 -6.8; 1146 -7.3; 1261 -8.3; 1387 -9.5; 1526 -10.9; 1678 -12.5; 1846 -13.3; 2031 -13.5; 2234 -14.8; 2457 -14.4; 2703 -12.4; 2973 -10.1; 3270 -7.6; 3597 -7.0; 3957 -7.5; 4353 -10.0; 4788 -10.6; 5267 -10.8; 5793 -12.2; 6373 -15.2; 7010 -14.1; 7711 -12.8; 8482 -12.1; 9330 -12.7; 10263 -12.5; 11289 -8.8; 12418 -6.5; 13660 -8.5; 15026 -12.6; 16529 -11.1; 18182 -7.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.12 | 5.9 dB  |
| Peaking | 237 Hz   | 0.39 | 4.2 dB  |
| Peaking | 2045 Hz  | 1.65 | -8.4 dB |
| Peaking | 7261 Hz  | 1.32 | -7.6 dB |
| Peaking | 15708 Hz | 2.4  | -6.3 dB |
| Peaking | 2561 Hz  | 5.78 | -2.1 dB |
| Peaking | 3534 Hz  | 3.63 | 3.4 dB  |
| Peaking | 8124 Hz  | 2.83 | 5.2 dB  |
| Peaking | 9989 Hz  | 0.98 | -5.7 dB |
| Peaking | 12183 Hz | 2.51 | 6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.7 dB  |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.6 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yuin%20PK2/Yuin%20PK2.png)
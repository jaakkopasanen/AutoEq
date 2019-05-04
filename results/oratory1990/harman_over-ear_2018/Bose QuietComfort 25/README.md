# Bose QuietComfort 25
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.8; 25 -5.7; 28 -6.8; 31 -7.6; 34 -8.1; 37 -8.4; 41 -8.5; 45 -8.5; 49 -8.3; 54 -8.1; 60 -7.9; 66 -7.8; 72 -7.8; 79 -7.8; 87 -8.0; 96 -8.1; 106 -8.2; 116 -8.4; 128 -8.5; 141 -8.6; 155 -8.6; 170 -8.5; 187 -8.4; 206 -8.3; 227 -8.0; 249 -7.7; 274 -7.4; 302 -7.0; 332 -6.5; 365 -6.1; 402 -5.9; 442 -5.7; 486 -5.7; 535 -5.6; 588 -5.5; 647 -5.5; 712 -6.0; 783 -6.5; 861 -6.9; 947 -6.8; 1042 -6.9; 1146 -7.8; 1261 -8.9; 1387 -8.8; 1526 -8.0; 1678 -7.8; 1846 -7.8; 2031 -8.0; 2234 -7.9; 2457 -7.8; 2703 -6.7; 2973 -2.1; 3270 -0.5; 3597 -5.1; 3957 -8.6; 4353 -7.0; 4788 -4.4; 5267 -4.3; 5793 -8.5; 6373 -10.0; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -10.7; 13660 -11.0; 15026 -7.6; 16529 -6.8; 18182 -8.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 2.61 | 4.1 dB  |
| Peaking | 70 Hz    | 0.36 | -2.0 dB |
| Peaking | 2035 Hz  | 0.99 | -2.0 dB |
| Peaking | 3176 Hz  | 6.05 | 8.1 dB  |
| Peaking | 13236 Hz | 3.66 | -5.7 dB |
| Peaking | 540 Hz   | 1.71 | 1.5 dB  |
| Peaking | 1297 Hz  | 6.01 | -1.8 dB |
| Peaking | 4037 Hz  | 5.5  | -4.3 dB |
| Peaking | 5523 Hz  | 1.65 | 4.6 dB  |
| Peaking | 6074 Hz  | 6.14 | -8.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)
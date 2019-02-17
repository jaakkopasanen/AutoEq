# Bose QuietComfort 25
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.6; 25 -5.5; 28 -6.6; 31 -7.4; 34 -7.9; 37 -8.2; 41 -8.3; 45 -8.3; 49 -8.2; 54 -8.1; 60 -7.9; 66 -7.8; 72 -7.8; 79 -7.8; 87 -7.9; 96 -8.0; 106 -8.2; 116 -8.3; 128 -8.5; 141 -8.6; 155 -8.6; 170 -8.5; 187 -8.4; 206 -8.3; 227 -7.9; 249 -7.7; 274 -7.3; 302 -6.9; 332 -6.5; 365 -6.1; 402 -5.8; 442 -5.7; 486 -5.6; 535 -5.6; 588 -5.5; 647 -5.4; 712 -6.0; 783 -6.4; 861 -6.8; 947 -6.6; 1042 -6.7; 1146 -7.6; 1261 -8.7; 1387 -8.6; 1526 -8.0; 1678 -8.0; 1846 -8.0; 2031 -8.1; 2234 -8.1; 2457 -8.4; 2703 -7.0; 2973 -2.4; 3270 -0.5; 3597 -5.1; 3957 -8.5; 4353 -6.9; 4788 -4.3; 5267 -4.2; 5793 -8.2; 6373 -9.6; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -10.6; 13660 -11.3; 15026 -7.9; 16529 -6.9; 18182 -7.9; 20000 -6.7
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
| Peaking | 20 Hz    | 2.82 | 3.8 dB  |
| Peaking | 79 Hz    | 0.42 | -1.9 dB |
| Peaking | 2221 Hz  | 1.11 | -2.3 dB |
| Peaking | 3167 Hz  | 5.9  | 8.3 dB  |
| Peaking | 13345 Hz | 3.5  | -5.8 dB |
| Peaking | 544 Hz   | 1.71 | 1.5 dB  |
| Peaking | 1306 Hz  | 5.83 | -1.8 dB |
| Peaking | 4021 Hz  | 5.87 | -4.1 dB |
| Peaking | 5527 Hz  | 1.73 | 4.6 dB  |
| Peaking | 6086 Hz  | 6.91 | -8.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)
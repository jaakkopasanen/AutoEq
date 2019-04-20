# Monoprice M650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.6; 25 -8.0; 28 -8.4; 31 -8.7; 34 -9.0; 37 -9.2; 41 -9.4; 45 -9.6; 49 -9.8; 54 -9.9; 60 -10.1; 66 -10.1; 72 -10.2; 79 -10.4; 87 -10.7; 96 -11.3; 106 -11.9; 116 -12.2; 128 -12.4; 141 -12.8; 155 -13.1; 170 -13.3; 187 -13.3; 206 -13.2; 227 -13.0; 249 -12.8; 274 -12.4; 302 -11.8; 332 -11.3; 365 -10.7; 402 -10.1; 442 -9.5; 486 -8.8; 535 -7.9; 588 -7.1; 647 -6.2; 712 -4.8; 783 -4.1; 861 -3.0; 947 -2.2; 1042 -1.2; 1146 -0.6; 1261 -0.5; 1387 -0.8; 1526 -1.1; 1678 -1.6; 1846 -2.7; 2031 -3.7; 2234 -4.5; 2457 -5.0; 2703 -5.6; 2973 -5.7; 3270 -3.4; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -4.0; 5793 -6.7; 6373 -6.3; 7010 -6.5; 7711 -7.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice M650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice M650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 40 Hz    |  1.11 | -1.6 dB |
| Peaking | 204 Hz   |  0.43 | -7.1 dB |
| Peaking | 1299 Hz  |  0.75 | 8.7 dB  |
| Peaking | 3321 Hz  |  0.58 | -5.5 dB |
| Peaking | 4147 Hz  |  1.79 | 10.5 dB |
| Peaking | 2969 Hz  |  8.4  | -1.0 dB |
| Peaking | 3471 Hz  |  9.07 | 1.3 dB  |
| Peaking | 5791 Hz  | 11.32 | -1.6 dB |
| Peaking | 10837 Hz |  1.89 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Monoprice%20M650/Monoprice%20M650.png)
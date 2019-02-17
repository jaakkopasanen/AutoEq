# Sennheiser HD 25-1 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -1.1; 79 -2.5; 87 -3.6; 96 -4.7; 106 -5.7; 116 -6.3; 128 -6.2; 141 -6.2; 155 -6.6; 170 -6.6; 187 -6.8; 206 -6.9; 227 -7.1; 249 -7.1; 274 -7.0; 302 -6.8; 332 -6.5; 365 -6.0; 402 -5.3; 442 -5.1; 486 -4.9; 535 -4.5; 588 -4.4; 647 -4.4; 712 -4.7; 783 -5.3; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -6.8; 1261 -5.6; 1387 -6.0; 1526 -6.2; 1678 -6.6; 1846 -7.0; 2031 -7.3; 2234 -7.6; 2457 -7.8; 2703 -7.7; 2973 -7.5; 3270 -6.4; 3597 -5.4; 3957 -4.8; 4353 -0.5; 4788 -2.4; 5267 -3.7; 5793 -1.8; 6373 -6.8; 7010 -9.2; 7711 -10.9; 8482 -12.7; 9330 -11.2; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.7  | 7.1 dB  |
| Peaking | 602 Hz   | 2.2  | 2.4 dB  |
| Peaking | 3114 Hz  | 1.28 | -4.1 dB |
| Peaking | 4554 Hz  | 1.26 | 7.2 dB  |
| Peaking | 8196 Hz  | 2.52 | -7.8 dB |
| Peaking | 38 Hz    | 3.13 | -1.1 dB |
| Peaking | 70 Hz    | 2.4  | 2.7 dB  |
| Peaking | 132 Hz   | 0.71 | -1.3 dB |
| Peaking | 1334 Hz  | 6.72 | 0.8 dB  |
| Peaking | 10667 Hz | 7.3  | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%2025-1%20II/Sennheiser%20HD%2025-1%20II.png)
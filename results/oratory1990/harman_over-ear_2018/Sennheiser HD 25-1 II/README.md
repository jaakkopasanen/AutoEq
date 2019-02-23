# Sennheiser HD 25-1 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -1.3; 79 -2.8; 87 -3.8; 96 -4.9; 106 -5.9; 116 -6.5; 128 -6.4; 141 -6.5; 155 -6.8; 170 -6.8; 187 -7.0; 206 -7.1; 227 -7.4; 249 -7.3; 274 -7.3; 302 -7.0; 332 -6.7; 365 -6.2; 402 -5.5; 442 -5.3; 486 -5.1; 535 -4.7; 588 -4.7; 647 -4.6; 712 -4.9; 783 -5.5; 861 -6.2; 947 -6.5; 1042 -7.0; 1146 -7.0; 1261 -5.8; 1387 -6.2; 1526 -6.5; 1678 -6.8; 1846 -7.3; 2031 -7.5; 2234 -7.9; 2457 -8.1; 2703 -8.0; 2973 -7.7; 3270 -6.6; 3597 -5.7; 3957 -5.0; 4353 -0.5; 4788 -2.7; 5267 -4.0; 5793 -2.0; 6373 -7.0; 7010 -9.5; 7711 -11.1; 8482 -12.9; 9330 -11.4; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.74 | 7.1 dB  |
| Peaking | 603 Hz   | 2.5  | 2.2 dB  |
| Peaking | 3111 Hz  | 1.21 | -3.9 dB |
| Peaking | 4548 Hz  | 1.4  | 7.1 dB  |
| Peaking | 8233 Hz  | 2.63 | -7.7 dB |
| Peaking | 37 Hz    | 3.26 | -1.2 dB |
| Peaking | 68 Hz    | 2.52 | 2.9 dB  |
| Peaking | 159 Hz   | 0.51 | -1.4 dB |
| Peaking | 436 Hz   | 2.78 | 1.2 dB  |
| Peaking | 10576 Hz | 7.02 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%2025-1%20II/Sennheiser%20HD%2025-1%20II.png)
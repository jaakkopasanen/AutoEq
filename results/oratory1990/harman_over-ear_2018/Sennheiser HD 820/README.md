# Sennheiser HD 820
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.5; 25 -10.8; 28 -11.2; 31 -11.5; 34 -11.7; 37 -11.9; 41 -12.2; 45 -12.3; 49 -12.4; 54 -12.4; 60 -12.1; 66 -11.1; 72 -8.9; 79 -7.1; 87 -8.7; 96 -11.5; 106 -13.1; 116 -13.9; 128 -14.1; 141 -13.9; 155 -14.0; 170 -13.4; 187 -12.2; 206 -10.0; 227 -7.0; 249 -3.1; 274 -0.5; 302 -0.5; 332 -1.5; 365 -3.4; 402 -4.6; 442 -5.6; 486 -6.2; 535 -6.7; 588 -7.1; 647 -7.2; 712 -7.4; 783 -7.8; 861 -8.3; 947 -8.7; 1042 -8.6; 1146 -8.3; 1261 -7.3; 1387 -6.4; 1526 -5.8; 1678 -5.3; 1846 -5.0; 2031 -5.0; 2234 -5.1; 2457 -6.0; 2703 -6.9; 2973 -6.4; 3270 -4.1; 3597 -2.1; 3957 -0.9; 4353 -2.3; 4788 -7.3; 5267 -8.1; 5793 -5.6; 6373 -4.7; 7010 -5.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.8; 15026 -6.7; 16529 -6.5; 18182 -7.2; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 820 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 820 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 1.26 | -4.7 dB |
| Peaking | 51 Hz   | 2.97 | -3.8 dB |
| Peaking | 155 Hz  | 1.03 | -9.0 dB |
| Peaking | 285 Hz  | 2.26 | 10.3 dB |
| Peaking | 3891 Hz | 4.46 | 6.2 dB  |
| Peaking | 81 Hz   | 6.98 | 3.6 dB  |
| Peaking | 107 Hz  | 4.82 | -1.6 dB |
| Peaking | 1004 Hz | 1.8  | -2.7 dB |
| Peaking | 1858 Hz | 1.52 | 2.0 dB  |
| Peaking | 2739 Hz | 5.43 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -9.5 dB |
| Peaking | 250 Hz   | 1.41 | 4.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20820/Sennheiser%20HD%20820.png)
# JBL Duet NC (ANC Off)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -8.1; 25 -8.4; 28 -8.7; 31 -8.8; 34 -9.0; 37 -9.2; 41 -9.3; 45 -9.1; 49 -8.7; 54 -8.1; 60 -7.3; 66 -6.7; 72 -5.6; 79 -4.2; 87 -4.2; 96 -4.9; 106 -5.2; 116 -4.9; 128 -5.2; 141 -6.1; 155 -6.7; 170 -6.1; 187 -4.8; 206 -3.2; 227 -1.0; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -1.1; 535 -2.8; 588 -3.5; 647 -4.1; 712 -5.0; 783 -5.7; 861 -6.2; 947 -6.5; 1042 -6.4; 1146 -6.0; 1261 -5.2; 1387 -5.3; 1526 -5.1; 1678 -3.8; 1846 -2.7; 2031 -1.7; 2234 -0.9; 2457 -1.0; 2703 -1.5; 2973 -0.5; 3270 -0.6; 3597 -5.2; 3957 -5.9; 4353 -4.8; 4788 -3.6; 5267 -0.5; 5793 -4.5; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Duet NC (ANC Off) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Duet NC (ANC Off) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 82 Hz   |  0.41 | -6.3 dB |
| Peaking | 85 Hz   |  1.17 | 7.6 dB  |
| Peaking | 306 Hz  |  0.92 | 8.4 dB  |
| Peaking | 2537 Hz |  1.67 | 6.0 dB  |
| Peaking | 5385 Hz |  4.38 | 4.9 dB  |
| Peaking | 468 Hz  |  6.34 | 1.8 dB  |
| Peaking | 934 Hz  |  2.76 | -1.5 dB |
| Peaking | 3300 Hz |  6.64 | 4.1 dB  |
| Peaking | 3660 Hz |  4.1  | -3.1 dB |
| Peaking | 6620 Hz | 12.05 | 3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 5.0 dB  |
| Peaking | 500 Hz   | 1.41 | 4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/JBL%20Duet%20NC%20(ANC%20Off)/JBL%20Duet%20NC%20(ANC%20Off).png)
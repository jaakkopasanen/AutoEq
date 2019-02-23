# Sennheiser HD 598 CS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.7; 25 -8.9; 28 -9.2; 31 -9.3; 34 -9.4; 37 -9.5; 41 -9.5; 45 -9.5; 49 -9.4; 54 -9.2; 60 -9.1; 66 -9.0; 72 -9.0; 79 -8.7; 87 -8.6; 96 -8.6; 106 -8.3; 116 -8.2; 128 -8.5; 141 -8.9; 155 -9.2; 170 -9.2; 187 -8.2; 206 -7.1; 227 -5.9; 249 -4.5; 274 -3.4; 302 -2.9; 332 -3.1; 365 -3.6; 402 -4.3; 442 -5.4; 486 -6.0; 535 -6.0; 588 -6.1; 647 -6.2; 712 -6.5; 783 -6.8; 861 -7.2; 947 -7.4; 1042 -7.3; 1146 -7.2; 1261 -6.9; 1387 -6.6; 1526 -6.4; 1678 -6.3; 1846 -6.3; 2031 -6.1; 2234 -5.6; 2457 -4.5; 2703 -3.0; 2973 -2.8; 3270 -4.8; 3597 -5.2; 3957 -2.5; 4353 -0.8; 4788 -0.9; 5267 -0.7; 5793 -1.6; 6373 -0.5; 7010 -2.5; 7711 -4.7; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.4; 15026 -5.4; 16529 -6.1; 18182 -8.7; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 CS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 CS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 36 Hz    |  0.66 | -4.6 dB |
| Peaking | 93 Hz    |  1.52 | -2.1 dB |
| Peaking | 160 Hz   |  3.45 | -3.7 dB |
| Peaking | 1073 Hz  |  1.29 | -2.5 dB |
| Peaking | 5188 Hz  |  1.7  | 4.7 dB  |
| Peaking | 311 Hz   |  2.69 | 3.4 dB  |
| Peaking | 1294 Hz  |  0.08 | -0.4 dB |
| Peaking | 2797 Hz  |  7.28 | 2.6 dB  |
| Peaking | 6545 Hz  | 10.79 | 2.8 dB  |
| Peaking | 19737 Hz |  0.98 | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20598%20CS/Sennheiser%20HD%20598%20CS.png)
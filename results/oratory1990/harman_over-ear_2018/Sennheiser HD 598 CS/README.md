# Sennheiser HD 598 CS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.4; 25 -8.6; 28 -8.8; 31 -9.0; 34 -9.1; 37 -9.1; 41 -9.2; 45 -9.1; 49 -9.0; 54 -8.9; 60 -8.7; 66 -8.7; 72 -8.6; 79 -8.3; 87 -8.2; 96 -8.2; 106 -8.0; 116 -7.9; 128 -8.2; 141 -8.6; 155 -8.9; 170 -8.8; 187 -7.8; 206 -6.7; 227 -5.5; 249 -4.1; 274 -3.0; 302 -2.5; 332 -2.7; 365 -3.2; 402 -3.9; 442 -5.1; 486 -5.6; 535 -5.6; 588 -5.7; 647 -5.8; 712 -6.2; 783 -6.5; 861 -6.9; 947 -7.0; 1042 -7.0; 1146 -6.8; 1261 -6.6; 1387 -6.2; 1526 -6.1; 1678 -6.0; 1846 -6.1; 2031 -6.0; 2234 -5.5; 2457 -4.3; 2703 -2.8; 2973 -2.5; 3270 -4.6; 3597 -5.0; 3957 -2.3; 4353 -0.6; 4788 -0.6; 5267 -0.6; 5793 -1.4; 6373 -0.5; 7010 -2.2; 7711 -4.4; 8482 -4.7; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -5.3; 15026 -5.2; 16529 -6.0; 18182 -8.7; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 CS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 CS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 40 Hz    |  0.35 | -4.4 dB |
| Peaking | 166 Hz   |  2    | -3.1 dB |
| Peaking | 302 Hz   |  1.99 | 3.7 dB  |
| Peaking | 1015 Hz  |  0.81 | -2.3 dB |
| Peaking | 5151 Hz  |  1.67 | 4.7 dB  |
| Peaking | 2157 Hz  |  3.04 | -1.3 dB |
| Peaking | 2862 Hz  |  2.92 | 2.6 dB  |
| Peaking | 3457 Hz  |  7.21 | -3.3 dB |
| Peaking | 6579 Hz  | 12.65 | 2.2 dB  |
| Peaking | 19910 Hz |  0.87 | -7.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20598%20CS/Sennheiser%20HD%20598%20CS.png)
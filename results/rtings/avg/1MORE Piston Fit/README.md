# 1MORE Piston Fit
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.7; 72 -1.4; 79 -2.2; 87 -3.1; 96 -3.9; 106 -4.7; 116 -5.4; 128 -6.0; 141 -6.5; 155 -7.0; 170 -7.3; 187 -7.5; 206 -7.6; 227 -7.8; 249 -8.0; 274 -8.0; 302 -8.0; 332 -7.9; 365 -7.7; 402 -7.4; 442 -7.1; 486 -6.6; 535 -6.0; 588 -5.3; 647 -4.5; 712 -3.8; 783 -3.2; 861 -2.8; 947 -2.7; 1042 -3.3; 1146 -4.1; 1261 -4.3; 1387 -4.5; 1526 -4.6; 1678 -5.2; 1846 -6.6; 2031 -7.7; 2234 -8.0; 2457 -6.2; 2703 -3.5; 2973 -6.1; 3270 -8.8; 3597 -9.4; 3957 -9.7; 4353 -10.4; 4788 -11.6; 5267 -12.1; 5793 -10.4; 6373 -7.3; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Piston Fit GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Piston Fit ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 51 Hz   |  0.32 | 7.9 dB  |
| Peaking | 165 Hz  |  0.46 | -5.0 dB |
| Peaking | 883 Hz  |  1.32 | 4.5 dB  |
| Peaking | 2725 Hz | 11.19 | 4.0 dB  |
| Peaking | 4742 Hz |  2.06 | -5.6 dB |
| Peaking | 1561 Hz |  4.58 | 1.2 dB  |
| Peaking | 2096 Hz |  4.99 | -2.0 dB |
| Peaking | 5575 Hz |  6.93 | -2.1 dB |
| Peaking | 7044 Hz |  3.28 | 2.9 dB  |
| Peaking | 7635 Hz |  2.34 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Piston%20Fit/1MORE%20Piston%20Fit.png)
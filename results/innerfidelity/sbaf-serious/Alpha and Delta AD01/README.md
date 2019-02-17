# Alpha and Delta AD01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.5; 23 -14.6; 25 -14.6; 28 -14.6; 31 -14.6; 34 -14.5; 37 -14.4; 41 -14.3; 45 -14.3; 49 -14.2; 54 -14.1; 60 -14.0; 66 -13.9; 72 -13.9; 79 -13.8; 87 -13.8; 96 -13.8; 106 -13.5; 116 -13.3; 128 -13.1; 141 -12.9; 155 -12.6; 170 -12.3; 187 -11.9; 206 -11.5; 227 -11.0; 249 -10.6; 274 -10.1; 302 -9.7; 332 -9.2; 365 -8.7; 402 -8.2; 442 -7.7; 486 -7.4; 535 -6.9; 588 -6.3; 647 -6.0; 712 -5.8; 783 -5.6; 861 -5.8; 947 -6.2; 1042 -6.7; 1146 -6.9; 1261 -7.4; 1387 -8.0; 1526 -8.9; 1678 -9.7; 1846 -10.2; 2031 -10.7; 2234 -11.0; 2457 -10.1; 2703 -8.4; 2973 -5.3; 3270 -2.1; 3597 -1.0; 3957 -3.3; 4353 -6.8; 4788 -7.6; 5267 -3.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.5; 9330 -8.2; 10263 -7.0; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Alpha and Delta AD01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Alpha and Delta AD01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 42 Hz   |  0.19 | -8.2 dB |
| Peaking | 2151 Hz |  1.99 | -5.1 dB |
| Peaking | 3454 Hz |  4.69 | 7.0 dB  |
| Peaking | 6072 Hz |  4.24 | 6.8 dB  |
| Peaking | 9340 Hz |  3.69 | -1.8 dB |
| Peaking | 204 Hz  |  1.25 | -0.7 dB |
| Peaking | 722 Hz  |  1.38 | 1.8 dB  |
| Peaking | 1562 Hz |  4.34 | -1.1 dB |
| Peaking | 4620 Hz | 11.11 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Alpha%20and%20Delta%20AD01/Alpha%20and%20Delta%20AD01.png)
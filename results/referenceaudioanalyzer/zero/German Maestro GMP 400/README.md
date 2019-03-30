# German Maestro GMP 400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.2; 34 -2.0; 37 -2.8; 41 -3.6; 45 -4.2; 49 -4.7; 54 -5.2; 60 -5.8; 66 -6.2; 72 -6.5; 79 -6.8; 87 -7.1; 96 -7.2; 106 -7.4; 116 -7.4; 128 -7.4; 141 -7.4; 155 -7.4; 170 -7.4; 187 -7.4; 206 -7.3; 227 -7.1; 249 -6.9; 274 -6.6; 302 -6.3; 332 -6.1; 365 -5.8; 402 -5.5; 442 -5.3; 486 -5.0; 535 -4.7; 588 -4.3; 647 -4.0; 712 -3.5; 783 -3.0; 861 -2.6; 947 -2.6; 1042 -2.9; 1146 -4.2; 1261 -6.0; 1387 -6.4; 1526 -4.4; 1678 -2.8; 1846 -4.2; 2031 -6.0; 2234 -7.3; 2457 -8.9; 2703 -9.9; 2973 -10.0; 3270 -9.3; 3597 -7.9; 3957 -5.4; 4353 -2.8; 4788 -2.3; 5267 -3.7; 5793 -6.1; 6373 -9.1; 7010 -12.2; 7711 -14.4; 8482 -14.4; 9330 -12.0; 10263 -9.2; 11289 -8.7; 12418 -8.6; 13660 -6.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`German Maestro GMP 400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `German Maestro GMP 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.49 | 6.8 dB  |
| Peaking | 888 Hz   | 1.08 | 3.8 dB  |
| Peaking | 3012 Hz  | 2.53 | -5.0 dB |
| Peaking | 4803 Hz  | 2.13 | 6.6 dB  |
| Peaking | 7962 Hz  | 1.83 | -9.3 dB |
| Peaking | 136 Hz   | 0.96 | -1.3 dB |
| Peaking | 1343 Hz  | 5.29 | -2.8 dB |
| Peaking | 1687 Hz  | 4.22 | 3.4 dB  |
| Peaking | 2433 Hz  | 5.54 | -1.1 dB |
| Peaking | 14525 Hz | 5.19 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/German%20Maestro%20GMP%20400/German%20Maestro%20GMP%20400.png)
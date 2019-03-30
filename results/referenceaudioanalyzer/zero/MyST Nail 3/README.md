# MyST Nail 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.9; 25 -12.1; 28 -12.2; 31 -12.3; 34 -12.4; 37 -12.4; 41 -12.6; 45 -12.7; 49 -12.7; 54 -12.7; 60 -12.7; 66 -12.7; 72 -12.7; 79 -12.7; 87 -12.7; 96 -12.7; 106 -12.7; 116 -12.7; 128 -12.7; 141 -12.6; 155 -12.3; 170 -12.3; 187 -12.0; 206 -11.9; 227 -11.6; 249 -11.2; 274 -11.0; 302 -11.6; 332 -12.6; 365 -12.8; 402 -12.2; 442 -11.7; 486 -11.2; 535 -10.8; 588 -10.3; 647 -10.0; 712 -9.5; 783 -9.1; 861 -8.7; 947 -8.3; 1042 -8.0; 1146 -7.7; 1261 -7.5; 1387 -7.5; 1526 -7.5; 1678 -7.5; 1846 -7.6; 2031 -7.9; 2234 -8.5; 2457 -9.1; 2703 -8.6; 2973 -6.5; 3270 -3.6; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MyST Nail 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MyST Nail 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.36 | -5.6 dB |
| Peaking | 129 Hz  | 0.78 | -3.1 dB |
| Peaking | 413 Hz  | 0.73 | -4.7 dB |
| Peaking | 2540 Hz | 2.28 | -5.0 dB |
| Peaking | 4401 Hz | 1.22 | 7.6 dB  |
| Peaking | 518 Hz  | 5.33 | 0.3 dB  |
| Peaking | 3645 Hz | 4.98 | 2.2 dB  |
| Peaking | 4226 Hz | 1.88 | -1.5 dB |
| Peaking | 6301 Hz | 2.81 | 4.7 dB  |
| Peaking | 7419 Hz | 1.64 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -4.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MyST%20Nail%203/MyST%20Nail%203.png)
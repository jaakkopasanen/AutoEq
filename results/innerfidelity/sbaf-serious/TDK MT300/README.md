# TDK MT300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.1; 23 -14.1; 25 -14.1; 28 -14.0; 31 -14.0; 34 -13.9; 37 -13.9; 41 -14.0; 45 -13.9; 49 -13.9; 54 -14.0; 60 -14.0; 66 -14.1; 72 -14.2; 79 -14.3; 87 -14.4; 96 -14.5; 106 -14.5; 116 -14.3; 128 -14.2; 141 -14.1; 155 -13.8; 170 -13.5; 187 -13.0; 206 -12.6; 227 -12.0; 249 -11.5; 274 -10.8; 302 -10.2; 332 -9.5; 365 -8.7; 402 -7.9; 442 -7.1; 486 -6.6; 535 -6.0; 588 -5.2; 647 -4.9; 712 -4.8; 783 -4.5; 861 -4.8; 947 -4.9; 1042 -5.4; 1146 -5.6; 1261 -5.6; 1387 -5.8; 1526 -5.6; 1678 -4.9; 1846 -3.7; 2031 -2.5; 2234 -1.5; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -1.0; 3597 -2.5; 3957 -4.9; 4353 -8.9; 4788 -12.4; 5267 -8.7; 5793 -3.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TDK MT300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK MT300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 128 Hz  | 0.08 | -8.4 dB |
| Peaking | 639 Hz  | 0.62 | 8.6 dB  |
| Peaking | 2809 Hz | 1.15 | 8.0 dB  |
| Peaking | 4808 Hz | 3.8  | -9.3 dB |
| Peaking | 6202 Hz | 4.86 | 6.7 dB  |
| Peaking | 31 Hz   | 0.32 | -1.5 dB |
| Peaking | 44 Hz   | 0.82 | 1.9 dB  |
| Peaking | 1529 Hz | 4.66 | -0.7 dB |
| Peaking | 2021 Hz | 6.22 | 0.6 dB  |
| Peaking | 8347 Hz | 4.17 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/TDK%20MT300/TDK%20MT300.png)
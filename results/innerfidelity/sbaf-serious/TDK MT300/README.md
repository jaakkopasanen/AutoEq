# TDK MT300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.7; 23 -14.7; 25 -14.7; 28 -14.7; 31 -14.6; 34 -14.6; 37 -14.6; 41 -14.6; 45 -14.6; 49 -14.6; 54 -14.6; 60 -14.7; 66 -14.8; 72 -14.8; 79 -14.9; 87 -15.1; 96 -15.2; 106 -15.1; 116 -14.9; 128 -14.8; 141 -14.7; 155 -14.4; 170 -14.1; 187 -13.7; 206 -13.3; 227 -12.7; 249 -12.1; 274 -11.4; 302 -10.8; 332 -10.1; 365 -9.3; 402 -8.6; 442 -7.7; 486 -7.2; 535 -6.6; 588 -5.8; 647 -5.5; 712 -5.5; 783 -5.1; 861 -5.4; 947 -5.6; 1042 -6.0; 1146 -6.2; 1261 -6.3; 1387 -6.4; 1526 -6.3; 1678 -5.6; 1846 -4.3; 2031 -3.1; 2234 -2.2; 2457 -1.2; 2703 -0.9; 2973 -0.8; 3270 -1.6; 3597 -3.1; 3957 -5.5; 4353 -9.5; 4788 -13.1; 5267 -9.4; 5793 -3.8; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TDK MT300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK MT300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 61 Hz   | 0.22 | -9.8 dB  |
| Peaking | 2916 Hz | 1.47 | 6.0 dB   |
| Peaking | 4814 Hz | 3.44 | -10.3 dB |
| Peaking | 6320 Hz | 3.58 | 7.3 dB   |
| Peaking | 7572 Hz | 2.4  | -1.3 dB  |
| Peaking | 17 Hz   | 1.19 | -2.4 dB  |
| Peaking | 52 Hz   | 0.82 | 1.4 dB   |
| Peaking | 195 Hz  | 0.71 | -1.3 dB  |
| Peaking | 635 Hz  | 1.06 | 2.1 dB   |
| Peaking | 1388 Hz | 2.62 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/TDK%20MT300/TDK%20MT300.png)
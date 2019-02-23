# HiFiMAN RE-272
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.1; 25 -2.1; 28 -2.2; 31 -2.3; 34 -2.4; 37 -2.5; 41 -2.6; 45 -2.8; 49 -3.1; 54 -3.3; 60 -3.6; 66 -3.9; 72 -4.2; 79 -4.6; 87 -5.1; 96 -5.6; 106 -5.8; 116 -6.1; 128 -6.5; 141 -6.9; 155 -7.1; 170 -7.3; 187 -7.5; 206 -7.7; 227 -7.8; 249 -7.9; 274 -7.9; 302 -7.9; 332 -7.9; 365 -8.0; 402 -7.8; 442 -7.6; 486 -7.6; 535 -7.2; 588 -6.6; 647 -6.1; 712 -5.9; 783 -5.6; 861 -5.9; 947 -6.5; 1042 -7.4; 1146 -8.5; 1261 -9.8; 1387 -11.5; 1526 -13.4; 1678 -15.0; 1846 -15.7; 2031 -14.4; 2234 -11.5; 2457 -7.7; 2703 -4.0; 2973 -1.3; 3270 -0.6; 3597 -0.8; 3957 -2.5; 4353 -5.0; 4788 -4.1; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.7; 9330 -9.1; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-272 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-272 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 1.03 | 4.5 dB   |
| Peaking | 55 Hz   | 1.74 | 2.3 dB   |
| Peaking | 1846 Hz | 1.94 | -11.0 dB |
| Peaking | 3164 Hz | 2.25 | 8.2 dB   |
| Peaking | 5842 Hz | 3.69 | 6.4 dB   |
| Peaking | 305 Hz  | 0.81 | -1.7 dB  |
| Peaking | 651 Hz  | 3.76 | 0.6 dB   |
| Peaking | 832 Hz  | 2.31 | 1.9 dB   |
| Peaking | 1418 Hz | 5.2  | -1.0 dB  |
| Peaking | 9298 Hz | 6.42 | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-272/HiFiMAN%20RE-272.png)
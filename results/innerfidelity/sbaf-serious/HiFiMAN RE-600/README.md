# HiFiMAN RE-600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.4; 25 -2.5; 28 -2.6; 31 -2.7; 34 -2.8; 37 -2.9; 41 -3.0; 45 -3.1; 49 -3.3; 54 -3.6; 60 -3.9; 66 -4.2; 72 -4.5; 79 -4.9; 87 -5.3; 96 -5.7; 106 -6.0; 116 -6.1; 128 -6.4; 141 -6.7; 155 -6.8; 170 -6.9; 187 -7.0; 206 -7.0; 227 -6.9; 249 -6.8; 274 -6.7; 302 -6.5; 332 -6.3; 365 -6.1; 402 -5.9; 442 -5.5; 486 -5.5; 535 -5.3; 588 -5.0; 647 -4.9; 712 -5.0; 783 -5.0; 861 -5.5; 947 -6.0; 1042 -6.8; 1146 -7.6; 1261 -8.5; 1387 -9.8; 1526 -11.2; 1678 -12.4; 1846 -12.0; 2031 -11.2; 2234 -9.5; 2457 -5.7; 2703 -2.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.9; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.95 | 4.0 dB   |
| Peaking | 52 Hz   | 1.51 | 2.1 dB   |
| Peaking | 729 Hz  | 1.37 | 2.2 dB   |
| Peaking | 1865 Hz | 1.38 | -10.9 dB |
| Peaking | 3293 Hz | 0.82 | 9.5 dB   |
| Peaking | 188 Hz  | 1.9  | -0.8 dB  |
| Peaking | 2846 Hz | 4.95 | 3.2 dB   |
| Peaking | 2984 Hz | 1.89 | -1.9 dB  |
| Peaking | 6367 Hz | 2.23 | 5.0 dB   |
| Peaking | 7534 Hz | 1.61 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | 9.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-600/HiFiMAN%20RE-600.png)
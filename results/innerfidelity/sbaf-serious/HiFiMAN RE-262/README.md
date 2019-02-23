# HiFiMAN RE-262
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.0; 25 -3.1; 28 -3.2; 31 -3.3; 34 -3.4; 37 -3.5; 41 -3.7; 45 -3.9; 49 -4.0; 54 -4.2; 60 -4.6; 66 -5.0; 72 -5.4; 79 -5.8; 87 -6.2; 96 -6.6; 106 -6.9; 116 -7.3; 128 -7.7; 141 -8.0; 155 -8.3; 170 -8.5; 187 -8.6; 206 -8.9; 227 -9.0; 249 -9.1; 274 -9.2; 302 -9.3; 332 -9.3; 365 -9.3; 402 -9.3; 442 -9.1; 486 -9.2; 535 -9.1; 588 -8.6; 647 -8.4; 712 -8.3; 783 -7.9; 861 -8.2; 947 -8.7; 1042 -9.4; 1146 -10.4; 1261 -11.8; 1387 -13.4; 1526 -15.1; 1678 -15.8; 1846 -14.4; 2031 -11.5; 2234 -8.4; 2457 -5.1; 2703 -2.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.7; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-262 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-262 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 0.41 | 3.5 dB   |
| Peaking | 260 Hz  | 0.51 | -2.9 dB  |
| Peaking | 1696 Hz | 1.71 | -11.4 dB |
| Peaking | 3131 Hz | 1.36 | 8.2 dB   |
| Peaking | 5647 Hz | 2.75 | 5.1 dB   |
| Peaking | 501 Hz  | 4.08 | -0.5 dB  |
| Peaking | 818 Hz  | 4.24 | 0.7 dB   |
| Peaking | 6534 Hz | 7.3  | 2.2 dB   |
| Peaking | 7842 Hz | 2.21 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -7.2 dB |
| Peaking | 4000 Hz  | 1.41 | 10.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-262/HiFiMAN%20RE-262.png)
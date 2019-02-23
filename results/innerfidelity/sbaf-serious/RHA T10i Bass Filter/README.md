# RHA T10i Bass Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.2; 23 -14.4; 25 -14.6; 28 -14.8; 31 -15.0; 34 -15.2; 37 -15.3; 41 -15.3; 45 -15.3; 49 -15.4; 54 -15.5; 60 -15.5; 66 -15.6; 72 -15.6; 79 -15.7; 87 -15.8; 96 -15.8; 106 -15.6; 116 -15.4; 128 -15.3; 141 -15.1; 155 -14.8; 170 -14.4; 187 -14.0; 206 -13.5; 227 -12.9; 249 -12.4; 274 -11.7; 302 -11.1; 332 -10.4; 365 -9.7; 402 -9.1; 442 -8.3; 486 -7.8; 535 -7.2; 588 -6.3; 647 -5.7; 712 -5.6; 783 -4.9; 861 -4.5; 947 -4.1; 1042 -4.5; 1146 -4.8; 1261 -5.2; 1387 -5.9; 1526 -6.8; 1678 -7.5; 1846 -7.9; 2031 -8.0; 2234 -7.8; 2457 -6.7; 2703 -5.3; 2973 -3.7; 3270 -3.0; 3597 -3.2; 3957 -2.0; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -13.4; 9330 -15.9; 10263 -13.5; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T10i Bass Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Bass Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.34 | -7.3 dB  |
| Peaking | 142 Hz   | 0.48 | -6.7 dB  |
| Peaking | 826 Hz   | 1.7  | 3.1 dB   |
| Peaking | 5464 Hz  | 1.26 | 7.6 dB   |
| Peaking | 9222 Hz  | 3.14 | -12.6 dB |
| Peaking | 563 Hz   | 4.09 | 0.7 dB   |
| Peaking | 1225 Hz  | 2.29 | 1.8 dB   |
| Peaking | 2296 Hz  | 1.03 | -4.3 dB  |
| Peaking | 3011 Hz  | 1.64 | 4.0 dB   |
| Peaking | 11646 Hz | 7.92 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.4 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Bass%20Filter/RHA%20T10i%20Bass%20Filter.png)
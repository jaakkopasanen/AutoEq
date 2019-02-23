# RHA S500i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.5; 31 -1.8; 34 -2.1; 37 -2.4; 41 -2.7; 45 -3.0; 49 -3.3; 54 -3.6; 60 -4.0; 66 -4.4; 72 -4.7; 79 -5.0; 87 -5.5; 96 -5.9; 106 -6.0; 116 -6.2; 128 -6.2; 141 -6.6; 155 -6.6; 170 -6.5; 187 -6.5; 206 -6.4; 227 -6.1; 249 -6.0; 274 -5.8; 302 -5.6; 332 -5.3; 365 -5.0; 402 -4.7; 442 -4.3; 486 -4.1; 535 -3.9; 588 -3.4; 647 -3.3; 712 -3.3; 783 -3.2; 861 -3.4; 947 -3.8; 1042 -4.5; 1146 -5.2; 1261 -5.8; 1387 -6.8; 1526 -7.8; 1678 -8.6; 1846 -9.2; 2031 -9.8; 2234 -10.9; 2457 -12.3; 2703 -14.4; 2973 -13.2; 3270 -8.5; 3597 -4.8; 3957 -3.4; 4353 -4.5; 4788 -4.6; 5267 -3.8; 5793 -4.3; 6373 -7.0; 7010 -10.3; 7711 -10.3; 8482 -8.2; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -8.0; 15026 -6.9; 16529 -6.4; 18182 -6.4; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA S500i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA S500i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.67 | 5.6 dB   |
| Peaking | 748 Hz   | 0.97 | 3.9 dB   |
| Peaking | 2877 Hz  | 1.37 | -18.1 dB |
| Peaking | 3557 Hz  | 1.06 | 13.1 dB  |
| Peaking | 7391 Hz  | 3.91 | -5.8 dB  |
| Peaking | 57 Hz    | 2.41 | 0.6 dB   |
| Peaking | 155 Hz   | 1.3  | -0.8 dB  |
| Peaking | 1671 Hz  | 3.21 | -0.8 dB  |
| Peaking | 2033 Hz  | 0.06 | 0.2 dB   |
| Peaking | 13936 Hz | 4.14 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20S500i/RHA%20S500i.png)
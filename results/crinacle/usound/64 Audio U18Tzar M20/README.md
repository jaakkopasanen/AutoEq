# 64 Audio U18Tzar M20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.1; 25 -5.5; 28 -6.1; 31 -6.4; 34 -6.7; 37 -7.0; 41 -7.3; 45 -7.6; 49 -7.9; 54 -8.1; 60 -8.4; 66 -8.7; 72 -9.0; 79 -9.3; 87 -9.6; 96 -9.8; 106 -10.0; 116 -10.3; 128 -10.4; 141 -10.4; 155 -10.3; 170 -10.3; 187 -10.2; 206 -10.1; 227 -9.8; 249 -9.4; 274 -9.2; 302 -8.9; 332 -8.6; 365 -8.3; 402 -7.9; 442 -7.6; 486 -7.3; 535 -6.9; 588 -6.5; 647 -6.1; 712 -5.7; 783 -5.2; 861 -4.9; 947 -4.7; 1042 -5.0; 1146 -5.6; 1261 -6.3; 1387 -6.6; 1526 -6.4; 1678 -6.0; 1846 -5.6; 2031 -5.7; 2234 -6.1; 2457 -4.3; 2703 -2.9; 2973 -3.0; 3270 -3.4; 3597 -3.1; 3957 -1.5; 4353 -0.5; 4788 -2.6; 5267 -3.3; 5793 -1.8; 6373 -3.6; 7010 -6.7; 7711 -7.6; 8482 -6.5; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -7.2; 15026 -10.2; 16529 -14.2; 18182 -15.6; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio U18Tzar M20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio U18Tzar M20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 114 Hz   | 0.75 | -3.6 dB  |
| Peaking | 238 Hz   | 1.27 | -2.1 dB  |
| Peaking | 2760 Hz  | 4.46 | 2.1 dB   |
| Peaking | 4408 Hz  | 1.63 | 5.2 dB   |
| Peaking | 17616 Hz | 1.43 | -10.8 dB |
| Peaking | 20 Hz    | 2.39 | 2.3 dB   |
| Peaking | 894 Hz   | 3.04 | 1.9 dB   |
| Peaking | 6116 Hz  | 5.45 | 4.5 dB   |
| Peaking | 6773 Hz  | 2.01 | -2.7 dB  |
| Peaking | 12306 Hz | 2.42 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -7.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20U18Tzar%20M20/64%20Audio%20U18Tzar%20M20.png)
# ARC Pollux
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.5; 25 -2.6; 28 -2.8; 31 -2.8; 34 -2.9; 37 -3.0; 41 -3.2; 45 -3.3; 49 -3.5; 54 -3.6; 60 -3.9; 66 -4.2; 72 -4.6; 79 -5.0; 87 -5.5; 96 -5.9; 106 -6.3; 116 -6.8; 128 -7.1; 141 -7.5; 155 -7.9; 170 -8.1; 187 -8.3; 206 -8.5; 227 -8.6; 249 -8.7; 274 -8.8; 302 -8.8; 332 -8.7; 365 -8.6; 402 -8.6; 442 -8.6; 486 -8.5; 535 -8.4; 588 -8.3; 647 -8.2; 712 -8.0; 783 -7.8; 861 -7.8; 947 -8.0; 1042 -8.5; 1146 -9.4; 1261 -10.1; 1387 -10.4; 1526 -10.2; 1678 -9.9; 1846 -9.3; 2031 -8.2; 2234 -6.5; 2457 -4.5; 2703 -2.5; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.8; 4788 -2.4; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.7; 8482 -9.6; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -16.3; 16529 -13.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ARC Pollux GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ARC Pollux ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.35 | 4.3 dB   |
| Peaking | 889 Hz   | 0.09 | -2.8 dB  |
| Peaking | 3464 Hz  | 1.71 | 9.2 dB   |
| Peaking | 5885 Hz  | 3.1  | 6.8 dB   |
| Peaking | 15699 Hz | 3.41 | -11.8 dB |
| Peaking | 919 Hz   | 1.07 | 4.1 dB   |
| Peaking | 1314 Hz  | 0.79 | -4.1 dB  |
| Peaking | 2609 Hz  | 3.51 | 2.6 dB   |
| Peaking | 8188 Hz  | 4.25 | -5.9 dB  |
| Peaking | 8795 Hz  | 1    | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -7.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/ARC%20Pollux/ARC%20Pollux.png)
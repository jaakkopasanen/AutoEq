# 64 Audio A6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.4; 25 -10.5; 28 -10.6; 31 -10.6; 34 -10.6; 37 -10.5; 41 -10.4; 45 -10.4; 49 -10.3; 54 -10.2; 60 -10.1; 66 -10.0; 72 -9.9; 79 -9.9; 87 -9.9; 96 -9.8; 106 -9.8; 116 -9.7; 128 -9.6; 141 -9.5; 155 -9.3; 170 -9.1; 187 -9.0; 206 -8.8; 227 -8.6; 249 -8.4; 274 -8.3; 302 -8.2; 332 -8.2; 365 -8.2; 402 -8.2; 442 -8.3; 486 -8.3; 535 -8.2; 588 -8.1; 647 -7.8; 712 -7.4; 783 -6.8; 861 -6.1; 947 -5.7; 1042 -5.6; 1146 -5.8; 1261 -6.2; 1387 -6.4; 1526 -6.2; 1678 -5.8; 1846 -5.4; 2031 -5.3; 2234 -5.1; 2457 -4.7; 2703 -4.2; 2973 -3.8; 3270 -3.3; 3597 -3.5; 3957 -4.5; 4353 -5.5; 4788 -5.4; 5267 -3.3; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -7.9; 16529 -12.7; 18182 -15.4; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.11 | -4.0 dB  |
| Peaking | 508 Hz   | 2.25 | -1.3 dB  |
| Peaking | 3045 Hz  | 1.6  | 2.8 dB   |
| Peaking | 6079 Hz  | 4.12 | 6.3 dB   |
| Peaking | 18100 Hz | 1.51 | -10.2 dB |
| Peaking | 662 Hz   | 4.23 | -0.5 dB  |
| Peaking | 981 Hz   | 3.52 | 1.2 dB   |
| Peaking | 6792 Hz  | 8    | 1.6 dB   |
| Peaking | 7328 Hz  | 3.08 | -1.1 dB  |
| Peaking | 13668 Hz | 3.48 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -5.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20A6/64%20Audio%20A6.png)
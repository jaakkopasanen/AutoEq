# 64 Audio Tia Fourte
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.0; 25 -9.0; 28 -8.9; 31 -8.7; 34 -8.5; 37 -8.4; 41 -8.3; 45 -8.2; 49 -8.1; 54 -7.9; 60 -7.8; 66 -7.7; 72 -7.7; 79 -7.7; 87 -7.7; 96 -7.8; 106 -7.9; 116 -7.9; 128 -7.9; 141 -8.0; 155 -8.0; 170 -8.1; 187 -8.1; 206 -8.0; 227 -8.0; 249 -8.1; 274 -8.1; 302 -8.1; 332 -8.2; 365 -8.2; 402 -8.2; 442 -8.4; 486 -8.7; 535 -9.0; 588 -9.5; 647 -9.8; 712 -9.7; 783 -8.8; 861 -7.0; 947 -5.0; 1042 -3.4; 1146 -2.6; 1261 -2.7; 1387 -3.3; 1526 -3.8; 1678 -4.3; 1846 -4.9; 2031 -5.5; 2234 -6.1; 2457 -6.2; 2703 -5.7; 2973 -4.7; 3270 -3.4; 3597 -1.6; 3957 -0.5; 4353 -1.7; 4788 -3.5; 5267 -6.0; 5793 -6.6; 6373 -6.3; 7010 -7.3; 7711 -10.4; 8482 -9.9; 9330 -6.6; 10263 -6.5; 11289 -6.8; 12418 -8.8; 13660 -10.5; 15026 -11.5; 16529 -13.5; 18182 -17.3; 20000 -18.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio Tia Fourte GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio Tia Fourte ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.01 | -1.5 dB  |
| Peaking | 707 Hz   | 1.77 | -3.8 dB  |
| Peaking | 1179 Hz  | 1.36 | 6.0 dB   |
| Peaking | 3952 Hz  | 3.08 | 6.8 dB   |
| Peaking | 19228 Hz | 0.51 | -11.9 dB |
| Peaking | 23 Hz    | 1.83 | -1.2 dB  |
| Peaking | 1705 Hz  | 5.9  | 0.5 dB   |
| Peaking | 3789 Hz  | 1.48 | 0.5 dB   |
| Peaking | 8030 Hz  | 5.37 | -4.6 dB  |
| Peaking | 10286 Hz | 2.23 | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -8.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20Tia%20Fourte/64%20Audio%20Tia%20Fourte.png)
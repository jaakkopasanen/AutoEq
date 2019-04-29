# 64 Audio A12t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.1; 25 -7.3; 28 -7.6; 31 -7.8; 34 -7.9; 37 -7.9; 41 -8.0; 45 -8.0; 49 -7.9; 54 -7.9; 60 -7.8; 66 -7.8; 72 -7.8; 79 -7.8; 87 -7.8; 96 -7.8; 106 -7.8; 116 -7.7; 128 -7.5; 141 -7.4; 155 -7.3; 170 -7.1; 187 -6.8; 206 -6.6; 227 -6.3; 249 -6.2; 274 -6.0; 302 -5.9; 332 -5.8; 365 -5.9; 402 -5.9; 442 -6.1; 486 -6.2; 535 -6.3; 588 -6.2; 647 -6.0; 712 -5.5; 783 -5.0; 861 -4.5; 947 -4.2; 1042 -4.2; 1146 -4.7; 1261 -5.3; 1387 -5.7; 1526 -5.8; 1678 -5.7; 1846 -5.8; 2031 -6.2; 2234 -6.2; 2457 -4.7; 2703 -2.6; 2973 -1.2; 3270 -0.5; 3597 -0.7; 3957 -1.5; 4353 -2.3; 4788 -4.0; 5267 -3.2; 5793 -0.9; 6373 -3.3; 7010 -4.1; 7711 -4.5; 8482 -4.8; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -7.8; 15026 -12.0; 16529 -16.0; 18182 -18.4; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A12t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A12t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.32 | -2.5 dB  |
| Peaking | 342 Hz   | 0.05 | -0.8 dB  |
| Peaking | 3419 Hz  | 2.61 | 4.8 dB   |
| Peaking | 11032 Hz | 0.43 | 3.0 dB   |
| Peaking | 17593 Hz | 0.87 | -15.7 dB |
| Peaking | 967 Hz   | 4.15 | 1.7 dB   |
| Peaking | 2085 Hz  | 4.14 | -1.8 dB  |
| Peaking | 5818 Hz  | 8.07 | 3.4 dB   |
| Peaking | 8182 Hz  | 1.43 | -1.0 dB  |
| Peaking | 12570 Hz | 5.59 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -12.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20A12t/64%20Audio%20A12t.png)
# 64 Audio U18Tzar sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.4; 25 -6.6; 28 -6.9; 31 -7.2; 34 -7.5; 37 -7.7; 41 -7.9; 45 -8.0; 49 -8.1; 54 -8.2; 60 -8.4; 66 -8.6; 72 -8.8; 79 -9.0; 87 -9.2; 96 -9.4; 106 -9.6; 116 -9.7; 128 -9.7; 141 -9.8; 155 -9.8; 170 -9.7; 187 -9.5; 206 -9.3; 227 -9.2; 249 -8.9; 274 -8.7; 302 -8.4; 332 -8.1; 365 -7.8; 402 -7.5; 442 -7.2; 486 -6.9; 535 -6.5; 588 -6.2; 647 -5.9; 712 -5.4; 783 -5.0; 861 -4.6; 947 -4.5; 1042 -4.7; 1146 -5.3; 1261 -5.9; 1387 -6.1; 1526 -5.9; 1678 -5.4; 1846 -4.9; 2031 -4.9; 2234 -5.2; 2457 -4.6; 2703 -3.2; 2973 -3.3; 3270 -3.7; 3597 -2.8; 3957 -0.9; 4353 -0.5; 4788 -2.9; 5267 -3.5; 5793 -3.6; 6373 -6.8; 7010 -7.4; 7711 -6.9; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -6.1; 15026 -8.5; 16529 -16.5; 18182 -20.0; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio U18Tzar sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio U18Tzar sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 1.27 | -0.7 dB  |
| Peaking | 143 Hz   | 0.46 | -3.8 dB  |
| Peaking | 870 Hz   | 1.88 | 1.8 dB   |
| Peaking | 4083 Hz  | 1.97 | 5.2 dB   |
| Peaking | 17891 Hz | 1.78 | -16.4 dB |
| Peaking | 2775 Hz  | 4.73 | 1.5 dB   |
| Peaking | 3433 Hz  | 6.71 | -1.2 dB  |
| Peaking | 6954 Hz  | 5.44 | -2.6 dB  |
| Peaking | 14197 Hz | 1.22 | 2.3 dB   |
| Peaking | 16540 Hz | 3.32 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -8.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20U18Tzar%20sample%201/64%20Audio%20U18Tzar%20sample%201.png)
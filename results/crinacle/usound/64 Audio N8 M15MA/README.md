# 64 Audio N8 M15MA
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.9; 25 -8.0; 28 -8.2; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.8; 45 -9.0; 49 -9.1; 54 -9.3; 60 -9.6; 66 -9.8; 72 -10.1; 79 -10.4; 87 -10.7; 96 -11.0; 106 -11.3; 116 -11.5; 128 -11.6; 141 -11.7; 155 -11.7; 170 -11.6; 187 -11.5; 206 -11.3; 227 -11.0; 249 -10.8; 274 -10.4; 302 -10.1; 332 -9.7; 365 -9.4; 402 -9.0; 442 -8.6; 486 -8.1; 535 -7.7; 588 -7.2; 647 -6.7; 712 -6.1; 783 -5.6; 861 -5.1; 947 -4.9; 1042 -5.1; 1146 -5.8; 1261 -6.7; 1387 -7.4; 1526 -7.6; 1678 -7.5; 1846 -7.1; 2031 -6.7; 2234 -6.1; 2457 -5.2; 2703 -4.2; 2973 -3.3; 3270 -2.6; 3597 -2.5; 3957 -2.9; 4353 -3.4; 4788 -4.1; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.1; 16529 -14.9; 18182 -16.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15MA GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15MA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 89 Hz    | 0.46 | -3.4 dB  |
| Peaking | 207 Hz   | 0.81 | -3.1 dB  |
| Peaking | 3436 Hz  | 2.33 | 4.0 dB   |
| Peaking | 5926 Hz  | 3.21 | 6.2 dB   |
| Peaking | 17633 Hz | 1.53 | -11.5 dB |
| Peaking | 940 Hz   | 2.38 | 2.3 dB   |
| Peaking | 1547 Hz  | 2.43 | -1.7 dB  |
| Peaking | 6673 Hz  | 7.6  | 1.3 dB   |
| Peaking | 7532 Hz  | 3.94 | -1.2 dB  |
| Peaking | 13276 Hz | 3.58 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -7.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15MA/64%20Audio%20N8%20M15MA.png)
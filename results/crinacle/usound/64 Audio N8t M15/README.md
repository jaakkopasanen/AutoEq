# 64 Audio N8t M15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.8; 25 -7.0; 28 -7.3; 31 -7.4; 34 -7.5; 37 -7.6; 41 -7.6; 45 -7.6; 49 -7.7; 54 -7.7; 60 -7.7; 66 -7.7; 72 -7.7; 79 -7.8; 87 -7.9; 96 -7.9; 106 -7.7; 116 -7.8; 128 -7.6; 141 -7.5; 155 -7.2; 170 -7.0; 187 -6.8; 206 -6.5; 227 -6.2; 249 -5.9; 274 -5.6; 302 -5.3; 332 -5.0; 365 -4.8; 402 -4.5; 442 -4.4; 486 -4.2; 535 -4.0; 588 -3.8; 647 -3.6; 712 -3.3; 783 -3.0; 861 -2.7; 947 -2.6; 1042 -2.7; 1146 -3.3; 1261 -4.0; 1387 -4.4; 1526 -4.3; 1678 -3.9; 1846 -3.4; 2031 -3.1; 2234 -2.8; 2457 -2.2; 2703 -1.4; 2973 -0.8; 3270 -0.5; 3597 -1.0; 3957 -1.7; 4353 -2.0; 4788 -2.9; 5267 -3.6; 5793 -0.9; 6373 -0.6; 7010 -3.7; 7711 -4.1; 8482 -3.9; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -6.4; 18182 -7.3; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8t M15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8t M15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.38 | -3.5 dB |
| Peaking | 145 Hz   | 0.84 | -2.2 dB |
| Peaking | 3412 Hz  | 1.16 | 3.1 dB  |
| Peaking | 15539 Hz | 2.3  | 1.1 dB  |
| Peaking | 17394 Hz | 2.2  | -5.2 dB |
| Peaking | 953 Hz   | 1.82 | 1.6 dB  |
| Peaking | 1427 Hz  | 2.33 | -1.4 dB |
| Peaking | 5182 Hz  | 4.5  | -2.5 dB |
| Peaking | 6146 Hz  | 3.56 | 4.5 dB  |
| Peaking | 7205 Hz  | 3.56 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8t%20M15/64%20Audio%20N8t%20M15.png)
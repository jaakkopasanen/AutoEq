# 64 Audio N8 M15 custom sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.5; 25 -7.7; 28 -8.0; 31 -8.2; 34 -8.3; 37 -8.4; 41 -8.6; 45 -8.8; 49 -8.8; 54 -9.0; 60 -9.2; 66 -9.5; 72 -9.7; 79 -10.0; 87 -10.4; 96 -10.6; 106 -10.7; 116 -10.9; 128 -11.1; 141 -11.1; 155 -11.2; 170 -11.2; 187 -11.2; 206 -10.9; 227 -10.8; 249 -10.6; 274 -10.3; 302 -10.0; 332 -9.6; 365 -9.3; 402 -9.0; 442 -8.6; 486 -8.2; 535 -7.8; 588 -7.3; 647 -6.9; 712 -6.3; 783 -5.8; 861 -5.4; 947 -5.2; 1042 -5.4; 1146 -6.1; 1261 -7.0; 1387 -7.7; 1526 -7.9; 1678 -7.8; 1846 -7.4; 2031 -6.9; 2234 -6.3; 2457 -5.4; 2703 -4.3; 2973 -3.4; 3270 -2.7; 3597 -2.5; 3957 -3.0; 4353 -3.5; 4788 -4.1; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.7; 16529 -13.3; 18182 -15.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 custom sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 custom sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 103 Hz   | 0.47 | -3.7 dB |
| Peaking | 240 Hz   | 0.91 | -2.4 dB |
| Peaking | 3447 Hz  | 2.6  | 3.9 dB  |
| Peaking | 5898 Hz  | 3.18 | 6.3 dB  |
| Peaking | 17826 Hz | 1.48 | -9.9 dB |
| Peaking | 979 Hz   | 1.45 | 4.6 dB  |
| Peaking | 1329 Hz  | 0.71 | -3.8 dB |
| Peaking | 2588 Hz  | 1.3  | 1.7 dB  |
| Peaking | 7840 Hz  | 7.23 | -1.0 dB |
| Peaking | 13633 Hz | 3.5  | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15%20custom%20sample%202/64%20Audio%20N8%20M15%20custom%20sample%202.png)
# 64 Audio N8 M15 custom sample 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.7; 25 -9.9; 28 -10.1; 31 -10.2; 34 -10.2; 37 -10.2; 41 -10.3; 45 -10.4; 49 -10.4; 54 -10.4; 60 -10.4; 66 -10.5; 72 -10.5; 79 -10.6; 87 -10.8; 96 -10.8; 106 -10.7; 116 -10.9; 128 -10.8; 141 -10.7; 155 -10.5; 170 -10.5; 187 -10.3; 206 -10.1; 227 -9.8; 249 -9.6; 274 -9.4; 302 -9.1; 332 -8.9; 365 -8.7; 402 -8.5; 442 -8.3; 486 -8.1; 535 -7.8; 588 -7.6; 647 -7.2; 712 -6.7; 783 -6.1; 861 -5.6; 947 -5.3; 1042 -5.4; 1146 -6.1; 1261 -6.9; 1387 -7.6; 1526 -7.9; 1678 -7.6; 1846 -7.3; 2031 -6.9; 2234 -6.4; 2457 -5.6; 2703 -4.6; 2973 -3.6; 3270 -2.9; 3597 -2.7; 3957 -2.8; 4353 -2.7; 4788 -2.9; 5267 -2.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -7.4; 16529 -11.4; 18182 -12.6; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 custom sample 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 custom sample 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.37 | -3.1 dB |
| Peaking | 159 Hz   | 0.49 | -3.4 dB |
| Peaking | 3664 Hz  | 2.1  | 3.9 dB  |
| Peaking | 5975 Hz  | 3.49 | 5.9 dB  |
| Peaking | 17691 Hz | 1.72 | -7.3 dB |
| Peaking | 994 Hz   | 1.7  | 4.2 dB  |
| Peaking | 1245 Hz  | 0.85 | -3.1 dB |
| Peaking | 2829 Hz  | 2.67 | 1.2 dB  |
| Peaking | 8014 Hz  | 6.62 | -1.0 dB |
| Peaking | 14044 Hz | 3.76 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15%20custom%20sample%204/64%20Audio%20N8%20M15%20custom%20sample%204.png)
# 64 Audio N8 custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.8; 25 -3.3; 28 -3.8; 31 -4.3; 34 -4.6; 37 -4.9; 41 -5.3; 45 -5.6; 49 -5.9; 54 -6.1; 60 -6.5; 66 -6.9; 72 -7.2; 79 -7.6; 87 -8.0; 96 -8.3; 106 -8.5; 116 -8.9; 128 -9.2; 141 -9.4; 155 -9.5; 170 -9.6; 187 -9.8; 206 -9.7; 227 -9.7; 249 -9.7; 274 -9.6; 302 -9.4; 332 -9.3; 365 -9.1; 402 -8.9; 442 -8.7; 486 -8.4; 535 -8.1; 588 -7.8; 647 -7.4; 712 -6.9; 783 -6.4; 861 -6.0; 947 -5.8; 1042 -6.0; 1146 -6.7; 1261 -7.6; 1387 -8.3; 1526 -8.6; 1678 -8.4; 1846 -7.9; 2031 -7.4; 2234 -6.7; 2457 -5.7; 2703 -4.7; 2973 -3.8; 3270 -3.1; 3597 -2.9; 3957 -3.2; 4353 -3.5; 4788 -4.0; 5267 -2.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.8; 15026 -9.5; 16529 -11.3; 18182 -12.4; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.57 | 5.8 dB  |
| Peaking | 195 Hz   | 0.56 | -3.5 dB |
| Peaking | 5409 Hz  | 0.58 | 13.0 dB |
| Peaking | 9857 Hz  | 0.18 | -9.5 dB |
| Peaking | 12966 Hz | 1.35 | 5.7 dB  |
| Peaking | 976 Hz   | 1.42 | 4.6 dB  |
| Peaking | 1342 Hz  | 0.67 | -3.8 dB |
| Peaking | 3322 Hz  | 1.13 | 4.1 dB  |
| Peaking | 5136 Hz  | 1.44 | -5.5 dB |
| Peaking | 5897 Hz  | 3.45 | 5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -5.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20custom/64%20Audio%20N8%20custom.png)
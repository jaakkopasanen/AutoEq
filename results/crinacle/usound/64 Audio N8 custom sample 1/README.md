# 64 Audio N8 custom sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.9; 25 -4.2; 28 -4.6; 31 -4.8; 34 -5.0; 37 -5.1; 41 -5.3; 45 -5.5; 49 -5.6; 54 -5.8; 60 -6.0; 66 -6.2; 72 -6.4; 79 -6.7; 87 -6.9; 96 -7.2; 106 -7.5; 116 -7.7; 128 -7.9; 141 -8.2; 155 -8.4; 170 -8.5; 187 -8.6; 206 -8.6; 227 -8.6; 249 -8.6; 274 -8.6; 302 -8.5; 332 -8.4; 365 -8.3; 402 -8.2; 442 -8.0; 486 -7.8; 535 -7.6; 588 -7.3; 647 -7.0; 712 -6.5; 783 -6.1; 861 -5.7; 947 -5.5; 1042 -5.7; 1146 -6.5; 1261 -7.4; 1387 -8.1; 1526 -8.3; 1678 -8.0; 1846 -7.4; 2031 -6.8; 2234 -6.0; 2457 -5.2; 2703 -4.3; 2973 -3.6; 3270 -3.1; 3597 -3.1; 3957 -3.2; 4353 -3.2; 4788 -3.5; 5267 -3.7; 5793 -0.5; 6373 -0.6; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -9.5; 15026 -12.6; 16529 -11.6; 18182 -10.3; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 custom sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 custom sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.3  | 2.8 dB  |
| Peaking | 230 Hz   | 0.46 | -2.7 dB |
| Peaking | 5973 Hz  | 0.99 | 6.6 dB  |
| Peaking | 12051 Hz | 1.64 | 7.8 dB  |
| Peaking | 14007 Hz | 0.49 | -9.2 dB |
| Peaking | 987 Hz   | 1.92 | 2.4 dB  |
| Peaking | 1491 Hz  | 1.3  | -3.4 dB |
| Peaking | 4529 Hz  | 0.73 | 2.7 dB  |
| Peaking | 4920 Hz  | 3.45 | -4.1 dB |
| Peaking | 7719 Hz  | 4.39 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -7.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20custom%20sample%201/64%20Audio%20N8%20custom%20sample%201.png)
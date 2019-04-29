# 64 Audio N8 M15 custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.6; 25 -9.8; 28 -10.0; 31 -10.1; 34 -10.1; 37 -10.2; 41 -10.2; 45 -10.3; 49 -10.3; 54 -10.3; 60 -10.4; 66 -10.5; 72 -10.6; 79 -10.7; 87 -10.9; 96 -11.0; 106 -10.9; 116 -11.1; 128 -11.1; 141 -11.0; 155 -10.9; 170 -10.8; 187 -10.7; 206 -10.5; 227 -10.2; 249 -10.0; 274 -9.8; 302 -9.5; 332 -9.2; 365 -8.9; 402 -8.7; 442 -8.4; 486 -8.1; 535 -7.8; 588 -7.4; 647 -7.0; 712 -6.5; 783 -5.9; 861 -5.5; 947 -5.3; 1042 -5.4; 1146 -6.1; 1261 -7.0; 1387 -7.7; 1526 -8.0; 1678 -7.8; 1846 -7.4; 2031 -7.0; 2234 -6.5; 2457 -5.6; 2703 -4.5; 2973 -3.5; 3270 -2.8; 3597 -2.6; 3957 -2.9; 4353 -3.1; 4788 -3.6; 5267 -2.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.8; 16529 -9.2; 18182 -11.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 49 Hz    | 0.27 | -3.6 dB |
| Peaking | 194 Hz   | 0.68 | -2.5 dB |
| Peaking | 3450 Hz  | 2.07 | 4.5 dB  |
| Peaking | 5945 Hz  | 2.38 | 6.9 dB  |
| Peaking | 18781 Hz | 0.03 | -1.4 dB |
| Peaking | 961 Hz   | 2.55 | 2.1 dB  |
| Peaking | 1538 Hz  | 2.22 | -1.6 dB |
| Peaking | 7751 Hz  | 3.8  | -1.5 dB |
| Peaking | 17205 Hz | 0.31 | 2.1 dB  |
| Peaking | 17941 Hz | 1.53 | -5.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15%20custom/64%20Audio%20N8%20M15%20custom.png)
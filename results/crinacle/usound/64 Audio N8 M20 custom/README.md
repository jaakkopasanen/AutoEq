# 64 Audio N8 M20 custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.7; 25 -9.7; 28 -9.7; 31 -9.5; 34 -9.4; 37 -9.2; 41 -9.1; 45 -9.0; 49 -8.9; 54 -8.7; 60 -8.5; 66 -8.5; 72 -8.5; 79 -8.5; 87 -8.5; 96 -8.6; 106 -8.7; 116 -8.8; 128 -8.8; 141 -9.0; 155 -9.0; 170 -9.0; 187 -9.0; 206 -9.1; 227 -9.0; 249 -8.9; 274 -8.8; 302 -8.7; 332 -8.6; 365 -8.5; 402 -8.3; 442 -8.1; 486 -7.9; 535 -7.6; 588 -7.3; 647 -7.0; 712 -6.5; 783 -6.0; 861 -5.6; 947 -5.5; 1042 -5.7; 1146 -6.4; 1261 -7.4; 1387 -8.0; 1526 -8.2; 1678 -7.8; 1846 -7.3; 2031 -6.6; 2234 -5.9; 2457 -5.1; 2703 -4.2; 2973 -3.6; 3270 -3.2; 3597 -3.1; 3957 -3.2; 4353 -3.1; 4788 -3.4; 5267 -3.6; 5793 -0.5; 6373 -0.7; 7010 -3.6; 7711 -5.9; 8482 -6.1; 9330 -6.1; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -9.5; 15026 -12.6; 16529 -11.4; 18182 -10.1; 20000 -8.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M20 custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M20 custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.43 | -3.5 dB |
| Peaking | 210 Hz   | 0.47 | -2.8 dB |
| Peaking | 5882 Hz  | 0.95 | 6.7 dB  |
| Peaking | 12182 Hz | 1.65 | 7.9 dB  |
| Peaking | 13741 Hz | 0.51 | -9.3 dB |
| Peaking | 981 Hz   | 1.59 | 3.6 dB  |
| Peaking | 1486 Hz  | 0.84 | -4.4 dB |
| Peaking | 3268 Hz  | 0.73 | 3.5 dB  |
| Peaking | 5462 Hz  | 1.56 | -5.1 dB |
| Peaking | 6095 Hz  | 4.44 | 5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -7.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M20%20custom/64%20Audio%20N8%20M20%20custom.png)
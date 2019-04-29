# 64 Audio N8 M15 custom sample 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.9; 25 -11.0; 28 -11.2; 31 -11.3; 34 -11.3; 37 -11.4; 41 -11.4; 45 -11.3; 49 -11.3; 54 -11.3; 60 -11.4; 66 -11.4; 72 -11.4; 79 -11.5; 87 -11.6; 96 -11.6; 106 -11.6; 116 -11.6; 128 -11.5; 141 -11.4; 155 -11.2; 170 -11.1; 187 -10.9; 206 -10.6; 227 -10.4; 249 -10.1; 274 -9.8; 302 -9.5; 332 -9.2; 365 -8.9; 402 -8.6; 442 -8.4; 486 -8.0; 535 -7.7; 588 -7.3; 647 -6.9; 712 -6.4; 783 -5.9; 861 -5.5; 947 -5.2; 1042 -5.4; 1146 -6.0; 1261 -6.9; 1387 -7.7; 1526 -7.9; 1678 -7.7; 1846 -7.4; 2031 -7.1; 2234 -6.6; 2457 -5.7; 2703 -4.6; 2973 -3.6; 3270 -3.0; 3597 -2.8; 3957 -3.0; 4353 -3.0; 4788 -3.6; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -6.5; 16529 -8.1; 18182 -11.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 custom sample 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 custom sample 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.25 | -4.7 dB |
| Peaking | 187 Hz   | 0.68 | -2.5 dB |
| Peaking | 3486 Hz  | 2.08 | 4.2 dB  |
| Peaking | 5910 Hz  | 2.54 | 6.8 dB  |
| Peaking | 17152 Hz | 0.05 | -1.2 dB |
| Peaking | 964 Hz   | 2.44 | 2.1 dB  |
| Peaking | 1543 Hz  | 2.24 | -1.6 dB |
| Peaking | 7829 Hz  | 4.69 | -1.2 dB |
| Peaking | 17966 Hz | 1.63 | -6.4 dB |
| Peaking | 18388 Hz | 0.34 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15%20custom%20sample%205/64%20Audio%20N8%20M15%20custom%20sample%205.png)
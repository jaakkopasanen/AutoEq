# 64 Audio N8 modded
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -9.9; 25 -9.8; 28 -9.5; 31 -9.3; 34 -9.0; 37 -8.7; 41 -8.3; 45 -8.1; 49 -7.9; 54 -7.7; 60 -7.4; 66 -7.2; 72 -7.2; 79 -7.2; 87 -7.3; 96 -7.4; 106 -7.5; 116 -7.7; 128 -7.8; 141 -7.9; 155 -8.0; 170 -8.1; 187 -8.3; 206 -8.4; 227 -8.5; 249 -8.5; 274 -8.5; 302 -8.6; 332 -8.6; 365 -8.5; 402 -8.4; 442 -8.4; 486 -8.2; 535 -8.0; 588 -7.8; 647 -7.5; 712 -7.1; 783 -6.7; 861 -6.3; 947 -6.2; 1042 -6.4; 1146 -7.2; 1261 -8.1; 1387 -9.0; 1526 -9.3; 1678 -9.2; 1846 -8.9; 2031 -8.4; 2234 -7.7; 2457 -6.7; 2703 -5.5; 2973 -4.4; 3270 -3.7; 3597 -3.4; 3957 -3.7; 4353 -4.1; 4788 -4.7; 5267 -2.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.3; 15026 -8.7; 16529 -10.7; 18182 -15.3; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 modded GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 modded ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.03 | -1.7 dB  |
| Peaking | 1726 Hz  | 2.11 | -3.1 dB  |
| Peaking | 3436 Hz  | 2.25 | 3.2 dB   |
| Peaking | 5948 Hz  | 3.4  | 6.5 dB   |
| Peaking | 18968 Hz | 0.89 | -10.1 dB |
| Peaking | 21 Hz    | 0.68 | -2.1 dB  |
| Peaking | 71 Hz    | 0.61 | 1.6 dB   |
| Peaking | 403 Hz   | 0.31 | -0.9 dB  |
| Peaking | 892 Hz   | 2.18 | 1.9 dB   |
| Peaking | 12122 Hz | 5.22 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -5.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20modded/64%20Audio%20N8%20modded.png)
# 64 Audio N8 custom sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.4; 25 -5.7; 28 -6.1; 31 -6.3; 34 -6.5; 37 -6.6; 41 -6.8; 45 -7.0; 49 -7.1; 54 -7.3; 60 -7.5; 66 -7.7; 72 -7.9; 79 -8.2; 87 -8.4; 96 -8.7; 106 -9.0; 116 -9.2; 128 -9.4; 141 -9.7; 155 -9.9; 170 -10.0; 187 -10.1; 206 -10.1; 227 -10.1; 249 -10.1; 274 -10.1; 302 -9.9; 332 -9.8; 365 -9.5; 402 -9.4; 442 -9.2; 486 -8.9; 535 -8.6; 588 -8.3; 647 -8.0; 712 -7.5; 783 -7.1; 861 -6.8; 947 -6.6; 1042 -6.9; 1146 -7.6; 1261 -8.3; 1387 -8.6; 1526 -8.5; 1678 -8.2; 1846 -7.5; 2031 -6.6; 2234 -5.2; 2457 -3.8; 2703 -2.5; 2973 -1.6; 3270 -1.2; 3597 -1.4; 3957 -2.0; 4353 -2.4; 4788 -3.0; 5267 -3.2; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.9; 13660 -18.8; 15026 -29.3; 16529 -30.8; 18182 -27.2; 20000 -20.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 custom sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 custom sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 256 Hz   | 0.39 | -4.1 dB  |
| Peaking | 1589 Hz  | 1.46 | -5.7 dB  |
| Peaking | 5875 Hz  | 0.31 | 17.1 dB  |
| Peaking | 12134 Hz | 1.77 | 14.7 dB  |
| Peaking | 15496 Hz | 0.37 | -35.5 dB |
| Peaking | 20 Hz    | 1.58 | 1.5 dB   |
| Peaking | 3146 Hz  | 3.74 | 1.4 dB   |
| Peaking | 5076 Hz  | 6.07 | -1.6 dB  |
| Peaking | 5786 Hz  | 1.43 | -2.1 dB  |
| Peaking | 6068 Hz  | 4.02 | 4.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB   |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 16000 Hz | 1.41 | -30.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20custom%20sample%201/64%20Audio%20N8%20custom%20sample%201.png)
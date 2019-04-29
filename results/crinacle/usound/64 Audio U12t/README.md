# 64 Audio U12t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.9; 25 -6.1; 28 -6.4; 31 -6.5; 34 -6.6; 37 -6.7; 41 -6.7; 45 -6.8; 49 -6.8; 54 -6.7; 60 -6.6; 66 -6.6; 72 -6.6; 79 -6.7; 87 -6.7; 96 -6.7; 106 -6.7; 116 -6.6; 128 -6.6; 141 -6.5; 155 -6.4; 170 -6.2; 187 -6.1; 206 -5.9; 227 -5.8; 249 -5.6; 274 -5.6; 302 -5.5; 332 -5.6; 365 -5.7; 402 -5.9; 442 -6.0; 486 -6.2; 535 -6.2; 588 -6.2; 647 -5.9; 712 -5.5; 783 -4.9; 861 -4.4; 947 -4.1; 1042 -4.2; 1146 -4.7; 1261 -5.4; 1387 -5.9; 1526 -6.1; 1678 -6.2; 1846 -6.3; 2031 -6.8; 2234 -6.6; 2457 -4.9; 2703 -2.5; 2973 -1.1; 3270 -0.5; 3597 -1.1; 3957 -2.3; 4353 -3.2; 4788 -4.5; 5267 -1.8; 5793 -1.2; 6373 -3.5; 7010 -3.8; 7711 -4.3; 8482 -4.6; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -7.1; 15026 -12.2; 16529 -18.1; 18182 -20.4; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio U12t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio U12t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 70 Hz    | 0.14 | -1.9 dB  |
| Peaking | 2200 Hz  | 1.34 | -9.1 dB  |
| Peaking | 2749 Hz  | 0.95 | 8.9 dB   |
| Peaking | 12426 Hz | 1.41 | 4.6 dB   |
| Peaking | 17550 Hz | 0.92 | -17.7 dB |
| Peaking | 573 Hz   | 3.35 | -1.0 dB  |
| Peaking | 944 Hz   | 4.62 | 1.1 dB   |
| Peaking | 4762 Hz  | 4.96 | -2.7 dB  |
| Peaking | 5544 Hz  | 5.45 | 3.3 dB   |
| Peaking | 11324 Hz | 5.21 | -0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -13.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20U12t/64%20Audio%20U12t.png)
# 64 Audio N8 M15 pre-RMA
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.4; 25 -10.4; 28 -10.3; 31 -10.1; 34 -10.0; 37 -9.8; 41 -9.7; 45 -9.5; 49 -9.4; 54 -9.2; 60 -9.1; 66 -9.1; 72 -9.1; 79 -9.1; 87 -9.1; 96 -9.2; 106 -9.2; 116 -9.3; 128 -9.4; 141 -9.5; 155 -9.5; 170 -9.6; 187 -9.5; 206 -9.5; 227 -9.5; 249 -9.4; 274 -9.3; 302 -9.1; 332 -9.0; 365 -8.9; 402 -8.7; 442 -8.5; 486 -8.3; 535 -8.0; 588 -7.7; 647 -7.3; 712 -6.8; 783 -6.4; 861 -6.0; 947 -5.7; 1042 -5.9; 1146 -6.6; 1261 -7.5; 1387 -8.1; 1526 -8.2; 1678 -7.9; 1846 -7.3; 2031 -6.7; 2234 -5.9; 2457 -5.1; 2703 -4.2; 2973 -3.5; 3270 -3.1; 3597 -3.0; 3957 -3.1; 4353 -3.1; 4788 -3.5; 5267 -3.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.8; 15026 -13.5; 16529 -15.3; 18182 -12.3; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 pre-RMA GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 pre-RMA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.36 | -3.9 dB  |
| Peaking | 209 Hz   | 0.48 | -2.9 dB  |
| Peaking | 5336 Hz  | 1.01 | 5.1 dB   |
| Peaking | 13382 Hz | 1.95 | 6.6 dB   |
| Peaking | 15826 Hz | 0.87 | -11.1 dB |
| Peaking | 1604 Hz  | 3.22 | -2.3 dB  |
| Peaking | 3073 Hz  | 3.05 | 1.4 dB   |
| Peaking | 5041 Hz  | 3.82 | -4.0 dB  |
| Peaking | 6074 Hz  | 1.96 | 3.9 dB   |
| Peaking | 7544 Hz  | 3.35 | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -8.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15%20pre-RMA/64%20Audio%20N8%20M15%20pre-RMA.png)
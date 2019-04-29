# Sony MH755 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -6.9; 25 -7.0; 28 -7.0; 31 -6.9; 34 -6.9; 37 -6.8; 41 -6.6; 45 -6.4; 49 -6.2; 54 -6.1; 60 -5.9; 66 -5.8; 72 -5.7; 79 -5.6; 87 -5.5; 96 -5.4; 106 -5.4; 116 -5.2; 128 -5.1; 141 -5.0; 155 -4.8; 170 -4.6; 187 -4.3; 206 -4.1; 227 -3.8; 249 -3.5; 274 -3.3; 302 -3.0; 332 -2.7; 365 -2.5; 402 -2.3; 442 -2.1; 486 -1.9; 535 -1.7; 588 -1.5; 647 -1.2; 712 -1.0; 783 -0.7; 861 -0.5; 947 -0.6; 1042 -1.0; 1146 -1.8; 1261 -2.5; 1387 -2.9; 1526 -2.8; 1678 -2.5; 1846 -2.2; 2031 -2.0; 2234 -2.2; 2457 -2.7; 2703 -3.5; 2973 -4.5; 3270 -4.9; 3597 -4.5; 3957 -3.6; 4353 -2.5; 4788 -1.9; 5267 -1.9; 5793 -2.7; 6373 -5.1; 7010 -6.3; 7711 -3.0; 8482 -2.6; 9330 -2.6; 10263 -2.6; 11289 -2.6; 12418 -2.6; 13660 -2.6; 15026 -4.4; 16529 -5.2; 18182 -2.7; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH755 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH755 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.05 | -3.8 dB |
| Peaking | 478 Hz   | 0.42 | 2.8 dB  |
| Peaking | 3234 Hz  | 3.72 | -2.8 dB |
| Peaking | 6826 Hz  | 7.45 | -4.3 dB |
| Peaking | 16151 Hz | 3.28 | -3.3 dB |
| Peaking | 28 Hz    | 0.81 | -0.7 dB |
| Peaking | 71 Hz    | 1.44 | 0.5 dB  |
| Peaking | 916 Hz   | 3.25 | 1.1 dB  |
| Peaking | 1380 Hz  | 3.46 | -1.3 dB |
| Peaking | 5041 Hz  | 5.54 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MH755%20sample%201/Sony%20MH755%20sample%201.png)
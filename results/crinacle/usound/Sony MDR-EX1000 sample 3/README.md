# Sony MDR-EX1000 sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.9; 41 -1.2; 45 -1.5; 49 -1.8; 54 -2.2; 60 -2.6; 66 -3.0; 72 -3.4; 79 -3.9; 87 -4.3; 96 -4.9; 106 -5.4; 116 -5.8; 128 -6.2; 141 -6.6; 155 -6.9; 170 -7.2; 187 -7.5; 206 -7.7; 227 -7.8; 249 -7.9; 274 -8.0; 302 -8.1; 332 -8.0; 365 -7.9; 402 -7.9; 442 -7.7; 486 -7.5; 535 -7.3; 588 -7.0; 647 -6.5; 712 -5.9; 783 -5.3; 861 -4.8; 947 -4.5; 1042 -4.7; 1146 -5.3; 1261 -6.0; 1387 -6.7; 1526 -7.0; 1678 -7.1; 1846 -7.3; 2031 -7.6; 2234 -7.9; 2457 -8.0; 2703 -7.3; 2973 -5.9; 3270 -4.0; 3597 -2.5; 3957 -1.7; 4353 -2.1; 4788 -3.9; 5267 -8.2; 5793 -11.9; 6373 -7.7; 7010 -5.7; 7711 -8.5; 8482 -8.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.29 | 6.8 dB  |
| Peaking | 557 Hz  | 0.08 | -3.0 dB |
| Peaking | 924 Hz  | 1.11 | 4.7 dB  |
| Peaking | 4055 Hz | 2.01 | 7.4 dB  |
| Peaking | 5687 Hz | 6.79 | -6.7 dB |
| Peaking | 2479 Hz | 5.61 | -1.0 dB |
| Peaking | 6948 Hz | 8.96 | 2.3 dB  |
| Peaking | 8140 Hz | 5.1  | -3.3 dB |
| Peaking | 9064 Hz | 3.17 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MDR-EX1000%20sample%203/Sony%20MDR-EX1000%20sample%203.png)
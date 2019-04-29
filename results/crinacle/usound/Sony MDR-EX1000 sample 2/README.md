# Sony MDR-EX1000 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -0.9; 49 -1.1; 54 -1.5; 60 -1.9; 66 -2.3; 72 -2.7; 79 -3.1; 87 -3.6; 96 -4.1; 106 -4.6; 116 -5.1; 128 -5.5; 141 -6.0; 155 -6.4; 170 -6.6; 187 -6.8; 206 -7.0; 227 -7.1; 249 -7.3; 274 -7.5; 302 -7.5; 332 -7.5; 365 -7.8; 402 -7.5; 442 -7.6; 486 -7.4; 535 -7.3; 588 -7.0; 647 -6.5; 712 -5.9; 783 -5.4; 861 -4.8; 947 -4.5; 1042 -4.9; 1146 -5.6; 1261 -6.5; 1387 -7.1; 1526 -7.3; 1678 -7.5; 1846 -7.8; 2031 -8.2; 2234 -8.8; 2457 -9.1; 2703 -8.4; 2973 -6.8; 3270 -4.9; 3597 -3.5; 3957 -2.9; 4353 -3.5; 4788 -5.9; 5267 -10.6; 5793 -10.7; 6373 -5.9; 7010 -5.1; 7711 -8.4; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.61 | 6.6 dB  |
| Peaking | 961 Hz  | 3.32 | 2.6 dB  |
| Peaking | 2727 Hz | 1.09 | -4.7 dB |
| Peaking | 3783 Hz | 1.63 | 6.9 dB  |
| Peaking | 5472 Hz | 6.13 | -7.2 dB |
| Peaking | 35 Hz   | 2.6  | -0.7 dB |
| Peaking | 75 Hz   | 1.55 | 0.9 dB  |
| Peaking | 294 Hz  | 0.92 | -1.4 dB |
| Peaking | 6805 Hz | 8.24 | 2.6 dB  |
| Peaking | 7960 Hz | 7.39 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MDR-EX1000%20sample%202/Sony%20MDR-EX1000%20sample%202.png)
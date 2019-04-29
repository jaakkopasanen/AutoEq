# Sony MDR-EX1000 sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.1; 31 -1.4; 34 -1.8; 37 -2.0; 41 -2.4; 45 -2.7; 49 -3.0; 54 -3.3; 60 -3.8; 66 -4.2; 72 -4.6; 79 -5.0; 87 -5.5; 96 -6.1; 106 -6.5; 116 -7.0; 128 -7.4; 141 -7.8; 155 -8.1; 170 -8.4; 187 -8.7; 206 -8.8; 227 -9.0; 249 -9.0; 274 -9.2; 302 -9.2; 332 -9.0; 365 -8.8; 402 -8.7; 442 -8.6; 486 -8.3; 535 -8.0; 588 -7.7; 647 -7.1; 712 -6.6; 783 -6.0; 861 -5.5; 947 -5.3; 1042 -5.5; 1146 -6.0; 1261 -6.5; 1387 -6.8; 1526 -6.9; 1678 -7.0; 1846 -7.1; 2031 -7.0; 2234 -6.8; 2457 -6.2; 2703 -5.2; 2973 -3.6; 3270 -1.8; 3597 -0.6; 3957 -0.5; 4353 -1.0; 4788 -3.0; 5267 -7.4; 5793 -10.8; 6373 -6.2; 7010 -4.1; 7711 -6.2; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.2; 13660 -9.9; 15026 -10.8; 16529 -11.5; 18182 -13.6; 20000 -18.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.68 | 5.8 dB   |
| Peaking | 56 Hz    | 1.19 | 1.5 dB   |
| Peaking | 250 Hz   | 0.76 | -3.0 dB  |
| Peaking | 3801 Hz  | 2.83 | 7.1 dB   |
| Peaking | 20110 Hz | 0.45 | -11.0 dB |
| Peaking | 921 Hz   | 4.08 | 1.8 dB   |
| Peaking | 4685 Hz  | 5.51 | 2.8 dB   |
| Peaking | 5757 Hz  | 4.51 | -6.8 dB  |
| Peaking | 6660 Hz  | 3.77 | 1.7 dB   |
| Peaking | 6745 Hz  | 5.17 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -6.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MDR-EX1000%20sample%203/Sony%20MDR-EX1000%20sample%203.png)
# Sony MDR-EX1000 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.4; 31 -1.7; 34 -1.9; 37 -2.1; 41 -2.4; 45 -2.7; 49 -2.9; 54 -3.3; 60 -3.6; 66 -4.0; 72 -4.4; 79 -4.8; 87 -5.3; 96 -5.9; 106 -6.4; 116 -6.8; 128 -7.2; 141 -7.7; 155 -8.1; 170 -8.3; 187 -8.5; 206 -8.8; 227 -8.9; 249 -9.0; 274 -9.2; 302 -9.2; 332 -9.0; 365 -8.9; 402 -8.8; 442 -8.8; 486 -8.5; 535 -8.2; 588 -7.8; 647 -7.3; 712 -6.9; 783 -6.4; 861 -6.0; 947 -6.0; 1042 -6.4; 1146 -7.1; 1261 -7.7; 1387 -7.8; 1526 -7.9; 1678 -8.1; 1846 -8.1; 2031 -7.5; 2234 -6.0; 2457 -3.9; 2703 -1.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -4.2; 5267 -10.1; 5793 -9.0; 6373 -3.6; 7010 -4.0; 7711 -6.2; 8482 -7.7; 9330 -7.5; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -14.4; 16529 -11.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.63 | 5.6 dB  |
| Peaking | 55 Hz    | 0.68 | 2.3 dB  |
| Peaking | 252 Hz   | 0.53 | -2.9 dB |
| Peaking | 3434 Hz  | 2.33 | 7.3 dB  |
| Peaking | 15540 Hz | 3.06 | -9.4 dB |
| Peaking | 1810 Hz  | 2.49 | -2.4 dB |
| Peaking | 2707 Hz  | 6.11 | 2.4 dB  |
| Peaking | 4467 Hz  | 5.29 | 4.0 dB  |
| Peaking | 5446 Hz  | 4.35 | -6.8 dB |
| Peaking | 6543 Hz  | 6.37 | 5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MDR-EX1000%20sample%201/Sony%20MDR-EX1000%20sample%201.png)
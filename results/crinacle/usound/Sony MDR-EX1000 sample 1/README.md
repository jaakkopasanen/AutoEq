# Sony MDR-EX1000 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.8; 37 -1.0; 41 -1.2; 45 -1.5; 49 -1.8; 54 -2.1; 60 -2.4; 66 -2.8; 72 -3.3; 79 -3.7; 87 -4.1; 96 -4.7; 106 -5.3; 116 -5.6; 128 -6.0; 141 -6.6; 155 -6.9; 170 -7.1; 187 -7.4; 206 -7.6; 227 -7.8; 249 -7.8; 274 -8.0; 302 -8.1; 332 -8.1; 365 -8.0; 402 -7.9; 442 -8.0; 486 -7.7; 535 -7.4; 588 -7.1; 647 -6.7; 712 -6.2; 783 -5.7; 861 -5.3; 947 -5.2; 1042 -5.6; 1146 -6.4; 1261 -7.2; 1387 -7.6; 1526 -8.0; 1678 -8.3; 1846 -8.3; 2031 -8.1; 2234 -7.2; 2457 -5.6; 2703 -4.0; 2973 -2.5; 3270 -1.5; 3597 -1.2; 3957 -1.5; 4353 -2.4; 4788 -5.1; 5267 -11.0; 5793 -10.1; 6373 -5.1; 7010 -4.7; 7711 -8.7; 8482 -9.4; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 31 Hz   |  0.68 | 6.5 dB   |
| Peaking | 1975 Hz |  1.5  | -4.9 dB  |
| Peaking | 3810 Hz |  0.78 | 7.1 dB   |
| Peaking | 5396 Hz |  4.97 | -10.6 dB |
| Peaking | 8278 Hz |  4.91 | -5.2 dB  |
| Peaking | 34 Hz   |  1.01 | -3.6 dB  |
| Peaking | 37 Hz   |  0.33 | 3.2 dB   |
| Peaking | 248 Hz  |  0.37 | -2.2 dB  |
| Peaking | 870 Hz  |  2.1  | 2.2 dB   |
| Peaking | 6820 Hz | 12.42 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MDR-EX1000%20sample%201/Sony%20MDR-EX1000%20sample%201.png)
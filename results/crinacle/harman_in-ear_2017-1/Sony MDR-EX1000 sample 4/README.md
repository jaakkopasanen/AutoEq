# Sony MDR-EX1000 sample 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.7; 34 -0.9; 37 -1.2; 41 -1.5; 45 -1.8; 49 -2.0; 54 -2.3; 60 -2.6; 66 -3.0; 72 -3.4; 79 -3.8; 87 -4.4; 96 -4.8; 106 -5.4; 116 -5.8; 128 -6.3; 141 -6.7; 155 -7.1; 170 -7.4; 187 -7.7; 206 -7.8; 227 -8.0; 249 -8.2; 274 -8.3; 302 -8.4; 332 -8.4; 365 -8.3; 402 -8.2; 442 -8.2; 486 -8.1; 535 -7.8; 588 -7.5; 647 -7.1; 712 -6.7; 783 -6.2; 861 -5.7; 947 -5.6; 1042 -5.8; 1146 -6.4; 1261 -7.1; 1387 -7.5; 1526 -7.7; 1678 -7.9; 1846 -8.2; 2031 -8.6; 2234 -8.6; 2457 -8.0; 2703 -6.3; 2973 -4.0; 3270 -2.0; 3597 -1.0; 3957 -0.9; 4353 -2.0; 4788 -4.7; 5267 -10.0; 5793 -10.2; 6373 -4.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.1; 15026 -10.1; 16529 -11.1; 18182 -11.8; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 sample 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 sample 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.99 | 6.2 dB  |
| Peaking | 58 Hz    | 1.72 | 2.8 dB  |
| Peaking | 2373 Hz  | 1.31 | -5.4 dB |
| Peaking | 3622 Hz  | 1.25 | 8.3 dB  |
| Peaking | 5475 Hz  | 6.5  | -8.6 dB |
| Peaking | 95 Hz    | 1.84 | 1.1 dB  |
| Peaking | 322 Hz   | 0.52 | -2.0 dB |
| Peaking | 906 Hz   | 2.15 | 1.9 dB  |
| Peaking | 6710 Hz  | 9.42 | 3.5 dB  |
| Peaking | 19925 Hz | 0.43 | -8.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MDR-EX1000%20sample%204/Sony%20MDR-EX1000%20sample%204.png)
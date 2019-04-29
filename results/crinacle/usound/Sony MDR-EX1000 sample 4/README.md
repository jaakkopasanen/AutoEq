# Sony MDR-EX1000 sample 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.8; 54 -1.1; 60 -1.5; 66 -1.8; 72 -2.2; 79 -2.7; 87 -3.2; 96 -3.7; 106 -4.2; 116 -4.7; 128 -5.1; 141 -5.5; 155 -5.9; 170 -6.2; 187 -6.5; 206 -6.7; 227 -6.9; 249 -7.0; 274 -7.2; 302 -7.3; 332 -7.4; 365 -7.4; 402 -7.4; 442 -7.4; 486 -7.3; 535 -7.1; 588 -6.9; 647 -6.5; 712 -6.0; 783 -5.5; 861 -5.0; 947 -4.8; 1042 -4.9; 1146 -5.7; 1261 -6.6; 1387 -7.3; 1526 -7.8; 1678 -8.0; 1846 -8.4; 2031 -9.1; 2234 -9.8; 2457 -9.8; 2703 -8.4; 2973 -6.2; 3270 -4.3; 3597 -3.0; 3957 -2.5; 4353 -3.2; 4788 -5.6; 5267 -10.9; 5793 -11.3; 6373 -5.8; 7010 -4.3; 7711 -7.6; 8482 -8.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 sample 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 sample 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.56 | 6.6 dB  |
| Peaking | 982 Hz  | 3.08 | 2.4 dB  |
| Peaking | 2529 Hz | 1.2  | -6.1 dB |
| Peaking | 3683 Hz | 1.37 | 7.4 dB  |
| Peaking | 5480 Hz | 6.12 | -8.6 dB |
| Peaking | 37 Hz   | 2.75 | -0.7 dB |
| Peaking | 75 Hz   | 1.57 | 0.8 dB  |
| Peaking | 300 Hz  | 0.97 | -1.2 dB |
| Peaking | 6895 Hz | 7.82 | 2.9 dB  |
| Peaking | 8135 Hz | 6.58 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MDR-EX1000%20sample%204/Sony%20MDR-EX1000%20sample%204.png)
# Sony MDR-EX1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.9; 45 -1.1; 49 -1.4; 54 -1.7; 60 -2.1; 66 -2.5; 72 -2.9; 79 -3.3; 87 -3.8; 96 -4.4; 106 -4.9; 116 -5.3; 128 -5.7; 141 -6.2; 155 -6.5; 170 -6.8; 187 -7.1; 206 -7.2; 227 -7.4; 249 -7.5; 274 -7.7; 302 -7.8; 332 -7.8; 365 -7.8; 402 -7.7; 442 -7.7; 486 -7.5; 535 -7.3; 588 -7.0; 647 -6.5; 712 -6.0; 783 -5.5; 861 -5.0; 947 -4.8; 1042 -5.0; 1146 -5.7; 1261 -6.6; 1387 -7.2; 1526 -7.5; 1678 -7.7; 1846 -8.0; 2031 -8.3; 2234 -8.4; 2457 -8.1; 2703 -7.0; 2973 -5.3; 3270 -3.7; 3597 -2.5; 3957 -2.2; 4353 -2.8; 4788 -5.1; 5267 -10.2; 5793 -11.0; 6373 -6.1; 7010 -4.9; 7711 -8.3; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.44 | 6.3 dB  |
| Peaking | 934 Hz  | 0.73 | 8.6 dB  |
| Peaking | 1235 Hz | 0.28 | -7.5 dB |
| Peaking | 3945 Hz | 1.38 | 8.3 dB  |
| Peaking | 5509 Hz | 6.26 | -7.5 dB |
| Peaking | 6042 Hz | 4.22 | -1.6 dB |
| Peaking | 6752 Hz | 4.54 | 3.5 dB  |
| Peaking | 7800 Hz | 4.47 | -0.8 dB |
| Peaking | 8128 Hz | 5.46 | -3.1 dB |
| Peaking | 8868 Hz | 2.41 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MDR-EX1000/Sony%20MDR-EX1000.png)
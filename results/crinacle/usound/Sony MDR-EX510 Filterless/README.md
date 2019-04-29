# Sony MDR-EX510 Filterless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.7; 31 -2.1; 34 -2.5; 37 -2.8; 41 -3.1; 45 -3.3; 49 -3.6; 54 -3.9; 60 -4.2; 66 -4.6; 72 -4.9; 79 -5.3; 87 -5.7; 96 -6.2; 106 -6.5; 116 -6.9; 128 -7.3; 141 -7.5; 155 -7.7; 170 -7.8; 187 -7.9; 206 -7.9; 227 -7.8; 249 -7.7; 274 -7.6; 302 -7.3; 332 -7.1; 365 -6.8; 402 -6.6; 442 -6.3; 486 -6.0; 535 -5.7; 588 -5.3; 647 -4.8; 712 -4.3; 783 -3.8; 861 -3.4; 947 -3.2; 1042 -3.3; 1146 -3.8; 1261 -4.4; 1387 -4.9; 1526 -5.1; 1678 -5.0; 1846 -5.0; 2031 -5.6; 2234 -6.3; 2457 -6.6; 2703 -6.8; 2973 -6.6; 3270 -5.5; 3597 -4.7; 3957 -4.5; 4353 -5.1; 4788 -6.9; 5267 -9.7; 5793 -8.8; 6373 -5.2; 7010 -4.2; 7711 -7.0; 8482 -7.3; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX510 Filterless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX510 Filterless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.7  | 5.6 dB  |
| Peaking | 55 Hz   | 0.74 | 1.4 dB  |
| Peaking | 182 Hz  | 0.61 | -2.4 dB |
| Peaking | 921 Hz  | 1.37 | 3.0 dB  |
| Peaking | 5436 Hz | 8.06 | -4.7 dB |
| Peaking | 2793 Hz | 2.78 | -2.1 dB |
| Peaking | 4028 Hz | 1.6  | 2.8 dB  |
| Peaking | 5046 Hz | 2.28 | -2.2 dB |
| Peaking | 6860 Hz | 5.8  | 2.7 dB  |
| Peaking | 8076 Hz | 7.2  | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MDR-EX510%20Filterless/Sony%20MDR-EX510%20Filterless.png)
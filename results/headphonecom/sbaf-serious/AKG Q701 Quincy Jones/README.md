# AKG Q701 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.3; 31 -2.0; 34 -2.7; 37 -3.3; 41 -3.9; 45 -4.5; 49 -5.1; 54 -5.8; 60 -6.5; 66 -6.9; 72 -7.1; 79 -6.9; 87 -7.9; 96 -8.8; 106 -9.2; 116 -8.7; 128 -9.6; 141 -10.1; 155 -10.4; 170 -10.3; 187 -10.6; 206 -10.7; 227 -10.6; 249 -10.6; 274 -10.5; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.5; 442 -9.1; 486 -8.9; 535 -8.5; 588 -7.3; 647 -7.6; 712 -7.4; 783 -7.2; 861 -7.2; 947 -6.7; 1042 -6.3; 1146 -6.2; 1261 -6.5; 1387 -7.6; 1526 -9.0; 1678 -9.7; 1846 -11.3; 2031 -12.1; 2234 -10.5; 2457 -9.3; 2703 -7.5; 2973 -6.1; 3270 -5.0; 3597 -4.5; 3957 -6.0; 4353 -7.9; 4788 -7.7; 5267 -9.2; 5793 -12.4; 6373 -13.0; 7010 -11.0; 7711 -11.2; 8482 -9.9; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.9  | 6.2 dB  |
| Peaking | 202 Hz  | 0.59 | -4.4 dB |
| Peaking | 2012 Hz | 2.85 | -5.8 dB |
| Peaking | 3489 Hz | 2.94 | 3.3 dB  |
| Peaking | 6406 Hz | 2.03 | -6.6 dB |
| Peaking | 423 Hz  | 3.46 | -0.6 dB |
| Peaking | 1161 Hz | 2.37 | 1.4 dB  |
| Peaking | 1525 Hz | 4.67 | -1.2 dB |
| Peaking | 8250 Hz | 4.87 | -2.9 dB |
| Peaking | 9151 Hz | 1.63 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20Q701%20Quincy%20Jones/AKG%20Q701%20Quincy%20Jones.png)
# JBL E65BTNC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.3; 25 -12.1; 28 -11.8; 31 -11.6; 34 -11.3; 37 -11.1; 41 -10.8; 45 -10.5; 49 -10.3; 54 -10.1; 60 -9.9; 66 -9.7; 72 -9.4; 79 -9.2; 87 -9.1; 96 -9.4; 106 -9.8; 116 -10.1; 128 -10.1; 141 -9.6; 155 -9.0; 170 -8.2; 187 -7.3; 206 -6.3; 227 -5.5; 249 -4.6; 274 -4.0; 302 -3.7; 332 -3.7; 365 -3.9; 402 -4.1; 442 -4.4; 486 -4.4; 535 -4.2; 588 -4.2; 647 -4.1; 712 -4.2; 783 -4.7; 861 -5.1; 947 -5.9; 1042 -6.7; 1146 -6.9; 1261 -6.3; 1387 -6.2; 1526 -6.6; 1678 -5.5; 1846 -4.9; 2031 -4.3; 2234 -3.5; 2457 -2.8; 2703 -2.1; 2973 -0.5; 3270 -4.2; 3597 -8.9; 3957 -7.5; 4353 -4.9; 4788 -2.4; 5267 -3.0; 5793 -6.2; 6373 -6.8; 7010 -9.8; 7711 -9.2; 8482 -5.8; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -6.3; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E65BTNC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E65BTNC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.74 | -6.6 dB |
| Peaking | 64 Hz   | 1.3  | -2.4 dB |
| Peaking | 127 Hz  | 2.36 | -4.0 dB |
| Peaking | 2805 Hz | 4.56 | 4.9 dB  |
| Peaking | 7312 Hz | 6.1  | -5.2 dB |
| Peaking | 307 Hz  | 3.05 | 1.8 dB  |
| Peaking | 1087 Hz | 0.59 | 4.3 dB  |
| Peaking | 1175 Hz | 1.2  | -5.6 dB |
| Peaking | 3696 Hz | 6.52 | -5.1 dB |
| Peaking | 4948 Hz | 7.51 | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E65BTNC/JBL%20E65BTNC.png)
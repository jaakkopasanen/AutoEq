# JBL E65BTNC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.9; 23 -12.7; 25 -12.5; 28 -12.2; 31 -12.0; 34 -11.7; 37 -11.4; 41 -11.1; 45 -10.8; 49 -10.6; 54 -10.4; 60 -10.2; 66 -10.1; 72 -9.8; 79 -9.6; 87 -9.5; 96 -9.8; 106 -10.3; 116 -10.5; 128 -10.5; 141 -10.1; 155 -9.4; 170 -8.6; 187 -7.7; 206 -6.7; 227 -5.8; 249 -4.9; 274 -4.3; 302 -3.9; 332 -3.9; 365 -4.1; 402 -4.3; 442 -4.6; 486 -4.5; 535 -4.3; 588 -4.2; 647 -4.1; 712 -4.2; 783 -4.7; 861 -5.2; 947 -5.9; 1042 -6.7; 1146 -7.0; 1261 -6.3; 1387 -6.2; 1526 -6.6; 1678 -5.5; 1846 -4.8; 2031 -4.0; 2234 -2.8; 2457 -2.0; 2703 -1.9; 2973 -0.5; 3270 -4.5; 3597 -9.4; 3957 -8.0; 4353 -5.5; 4788 -2.1; 5267 -2.7; 5793 -6.3; 6373 -8.0; 7010 -9.7; 7711 -8.7; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -7.3; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E65BTNC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E65BTNC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.78 | -6.3 dB |
| Peaking | 65 Hz   | 1.43 | -2.2 dB |
| Peaking | 126 Hz  | 2.65 | -3.8 dB |
| Peaking | 2599 Hz | 3    | 5.4 dB  |
| Peaking | 4973 Hz | 9.75 | 5.5 dB  |
| Peaking | 319 Hz  | 2.18 | 2.8 dB  |
| Peaking | 618 Hz  | 2.06 | 2.2 dB  |
| Peaking | 3067 Hz | 7.44 | 3.8 dB  |
| Peaking | 3598 Hz | 6    | -5.0 dB |
| Peaking | 7149 Hz | 5.43 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E65BTNC/JBL%20E65BTNC.png)
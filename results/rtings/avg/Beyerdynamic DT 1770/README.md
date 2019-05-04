# Beyerdynamic DT 1770
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.4; 25 -4.6; 28 -4.9; 31 -5.2; 34 -5.4; 37 -5.5; 41 -5.5; 45 -5.5; 49 -5.5; 54 -5.6; 60 -5.7; 66 -5.8; 72 -6.0; 79 -6.3; 87 -6.6; 96 -7.1; 106 -7.4; 116 -7.6; 128 -7.6; 141 -7.3; 155 -6.7; 170 -5.7; 187 -4.2; 206 -2.7; 227 -1.7; 249 -2.1; 274 -3.7; 302 -5.4; 332 -6.6; 365 -7.2; 402 -7.3; 442 -7.2; 486 -7.3; 535 -7.3; 588 -7.3; 647 -7.2; 712 -7.1; 783 -6.8; 861 -6.4; 947 -6.1; 1042 -5.9; 1146 -5.7; 1261 -5.7; 1387 -5.9; 1526 -6.1; 1678 -6.2; 1846 -5.7; 2031 -5.4; 2234 -6.3; 2457 -5.7; 2703 -4.5; 2973 -3.1; 3270 -2.4; 3597 -2.4; 3957 -0.5; 4353 -2.4; 4788 -7.6; 5267 -7.6; 5793 -7.9; 6373 -9.2; 7010 -8.8; 7711 -9.9; 8482 -9.6; 9330 -6.7; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1770 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1770 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 15 Hz   |  0.15 | 1.4 dB  |
| Peaking | 211 Hz  |  0.54 | -5.1 dB |
| Peaking | 228 Hz  |  1.75 | 9.3 dB  |
| Peaking | 3853 Hz |  2.11 | 6.9 dB  |
| Peaking | 6191 Hz |  1.15 | -4.5 dB |
| Peaking | 1120 Hz |  4    | 0.7 dB  |
| Peaking | 4200 Hz | 12.74 | 2.1 dB  |
| Peaking | 4766 Hz |  7.43 | -2.6 dB |
| Peaking | 8220 Hz |  3.5  | -5.0 dB |
| Peaking | 8525 Hz |  1.44 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%201770/Beyerdynamic%20DT%201770.png)
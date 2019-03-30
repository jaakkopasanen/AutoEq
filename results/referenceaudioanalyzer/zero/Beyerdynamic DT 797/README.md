# Beyerdynamic DT 797
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.6; 25 -3.4; 28 -4.4; 31 -5.2; 34 -5.8; 37 -6.3; 41 -6.7; 45 -6.8; 49 -6.6; 54 -6.4; 60 -6.3; 66 -6.0; 72 -5.5; 79 -5.4; 87 -6.2; 96 -6.8; 106 -7.1; 116 -7.3; 128 -7.3; 141 -6.9; 155 -5.9; 170 -4.7; 187 -3.8; 206 -3.5; 227 -3.9; 249 -4.1; 274 -4.1; 302 -4.0; 332 -3.8; 365 -3.7; 402 -3.5; 442 -3.3; 486 -3.0; 535 -2.7; 588 -2.3; 647 -2.0; 712 -1.6; 783 -1.3; 861 -1.1; 947 -1.2; 1042 -1.1; 1146 -0.8; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.8; 1846 -1.4; 2031 -2.2; 2234 -3.6; 2457 -5.1; 2703 -6.1; 2973 -6.2; 3270 -5.7; 3597 -5.7; 3957 -5.7; 4353 -4.9; 4788 -3.6; 5267 -2.8; 5793 -2.5; 6373 -2.7; 7010 -5.8; 7711 -9.7; 8482 -12.1; 9330 -12.4; 10263 -11.9; 11289 -11.9; 12418 -12.4; 13660 -11.5; 15026 -8.1; 16529 -4.3; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 797 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 797 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.44 | 3.9 dB  |
| Peaking | 43 Hz    | 1.06 | -3.0 dB |
| Peaking | 119 Hz   | 2.3  | -3.3 dB |
| Peaking | 1107 Hz  | 0.92 | 3.8 dB  |
| Peaking | 11231 Hz | 1.08 | -9.3 dB |
| Peaking | 1858 Hz  | 1.79 | 3.4 dB  |
| Peaking | 2740 Hz  | 0.91 | -3.8 dB |
| Peaking | 6145 Hz  | 1.57 | 5.5 dB  |
| Peaking | 8156 Hz  | 3.15 | -5.2 dB |
| Peaking | 17146 Hz | 3.65 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20797/Beyerdynamic%20DT%20797.png)
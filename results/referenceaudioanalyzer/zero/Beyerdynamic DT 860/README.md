# Beyerdynamic DT 860
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.7; 31 -2.1; 34 -2.5; 37 -2.8; 41 -3.1; 45 -3.3; 49 -3.4; 54 -3.5; 60 -3.4; 66 -3.5; 72 -3.7; 79 -4.1; 87 -4.4; 96 -4.7; 106 -4.7; 116 -4.7; 128 -4.9; 141 -5.1; 155 -5.0; 170 -4.8; 187 -4.7; 206 -4.6; 227 -4.4; 249 -4.3; 274 -4.1; 302 -4.0; 332 -3.8; 365 -3.8; 402 -3.6; 442 -3.7; 486 -3.8; 535 -3.8; 588 -3.5; 647 -3.4; 712 -3.4; 783 -3.6; 861 -3.8; 947 -3.7; 1042 -3.8; 1146 -3.8; 1261 -3.8; 1387 -3.8; 1526 -3.8; 1678 -4.2; 1846 -4.8; 2031 -5.3; 2234 -5.7; 2457 -6.2; 2703 -7.0; 2973 -7.6; 3270 -7.5; 3597 -6.4; 3957 -5.7; 4353 -7.3; 4788 -9.1; 5267 -11.9; 5793 -16.1; 6373 -18.2; 7010 -16.6; 7711 -9.7; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 860 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 860 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 0.69 | 5.1 dB   |
| Peaking | 63 Hz   | 2.13 | 1.1 dB   |
| Peaking | 2037 Hz | 0.12 | 2.4 dB   |
| Peaking | 2797 Hz | 1.78 | -3.3 dB  |
| Peaking | 6325 Hz | 2.66 | -15.7 dB |
| Peaking | 3935 Hz | 7.58 | 1.7 dB   |
| Peaking | 7244 Hz | 7.36 | -4.5 dB  |
| Peaking | 8044 Hz | 2.33 | 4.2 dB   |
| Peaking | 8690 Hz | 0.46 | -1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | 1.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20860/Beyerdynamic%20DT%20860.png)
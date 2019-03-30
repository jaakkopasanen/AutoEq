# Beyerdynamic DT 660
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.2; 45 -1.6; 49 -1.7; 54 -1.6; 60 -1.3; 66 -0.7; 72 -0.5; 79 -0.5; 87 -0.9; 96 -2.0; 106 -2.2; 116 -2.3; 128 -2.5; 141 -2.8; 155 -3.0; 170 -3.2; 187 -3.2; 206 -3.2; 227 -3.5; 249 -3.6; 274 -4.0; 302 -4.2; 332 -4.4; 365 -4.5; 402 -4.5; 442 -4.1; 486 -3.6; 535 -3.5; 588 -3.5; 647 -3.8; 712 -3.9; 783 -4.1; 861 -4.3; 947 -4.5; 1042 -4.7; 1146 -5.0; 1261 -5.2; 1387 -5.4; 1526 -5.6; 1678 -5.9; 1846 -6.5; 2031 -7.1; 2234 -7.7; 2457 -7.7; 2703 -7.4; 2973 -7.0; 3270 -6.4; 3597 -6.0; 3957 -6.4; 4353 -9.9; 4788 -14.8; 5267 -18.1; 5793 -21.0; 6373 -22.1; 7010 -19.4; 7711 -12.6; 8482 -7.3; 9330 -6.6; 10263 -8.4; 11289 -10.2; 12418 -10.4; 13660 -8.4; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 660 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 660 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.98 | 4.4 dB   |
| Peaking | 75 Hz    | 0.45 | 4.8 dB   |
| Peaking | 663 Hz   | 0.66 | 2.5 dB   |
| Peaking | 6142 Hz  | 2.59 | -17.3 dB |
| Peaking | 21250 Hz | 1.96 | -2.5 dB  |
| Peaking | 3865 Hz  | 2.46 | 5.1 dB   |
| Peaking | 4637 Hz  | 0.59 | -1.7 dB  |
| Peaking | 4876 Hz  | 6.09 | -3.1 dB  |
| Peaking | 8878 Hz  | 4.4  | 5.1 dB   |
| Peaking | 12114 Hz | 3.2  | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 3.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | -8.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20660/Beyerdynamic%20DT%20660.png)
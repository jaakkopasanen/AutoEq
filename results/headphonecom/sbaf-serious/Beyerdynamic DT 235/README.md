# Beyerdynamic DT 235
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.8; 141 -1.4; 155 -1.5; 170 -1.2; 187 -0.8; 206 -1.2; 227 -1.3; 249 -1.6; 274 -1.9; 302 -2.3; 332 -2.6; 365 -3.1; 402 -3.5; 442 -3.5; 486 -4.1; 535 -4.4; 588 -4.7; 647 -5.0; 712 -5.9; 783 -7.2; 861 -7.8; 947 -7.3; 1042 -6.1; 1146 -4.6; 1261 -3.4; 1387 -3.3; 1526 -4.7; 1678 -7.8; 1846 -7.3; 2031 -4.3; 2234 -3.4; 2457 -2.2; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -4.6; 4788 -11.8; 5267 -7.5; 5793 -3.9; 6373 -5.1; 7010 -7.9; 7711 -10.2; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -12.3; 15026 -13.2; 16529 -9.0; 18182 -6.5; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 235 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 235 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.24 | 5.6 dB   |
| Peaking | 103 Hz   | 0.48 | 4.0 dB   |
| Peaking | 274 Hz   | 0.9  | 2.7 dB   |
| Peaking | 3082 Hz  | 2.15 | 7.0 dB   |
| Peaking | 14697 Hz | 2.46 | -7.7 dB  |
| Peaking | 873 Hz   | 4.45 | -2.5 dB  |
| Peaking | 1293 Hz  | 6.2  | 3.1 dB   |
| Peaking | 4875 Hz  | 7.06 | -10.5 dB |
| Peaking | 5826 Hz  | 1.14 | 4.1 dB   |
| Peaking | 7531 Hz  | 3.9  | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 4.3 dB  |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20235/Beyerdynamic%20DT%20235.png)
# Beyerdynamic DT 235
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.9; 87 -1.5; 96 -2.1; 106 -2.8; 116 -3.2; 128 -3.8; 141 -4.3; 155 -4.5; 170 -4.2; 187 -3.8; 206 -4.2; 227 -4.3; 249 -4.6; 274 -4.9; 302 -5.2; 332 -5.6; 365 -6.1; 402 -6.4; 442 -6.5; 486 -7.1; 535 -7.4; 588 -7.7; 647 -8.0; 712 -8.9; 783 -10.2; 861 -10.7; 947 -10.3; 1042 -9.1; 1146 -7.6; 1261 -6.4; 1387 -6.3; 1526 -7.7; 1678 -10.8; 1846 -10.3; 2031 -7.2; 2234 -6.4; 2457 -5.1; 2703 -3.4; 2973 -2.3; 3270 -1.8; 3597 -0.5; 3957 -0.5; 4353 -7.6; 4788 -14.7; 5267 -10.4; 5793 -6.9; 6373 -8.1; 7010 -10.9; 7711 -13.2; 8482 -10.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.8; 13660 -15.2; 15026 -16.1; 16529 -12.0; 18182 -8.4; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 235 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 235 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.36 | 6.5 dB   |
| Peaking | 3693 Hz  | 2.82 | 8.1 dB   |
| Peaking | 4802 Hz  | 6.1  | -11.1 dB |
| Peaking | 7625 Hz  | 5.41 | -7.1 dB  |
| Peaking | 14871 Hz | 2.09 | -11.0 dB |
| Peaking | 849 Hz   | 2.55 | -4.6 dB  |
| Peaking | 1761 Hz  | 6.31 | -5.4 dB  |
| Peaking | 2801 Hz  | 4.99 | 1.9 dB   |
| Peaking | 11043 Hz | 3.87 | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | -8.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20235/Beyerdynamic%20DT%20235.png)
# Beyerdynamic DT 250-250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.0; 87 -1.8; 96 -2.4; 106 -2.9; 116 -3.4; 128 -4.1; 141 -4.7; 155 -4.8; 170 -5.0; 187 -5.6; 206 -6.0; 227 -6.3; 249 -6.3; 274 -6.3; 302 -6.4; 332 -6.6; 365 -6.7; 402 -6.6; 442 -6.3; 486 -5.9; 535 -5.7; 588 -5.4; 647 -5.5; 712 -5.7; 783 -5.9; 861 -6.1; 947 -6.4; 1042 -4.6; 1146 -4.0; 1261 -4.8; 1387 -5.7; 1526 -7.5; 1678 -8.5; 1846 -8.5; 2031 -8.4; 2234 -8.5; 2457 -9.2; 2703 -9.2; 2973 -7.9; 3270 -7.1; 3597 -8.0; 3957 -8.4; 4353 -8.4; 4788 -7.4; 5267 -4.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -10.5; 10263 -11.2; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 250-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.44 | 6.7 dB  |
| Peaking | 1155 Hz | 2.9  | 3.7 dB  |
| Peaking | 2819 Hz | 0.55 | -2.6 dB |
| Peaking | 6045 Hz | 3.38 | 8.1 dB  |
| Peaking | 9856 Hz | 5.18 | -5.7 dB |
| Peaking | 75 Hz   | 4.69 | 1.1 dB  |
| Peaking | 610 Hz  | 4.05 | 1.3 dB  |
| Peaking | 3214 Hz | 3.87 | 3.8 dB  |
| Peaking | 3470 Hz | 1.72 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20250-250/Beyerdynamic%20DT%20250-250.png)
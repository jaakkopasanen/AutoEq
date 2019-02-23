# Beyerdynamic DT 250-250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.5; 87 -2.3; 96 -2.9; 106 -3.4; 116 -3.9; 128 -4.6; 141 -5.2; 155 -5.3; 170 -5.5; 187 -6.1; 206 -6.5; 227 -6.8; 249 -6.8; 274 -6.7; 302 -6.9; 332 -7.1; 365 -7.2; 402 -7.1; 442 -6.8; 486 -6.4; 535 -6.2; 588 -5.9; 647 -6.0; 712 -6.2; 783 -6.4; 861 -6.6; 947 -6.8; 1042 -5.1; 1146 -4.5; 1261 -5.3; 1387 -6.2; 1526 -8.0; 1678 -9.0; 1846 -9.0; 2031 -8.9; 2234 -9.0; 2457 -9.7; 2703 -9.7; 2973 -8.3; 3270 -7.6; 3597 -8.5; 3957 -8.9; 4353 -8.9; 4788 -7.9; 5267 -4.5; 5793 -0.5; 6373 -1.0; 7010 -4.3; 7711 -6.2; 8482 -6.9; 9330 -11.0; 10263 -11.7; 11289 -7.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 250-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.52 | 6.8 dB  |
| Peaking | 2331 Hz | 1.94 | -3.1 dB |
| Peaking | 4621 Hz | 2.22 | -4.4 dB |
| Peaking | 5885 Hz | 2.83 | 8.6 dB  |
| Peaking | 9828 Hz | 4.37 | -6.6 dB |
| Peaking | 43 Hz   | 2.43 | -1.0 dB |
| Peaking | 73 Hz   | 2.07 | 1.2 dB  |
| Peaking | 256 Hz  | 1.18 | -1.1 dB |
| Peaking | 1152 Hz | 4.44 | 2.7 dB  |
| Peaking | 1670 Hz | 6.14 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20250-250/Beyerdynamic%20DT%20250-250.png)
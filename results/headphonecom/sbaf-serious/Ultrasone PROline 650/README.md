# Ultrasone PROline 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.7; 25 -7.2; 28 -7.8; 31 -8.2; 34 -8.6; 37 -8.9; 41 -9.0; 45 -8.4; 49 -6.8; 54 -5.7; 60 -7.6; 66 -9.3; 72 -10.3; 79 -10.4; 87 -9.7; 96 -9.6; 106 -9.6; 116 -8.6; 128 -8.4; 141 -8.6; 155 -8.0; 170 -7.0; 187 -6.5; 206 -5.3; 227 -4.3; 249 -3.1; 274 -1.9; 302 -1.7; 332 -2.2; 365 -2.9; 402 -3.9; 442 -4.5; 486 -3.9; 535 -0.5; 588 -3.8; 647 -4.9; 712 -5.1; 783 -5.4; 861 -5.8; 947 -6.2; 1042 -6.7; 1146 -6.8; 1261 -6.8; 1387 -7.4; 1526 -8.5; 1678 -9.4; 1846 -9.3; 2031 -8.0; 2234 -1.9; 2457 -2.2; 2703 -7.9; 2973 -8.0; 3270 -8.7; 3597 -10.2; 3957 -10.5; 4353 -9.7; 4788 -6.9; 5267 -7.1; 5793 -3.0; 6373 -7.1; 7010 -5.9; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -7.1; 15026 -14.1; 16529 -13.4; 18182 -6.1; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PROline 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PROline 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 130 Hz   |  0.36 | -5.6 dB  |
| Peaking | 292 Hz   |  0.87 | 7.1 dB   |
| Peaking | 1646 Hz  |  3.5  | -4.4 dB  |
| Peaking | 3837 Hz  |  3.24 | -5.7 dB  |
| Peaking | 15727 Hz |  2.53 | -10.9 dB |
| Peaking | 53 Hz    |  7.3  | 3.2 dB   |
| Peaking | 531 Hz   | 10.03 | 4.5 dB   |
| Peaking | 1191 Hz  |  0.35 | -0.8 dB  |
| Peaking | 2338 Hz  | 11.56 | 8.3 dB   |
| Peaking | 12218 Hz |  2.55 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -8.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20PROline%20650/Ultrasone%20PROline%20650.png)
# Ultrasone PROline 550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.6; 49 -2.3; 54 -2.5; 60 -3.2; 66 -3.7; 72 -3.9; 79 -4.0; 87 -3.8; 96 -3.7; 106 -3.5; 116 -3.3; 128 -2.8; 141 -2.5; 155 -1.8; 170 -0.8; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -2.2; 365 -6.1; 402 -9.1; 442 -10.8; 486 -11.5; 535 -11.4; 588 -11.6; 647 -9.8; 712 -9.6; 783 -9.6; 861 -9.8; 947 -9.9; 1042 -10.0; 1146 -10.0; 1261 -9.8; 1387 -9.5; 1526 -9.9; 1678 -9.5; 1846 -7.6; 2031 -7.7; 2234 -8.6; 2457 -11.2; 2703 -8.3; 2973 -6.0; 3270 -6.7; 3597 -8.3; 3957 -5.7; 4353 -6.7; 4788 -9.6; 5267 -9.6; 5793 -6.9; 6373 -1.0; 7010 -4.0; 7711 -9.3; 8482 -12.6; 9330 -14.4; 10263 -9.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.1; 16529 -12.4; 18182 -12.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PROline 550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PROline 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 27 Hz    |  0.93 | 6.1 dB   |
| Peaking | 296 Hz   |  0.6  | 22.2 dB  |
| Peaking | 427 Hz   |  0.53 | -20.2 dB |
| Peaking | 9160 Hz  |  5.41 | -8.7 dB  |
| Peaking | 17399 Hz |  1.61 | -7.6 dB  |
| Peaking | 4734 Hz  | 10.28 | -3.2 dB  |
| Peaking | 5573 Hz  |  6.95 | -9.4 dB  |
| Peaking | 6170 Hz  |  3.1  | 9.4 dB   |
| Peaking | 8001 Hz  |  4.62 | -4.1 dB  |
| Peaking | 12211 Hz |  3.03 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | 8.1 dB  |
| Peaking | 500 Hz   | 1.41 | -6.1 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20PROline%20550/Ultrasone%20PROline%20550.png)
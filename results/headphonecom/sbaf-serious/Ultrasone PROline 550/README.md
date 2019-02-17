# Ultrasone PROline 550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -2.6; 402 -5.6; 442 -7.3; 486 -8.1; 535 -7.9; 588 -8.1; 647 -6.3; 712 -6.1; 783 -6.1; 861 -6.4; 947 -6.4; 1042 -6.6; 1146 -6.5; 1261 -6.3; 1387 -6.0; 1526 -6.4; 1678 -6.0; 1846 -4.1; 2031 -4.2; 2234 -5.1; 2457 -7.7; 2703 -4.8; 2973 -2.5; 3270 -3.3; 3597 -4.9; 3957 -2.2; 4353 -3.2; 4788 -6.1; 5267 -6.1; 5793 -3.6; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -9.1; 9330 -11.0; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -8.9; 18182 -9.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PROline 550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PROline 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 67 Hz    |  0.22 | 6.7 dB  |
| Peaking | 3503 Hz  |  1.83 | 3.3 dB  |
| Peaking | 6408 Hz  |  6.42 | 6.0 dB  |
| Peaking | 9185 Hz  |  5.02 | -5.1 dB |
| Peaking | 17486 Hz |  2.28 | -3.7 dB |
| Peaking | 22 Hz    |  2.57 | 1.2 dB  |
| Peaking | 335 Hz   |  1.61 | 6.0 dB  |
| Peaking | 448 Hz   |  1.58 | -6.5 dB |
| Peaking | 1981 Hz  |  4.99 | 2.2 dB  |
| Peaking | 2466 Hz  | 11.36 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 4.2 dB  |
| Peaking | 250 Hz   | 1.41 | 6.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20PROline%20550/Ultrasone%20PROline%20550.png)
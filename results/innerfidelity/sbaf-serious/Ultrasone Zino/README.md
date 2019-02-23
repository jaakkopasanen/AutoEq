# Ultrasone Zino
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.7; 31 -2.7; 34 -3.6; 37 -4.5; 41 -5.4; 45 -6.2; 49 -6.9; 54 -7.7; 60 -8.3; 66 -8.8; 72 -9.1; 79 -9.3; 87 -9.2; 96 -9.0; 106 -8.9; 116 -8.6; 128 -8.3; 141 -8.0; 155 -7.4; 170 -6.8; 187 -6.2; 206 -5.5; 227 -4.7; 249 -4.3; 274 -3.7; 302 -2.5; 332 -2.0; 365 -1.8; 402 -2.5; 442 -2.8; 486 -2.5; 535 -1.6; 588 -0.6; 647 -0.5; 712 -0.5; 783 -0.5; 861 -2.3; 947 -5.2; 1042 -8.0; 1146 -10.1; 1261 -11.1; 1387 -12.5; 1526 -14.0; 1678 -15.2; 1846 -16.0; 2031 -16.4; 2234 -15.2; 2457 -10.0; 2703 -6.6; 2973 -5.9; 3270 -4.2; 3597 -3.2; 3957 -1.5; 4353 -8.1; 4788 -5.7; 5267 -4.9; 5793 -9.1; 6373 -9.3; 7010 -7.0; 7711 -6.2; 8482 -7.6; 9330 -9.3; 10263 -9.5; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Zino GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Zino ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 24 Hz    |  1.29 | 6.8 dB   |
| Peaking | 316 Hz   |  0.67 | 10.0 dB  |
| Peaking | 738 Hz   |  1.27 | 11.3 dB  |
| Peaking | 2047 Hz  |  0.23 | -40.2 dB |
| Peaking | 2996 Hz  |  0.29 | 34.7 dB  |
| Peaking | 3841 Hz  | 16.7  | 4.5 dB   |
| Peaking | 6118 Hz  |  6.5  | -3.7 dB  |
| Peaking | 7579 Hz  |  5.01 | 1.8 dB   |
| Peaking | 9803 Hz  |  3.11 | -3.2 dB  |
| Peaking | 14379 Hz |  0.66 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB   |
| Peaking | 62 Hz    | 1.41 | -3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB   |
| Peaking | 500 Hz   | 1.41 | 6.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Zino/Ultrasone%20Zino.png)
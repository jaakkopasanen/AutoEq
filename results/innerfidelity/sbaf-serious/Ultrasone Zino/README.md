# Ultrasone Zino
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.4; 31 -2.4; 34 -3.3; 37 -4.1; 41 -5.1; 45 -5.9; 49 -6.6; 54 -7.3; 60 -8.0; 66 -8.4; 72 -8.8; 79 -8.9; 87 -8.9; 96 -8.7; 106 -8.6; 116 -8.3; 128 -8.0; 141 -7.6; 155 -7.1; 170 -6.4; 187 -5.9; 206 -5.2; 227 -4.3; 249 -4.0; 274 -3.4; 302 -2.1; 332 -1.6; 365 -1.5; 402 -2.2; 442 -2.5; 486 -2.1; 535 -1.3; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -2.0; 947 -4.9; 1042 -7.7; 1146 -9.8; 1261 -10.8; 1387 -12.2; 1526 -13.6; 1678 -14.8; 1846 -15.6; 2031 -16.1; 2234 -14.8; 2457 -9.6; 2703 -6.3; 2973 -5.6; 3270 -3.9; 3597 -2.9; 3957 -1.3; 4353 -7.8; 4788 -5.4; 5267 -4.6; 5793 -8.8; 6373 -8.9; 7010 -6.7; 7711 -6.2; 8482 -7.2; 9330 -9.0; 10263 -9.2; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.7
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
| Peaking | 24 Hz    |  1.26 | 6.8 dB   |
| Peaking | 317 Hz   |  0.66 | 10.2 dB  |
| Peaking | 743 Hz   |  1.22 | 11.1 dB  |
| Peaking | 2048 Hz  |  0.23 | -39.6 dB |
| Peaking | 3009 Hz  |  0.3  | 34.5 dB  |
| Peaking | 3827 Hz  | 16.78 | 4.2 dB   |
| Peaking | 6131 Hz  |  6.98 | -3.6 dB  |
| Peaking | 7539 Hz  |  5.02 | 1.5 dB   |
| Peaking | 9812 Hz  |  3.4  | -2.9 dB  |
| Peaking | 14503 Hz |  0.63 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB   |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | 2.2 dB   |
| Peaking | 500 Hz   | 1.41 | 6.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Zino/Ultrasone%20Zino.png)
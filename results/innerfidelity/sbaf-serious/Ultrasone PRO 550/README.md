# Ultrasone PRO 550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.1; 34 -2.0; 37 -2.7; 41 -3.5; 45 -4.0; 49 -4.1; 54 -4.2; 60 -3.5; 66 -3.5; 72 -4.4; 79 -4.7; 87 -4.9; 96 -4.8; 106 -4.4; 116 -4.1; 128 -3.9; 141 -3.5; 155 -2.9; 170 -1.9; 187 -1.0; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -1.7; 365 -4.1; 402 -5.4; 442 -5.8; 486 -6.0; 535 -6.0; 588 -4.9; 647 -3.4; 712 -4.7; 783 -5.4; 861 -6.0; 947 -6.4; 1042 -6.4; 1146 -5.8; 1261 -5.9; 1387 -6.1; 1526 -6.9; 1678 -6.4; 1846 -4.6; 2031 -2.2; 2234 -2.2; 2457 -4.7; 2703 -2.8; 2973 -2.6; 3270 -4.3; 3597 -4.4; 3957 -3.1; 4353 -0.5; 4788 -0.9; 5267 -0.6; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -8.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  0.57 | 6.2 dB  |
| Peaking | 233 Hz   |  1.17 | 6.4 dB  |
| Peaking | 2222 Hz  |  2.8  | 3.8 dB  |
| Peaking | 4645 Hz  |  2.33 | 5.5 dB  |
| Peaking | 6171 Hz  |  4.8  | 4.2 dB  |
| Peaking | 458 Hz   |  3.56 | -1.5 dB |
| Peaking | 647 Hz   |  6.49 | 2.6 dB  |
| Peaking | 1575 Hz  |  7.05 | -1.6 dB |
| Peaking | 2889 Hz  | 10.11 | 2.5 dB  |
| Peaking | 17843 Hz |  0.17 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 6.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20550/Ultrasone%20PRO%20550.png)
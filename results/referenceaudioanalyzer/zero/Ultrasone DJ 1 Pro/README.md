# Ultrasone DJ 1 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.4; 31 -2.6; 34 -3.6; 37 -4.2; 41 -4.6; 45 -4.7; 49 -4.6; 54 -4.5; 60 -4.9; 66 -5.3; 72 -5.4; 79 -5.2; 87 -4.9; 96 -4.4; 106 -4.0; 116 -3.4; 128 -2.7; 141 -1.9; 155 -1.0; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.9; 332 -3.8; 365 -6.9; 402 -9.1; 442 -10.3; 486 -10.8; 535 -10.9; 588 -10.2; 647 -8.6; 712 -8.0; 783 -8.6; 861 -9.1; 947 -9.3; 1042 -9.3; 1146 -9.0; 1261 -8.6; 1387 -8.4; 1526 -8.3; 1678 -7.8; 1846 -6.5; 2031 -4.9; 2234 -4.6; 2457 -5.6; 2703 -5.5; 2973 -6.2; 3270 -9.0; 3597 -10.3; 3957 -9.3; 4353 -7.0; 4788 -8.1; 5267 -11.9; 5793 -12.3; 6373 -8.7; 7010 -6.4; 7711 -8.9; 8482 -11.8; 9330 -12.4; 10263 -11.6; 11289 -11.6; 12418 -11.6; 13660 -9.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone DJ 1 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone DJ 1 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 23 Hz    |  1.58 | 6.3 dB   |
| Peaking | 281 Hz   |  0.72 | 14.7 dB  |
| Peaking | 426 Hz   |  0.78 | -13.4 dB |
| Peaking | 5501 Hz  |  5.68 | -5.7 dB  |
| Peaking | 10521 Hz |  1.35 | -6.0 dB  |
| Peaking | 696 Hz   |  5.12 | 2.2 dB   |
| Peaking | 1639 Hz  |  0.88 | -3.2 dB  |
| Peaking | 2190 Hz  |  1.4  | 4.8 dB   |
| Peaking | 3547 Hz  |  5.23 | -4.2 dB  |
| Peaking | 6920 Hz  | 10.24 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | 2.9 dB  |
| Peaking | 250 Hz   | 1.41 | 7.5 dB  |
| Peaking | 500 Hz   | 1.41 | -5.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20DJ%201%20Pro/Ultrasone%20DJ%201%20Pro.png)
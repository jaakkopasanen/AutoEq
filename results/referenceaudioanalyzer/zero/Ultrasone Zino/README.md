# Ultrasone Zino
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.8; 31 -2.9; 34 -3.9; 37 -4.7; 41 -5.5; 45 -6.2; 49 -6.7; 54 -7.1; 60 -7.3; 66 -7.3; 72 -7.3; 79 -7.2; 87 -7.0; 96 -6.9; 106 -6.5; 116 -6.2; 128 -5.7; 141 -5.3; 155 -4.8; 170 -4.2; 187 -3.5; 206 -3.1; 227 -2.9; 249 -2.5; 274 -1.9; 302 -1.2; 332 -0.6; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -1.7; 1042 -5.7; 1146 -8.5; 1261 -10.0; 1387 -10.4; 1526 -11.6; 1678 -14.1; 1846 -15.8; 2031 -16.2; 2234 -15.7; 2457 -14.8; 2703 -13.7; 2973 -12.0; 3270 -9.7; 3597 -8.1; 3957 -9.1; 4353 -10.4; 4788 -10.7; 5267 -10.9; 5793 -13.1; 6373 -14.4; 7010 -13.8; 7711 -12.7; 8482 -12.4; 9330 -13.4; 10263 -15.6; 11289 -17.9; 12418 -19.0; 13660 -17.6; 15026 -12.7; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Zino GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Zino ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 2.26 | 6.4 dB   |
| Peaking | 602 Hz   | 0.52 | 8.0 dB   |
| Peaking | 1905 Hz  | 1.14 | -12.2 dB |
| Peaking | 6474 Hz  | 2.53 | -5.5 dB  |
| Peaking | 12286 Hz | 1.39 | -13.1 dB |
| Peaking | 74 Hz    | 1.67 | -1.6 dB  |
| Peaking | 912 Hz   | 3.8  | 4.7 dB   |
| Peaking | 1143 Hz  | 1.63 | -3.9 dB  |
| Peaking | 1511 Hz  | 3    | 2.6 dB   |
| Peaking | 16758 Hz | 3.42 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB   |
| Peaking | 62 Hz    | 1.41 | -2.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB   |
| Peaking | 250 Hz   | 1.41 | 3.4 dB   |
| Peaking | 500 Hz   | 1.41 | 6.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -9.6 dB  |
| Peaking | 16000 Hz | 1.41 | -6.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20Zino/Ultrasone%20Zino.png)
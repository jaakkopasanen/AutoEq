# Ultrasone PRO 2900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.9; 25 -5.0; 28 -6.3; 31 -7.3; 34 -8.1; 37 -8.7; 41 -9.1; 45 -9.3; 49 -9.3; 54 -9.3; 60 -9.3; 66 -9.3; 72 -9.1; 79 -8.9; 87 -8.5; 96 -7.8; 106 -7.2; 116 -6.7; 128 -6.2; 141 -5.7; 155 -5.1; 170 -4.6; 187 -4.5; 206 -4.8; 227 -4.7; 249 -4.2; 274 -3.5; 302 -2.9; 332 -2.4; 365 -1.8; 402 -1.4; 442 -1.2; 486 -0.9; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.6; 783 -1.0; 861 -1.6; 947 -2.2; 1042 -2.9; 1146 -3.8; 1261 -4.7; 1387 -5.3; 1526 -6.1; 1678 -6.9; 1846 -6.9; 2031 -5.2; 2234 -2.8; 2457 -3.1; 2703 -5.5; 2973 -8.0; 3270 -10.2; 3597 -11.9; 3957 -13.8; 4353 -15.5; 4788 -16.4; 5267 -17.2; 5793 -18.4; 6373 -18.7; 7010 -16.8; 7711 -13.5; 8482 -11.2; 9330 -11.4; 10263 -12.7; 11289 -13.6; 12418 -13.7; 13660 -13.3; 15026 -12.3; 16529 -9.9; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 2900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 2900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 576 Hz   | 0.74 | 6.5 dB   |
| Peaking | 2409 Hz  | 4.18 | 6.1 dB   |
| Peaking | 5548 Hz  | 1.07 | -11.8 dB |
| Peaking | 13553 Hz | 1.21 | -6.3 dB  |
| Peaking | 20 Hz    | 2.5  | 4.7 dB   |
| Peaking | 54 Hz    | 1.08 | -3.5 dB  |
| Peaking | 1721 Hz  | 6.39 | -1.5 dB  |
| Peaking | 6700 Hz  | 7.23 | -1.9 dB  |
| Peaking | 8482 Hz  | 5.52 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 6.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.8 dB |
| Peaking | 8000 Hz  | 1.41 | -8.7 dB |
| Peaking | 16000 Hz | 1.41 | -5.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20PRO%202900/Ultrasone%20PRO%202900.png)
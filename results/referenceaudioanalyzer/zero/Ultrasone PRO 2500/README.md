# Ultrasone PRO 2500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.4; 34 -2.6; 37 -3.7; 41 -4.9; 45 -5.8; 49 -6.5; 54 -7.2; 60 -7.7; 66 -8.2; 72 -8.7; 79 -9.1; 87 -9.4; 96 -9.4; 106 -9.6; 116 -9.4; 128 -9.4; 141 -9.1; 155 -8.9; 170 -8.6; 187 -8.4; 206 -8.1; 227 -7.7; 249 -7.3; 274 -7.0; 302 -6.6; 332 -6.3; 365 -5.9; 402 -5.7; 442 -5.4; 486 -5.0; 535 -4.4; 588 -3.7; 647 -3.7; 712 -4.1; 783 -4.3; 861 -4.5; 947 -4.5; 1042 -4.5; 1146 -4.5; 1261 -4.8; 1387 -5.2; 1526 -5.5; 1678 -5.0; 1846 -3.1; 2031 -0.6; 2234 -0.5; 2457 -1.3; 2703 -2.2; 2973 -2.6; 3270 -4.4; 3597 -6.8; 3957 -8.0; 4353 -8.2; 4788 -7.9; 5267 -8.7; 5793 -12.8; 6373 -16.2; 7010 -15.9; 7711 -11.9; 8482 -7.8; 9330 -7.0; 10263 -8.7; 11289 -10.7; 12418 -11.8; 13660 -10.7; 15026 -7.4; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 2500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 2500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 1.27 | 6.8 dB   |
| Peaking | 100 Hz   | 0.92 | -3.6 dB  |
| Peaking | 2266 Hz  | 1.55 | 6.0 dB   |
| Peaking | 6565 Hz  | 2.97 | -10.8 dB |
| Peaking | 12614 Hz | 2.62 | -5.6 dB  |
| Peaking | 203 Hz   | 1.62 | -0.9 dB  |
| Peaking | 625 Hz   | 1.99 | 1.9 dB   |
| Peaking | 1302 Hz  | 0.26 | 1.1 dB   |
| Peaking | 1619 Hz  | 3.07 | -2.8 dB  |
| Peaking | 3916 Hz  | 3.98 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20PRO%202500/Ultrasone%20PRO%202500.png)
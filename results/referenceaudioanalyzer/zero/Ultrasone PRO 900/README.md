# Ultrasone PRO 900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.0; 25 -1.7; 28 -2.9; 31 -3.9; 34 -4.8; 37 -5.5; 41 -6.1; 45 -6.6; 49 -6.8; 54 -6.9; 60 -7.1; 66 -7.3; 72 -7.6; 79 -7.9; 87 -7.9; 96 -7.9; 106 -7.9; 116 -7.8; 128 -7.4; 141 -7.0; 155 -6.5; 170 -5.8; 187 -4.9; 206 -3.7; 227 -2.1; 249 -0.6; 274 -0.5; 302 -0.5; 332 -1.7; 365 -3.2; 402 -4.1; 442 -4.4; 486 -4.2; 535 -3.0; 588 -1.6; 647 -2.1; 712 -3.3; 783 -3.7; 861 -3.7; 947 -3.7; 1042 -3.2; 1146 -2.7; 1261 -3.1; 1387 -4.0; 1526 -4.8; 1678 -5.5; 1846 -5.9; 2031 -5.1; 2234 -3.4; 2457 -3.6; 2703 -5.8; 2973 -8.5; 3270 -10.8; 3597 -12.3; 3957 -13.7; 4353 -15.4; 4788 -16.2; 5267 -16.3; 5793 -16.6; 6373 -16.6; 7010 -14.4; 7711 -11.0; 8482 -9.8; 9330 -10.9; 10263 -12.2; 11289 -12.9; 12418 -13.1; 13660 -12.8; 15026 -11.6; 16529 -8.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 2.55 | 6.0 dB   |
| Peaking | 274 Hz   | 2.64 | 5.7 dB   |
| Peaking | 1628 Hz  | 0.3  | 4.2 dB   |
| Peaking | 5047 Hz  | 1.05 | -12.9 dB |
| Peaking | 13201 Hz | 1.25 | -6.1 dB  |
| Peaking | 97 Hz    | 1.38 | -2.0 dB  |
| Peaking | 602 Hz   | 6.86 | 2.5 dB   |
| Peaking | 2229 Hz  | 1.48 | -3.9 dB  |
| Peaking | 2406 Hz  | 3.44 | 6.9 dB   |
| Peaking | 17989 Hz | 3.35 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 5.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -8.6 dB |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | -5.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20PRO%20900/Ultrasone%20PRO%20900.png)
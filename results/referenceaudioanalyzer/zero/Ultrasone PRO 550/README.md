# Ultrasone PRO 550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -1.3; 72 -1.7; 79 -2.0; 87 -2.1; 96 -1.9; 106 -1.6; 116 -1.4; 128 -1.3; 141 -0.9; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -1.5; 365 -4.7; 402 -7.8; 442 -9.8; 486 -10.8; 535 -11.2; 588 -11.0; 647 -9.9; 712 -8.9; 783 -9.0; 861 -9.2; 947 -9.2; 1042 -9.1; 1146 -8.6; 1261 -8.2; 1387 -8.4; 1526 -8.8; 1678 -8.5; 1846 -7.4; 2031 -5.4; 2234 -4.8; 2457 -5.6; 2703 -5.2; 2973 -3.8; 3270 -5.9; 3597 -8.7; 3957 -8.9; 4353 -9.0; 4788 -11.8; 5267 -14.0; 5793 -12.1; 6373 -8.3; 7010 -8.5; 7711 -12.4; 8482 -15.7; 9330 -15.7; 10263 -13.6; 11289 -12.6; 12418 -12.9; 13660 -11.6; 15026 -7.9; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 0.08 | 5.5 dB   |
| Peaking | 315 Hz  | 1    | 11.0 dB  |
| Peaking | 455 Hz  | 0.93 | -11.8 dB |
| Peaking | 5192 Hz | 5.52 | -6.3 dB  |
| Peaking | 9888 Hz | 1.25 | -8.8 dB  |
| Peaking | 1529 Hz | 2.75 | -1.9 dB  |
| Peaking | 3112 Hz | 1.68 | 5.9 dB   |
| Peaking | 3595 Hz | 2.22 | -5.1 dB  |
| Peaking | 6755 Hz | 7.37 | 3.2 dB   |
| Peaking | 8393 Hz | 6.67 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | 3.4 dB  |
| Peaking | 250 Hz   | 1.41 | 7.6 dB  |
| Peaking | 500 Hz   | 1.41 | -5.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -8.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20PRO%20550/Ultrasone%20PRO%20550.png)
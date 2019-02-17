# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.3; 23 -14.6; 25 -14.8; 28 -15.0; 31 -15.1; 34 -15.1; 37 -15.0; 41 -15.0; 45 -15.0; 49 -15.0; 54 -15.1; 60 -15.3; 66 -15.5; 72 -15.7; 79 -15.9; 87 -16.2; 96 -16.5; 106 -16.7; 116 -16.8; 128 -16.9; 141 -16.9; 155 -16.8; 170 -16.7; 187 -16.4; 206 -16.0; 227 -15.5; 249 -14.9; 274 -15.4; 302 -14.6; 332 -13.8; 365 -13.0; 402 -12.3; 442 -11.6; 486 -10.8; 535 -10.0; 588 -9.1; 647 -8.3; 712 -7.5; 783 -6.7; 861 -6.0; 947 -5.6; 1042 -5.4; 1146 -5.3; 1261 -4.9; 1387 -4.6; 1526 -4.2; 1678 -3.9; 1846 -3.7; 2031 -3.3; 2234 -2.7; 2457 -2.1; 2703 -1.5; 2973 -1.0; 3270 -0.6; 3597 -0.5; 3957 -0.8; 4353 -1.3; 4788 -2.3; 5267 -3.9; 5793 -6.5; 6373 -10.7; 7010 -13.1; 7711 -12.2; 8482 -10.3; 9330 -11.6; 10263 -13.3; 11289 -12.5; 12418 -14.2; 13660 -19.8; 15026 -24.6; 16529 -25.9; 18182 -21.4; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.15 | -9.1 dB  |
| Peaking | 222 Hz   | 0.57 | -5.7 dB  |
| Peaking | 3376 Hz  | 1.05 | 6.8 dB   |
| Peaking | 16384 Hz | 0.6  | -21.0 dB |
| Peaking | 22050 Hz | 1.14 | -6.3 dB  |
| Peaking | 1000 Hz  | 2.12 | 1.1 dB   |
| Peaking | 4998 Hz  | 3.44 | 2.2 dB   |
| Peaking | 6850 Hz  | 4.23 | -5.5 dB  |
| Peaking | 11969 Hz | 3.18 | 3.7 dB   |
| Peaking | 14407 Hz | 3.61 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB  |
| Peaking | 62 Hz    | 1.41 | -6.7 dB  |
| Peaking | 125 Hz   | 1.41 | -9.3 dB  |
| Peaking | 250 Hz   | 1.41 | -8.2 dB  |
| Peaking | 500 Hz   | 1.41 | -3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB  |
| Peaking | 16000 Hz | 1.41 | -26.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)
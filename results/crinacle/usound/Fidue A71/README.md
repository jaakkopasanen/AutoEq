# Fidue A71
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.5; 23 -16.6; 25 -16.6; 28 -16.6; 31 -16.5; 34 -16.5; 37 -16.4; 41 -16.4; 45 -16.3; 49 -16.2; 54 -16.2; 60 -16.0; 66 -16.0; 72 -16.0; 79 -15.9; 87 -15.9; 96 -15.8; 106 -15.8; 116 -15.6; 128 -15.4; 141 -15.2; 155 -14.9; 170 -14.5; 187 -14.0; 206 -13.6; 227 -13.0; 249 -12.5; 274 -11.8; 302 -11.2; 332 -10.6; 365 -9.8; 402 -9.1; 442 -8.7; 486 -8.1; 535 -7.4; 588 -7.0; 647 -6.4; 712 -5.9; 783 -5.3; 861 -4.9; 947 -4.7; 1042 -4.8; 1146 -5.3; 1261 -5.9; 1387 -6.4; 1526 -6.7; 1678 -6.7; 1846 -6.6; 2031 -6.5; 2234 -6.4; 2457 -6.0; 2703 -4.6; 2973 -1.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.5; 7010 -7.5; 7711 -9.8; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A71 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A71 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.13 | -10.1 dB |
| Peaking | 755 Hz  | 1.32 | 2.8 dB   |
| Peaking | 4752 Hz | 1.1  | 7.3 dB   |
| Peaking | 7714 Hz | 3.94 | -6.6 dB  |
| Peaking | 1033 Hz | 3.22 | 1.4 dB   |
| Peaking | 2597 Hz | 2.97 | -1.9 dB  |
| Peaking | 3044 Hz | 0.64 | -2.5 dB  |
| Peaking | 3155 Hz | 2.44 | 5.6 dB   |
| Peaking | 6080 Hz | 6.68 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.4 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB  |
| Peaking | 125 Hz   | 1.41 | -7.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Fidue%20A71/Fidue%20A71.png)
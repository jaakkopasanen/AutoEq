# Astell & Kern AKR03 Roxanne (max)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.8; 23 -16.8; 25 -16.8; 28 -16.8; 31 -16.8; 34 -16.8; 37 -16.8; 41 -16.8; 45 -16.8; 49 -16.8; 54 -16.8; 60 -16.8; 66 -16.8; 72 -16.8; 79 -16.8; 87 -16.8; 96 -16.8; 106 -16.8; 116 -16.8; 128 -16.5; 141 -16.1; 155 -15.6; 170 -15.1; 187 -14.7; 206 -14.5; 227 -14.3; 249 -13.9; 274 -13.4; 302 -13.0; 332 -12.6; 365 -12.2; 402 -11.8; 442 -11.3; 486 -10.9; 535 -10.4; 588 -9.8; 647 -9.2; 712 -8.7; 783 -8.1; 861 -7.5; 947 -6.9; 1042 -6.4; 1146 -5.9; 1261 -5.5; 1387 -5.1; 1526 -4.4; 1678 -3.4; 1846 -2.5; 2031 -1.7; 2234 -1.3; 2457 -1.7; 2703 -2.9; 2973 -4.7; 3270 -4.4; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern AKR03 Roxanne (max) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern AKR03 Roxanne (max) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 90 Hz   | 0.23 | -9.8 dB |
| Peaking | 2044 Hz | 1.47 | 5.1 dB  |
| Peaking | 4225 Hz | 2.83 | 5.1 dB  |
| Peaking | 5832 Hz | 3.18 | 5.3 dB  |
| Peaking | 15 Hz   | 0.57 | -5.7 dB |
| Peaking | 55 Hz   | 2.03 | 0.2 dB  |
| Peaking | 1039 Hz | 3.86 | 0.7 dB  |
| Peaking | 8246 Hz | 4.31 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.5 dB |
| Peaking | 62 Hz    | 1.41 | -7.4 dB  |
| Peaking | 125 Hz   | 1.41 | -8.0 dB  |
| Peaking | 250 Hz   | 1.41 | -5.5 dB  |
| Peaking | 500 Hz   | 1.41 | -3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Astell%20&%20Kern%20AKR03%20Roxanne%20(max)/Astell%20&%20Kern%20AKR03%20Roxanne%20(max).png)
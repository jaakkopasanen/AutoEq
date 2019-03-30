# Sennheiser IE800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.6; 23 -15.0; 25 -15.4; 28 -15.7; 31 -16.0; 34 -16.0; 37 -16.1; 41 -16.1; 45 -16.0; 49 -15.9; 54 -15.8; 60 -15.5; 66 -15.2; 72 -14.8; 79 -14.5; 87 -14.1; 96 -13.6; 106 -13.0; 116 -12.4; 128 -11.8; 141 -11.5; 155 -11.2; 170 -11.0; 187 -10.6; 206 -10.3; 227 -10.0; 249 -9.7; 274 -9.2; 302 -8.7; 332 -8.2; 365 -7.8; 402 -7.5; 442 -7.1; 486 -6.8; 535 -6.6; 588 -6.3; 647 -6.2; 712 -6.0; 783 -6.0; 861 -5.9; 947 -5.9; 1042 -5.7; 1146 -5.5; 1261 -5.3; 1387 -5.3; 1526 -5.3; 1678 -5.1; 1846 -4.8; 2031 -4.4; 2234 -3.8; 2457 -3.0; 2703 -2.2; 2973 -1.4; 3270 -1.0; 3597 -0.6; 3957 -0.5; 4353 -0.6; 4788 -1.5; 5267 -3.5; 5793 -5.3; 6373 -4.7; 7010 -4.2; 7711 -6.2; 8482 -8.3; 9330 -13.1; 10263 -16.5; 11289 -16.0; 12418 -10.0; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.25 | -9.4 dB  |
| Peaking | 1637 Hz  | 1.41 | -1.2 dB  |
| Peaking | 3705 Hz  | 1.49 | 4.0 dB   |
| Peaking | 5185 Hz  | 0.19 | 2.9 dB   |
| Peaking | 10553 Hz | 2.22 | -14.0 dB |
| Peaking | 4696 Hz  | 5.19 | 1.2 dB   |
| Peaking | 5857 Hz  | 3.88 | -2.7 dB  |
| Peaking | 6805 Hz  | 2.56 | 2.3 dB   |
| Peaking | 12021 Hz | 0.53 | -0.8 dB  |
| Peaking | 13305 Hz | 4.84 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.6 dB |
| Peaking | 62 Hz    | 1.41 | -7.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20IE800/Sennheiser%20IE800.png)
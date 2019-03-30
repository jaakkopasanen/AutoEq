# Sennheiser eH 2270
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.0; 25 -1.6; 28 -2.7; 31 -3.6; 34 -4.3; 37 -4.9; 41 -5.6; 45 -6.2; 49 -6.7; 54 -7.1; 60 -7.4; 66 -7.5; 72 -7.5; 79 -7.3; 87 -7.2; 96 -7.5; 106 -8.1; 116 -8.7; 128 -9.1; 141 -9.0; 155 -8.5; 170 -7.7; 187 -6.8; 206 -6.2; 227 -5.8; 249 -5.0; 274 -3.6; 302 -1.9; 332 -0.9; 365 -1.5; 402 -3.1; 442 -4.5; 486 -5.5; 535 -6.1; 588 -6.5; 647 -6.6; 712 -6.5; 783 -6.7; 861 -6.8; 947 -6.5; 1042 -6.3; 1146 -6.2; 1261 -6.2; 1387 -6.2; 1526 -6.2; 1678 -6.3; 1846 -6.5; 2031 -6.8; 2234 -7.1; 2457 -7.4; 2703 -7.0; 2973 -6.3; 3270 -5.1; 3597 -2.2; 3957 -0.5; 4353 -5.7; 4788 -10.4; 5267 -10.6; 5793 -7.4; 6373 -6.4; 7010 -8.7; 7711 -9.8; 8482 -9.9; 9330 -9.2; 10263 -6.8; 11289 -6.4; 12418 -6.6; 13660 -10.3; 15026 -11.6; 16529 -7.6; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser eH 2270 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser eH 2270 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 2.49 | 6.2 dB  |
| Peaking | 338 Hz   | 3.3  | 6.1 dB  |
| Peaking | 3929 Hz  | 3.07 | 15.0 dB |
| Peaking | 4402 Hz  | 1.42 | -9.6 dB |
| Peaking | 14767 Hz | 2.84 | -5.9 dB |
| Peaking | 128 Hz   | 1.89 | -3.0 dB |
| Peaking | 6184 Hz  | 5.87 | 4.5 dB  |
| Peaking | 8931 Hz  | 1.3  | -3.8 dB |
| Peaking | 10900 Hz | 2.08 | 3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20eH%202270/Sennheiser%20eH%202270.png)
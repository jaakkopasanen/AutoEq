# Astrotec AX-7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.8; 25 -5.9; 28 -6.0; 31 -6.1; 34 -6.2; 37 -6.3; 41 -6.4; 45 -6.5; 49 -6.5; 54 -6.5; 60 -6.5; 66 -6.5; 72 -6.5; 79 -6.7; 87 -6.8; 96 -6.7; 106 -6.5; 116 -6.5; 128 -6.5; 141 -6.5; 155 -6.4; 170 -6.2; 187 -6.3; 206 -6.9; 227 -7.3; 249 -7.4; 274 -7.2; 302 -7.0; 332 -6.8; 365 -6.8; 402 -6.5; 442 -6.5; 486 -6.2; 535 -6.2; 588 -5.9; 647 -5.9; 712 -5.6; 783 -5.5; 861 -5.3; 947 -5.2; 1042 -5.2; 1146 -5.0; 1261 -4.9; 1387 -5.2; 1526 -5.3; 1678 -5.9; 1846 -6.6; 2031 -7.7; 2234 -9.0; 2457 -10.0; 2703 -9.9; 2973 -8.4; 3270 -6.4; 3597 -6.8; 3957 -9.7; 4353 -11.6; 4788 -10.5; 5267 -6.4; 5793 -0.7; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.6; 11289 -6.8; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec AX-7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX-7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 1046 Hz | 0.54 | 7.5 dB  |
| Peaking | 1339 Hz | 0.26 | -6.5 dB |
| Peaking | 4368 Hz | 7.01 | -3.7 dB |
| Peaking | 4925 Hz | 5.06 | -4.0 dB |
| Peaking | 6010 Hz | 2.85 | 8.9 dB  |
| Peaking | 70 Hz   | 0.79 | -0.5 dB |
| Peaking | 172 Hz  | 6.08 | 0.7 dB  |
| Peaking | 1810 Hz | 1.95 | 2.4 dB  |
| Peaking | 2497 Hz | 1.3  | -3.2 dB |
| Peaking | 3303 Hz | 4.31 | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Astrotec%20AX-7/Astrotec%20AX-7.png)
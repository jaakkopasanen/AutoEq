# Dunu Titan 1es
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.2; 25 -1.2; 28 -1.2; 31 -1.2; 34 -1.2; 37 -1.2; 41 -1.2; 45 -1.2; 49 -1.2; 54 -1.2; 60 -1.2; 66 -1.2; 72 -1.2; 79 -1.2; 87 -1.2; 96 -1.2; 106 -1.2; 116 -1.2; 128 -1.2; 141 -1.2; 155 -1.2; 170 -1.2; 187 -1.1; 206 -0.9; 227 -0.8; 249 -0.5; 274 -0.7; 302 -1.0; 332 -1.2; 365 -1.2; 402 -1.4; 442 -1.5; 486 -1.4; 535 -1.2; 588 -1.2; 647 -1.2; 712 -1.2; 783 -1.2; 861 -1.2; 947 -1.2; 1042 -1.5; 1146 -1.7; 1261 -2.0; 1387 -2.4; 1526 -2.8; 1678 -3.3; 1846 -3.8; 2031 -4.3; 2234 -4.7; 2457 -5.0; 2703 -5.1; 2973 -5.3; 3270 -5.4; 3597 -5.2; 3957 -6.0; 4353 -8.1; 4788 -10.5; 5267 -12.2; 5793 -11.5; 6373 -7.7; 7010 -1.6; 7711 -2.1; 8482 -2.4; 9330 -2.4; 10263 -2.4; 11289 -2.4; 12418 -2.4; 13660 -2.4; 15026 -2.4; 16529 -2.4; 18182 -2.4; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Titan 1es GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 1es ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 105 Hz   | 0.1  | 1.4 dB   |
| Peaking | 972 Hz   | 1.22 | 0.7 dB   |
| Peaking | 2364 Hz  | 1.33 | -2.2 dB  |
| Peaking | 5508 Hz  | 2.05 | -11.4 dB |
| Peaking | 7206 Hz  | 2.86 | 5.2 dB   |
| Peaking | 253 Hz   | 4.88 | 0.6 dB   |
| Peaking | 434 Hz   | 5.19 | -0.4 dB  |
| Peaking | 3778 Hz  | 5.55 | 1.4 dB   |
| Peaking | 4118 Hz  | 2.36 | -0.8 dB  |
| Peaking | 10785 Hz | 2.03 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -6.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20Titan%201es/Dunu%20Titan%201es.png)
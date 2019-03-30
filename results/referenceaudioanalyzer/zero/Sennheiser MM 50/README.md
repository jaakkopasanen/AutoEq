# Sennheiser MM 50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.6; 25 -12.7; 28 -12.8; 31 -12.9; 34 -13.0; 37 -13.1; 41 -13.1; 45 -13.1; 49 -13.1; 54 -13.1; 60 -13.1; 66 -13.1; 72 -13.1; 79 -13.0; 87 -12.8; 96 -12.8; 106 -12.8; 116 -12.5; 128 -12.4; 141 -12.2; 155 -12.0; 170 -11.7; 187 -11.4; 206 -11.1; 227 -10.6; 249 -10.2; 274 -9.8; 302 -9.4; 332 -9.0; 365 -8.6; 402 -8.4; 442 -8.1; 486 -7.6; 535 -7.0; 588 -6.4; 647 -5.7; 712 -5.1; 783 -4.4; 861 -3.8; 947 -3.2; 1042 -2.6; 1146 -2.0; 1261 -1.6; 1387 -1.2; 1526 -0.8; 1678 -0.5; 1846 -0.5; 2031 -0.9; 2234 -1.3; 2457 -1.7; 2703 -2.0; 2973 -2.3; 3270 -2.4; 3597 -2.4; 3957 -2.4; 4353 -2.7; 4788 -2.7; 5267 -2.7; 5793 -3.8; 6373 -7.3; 7010 -9.1; 7711 -6.7; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.27 | -5.5 dB |
| Peaking | 125 Hz   | 0.29 | -5.8 dB |
| Peaking | 1621 Hz  | 0.67 | 5.2 dB  |
| Peaking | 5370 Hz  | 1.41 | 2.8 dB  |
| Peaking | 6851 Hz  | 3.74 | -6.1 dB |
| Peaking | 313 Hz   | 2.46 | 0.3 dB  |
| Peaking | 473 Hz   | 3.82 | -0.4 dB |
| Peaking | 11339 Hz | 2.47 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20MM%2050/Sennheiser%20MM%2050.png)
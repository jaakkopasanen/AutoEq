# Koss The PLUG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.2; 25 -4.5; 28 -4.8; 31 -5.0; 34 -5.2; 37 -5.3; 41 -5.4; 45 -5.5; 49 -5.5; 54 -5.6; 60 -5.8; 66 -5.8; 72 -5.8; 79 -5.8; 87 -5.8; 96 -5.8; 106 -5.8; 116 -5.8; 128 -5.8; 141 -5.6; 155 -5.5; 170 -5.5; 187 -5.5; 206 -5.5; 227 -5.4; 249 -5.2; 274 -5.2; 302 -5.2; 332 -5.2; 365 -5.2; 402 -5.1; 442 -5.0; 486 -4.8; 535 -4.8; 588 -4.9; 647 -5.1; 712 -5.2; 783 -5.2; 861 -5.5; 947 -5.9; 1042 -6.3; 1146 -6.9; 1261 -7.6; 1387 -8.6; 1526 -10.1; 1678 -12.1; 1846 -14.7; 2031 -16.8; 2234 -17.1; 2457 -15.3; 2703 -12.2; 2973 -9.3; 3270 -7.5; 3597 -6.8; 3957 -7.4; 4353 -9.4; 4788 -12.0; 5267 -11.8; 5793 -6.5; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss The PLUG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss The PLUG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 18 Hz   |  1.18 | 2.0 dB   |
| Peaking | 569 Hz  |  0.61 | 1.3 dB   |
| Peaking | 2114 Hz |  2.14 | -12.2 dB |
| Peaking | 5137 Hz |  4.13 | -7.6 dB  |
| Peaking | 6360 Hz |  4.78 | 7.5 dB   |
| Peaking | 2114 Hz |  5.86 | 2.5 dB   |
| Peaking | 2398 Hz |  2.09 | -2.5 dB  |
| Peaking | 3379 Hz |  2.46 | 2.4 dB   |
| Peaking | 4596 Hz | 10.29 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB   |
| Peaking | 62 Hz    | 1.41 | -0.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB   |
| Peaking | 250 Hz   | 1.41 | 0.5 dB   |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Koss%20The%20PLUG/Koss%20The%20PLUG.png)
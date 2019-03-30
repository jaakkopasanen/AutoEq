# Philips SHE3590
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.9; 41 -1.2; 45 -1.5; 49 -1.8; 54 -2.1; 60 -2.3; 66 -2.5; 72 -2.6; 79 -2.7; 87 -2.9; 96 -2.9; 106 -2.9; 116 -3.1; 128 -3.3; 141 -3.2; 155 -3.2; 170 -3.2; 187 -3.2; 206 -3.2; 227 -3.2; 249 -3.2; 274 -3.2; 302 -3.2; 332 -3.2; 365 -3.2; 402 -3.2; 442 -3.3; 486 -3.5; 535 -3.8; 588 -3.9; 647 -4.1; 712 -4.3; 783 -4.5; 861 -4.5; 947 -4.5; 1042 -4.7; 1146 -5.1; 1261 -5.5; 1387 -5.9; 1526 -6.5; 1678 -7.5; 1846 -8.9; 2031 -10.9; 2234 -14.1; 2457 -18.5; 2703 -21.5; 2973 -21.2; 3270 -18.0; 3597 -13.9; 3957 -12.0; 4353 -12.1; 4788 -12.9; 5267 -14.3; 5793 -14.5; 6373 -12.1; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHE3590 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE3590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 24 Hz   |  0.49 | 5.7 dB   |
| Peaking | 748 Hz  |  0.09 | 3.2 dB   |
| Peaking | 2795 Hz |  1.96 | -18.5 dB |
| Peaking | 5784 Hz |  2.13 | -8.9 dB  |
| Peaking | 7204 Hz |  4.19 | 4.4 dB   |
| Peaking | 751 Hz  |  3.08 | -0.5 dB  |
| Peaking | 1657 Hz |  2.64 | 0.6 dB   |
| Peaking | 2411 Hz |  9.45 | -1.3 dB  |
| Peaking | 3874 Hz | 10.96 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 2.7 dB   |
| Peaking | 125 Hz   | 1.41 | 2.3 dB   |
| Peaking | 250 Hz   | 1.41 | 2.6 dB   |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -10.0 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHE3590/Philips%20SHE3590.png)
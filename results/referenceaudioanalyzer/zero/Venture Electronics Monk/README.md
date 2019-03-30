# Venture Electronics Monk
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.0; 72 -2.3; 79 -3.6; 87 -4.8; 96 -5.8; 106 -6.5; 116 -7.0; 128 -7.4; 141 -7.5; 155 -7.5; 170 -7.5; 187 -7.5; 206 -7.3; 227 -7.2; 249 -7.2; 274 -7.2; 302 -7.2; 332 -7.2; 365 -7.2; 402 -7.2; 442 -7.4; 486 -7.5; 535 -7.2; 588 -6.6; 647 -5.9; 712 -5.7; 783 -6.2; 861 -6.9; 947 -7.7; 1042 -8.5; 1146 -9.3; 1261 -9.9; 1387 -10.0; 1526 -9.4; 1678 -8.6; 1846 -7.9; 2031 -7.8; 2234 -8.0; 2457 -8.2; 2703 -7.7; 2973 -6.7; 3270 -5.3; 3597 -4.0; 3957 -3.3; 4353 -3.5; 4788 -4.9; 5267 -6.8; 5793 -7.6; 6373 -6.3; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venture Electronics Monk GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Monk ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.86 | 7.2 dB  |
| Peaking | 1335 Hz | 2.13 | -3.7 dB |
| Peaking | 2501 Hz | 3.06 | -1.7 dB |
| Peaking | 3951 Hz | 3.07 | 3.8 dB  |
| Peaking | 64 Hz   | 2.2  | 3.8 dB  |
| Peaking | 113 Hz  | 0.44 | -1.9 dB |
| Peaking | 717 Hz  | 4.6  | 1.5 dB  |
| Peaking | 5708 Hz | 6.27 | -1.9 dB |
| Peaking | 6869 Hz | 8.99 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Venture%20Electronics%20Monk/Venture%20Electronics%20Monk.png)
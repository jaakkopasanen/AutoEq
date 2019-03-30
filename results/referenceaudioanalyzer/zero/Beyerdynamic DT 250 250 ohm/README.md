# Beyerdynamic DT 250 250 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -1.5; 41 -2.2; 45 -2.8; 49 -3.3; 54 -3.8; 60 -4.4; 66 -4.6; 72 -4.7; 79 -4.9; 87 -5.1; 96 -5.2; 106 -5.2; 116 -5.6; 128 -6.1; 141 -6.2; 155 -6.2; 170 -6.2; 187 -6.2; 206 -6.1; 227 -5.8; 249 -5.4; 274 -5.0; 302 -4.9; 332 -4.9; 365 -4.9; 402 -4.9; 442 -4.9; 486 -4.8; 535 -4.9; 588 -5.0; 647 -5.2; 712 -5.2; 783 -5.4; 861 -6.0; 947 -6.2; 1042 -5.4; 1146 -4.9; 1261 -5.5; 1387 -6.6; 1526 -7.6; 1678 -8.4; 1846 -8.8; 2031 -8.8; 2234 -8.8; 2457 -8.5; 2703 -7.7; 2973 -6.2; 3270 -4.7; 3597 -6.1; 3957 -9.0; 4353 -10.2; 4788 -9.3; 5267 -7.2; 5793 -5.3; 6373 -5.1; 7010 -6.9; 7711 -8.4; 8482 -9.3; 9330 -10.8; 10263 -12.6; 11289 -13.5; 12418 -12.6; 13660 -9.9; 15026 -7.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 250 250 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250 250 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.72 | 6.3 dB  |
| Peaking | 527 Hz   | 0.59 | 1.6 dB  |
| Peaking | 1784 Hz  | 3.33 | -2.1 dB |
| Peaking | 2265 Hz  | 3.58 | -2.0 dB |
| Peaking | 11280 Hz | 1.73 | -7.5 dB |
| Peaking | 2742 Hz  | 5.09 | -1.0 dB |
| Peaking | 3376 Hz  | 3.13 | 4.4 dB  |
| Peaking | 4220 Hz  | 2.26 | -4.9 dB |
| Peaking | 5996 Hz  | 3.99 | 3.5 dB  |
| Peaking | 15533 Hz | 3.29 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20250%20250%20ohm/Beyerdynamic%20DT%20250%20250%20ohm.png)
# Beyerdynamic DT 250 80 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.5; 34 -2.3; 37 -3.0; 41 -3.8; 45 -4.4; 49 -5.0; 54 -5.7; 60 -6.3; 66 -6.6; 72 -6.8; 79 -7.1; 87 -7.5; 96 -7.8; 106 -8.2; 116 -8.8; 128 -9.3; 141 -9.6; 155 -9.8; 170 -9.9; 187 -9.6; 206 -9.5; 227 -9.1; 249 -8.5; 274 -7.6; 302 -6.8; 332 -6.2; 365 -5.4; 402 -4.5; 442 -3.5; 486 -3.0; 535 -3.0; 588 -3.4; 647 -4.0; 712 -4.5; 783 -5.1; 861 -5.3; 947 -4.7; 1042 -4.4; 1146 -5.2; 1261 -5.8; 1387 -6.5; 1526 -7.4; 1678 -8.4; 1846 -8.9; 2031 -8.9; 2234 -8.9; 2457 -8.9; 2703 -8.6; 2973 -7.9; 3270 -7.0; 3597 -6.3; 3957 -6.6; 4353 -7.3; 4788 -6.6; 5267 -3.8; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.1; 9330 -7.5; 10263 -7.6; 11289 -8.7; 12418 -9.9; 13660 -8.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 250 80 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250 80 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.89 | 6.3 dB  |
| Peaking | 216 Hz   | 0.6  | -6.3 dB |
| Peaking | 462 Hz   | 0.56 | 6.5 dB  |
| Peaking | 4552 Hz  | 0.2  | -3.0 dB |
| Peaking | 6078 Hz  | 2.3  | 8.8 dB  |
| Peaking | 1161 Hz  | 2.57 | 2.0 dB  |
| Peaking | 2503 Hz  | 0.43 | -1.3 dB |
| Peaking | 3469 Hz  | 2.95 | 2.9 dB  |
| Peaking | 12776 Hz | 2.38 | -4.2 dB |
| Peaking | 13629 Hz | 0.83 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20250%2080%20ohm/Beyerdynamic%20DT%20250%2080%20ohm.png)
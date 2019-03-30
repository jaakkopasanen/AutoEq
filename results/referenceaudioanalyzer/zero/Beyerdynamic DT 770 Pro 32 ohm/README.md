# Beyerdynamic DT 770 Pro 32 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.7; 25 -2.7; 28 -4.0; 31 -5.0; 34 -5.6; 37 -6.1; 41 -6.6; 45 -7.0; 49 -7.2; 54 -7.4; 60 -7.5; 66 -7.5; 72 -7.5; 79 -7.5; 87 -7.7; 96 -7.9; 106 -8.3; 116 -8.5; 128 -8.5; 141 -8.2; 155 -7.8; 170 -6.8; 187 -5.3; 206 -3.5; 227 -2.2; 249 -2.7; 274 -5.4; 302 -8.4; 332 -10.6; 365 -11.9; 402 -12.3; 442 -11.5; 486 -9.5; 535 -7.4; 588 -6.6; 647 -6.3; 712 -5.8; 783 -5.4; 861 -5.0; 947 -4.5; 1042 -4.0; 1146 -3.9; 1261 -3.9; 1387 -3.9; 1526 -3.9; 1678 -4.1; 1846 -4.3; 2031 -4.5; 2234 -4.6; 2457 -4.0; 2703 -3.1; 2973 -2.9; 3270 -4.0; 3597 -5.2; 3957 -4.8; 4353 -1.4; 4788 -1.8; 5267 -7.1; 5793 -8.3; 6373 -6.7; 7010 -7.5; 7711 -9.4; 8482 -9.4; 9330 -8.1; 10263 -8.1; 11289 -9.7; 12418 -10.1; 13660 -8.0; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 Pro 32 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 Pro 32 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 2.57 | 5.9 dB   |
| Peaking | 239 Hz   | 1.93 | 14.7 dB  |
| Peaking | 296 Hz   | 0.69 | -13.2 dB |
| Peaking | 3240 Hz  | 0.08 | 4.3 dB   |
| Peaking | 10003 Hz | 0.57 | -7.2 dB  |
| Peaking | 428 Hz   | 2.93 | -4.4 dB  |
| Peaking | 476 Hz   | 1.32 | 2.8 dB   |
| Peaking | 2007 Hz  | 2.61 | -1.4 dB  |
| Peaking | 4578 Hz  | 8.22 | 5.5 dB   |
| Peaking | 5506 Hz  | 6.2  | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | -5.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20770%20Pro%2032%20ohm/Beyerdynamic%20DT%20770%20Pro%2032%20ohm.png)
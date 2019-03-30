# MrSpeakers Alpha Dog
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.9; 25 -2.5; 28 -3.3; 31 -3.8; 34 -4.1; 37 -4.2; 41 -4.2; 45 -4.2; 49 -4.2; 54 -4.4; 60 -4.5; 66 -4.3; 72 -4.1; 79 -3.7; 87 -3.2; 96 -2.6; 106 -2.3; 116 -2.3; 128 -2.7; 141 -3.2; 155 -3.7; 170 -4.2; 187 -5.0; 206 -5.7; 227 -6.1; 249 -6.3; 274 -6.5; 302 -6.5; 332 -6.8; 365 -7.3; 402 -7.8; 442 -7.7; 486 -6.5; 535 -5.0; 588 -5.8; 647 -7.0; 712 -6.9; 783 -6.2; 861 -5.8; 947 -5.7; 1042 -6.6; 1146 -7.4; 1261 -7.2; 1387 -6.4; 1526 -5.7; 1678 -5.2; 1846 -4.8; 2031 -3.9; 2234 -2.8; 2457 -1.9; 2703 -1.4; 2973 -1.3; 3270 -2.3; 3597 -3.9; 3957 -5.2; 4353 -5.4; 4788 -3.7; 5267 -0.5; 5793 -1.1; 6373 -6.3; 7010 -9.7; 7711 -10.2; 8482 -8.8; 9330 -7.9; 10263 -7.5; 11289 -6.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Alpha Dog GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Alpha Dog ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 1.1  | 5.4 dB  |
| Peaking | 109 Hz   | 2.22 | 3.3 dB  |
| Peaking | 2798 Hz  | 2.77 | 4.9 dB  |
| Peaking | 5601 Hz  | 3.75 | 9.8 dB  |
| Peaking | 6968 Hz  | 1.37 | -6.6 dB |
| Peaking | 383 Hz   | 1.66 | -2.4 dB |
| Peaking | 1184 Hz  | 1.56 | -0.6 dB |
| Peaking | 1208 Hz  | 3.09 | -1.5 dB |
| Peaking | 2185 Hz  | 3.55 | 1.0 dB  |
| Peaking | 12703 Hz | 3.51 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | 3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MrSpeakers%20Alpha%20Dog/MrSpeakers%20Alpha%20Dog.png)
# Yamaha HPH-MT220
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.7; 25 -10.2; 28 -10.8; 31 -11.3; 34 -11.5; 37 -11.7; 41 -11.7; 45 -11.7; 49 -11.7; 54 -11.6; 60 -11.4; 66 -11.0; 72 -10.6; 79 -10.1; 87 -9.8; 96 -9.9; 106 -10.1; 116 -10.1; 128 -9.6; 141 -8.9; 155 -8.2; 170 -7.2; 187 -6.2; 206 -5.4; 227 -4.9; 249 -4.4; 274 -3.9; 302 -3.4; 332 -2.5; 365 -1.5; 402 -1.0; 442 -1.3; 486 -2.0; 535 -3.0; 588 -4.1; 647 -5.2; 712 -6.0; 783 -6.7; 861 -7.2; 947 -7.5; 1042 -7.5; 1146 -7.8; 1261 -7.7; 1387 -7.5; 1526 -7.2; 1678 -6.5; 1846 -5.5; 2031 -4.7; 2234 -4.2; 2457 -4.4; 2703 -4.7; 2973 -4.6; 3270 -3.9; 3597 -5.0; 3957 -7.8; 4353 -9.4; 4788 -8.6; 5267 -4.9; 5793 -0.5; 6373 -1.2; 7010 -3.4; 7711 -5.5; 8482 -7.1; 9330 -8.6; 10263 -9.5; 11289 -9.3; 12418 -8.9; 13660 -8.6; 15026 -7.3; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HPH-MT220 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HPH-MT220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.59 | -6.4 dB |
| Peaking | 120 Hz  | 2.29 | -2.6 dB |
| Peaking | 391 Hz  | 1.97 | 5.3 dB  |
| Peaking | 6312 Hz | 3.25 | 8.5 dB  |
| Peaking | 9352 Hz | 0.53 | -3.8 dB |
| Peaking | 235 Hz  | 3.21 | 0.9 dB  |
| Peaking | 1159 Hz | 1.43 | -2.9 dB |
| Peaking | 3394 Hz | 1.01 | 3.9 dB  |
| Peaking | 4435 Hz | 2.51 | -6.3 dB |
| Peaking | 5607 Hz | 9.39 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Yamaha%20HPH-MT220/Yamaha%20HPH-MT220.png)
# Yamaha HPH-PRO400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.2; 37 -2.0; 41 -2.8; 45 -3.2; 49 -3.3; 54 -3.5; 60 -4.1; 66 -4.9; 72 -5.5; 79 -6.1; 87 -6.6; 96 -6.9; 106 -7.2; 116 -7.5; 128 -8.0; 141 -8.4; 155 -8.8; 170 -9.2; 187 -9.4; 206 -9.1; 227 -7.8; 249 -5.6; 274 -4.0; 302 -4.6; 332 -5.6; 365 -6.5; 402 -7.3; 442 -7.9; 486 -8.1; 535 -8.2; 588 -8.5; 647 -8.8; 712 -8.8; 783 -8.8; 861 -8.8; 947 -8.3; 1042 -7.6; 1146 -7.0; 1261 -6.5; 1387 -6.2; 1526 -5.8; 1678 -5.6; 1846 -5.6; 2031 -5.3; 2234 -5.2; 2457 -5.5; 2703 -5.4; 2973 -5.5; 3270 -7.0; 3597 -9.0; 3957 -9.9; 4353 -9.5; 4788 -7.3; 5267 -3.5; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HPH-PRO400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HPH-PRO400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.81 | 6.4 dB  |
| Peaking | 160 Hz  | 2.12 | -3.2 dB |
| Peaking | 706 Hz  | 2.03 | -2.7 dB |
| Peaking | 4164 Hz | 4.05 | -4.8 dB |
| Peaking | 5953 Hz | 3.5  | 7.0 dB  |
| Peaking | 212 Hz  | 4.17 | -2.2 dB |
| Peaking | 278 Hz  | 3.11 | 3.4 dB  |
| Peaking | 454 Hz  | 3.56 | -1.2 dB |
| Peaking | 928 Hz  | 5.93 | -1.0 dB |
| Peaking | 2083 Hz | 1.65 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Yamaha%20HPH-PRO400/Yamaha%20HPH-PRO400.png)
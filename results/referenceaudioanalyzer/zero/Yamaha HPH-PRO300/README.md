# Yamaha HPH-PRO300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.3; 49 -1.9; 54 -2.7; 60 -3.6; 66 -4.2; 72 -4.8; 79 -5.4; 87 -5.9; 96 -5.9; 106 -5.9; 116 -6.2; 128 -6.6; 141 -7.4; 155 -8.2; 170 -9.0; 187 -9.7; 206 -10.1; 227 -9.5; 249 -8.2; 274 -7.5; 302 -7.9; 332 -8.2; 365 -8.0; 402 -7.5; 442 -7.1; 486 -6.9; 535 -6.9; 588 -6.8; 647 -6.6; 712 -7.0; 783 -7.6; 861 -8.2; 947 -8.7; 1042 -9.3; 1146 -9.9; 1261 -10.7; 1387 -11.2; 1526 -11.4; 1678 -11.5; 1846 -11.4; 2031 -10.7; 2234 -9.3; 2457 -7.6; 2703 -6.1; 2973 -4.9; 3270 -3.7; 3597 -2.7; 3957 -1.5; 4353 -0.5; 4788 -0.5; 5267 -2.4; 5793 -4.6; 6373 -4.9; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HPH-PRO300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HPH-PRO300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.7  | 6.6 dB  |
| Peaking | 198 Hz  | 1.68 | -3.7 dB |
| Peaking | 1328 Hz | 1.59 | -3.9 dB |
| Peaking | 1902 Hz | 2.41 | -3.9 dB |
| Peaking | 4309 Hz | 1.77 | 6.6 dB  |
| Peaking | 84 Hz   | 5.69 | -0.6 dB |
| Peaking | 267 Hz  | 6.94 | 0.9 dB  |
| Peaking | 346 Hz  | 4.09 | -1.0 dB |
| Peaking | 635 Hz  | 5.17 | 0.7 dB  |
| Peaking | 8806 Hz | 3.07 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Yamaha%20HPH-PRO300/Yamaha%20HPH-PRO300.png)
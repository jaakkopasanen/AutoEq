# Shure SRH440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.4; 37 -1.8; 41 -2.2; 45 -2.6; 49 -2.9; 54 -3.2; 60 -3.6; 66 -4.1; 72 -4.7; 79 -5.6; 87 -6.5; 96 -7.0; 106 -7.2; 116 -6.8; 128 -6.1; 141 -5.8; 155 -5.4; 170 -4.7; 187 -4.2; 206 -4.0; 227 -4.3; 249 -4.7; 274 -5.3; 302 -5.9; 332 -6.6; 365 -7.3; 402 -7.3; 442 -7.1; 486 -7.0; 535 -6.8; 588 -6.6; 647 -6.4; 712 -6.2; 783 -6.0; 861 -5.7; 947 -5.7; 1042 -5.5; 1146 -6.4; 1261 -7.0; 1387 -7.3; 1526 -7.5; 1678 -8.0; 1846 -8.6; 2031 -8.4; 2234 -7.2; 2457 -5.5; 2703 -5.3; 2973 -5.4; 3270 -6.4; 3597 -6.7; 3957 -6.5; 4353 -6.3; 4788 -6.0; 5267 -6.1; 5793 -5.4; 6373 -5.2; 7010 -6.5; 7711 -8.5; 8482 -10.2; 9330 -11.6; 10263 -10.4; 11289 -6.9; 12418 -6.5; 13660 -7.3; 15026 -7.4; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.17 | 6.3 dB  |
| Peaking | 49 Hz   | 2.17 | 2.3 dB  |
| Peaking | 207 Hz  | 2.9  | 2.7 dB  |
| Peaking | 1843 Hz | 4.78 | -2.4 dB |
| Peaking | 9377 Hz | 3.68 | -5.7 dB |
| Peaking | 101 Hz  | 4.71 | -1.6 dB |
| Peaking | 402 Hz  | 3.75 | -1.2 dB |
| Peaking | 930 Hz  | 3.93 | 1.1 dB  |
| Peaking | 2733 Hz | 4.9  | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | 2.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SRH440/Shure%20SRH440.png)
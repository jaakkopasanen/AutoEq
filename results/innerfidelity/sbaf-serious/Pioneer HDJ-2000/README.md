# Pioneer HDJ-2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -2.0; 60 -3.7; 66 -5.0; 72 -6.1; 79 -7.2; 87 -8.3; 96 -8.8; 106 -9.0; 116 -8.8; 128 -8.6; 141 -8.7; 155 -8.7; 170 -8.4; 187 -8.5; 206 -8.5; 227 -8.4; 249 -8.4; 274 -8.2; 302 -7.9; 332 -7.8; 365 -7.6; 402 -7.6; 442 -7.3; 486 -7.1; 535 -7.2; 588 -7.1; 647 -7.1; 712 -7.5; 783 -7.5; 861 -7.0; 947 -6.5; 1042 -6.9; 1146 -7.6; 1261 -7.6; 1387 -7.9; 1526 -8.1; 1678 -7.9; 1846 -7.2; 2031 -5.7; 2234 -3.4; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.8; 3597 -3.0; 3957 -5.8; 4353 -4.1; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 44 Hz   |  0.45 | 9.4 dB  |
| Peaking | 90 Hz   |  0.75 | -7.1 dB |
| Peaking | 956 Hz  |  0.07 | -1.2 dB |
| Peaking | 2806 Hz |  2.47 | 7.6 dB  |
| Peaking | 5596 Hz |  2.26 | 7.4 dB  |
| Peaking | 968 Hz  |  1.17 | 0.9 dB  |
| Peaking | 1600 Hz |  1.9  | -1.8 dB |
| Peaking | 2321 Hz |  6.01 | 1.6 dB  |
| Peaking | 4074 Hz | 10.17 | -2.5 dB |
| Peaking | 4699 Hz | 10.56 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-2000/Pioneer%20HDJ-2000.png)
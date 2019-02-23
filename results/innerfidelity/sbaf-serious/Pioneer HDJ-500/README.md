# Pioneer HDJ-500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.8; 45 -3.1; 49 -4.1; 54 -5.0; 60 -5.8; 66 -6.2; 72 -6.2; 79 -6.6; 87 -7.0; 96 -7.0; 106 -7.2; 116 -7.3; 128 -7.7; 141 -7.9; 155 -8.3; 170 -8.2; 187 -8.4; 206 -8.6; 227 -8.6; 249 -8.3; 274 -8.4; 302 -8.6; 332 -8.7; 365 -9.3; 402 -9.1; 442 -8.7; 486 -9.1; 535 -9.5; 588 -9.4; 647 -9.4; 712 -9.4; 783 -9.3; 861 -9.1; 947 -9.0; 1042 -8.6; 1146 -8.0; 1261 -7.3; 1387 -7.1; 1526 -6.4; 1678 -5.8; 1846 -4.3; 2031 -3.0; 2234 -1.9; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -1.3; 4353 -0.7; 4788 -7.5; 5267 -10.9; 5793 -9.6; 6373 -9.2; 7010 -8.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.6; 16529 -10.4; 18182 -9.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 28 Hz    |  1.09 | 6.9 dB  |
| Peaking | 679 Hz   |  0.26 | -3.5 dB |
| Peaking | 3494 Hz  |  0.76 | 10.3 dB |
| Peaking | 5504 Hz  |  1.95 | -9.9 dB |
| Peaking | 16950 Hz |  1.51 | -4.3 dB |
| Peaking | 19 Hz    |  2.87 | 1.6 dB  |
| Peaking | 306 Hz   |  2.53 | 0.7 dB  |
| Peaking | 2345 Hz  |  1.87 | 3.2 dB  |
| Peaking | 2647 Hz  |  0.8  | -2.3 dB |
| Peaking | 4369 Hz  | 10.07 | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-500/Pioneer%20HDJ-500.png)
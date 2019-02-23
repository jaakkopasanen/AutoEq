# NarMoo W1M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -13.3; 25 -13.4; 28 -13.4; 31 -13.3; 34 -13.3; 37 -13.2; 41 -13.2; 45 -13.1; 49 -13.0; 54 -13.0; 60 -12.9; 66 -12.9; 72 -12.9; 79 -12.9; 87 -13.0; 96 -13.0; 106 -12.9; 116 -12.7; 128 -12.7; 141 -12.6; 155 -12.4; 170 -12.3; 187 -12.0; 206 -11.8; 227 -11.5; 249 -11.3; 274 -11.1; 302 -10.8; 332 -10.5; 365 -10.3; 402 -10.1; 442 -9.7; 486 -9.6; 535 -9.3; 588 -8.9; 647 -8.6; 712 -8.5; 783 -8.1; 861 -8.0; 947 -8.0; 1042 -7.6; 1146 -7.3; 1261 -6.9; 1387 -6.6; 1526 -6.3; 1678 -6.0; 1846 -5.5; 2031 -5.1; 2234 -5.0; 2457 -4.8; 2703 -4.3; 2973 -2.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -4.5; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo W1M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo W1M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 14 Hz   |  0.31 | -5.8 dB |
| Peaking | 136 Hz  |  0.27 | -5.4 dB |
| Peaking | 3545 Hz |  1.88 | 6.3 dB  |
| Peaking | 6140 Hz |  3.39 | 6.0 dB  |
| Peaking | 7756 Hz |  2.05 | -1.4 dB |
| Peaking | 972 Hz  |  2.03 | -0.5 dB |
| Peaking | 2362 Hz |  1.05 | 0.9 dB  |
| Peaking | 2619 Hz |  3.79 | -1.5 dB |
| Peaking | 4919 Hz | 10.74 | -2.2 dB |
| Peaking | 5541 Hz | 13.34 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20W1M/NarMoo%20W1M.png)
# DIY MDR-XB950AP-Beyerdynamic DT250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.5; 54 -2.1; 60 -2.8; 66 -3.4; 72 -3.8; 79 -4.3; 87 -5.0; 96 -5.6; 106 -6.2; 116 -6.7; 128 -7.1; 141 -7.3; 155 -7.2; 170 -7.2; 187 -7.2; 206 -7.2; 227 -7.0; 249 -6.7; 274 -6.4; 302 -6.3; 332 -6.3; 365 -6.3; 402 -6.3; 442 -6.5; 486 -6.6; 535 -6.9; 588 -7.4; 647 -8.1; 712 -9.0; 783 -9.8; 861 -10.7; 947 -11.5; 1042 -12.4; 1146 -13.1; 1261 -13.2; 1387 -12.7; 1526 -11.7; 1678 -10.5; 1846 -8.9; 2031 -6.8; 2234 -4.6; 2457 -3.3; 2703 -3.2; 2973 -3.4; 3270 -2.9; 3597 -2.7; 3957 -3.5; 4353 -5.0; 4788 -7.0; 5267 -9.6; 5793 -10.4; 6373 -8.2; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`DIY MDR-XB950AP-Beyerdynamic DT250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `DIY MDR-XB950AP-Beyerdynamic DT250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 32 Hz   |  0.8  | 6.8 dB  |
| Peaking | 1301 Hz |  1.15 | -8.8 dB |
| Peaking | 3091 Hz |  0.78 | 6.2 dB  |
| Peaking | 5695 Hz |  2.2  | -7.0 dB |
| Peaking | 6899 Hz |  6.26 | 4.0 dB  |
| Peaking | 70 Hz   |  0.97 | 2.6 dB  |
| Peaking | 117 Hz  |  0.44 | -2.6 dB |
| Peaking | 366 Hz  |  0.77 | 1.7 dB  |
| Peaking | 827 Hz  |  2.55 | -0.9 dB |
| Peaking | 2370 Hz | 10.63 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -7.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/DIY%20MDR-XB950AP-Beyerdynamic%20DT250/DIY%20MDR-XB950AP-Beyerdynamic%20DT250.png)
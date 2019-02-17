# Jaybird Freedom 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.1; 25 -9.2; 28 -9.4; 31 -9.5; 34 -9.6; 37 -9.7; 41 -9.8; 45 -9.8; 49 -9.9; 54 -10.0; 60 -10.3; 66 -10.5; 72 -10.7; 79 -10.9; 87 -11.0; 96 -11.2; 106 -11.4; 116 -11.6; 128 -11.7; 141 -11.7; 155 -11.8; 170 -12.1; 187 -11.7; 206 -11.2; 227 -10.6; 249 -9.9; 274 -9.2; 302 -8.4; 332 -7.6; 365 -6.8; 402 -6.0; 442 -5.2; 486 -4.4; 535 -3.6; 588 -2.7; 647 -1.8; 712 -0.9; 783 -0.5; 861 -0.7; 947 -1.2; 1042 -1.9; 1146 -2.8; 1261 -3.5; 1387 -3.8; 1526 -4.0; 1678 -4.0; 1846 -4.6; 2031 -5.5; 2234 -6.3; 2457 -7.1; 2703 -7.0; 2973 -5.2; 3270 -3.1; 3597 -2.0; 3957 -1.6; 4353 -1.8; 4788 -1.9; 5267 -2.8; 5793 -4.8; 6373 -10.0; 7010 -13.8; 7711 -10.3; 8482 -5.6; 9330 -5.3; 10263 -9.2; 11289 -12.2; 12418 -10.2; 13660 -6.9; 15026 -7.7; 16529 -8.6; 18182 -4.8; 20000 -1.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Freedom 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Freedom 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.27 | -7.4 dB |
| Peaking | 142 Hz   | 0.74 | -5.3 dB |
| Peaking | 249 Hz   | 1.07 | -4.0 dB |
| Peaking | 6955 Hz  | 6.09 | -9.4 dB |
| Peaking | 12918 Hz | 0.51 | -7.7 dB |
| Peaking | 793 Hz   | 2.6  | 2.8 dB  |
| Peaking | 2764 Hz  | 1.07 | -7.5 dB |
| Peaking | 3744 Hz  | 1.52 | 6.6 dB  |
| Peaking | 11147 Hz | 1.43 | 4.4 dB  |
| Peaking | 11332 Hz | 3.61 | -8.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -7.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.2 dB |
| Peaking | 16000 Hz | 1.41 | -8.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Freedom%202/Jaybird%20Freedom%202.png)
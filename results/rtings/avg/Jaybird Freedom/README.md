# Jaybird Freedom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.4; 25 -3.5; 28 -3.5; 31 -3.5; 34 -3.5; 37 -3.4; 41 -3.4; 45 -3.4; 49 -3.4; 54 -3.5; 60 -3.8; 66 -4.2; 72 -4.4; 79 -4.8; 87 -5.1; 96 -5.5; 106 -5.9; 116 -6.3; 128 -6.7; 141 -7.0; 155 -7.1; 170 -7.1; 187 -6.9; 206 -6.8; 227 -6.8; 249 -7.3; 274 -7.1; 302 -6.5; 332 -6.0; 365 -5.4; 402 -5.0; 442 -4.5; 486 -3.9; 535 -3.4; 588 -2.7; 647 -2.1; 712 -1.6; 783 -1.2; 861 -1.2; 947 -1.5; 1042 -2.3; 1146 -3.3; 1261 -4.3; 1387 -5.1; 1526 -5.4; 1678 -5.8; 1846 -6.2; 2031 -6.7; 2234 -7.0; 2457 -7.4; 2703 -8.0; 2973 -7.1; 3270 -5.3; 3597 -3.8; 3957 -2.8; 4353 -2.2; 4788 -1.2; 5267 -0.6; 5793 -0.5; 6373 -2.3; 7010 -5.0; 7711 -7.9; 8482 -7.5; 9330 -5.1; 10263 -4.8; 11289 -6.9; 12418 -8.2; 13660 -4.9; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Freedom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Freedom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 212 Hz   | 0.94 | -2.6 dB |
| Peaking | 794 Hz   | 1.37 | 4.3 dB  |
| Peaking | 2538 Hz  | 1.27 | -4.4 dB |
| Peaking | 5867 Hz  | 1.1  | 11.4 dB |
| Peaking | 7337 Hz  | 1.16 | -9.5 dB |
| Peaking | 36 Hz    | 0.41 | 1.6 dB  |
| Peaking | 119 Hz   | 1.77 | -1.2 dB |
| Peaking | 8051 Hz  | 4.45 | -2.3 dB |
| Peaking | 9886 Hz  | 1.61 | 2.6 dB  |
| Peaking | 12028 Hz | 4.14 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Freedom/Jaybird%20Freedom.png)
# Jaybird Run XT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.2; 25 -9.2; 28 -9.2; 31 -9.2; 34 -9.2; 37 -9.2; 41 -9.2; 45 -9.2; 49 -9.2; 54 -9.2; 60 -9.3; 66 -9.3; 72 -9.4; 79 -9.5; 87 -9.5; 96 -9.6; 106 -9.6; 116 -9.5; 128 -9.4; 141 -9.2; 155 -8.9; 170 -8.7; 187 -8.5; 206 -8.3; 227 -7.8; 249 -7.4; 274 -6.9; 302 -6.4; 332 -5.9; 365 -5.4; 402 -4.8; 442 -4.3; 486 -3.8; 535 -3.1; 588 -2.4; 647 -1.7; 712 -1.2; 783 -0.8; 861 -0.8; 947 -1.2; 1042 -2.2; 1146 -3.3; 1261 -4.0; 1387 -4.6; 1526 -5.0; 1678 -5.6; 1846 -6.2; 2031 -7.0; 2234 -7.6; 2457 -7.6; 2703 -6.6; 2973 -4.5; 3270 -2.5; 3597 -1.4; 3957 -0.7; 4353 -0.5; 4788 -0.7; 5267 -0.6; 5793 -1.1; 6373 -3.7; 7010 -9.3; 7711 -8.9; 8482 -4.9; 9330 -4.9; 10263 -6.2; 11289 -7.8; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Run XT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Run XT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 63 Hz    | 0.2  | -4.8 dB |
| Peaking | 753 Hz   | 1.04 | 4.9 dB  |
| Peaking | 2321 Hz  | 1.54 | -4.9 dB |
| Peaking | 4427 Hz  | 1.14 | 5.9 dB  |
| Peaking | 7307 Hz  | 4.91 | -7.7 dB |
| Peaking | 3432 Hz  | 5.24 | 1.0 dB  |
| Peaking | 4641 Hz  | 1.99 | -0.8 dB |
| Peaking | 5794 Hz  | 5.21 | 1.7 dB  |
| Peaking | 11005 Hz | 6.86 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Run%20XT/Jaybird%20Run%20XT.png)
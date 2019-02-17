# Beats EP On-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.5; 25 -4.6; 28 -4.7; 31 -4.9; 34 -5.0; 37 -5.0; 41 -5.0; 45 -5.0; 49 -5.1; 54 -5.3; 60 -5.6; 66 -6.0; 72 -6.3; 79 -6.6; 87 -6.9; 96 -7.2; 106 -7.5; 116 -7.7; 128 -8.0; 141 -8.2; 155 -8.3; 170 -8.3; 187 -8.2; 206 -8.1; 227 -7.9; 249 -7.3; 274 -6.8; 302 -6.1; 332 -5.8; 365 -5.4; 402 -5.4; 442 -5.2; 486 -4.9; 535 -4.4; 588 -4.0; 647 -3.6; 712 -3.3; 783 -3.0; 861 -3.0; 947 -3.1; 1042 -3.2; 1146 -3.4; 1261 -3.7; 1387 -4.0; 1526 -4.4; 1678 -4.7; 1846 -5.1; 2031 -5.3; 2234 -4.4; 2457 -3.2; 2703 -2.5; 2973 -3.0; 3270 -3.3; 3597 -2.9; 3957 -2.6; 4353 -3.7; 4788 -6.0; 5267 -3.4; 5793 -0.5; 6373 -1.6; 7010 -4.3; 7711 -5.6; 8482 -6.7; 9330 -6.7; 10263 -4.5; 11289 -3.2; 12418 -3.2; 13660 -4.3; 15026 -5.1; 16529 -3.5; 18182 -3.2; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats EP On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats EP On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 55 Hz    | 0.31 | -1.4 dB |
| Peaking | 172 Hz   | 0.69 | -4.4 dB |
| Peaking | 1897 Hz  | 3.72 | -2.2 dB |
| Peaking | 5953 Hz  | 7.73 | 3.9 dB  |
| Peaking | 8655 Hz  | 2.5  | -3.9 dB |
| Peaking | 812 Hz   | 3.5  | 0.8 dB  |
| Peaking | 4562 Hz  | 1.87 | 1.7 dB  |
| Peaking | 4830 Hz  | 5.9  | -4.6 dB |
| Peaking | 11520 Hz | 4.01 | 1.1 dB  |
| Peaking | 14813 Hz | 3    | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20EP%20On-Ear/Beats%20EP%20On-Ear.png)
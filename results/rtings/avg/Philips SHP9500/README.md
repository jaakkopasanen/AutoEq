# Philips SHP9500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.4; 54 -2.1; 60 -2.9; 66 -3.6; 72 -4.2; 79 -4.8; 87 -5.4; 96 -5.9; 106 -6.3; 116 -6.5; 128 -6.7; 141 -6.7; 155 -6.6; 170 -6.5; 187 -6.4; 206 -6.2; 227 -5.8; 249 -5.6; 274 -5.6; 302 -5.5; 332 -5.5; 365 -5.5; 402 -5.5; 442 -5.6; 486 -5.8; 535 -5.8; 588 -5.7; 647 -5.7; 712 -5.7; 783 -5.6; 861 -5.6; 947 -5.6; 1042 -5.6; 1146 -5.7; 1261 -6.2; 1387 -6.6; 1526 -6.6; 1678 -6.4; 1846 -6.3; 2031 -5.6; 2234 -5.0; 2457 -5.4; 2703 -6.6; 2973 -7.1; 3270 -6.9; 3597 -7.5; 3957 -9.2; 4353 -9.6; 4788 -10.2; 5267 -10.4; 5793 -10.1; 6373 -6.9; 7010 -5.7; 7711 -6.6; 8482 -7.4; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.8; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHP9500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHP9500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.83 | 6.8 dB  |
| Peaking | 586 Hz   | 0.73 | 1.0 dB  |
| Peaking | 2273 Hz  | 5.31 | 1.8 dB  |
| Peaking | 4874 Hz  | 2.38 | -4.3 dB |
| Peaking | 18857 Hz | 1.67 | -4.2 dB |
| Peaking | 54 Hz    | 2.52 | 1.1 dB  |
| Peaking | 121 Hz   | 2.06 | -1.1 dB |
| Peaking | 5739 Hz  | 9.61 | -1.9 dB |
| Peaking | 6867 Hz  | 5.54 | 1.9 dB  |
| Peaking | 20154 Hz | 4.64 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Philips%20SHP9500/Philips%20SHP9500.png)
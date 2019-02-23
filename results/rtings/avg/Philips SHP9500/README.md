# Philips SHP9500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.6; 54 -2.3; 60 -3.1; 66 -3.9; 72 -4.5; 79 -5.0; 87 -5.5; 96 -6.0; 106 -6.4; 116 -6.7; 128 -6.9; 141 -6.8; 155 -6.8; 170 -6.7; 187 -6.6; 206 -6.3; 227 -5.9; 249 -5.7; 274 -5.6; 302 -5.6; 332 -5.5; 365 -5.4; 402 -5.6; 442 -5.7; 486 -5.7; 535 -5.7; 588 -5.7; 647 -5.6; 712 -5.6; 783 -5.5; 861 -5.5; 947 -5.5; 1042 -5.5; 1146 -5.6; 1261 -6.1; 1387 -6.5; 1526 -6.4; 1678 -6.2; 1846 -6.0; 2031 -5.2; 2234 -4.2; 2457 -4.4; 2703 -6.1; 2973 -7.1; 3270 -7.2; 3597 -7.7; 3957 -9.6; 4353 -9.9; 4788 -10.0; 5267 -9.8; 5793 -10.3; 6373 -7.9; 7010 -5.6; 7711 -6.2; 8482 -7.6; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -10.0; 20000 -8.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHP9500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHP9500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.83 | 6.8 dB  |
| Peaking | 2302 Hz  | 3.22 | 2.8 dB  |
| Peaking | 4749 Hz  | 1.88 | -4.0 dB |
| Peaking | 16477 Hz | 1.25 | 1.9 dB  |
| Peaking | 18701 Hz | 0.99 | -4.7 dB |
| Peaking | 128 Hz   | 1.04 | -2.1 dB |
| Peaking | 341 Hz   | 0.16 | 1.2 dB  |
| Peaking | 1760 Hz  | 1.45 | -0.9 dB |
| Peaking | 7128 Hz  | 1.68 | -2.5 dB |
| Peaking | 7303 Hz  | 4.19 | 4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Philips%20SHP9500/Philips%20SHP9500.png)
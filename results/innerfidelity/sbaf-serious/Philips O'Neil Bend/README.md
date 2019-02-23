# Philips O'Neil Bend
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.8; 25 -6.4; 28 -7.0; 31 -7.5; 34 -8.0; 37 -8.5; 41 -8.9; 45 -9.4; 49 -9.7; 54 -10.1; 60 -10.4; 66 -10.8; 72 -11.2; 79 -11.5; 87 -12.0; 96 -12.4; 106 -12.5; 116 -12.6; 128 -12.7; 141 -13.0; 155 -13.3; 170 -12.7; 187 -12.7; 206 -12.6; 227 -12.1; 249 -11.7; 274 -11.0; 302 -10.4; 332 -9.8; 365 -9.4; 402 -9.1; 442 -8.8; 486 -8.7; 535 -8.9; 588 -8.6; 647 -8.6; 712 -8.7; 783 -8.6; 861 -8.8; 947 -8.6; 1042 -8.4; 1146 -7.8; 1261 -7.1; 1387 -6.7; 1526 -6.0; 1678 -5.4; 1846 -4.4; 2031 -3.3; 2234 -2.2; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -1.8; 4353 -3.8; 4788 -3.2; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips O'Neil Bend GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips O'Neil Bend ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 75 Hz   |  0.81 | -2.9 dB |
| Peaking | 174 Hz  |  0.67 | -5.6 dB |
| Peaking | 931 Hz  |  1.07 | -2.2 dB |
| Peaking | 2888 Hz |  1.26 | 6.6 dB  |
| Peaking | 5906 Hz |  3.81 | 5.4 dB  |
| Peaking | 15 Hz   |  1.41 | 3.5 dB  |
| Peaking | 39 Hz   |  1.85 | -0.8 dB |
| Peaking | 3716 Hz | 11.02 | 1.1 dB  |
| Peaking | 6676 Hz |  7.58 | 2.0 dB  |
| Peaking | 7699 Hz |  1.86 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20O'Neil%20Bend/Philips%20O'Neil%20Bend.png)
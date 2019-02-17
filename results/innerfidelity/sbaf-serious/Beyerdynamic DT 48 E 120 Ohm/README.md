# Beyerdynamic DT 48 E 120 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.9; 72 -9.2; 79 -13.8; 87 -11.2; 96 -9.4; 106 -10.8; 116 -10.3; 128 -9.7; 141 -9.2; 155 -8.3; 170 -8.8; 187 -8.8; 206 -8.3; 227 -7.6; 249 -7.1; 274 -6.4; 302 -5.7; 332 -5.3; 365 -5.0; 402 -4.3; 442 -3.3; 486 -2.5; 535 -1.4; 588 -0.5; 647 -0.6; 712 -1.7; 783 -3.2; 861 -4.6; 947 -5.6; 1042 -7.4; 1146 -9.4; 1261 -10.5; 1387 -11.3; 1526 -12.1; 1678 -13.0; 1846 -12.8; 2031 -12.5; 2234 -11.3; 2457 -8.5; 2703 -5.7; 2973 -4.4; 3270 -4.0; 3597 -2.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -1.1; 7010 -5.1; 7711 -11.8; 8482 -15.0; 9330 -11.9; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -11.2; 16529 -16.5; 18182 -17.5; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 E 120 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 E 120 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.61 | 7.4 dB   |
| Peaking | 1801 Hz  | 1.04 | -17.7 dB |
| Peaking | 4246 Hz  | 0.15 | 11.3 dB  |
| Peaking | 8499 Hz  | 2.77 | -16.7 dB |
| Peaking | 17427 Hz | 0.71 | -15.6 dB |
| Peaking | 21 Hz    | 2.86 | 4.3 dB   |
| Peaking | 61 Hz    | 1.76 | 11.3 dB  |
| Peaking | 78 Hz    | 4.94 | -9.1 dB  |
| Peaking | 86 Hz    | 0.55 | -6.0 dB  |
| Peaking | 591 Hz   | 2.76 | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 6.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.0 dB |
| Peaking | 4000 Hz  | 1.41 | 10.2 dB |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -8.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20E%20120%20Ohm/Beyerdynamic%20DT%2048%20E%20120%20Ohm.png)
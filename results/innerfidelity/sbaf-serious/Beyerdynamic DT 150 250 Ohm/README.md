# Beyerdynamic DT 150 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.4; 25 -3.8; 28 -4.2; 31 -4.5; 34 -4.8; 37 -5.0; 41 -5.1; 45 -5.2; 49 -5.2; 54 -5.0; 60 -4.3; 66 -4.4; 72 -5.2; 79 -5.7; 87 -7.4; 96 -9.1; 106 -10.0; 116 -10.4; 128 -10.7; 141 -10.9; 155 -10.7; 170 -10.1; 187 -10.3; 206 -9.5; 227 -8.6; 249 -7.3; 274 -6.0; 302 -4.6; 332 -3.7; 365 -3.5; 402 -3.9; 442 -4.1; 486 -4.3; 535 -4.4; 588 -4.2; 647 -4.3; 712 -4.5; 783 -4.5; 861 -4.7; 947 -4.8; 1042 -4.6; 1146 -4.4; 1261 -4.3; 1387 -5.0; 1526 -5.7; 1678 -6.5; 1846 -7.1; 2031 -7.7; 2234 -8.0; 2457 -7.0; 2703 -5.9; 2973 -4.2; 3270 -3.2; 3597 -2.1; 3957 -3.7; 4353 -7.5; 4788 -6.6; 5267 -4.9; 5793 -4.4; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.9; 9330 -8.5; 10263 -6.1; 11289 -5.8; 12418 -5.8; 13660 -6.4; 15026 -6.7; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 150 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 150 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 71 Hz   |  0.57 | 7.6 dB   |
| Peaking | 133 Hz  |  0.49 | -11.5 dB |
| Peaking | 349 Hz  |  0.73 | 6.2 dB   |
| Peaking | 3526 Hz |  6.72 | 4.2 dB   |
| Peaking | 6444 Hz |  7.39 | 5.8 dB   |
| Peaking | 22 Hz   |  2.59 | 2.1 dB   |
| Peaking | 1193 Hz |  3.32 | 1.3 dB   |
| Peaking | 2106 Hz |  3.66 | -2.6 dB  |
| Peaking | 4488 Hz | 10.93 | -2.7 dB  |
| Peaking | 9444 Hz |  7.48 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20150%20250%20Ohm/Beyerdynamic%20DT%20150%20250%20Ohm.png)
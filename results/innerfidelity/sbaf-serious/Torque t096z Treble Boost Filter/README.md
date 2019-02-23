# Torque t096z Treble Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.2; 25 -4.6; 28 -5.0; 31 -5.3; 34 -5.5; 37 -5.6; 41 -5.9; 45 -6.1; 49 -6.3; 54 -6.6; 60 -6.9; 66 -7.2; 72 -7.5; 79 -8.0; 87 -8.3; 96 -8.6; 106 -8.8; 116 -9.0; 128 -9.1; 141 -9.3; 155 -9.3; 170 -9.2; 187 -9.0; 206 -8.9; 227 -8.5; 249 -8.2; 274 -7.7; 302 -7.3; 332 -6.7; 365 -6.1; 402 -5.5; 442 -4.7; 486 -4.4; 535 -3.7; 588 -3.0; 647 -2.5; 712 -2.2; 783 -1.8; 861 -1.9; 947 -2.1; 1042 -2.4; 1146 -2.7; 1261 -3.2; 1387 -3.9; 1526 -4.9; 1678 -5.5; 1846 -5.9; 2031 -6.1; 2234 -6.8; 2457 -7.6; 2703 -8.6; 2973 -8.6; 3270 -7.6; 3597 -6.4; 3957 -7.4; 4353 -11.2; 4788 -13.9; 5267 -9.6; 5793 -3.5; 6373 -0.5; 7010 -3.1; 7711 -5.4; 8482 -5.6; 9330 -5.6; 10263 -6.2; 11289 -8.1; 12418 -5.8; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Treble Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Treble Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 159 Hz   |  0.62 | -3.9 dB |
| Peaking | 794 Hz   |  0.94 | 4.4 dB  |
| Peaking | 2694 Hz  |  2.58 | -3.2 dB |
| Peaking | 4787 Hz  |  4.49 | -9.4 dB |
| Peaking | 6294 Hz  |  4.71 | 6.8 dB  |
| Peaking | 20 Hz    |  1.42 | 2.0 dB  |
| Peaking | 1269 Hz  |  3.96 | 0.6 dB  |
| Peaking | 1646 Hz  |  2.91 | -0.7 dB |
| Peaking | 3699 Hz  | 10.03 | 1.3 dB  |
| Peaking | 11154 Hz |  6.55 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Treble%20Boost%20Filter/Torque%20t096z%20Treble%20Boost%20Filter.png)
# Torque t096z Ushaped Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.8; 23 -14.8; 25 -14.8; 28 -14.7; 31 -14.6; 34 -14.5; 37 -14.3; 41 -14.2; 45 -14.0; 49 -13.9; 54 -13.7; 60 -13.6; 66 -13.4; 72 -13.3; 79 -13.2; 87 -13.1; 96 -13.0; 106 -12.7; 116 -12.3; 128 -12.1; 141 -11.8; 155 -11.4; 170 -10.9; 187 -10.4; 206 -9.9; 227 -9.3; 249 -8.7; 274 -8.1; 302 -7.4; 332 -6.8; 365 -6.1; 402 -5.5; 442 -4.8; 486 -4.3; 535 -3.7; 588 -2.9; 647 -2.5; 712 -2.3; 783 -1.9; 861 -2.1; 947 -2.3; 1042 -2.7; 1146 -3.1; 1261 -3.6; 1387 -4.4; 1526 -5.3; 1678 -6.1; 1846 -6.8; 2031 -7.2; 2234 -8.1; 2457 -9.1; 2703 -9.5; 2973 -8.4; 3270 -6.2; 3597 -5.0; 3957 -6.5; 4353 -10.8; 4788 -13.1; 5267 -7.7; 5793 -1.5; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.6; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Ushaped Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Ushaped Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.27 | -8.5 dB |
| Peaking | 132 Hz  | 0.67 | -3.6 dB |
| Peaking | 744 Hz  | 1.22 | 4.7 dB  |
| Peaking | 4758 Hz | 4.2  | -8.8 dB |
| Peaking | 6094 Hz | 4.19 | 7.8 dB  |
| Peaking | 224 Hz  | 4.44 | -0.2 dB |
| Peaking | 720 Hz  | 6.33 | -0.7 dB |
| Peaking | 1180 Hz | 2.32 | 1.4 dB  |
| Peaking | 2714 Hz | 1.73 | -4.4 dB |
| Peaking | 3560 Hz | 3.46 | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Ushaped%20Filter/Torque%20t096z%20Ushaped%20Filter.png)
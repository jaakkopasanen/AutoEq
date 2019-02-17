# Torque t096z Treble Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.8; 25 -5.2; 28 -5.6; 31 -5.9; 34 -6.1; 37 -6.3; 41 -6.5; 45 -6.7; 49 -6.9; 54 -7.2; 60 -7.5; 66 -7.8; 72 -8.1; 79 -8.6; 87 -8.9; 96 -9.2; 106 -9.4; 116 -9.6; 128 -9.7; 141 -10.0; 155 -9.9; 170 -9.8; 187 -9.6; 206 -9.5; 227 -9.1; 249 -8.8; 274 -8.3; 302 -7.9; 332 -7.3; 365 -6.8; 402 -6.2; 442 -5.4; 486 -5.0; 535 -4.4; 588 -3.6; 647 -3.1; 712 -2.8; 783 -2.4; 861 -2.5; 947 -2.7; 1042 -3.1; 1146 -3.4; 1261 -3.8; 1387 -4.5; 1526 -5.5; 1678 -6.1; 1846 -6.5; 2031 -6.7; 2234 -7.4; 2457 -8.3; 2703 -9.2; 2973 -9.2; 3270 -8.2; 3597 -7.0; 3957 -8.0; 4353 -11.8; 4788 -14.5; 5267 -10.3; 5793 -4.1; 6373 -0.9; 7010 -0.5; 7711 -2.6; 8482 -2.9; 9330 -2.9; 10263 -6.4; 11289 -8.8; 12418 -5.8; 13660 -3.2; 15026 -2.9; 16529 -2.9; 18182 -2.9; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t096z Treble Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Treble Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 88 Hz    | 0.45 | -5.2 dB  |
| Peaking | 216 Hz   | 0.92 | -3.9 dB  |
| Peaking | 2669 Hz  | 1.59 | -6.1 dB  |
| Peaking | 4704 Hz  | 5.37 | -11.5 dB |
| Peaking | 11269 Hz | 4.93 | -6.5 dB  |
| Peaking | 384 Hz   | 2.25 | -0.8 dB  |
| Peaking | 802 Hz   | 1.49 | 1.5 dB   |
| Peaking | 1626 Hz  | 3.62 | -1.5 dB  |
| Peaking | 5242 Hz  | 7.24 | -3.2 dB  |
| Peaking | 6578 Hz  | 3.74 | 4.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | -7.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Treble%20Boost%20Filter/Torque%20t096z%20Treble%20Boost%20Filter.png)
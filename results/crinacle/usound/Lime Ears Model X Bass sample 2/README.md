# Lime Ears Model X Bass sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.8; 25 -5.1; 28 -5.4; 31 -5.6; 34 -5.8; 37 -5.9; 41 -6.1; 45 -6.4; 49 -6.6; 54 -6.8; 60 -7.0; 66 -7.3; 72 -7.6; 79 -8.0; 87 -8.4; 96 -8.8; 106 -9.2; 116 -9.6; 128 -9.8; 141 -10.1; 155 -10.2; 170 -10.4; 187 -10.5; 206 -10.6; 227 -10.5; 249 -10.4; 274 -10.3; 302 -10.1; 332 -9.9; 365 -9.6; 402 -9.2; 442 -8.9; 486 -8.4; 535 -8.0; 588 -7.4; 647 -6.8; 712 -6.0; 783 -5.2; 861 -4.5; 947 -4.0; 1042 -3.8; 1146 -4.1; 1261 -4.6; 1387 -4.8; 1526 -4.6; 1678 -4.2; 1846 -4.0; 2031 -4.2; 2234 -4.2; 2457 -2.6; 2703 -0.6; 2973 -0.5; 3270 -1.6; 3597 -3.6; 3957 -3.4; 4353 -4.2; 4788 -6.9; 5267 -5.7; 5793 -2.4; 6373 -1.2; 7010 -4.0; 7711 -7.6; 8482 -11.1; 9330 -9.8; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X Bass sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X Bass sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 231 Hz  | 0.52 | -4.3 dB |
| Peaking | 1008 Hz | 1.18 | 3.2 dB  |
| Peaking | 2909 Hz | 2.23 | 6.0 dB  |
| Peaking | 6371 Hz | 4.59 | 5.9 dB  |
| Peaking | 8611 Hz | 4.33 | -5.8 dB |
| Peaking | 11 Hz   | 0.63 | 0.4 dB  |
| Peaking | 21 Hz   | 0.91 | 1.9 dB  |
| Peaking | 4226 Hz | 7.55 | 1.9 dB  |
| Peaking | 4957 Hz | 5.01 | -2.6 dB |
| Peaking | 5695 Hz | 7.91 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lime%20Ears%20Model%20X%20Bass%20sample%202/Lime%20Ears%20Model%20X%20Bass%20sample%202.png)